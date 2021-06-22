import * as assert from 'assert';
import {
  parse,
  printLocation,
  FieldDefinitionNode,
  ObjectTypeDefinitionNode,
  Source,
  DirectiveNode,
} from 'graphql/language';
import { GraphQLError, printError, syntaxError } from 'graphql/error';

// prettier-ignore
const ScalarTypes: ReadonlySet<string> = new Set([
  'bool',
  'string',
  'u64', 'u32', 'u16', 'u8',
  'i64', 'i32', 'i16', 'i8',
  'f64', 'f32',
]);

// prettier-ignore
type ScalarType =
  'bool' |
  'string' |
  'u64' | 'u32' | 'u16' | 'u8' |
  'i64' | 'i32' | 'i16' | 'i8' |
  'f64' | 'f32';

type ColumnType = ScalarType | 'row' | 'foreignrow';

const DIRECTIVE_REF = {
  NAME: 'ref',
};

const DIRECTIVE_UNIQUE = {
  NAME: 'unique',
};

interface TableColumn {
  name: string | null;
  description: string | null;
  array: boolean;
  type: ColumnType;
  unique: boolean;
  nullable: boolean;
  until: string | null;
  references:
    | { table: string | null; column: string | null }
    | { enum: string }
    | null;
}

interface SchemaTable {
  name: string;
  columns: TableColumn[];
}

// interface SchemaEnum {
//   name: string;
//   enum: string[];
// }

export function readSpecs(sources: readonly Source[]) {
  const typeDefsMap = new Map<string, ObjectTypeDefinitionNode>();

  for (const source of sources) {
    const doc = parse(source, { noLocation: false });

    for (const typeNode of doc.definitions) {
      if (typeNode.kind !== 'ObjectTypeDefinition') {
        throw new GraphQLError('Unsupported definition', typeNode);
      } else {
        typeDefsMap.set(typeNode.name.value, typeNode);
      }
    }
  }

  const tables: SchemaTable[] = [];
  for (const typeNode of typeDefsMap.values()) {
    const table: SchemaTable = {
      name: typeNode.name.value,
      columns: [],
    };

    assert.ok(typeNode.fields != null);
    for (const fieldNode of typeNode.fields) {
      table.columns.push(parseFieldNode(typeDefsMap, table.name, fieldNode));
    }

    tables.push(table);
  }

  return tables;
}

function parseFieldNode(
  typeDefsMap: ReadonlyMap<string, ObjectTypeDefinitionNode>,
  tableName: string,
  fieldNode: FieldDefinitionNode
): TableColumn {
  const unique = isUnique(fieldNode);
  const refFieldName = referencesField(fieldNode);
  const fieldType = unwrapType(fieldNode);
  let references: TableColumn['references'] = null;

  if (fieldType.name === tableName) {
    references = { table: tableName, column: null };
    fieldType.name = 'row' as ColumnType;
  } else if (fieldType.name === 'ref') {
    references = { table: null, column: null };
    fieldType.name = 'foreignrow' as ColumnType;
  } else if (!ScalarTypes.has(fieldType.name)) {
    if (typeDefsMap.has(fieldType.name)) {
      references = { table: fieldType.name, column: null };
      fieldType.name = 'foreignrow' as ColumnType;
    } else {
      throw new GraphQLError(
        `Can't find referenced table "${fieldType.name}".`,
        fieldNode.type
      );
    }
  }

  if (refFieldName) {
    assert.ok(references?.table);
    references.column = refFieldName;
    const refDefNode = typeDefsMap.get(references.table);
    assert.ok(refDefNode);

    let refFieldType: string | undefined;
    try {
      refFieldType = findReferencedField(refDefNode, refFieldName);
    } catch (e) {
      throw new GraphQLError(
        'An error occurred while validating the referenced column.',
        findDirective(fieldNode, DIRECTIVE_REF.NAME),
        undefined,
        undefined,
        undefined,
        e
      );
    }

    if (!refFieldType) {
      throw new GraphQLError(
        `Can't find column "${refFieldName}" in table "${references.table}".`,
        findDirective(fieldNode, DIRECTIVE_REF.NAME)
      );
    }
    fieldType.name = refFieldType;
  }

  assert.ok(
    ScalarTypes.has(fieldType.name) ||
      fieldType.name === 'row' ||
      fieldType.name === 'foreignrow'
  );

  const column: TableColumn = {
    name: fieldNode.name.value === '_' ? null : fieldNode.name.value,
    description: fieldNode.description?.value ?? null,
    array: fieldType.array,
    type: fieldType.name as ColumnType,
    nullable: fieldType.nullable,
    unique: unique,
    references: references,
    until: null, // TODO
  };

  return column;
}

function isUnique(field: FieldDefinitionNode): boolean {
  return findDirective(field, DIRECTIVE_UNIQUE.NAME) != null;
}

function referencesField(field: FieldDefinitionNode): string | undefined {
  const directive = findDirective(field, DIRECTIVE_REF.NAME);

  if (directive) {
    const { arguments: args } = directive;
    assert.ok(
      args?.length === 1 &&
        args[0].name.value === 'column' &&
        args[0].value.kind === 'StringValue',
      printLocation(directive.loc!)
    );
    return args[0].value.value;
  }
}

function unwrapType(field: FieldDefinitionNode): {
  array: boolean;
  nullable: boolean;
  name: string;
} {
  let nullable = true;
  let array = false;

  let { type } = field;
  if (type.kind === 'NonNullType') {
    nullable = false;
    type = type.type;
  } else if (type.kind === 'ListType') {
    array = true;
    nullable = false;
    type = type.type;
  }

  assert.ok(type.kind === 'NamedType', printLocation(field.type.loc!));

  if (ScalarTypes.has(type.name.value) && type.name.value !== 'string') {
    nullable = false;
  }

  return {
    array,
    nullable,
    name: type.name.value,
  };
}

function findReferencedField(
  typeNode: ObjectTypeDefinitionNode,
  name: string
): string | undefined {
  assert.ok(typeNode.fields != null);
  const fieldNode = typeNode.fields.find((field) => field.name.value === name);

  if (fieldNode) {
    const typeInfo = unwrapType(fieldNode);
    if (typeInfo.array) {
      throw new GraphQLError(
        'Сannot refer to a column with an array type.',
        fieldNode.type
      );
    }
    if (typeInfo.nullable) {
      throw new GraphQLError(
        'Сannot refer to a column with nullable values.',
        fieldNode.type
      );
    }
    if (!isUnique(fieldNode)) {
      throw new GraphQLError(
        'Values in the referenced column must be unique.',
        fieldNode
      );
    }
    if (!ScalarTypes.has(typeInfo.name)) {
      throw new GraphQLError(
        'Сannot refer to a column with a non-scalar type.',
        fieldNode.type
      );
    }

    return typeInfo.name;
  }
}

function findDirective(
  node: FieldDefinitionNode,
  name: string
): DirectiveNode | undefined {
  return (node.directives ?? []).find(
    (directive) => directive.name.value === name
  );
}
