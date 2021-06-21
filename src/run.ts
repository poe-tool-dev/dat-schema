import { readFileSync } from 'fs';
import * as assert from 'assert';
import {
  parse,
  print,
  printLocation,
  FieldDefinitionNode,
  ObjectTypeDefinitionNode,
} from 'graphql/language';

const file01 = readFileSync('./src/Harvest.gql', { encoding: 'utf-8' });

// prettier-ignore
const ScalarType = new Set([
  'bool',
  'string',
  'u64', 'u32', 'u16', 'u8',
  'i64', 'i32', 'i16', 'i8',
  'f64', 'f32',
] as const);

type ColumnType =
  | (typeof ScalarType extends Set<infer T> ? T : never)
  | 'row'
  | 'foreignrow';

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

// interface SchemaTable {
//   name: string;
//   columns: TableColumn[];
// }

// interface SchemaEnum {
//   name: string;
//   enum: string[];
// }

(function () {
  const typeDefsMap = new Map<string, ObjectTypeDefinitionNode>();

  const doc = parse(file01);

  for (const typeNode of doc.definitions) {
    if (typeNode.kind !== 'ObjectTypeDefinition') {
      throw printLocation(typeNode.loc!);
    } else {
      typeDefsMap.set(typeNode.name.value, typeNode);
    }
  }

  for (const typeNode of typeDefsMap.values()) {
    const tableName = typeNode.name.value;

    for (const fieldNode of typeNode.fields!) {
      const unique = isUnique(fieldNode);
      const refFieldName = referencesField(fieldNode);
      const fieldType = unwrapType(fieldNode);
      let references: TableColumn['references'] = null;

      if (tableName === fieldType.name) {
        references = { table: tableName, column: null };
        fieldType.name = 'row' as ColumnType;
      } else if (fieldType.name === 'ref') {
        references = { table: null, column: null };
        fieldType.name = 'foreignrow' as ColumnType;
      } else if (!ScalarType.has(fieldType.name as any)) {
        if (!typeDefsMap.has(fieldType.name)) {
          throw `Can't find referenced type.\n${printLocation(
            fieldNode.type.loc!
          )}`;
        }
        references = { table: fieldType.name, column: null };
        fieldType.name = 'foreignrow' as ColumnType;
      }

      if (refFieldName) {
        assert.ok(references?.table);
        references.column = refFieldName;
        const refDefNode = typeDefsMap.get(references.table);
        assert.ok(refDefNode);
        const refFieldType = findReferencedField(refDefNode, refFieldName);
        assert.ok(refFieldType);
        fieldType.name = refFieldType;
      }

      assert.ok(
        ScalarType.has(fieldType.name as any) ||
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
        until: null,
      };

      console.log(print(fieldNode), column);
    }
  }
})();

function isUnique(field: FieldDefinitionNode) {
  return (field.directives ?? []).some(
    (directive) => directive.name.value === 'unique'
  );
}

function referencesField(field: FieldDefinitionNode): string | undefined {
  const directive = (field.directives ?? []).find(
    (directive) => directive.name.value === 'ref'
  );

  if (directive) {
    const { arguments: args } = directive;
    assert.ok(
      args?.length === 1 &&
        args[0].name.value === 'field' &&
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

  if (ScalarType.has(type.name.value as any) && type.name.value !== 'string') {
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
  const fieldNode = typeNode.fields!.find((field) => field.name.value === name);

  if (fieldNode) {
    const typeInfo = unwrapType(fieldNode);
    assert.ok(
      isUnique(fieldNode) &&
        !typeInfo.array &&
        !typeInfo.nullable &&
        ScalarType.has(typeInfo.name as any)
    );
    return typeInfo.name;
  }
}
