import * as assert from 'assert';
import {
  parse,
  Source,
  ObjectTypeDefinitionNode,
  FieldDefinitionNode,
  DirectiveNode,
  EnumTypeDefinitionNode,
} from 'graphql/language';
import { GraphQLError } from 'graphql/error';
import { SchemaTable, TableColumn, ColumnType, RefUsingColumn, SchemaEnum } from './types';

// prettier-ignore
const ScalarTypes: ReadonlySet<string> = new Set([
  'bool',
  'string',
  'i32',
  'f32',
]);

const DIRECTIVE_REF = {
  NAME: 'ref',
  ARGS: {
    COLUMN: 'column',
  },
};

const DIRECTIVE_UNIQUE = {
  NAME: 'unique',
};

const DIRECTIVE_LOCALIZED = {
  NAME: 'localized',
};

const DIRECTIVE_FILE = {
  NAME: 'file',
  ARGS: {
    EXTENSION: 'ext',
  },
};

const DIRECTIVE_FILES_GROUP = {
  NAME: 'files',
  ARGS: {
    EXTENSION: 'ext',
  },
};

interface Context {
  typeDefsMap: ReadonlyMap<string, ObjectTypeDefinitionNode>;
  enumNamesMap: ReadonlyMap<string, EnumTypeDefinitionNode>;
}

export interface ReadSchemaResult {
	tables: SchemaTable[];
	enums: SchemaEnum[];
}

export function readSchemaSources(sources: readonly Source[]) : ReadSchemaResult {
  const typeDefsMap = new Map<string, ObjectTypeDefinitionNode>();
  const enumNamesMap = new Map<string, EnumTypeDefinitionNode>();

  for (const source of sources) {
    const doc = parse(source, { noLocation: false });

    for (const typeNode of doc.definitions) {
      if (typeNode.kind === 'EnumTypeDefinition') {
        if (enumNamesMap.has(typeNode.name.value)) {
          throw new GraphQLError(
            'Enum with this name has already been defined.',
            typeNode.name
          );
        }
        enumNamesMap.set(typeNode.name.value, typeNode);
      } else if (typeNode.kind === 'ObjectTypeDefinition') {
        if (typeDefsMap.has(typeNode.name.value)) {
          throw new GraphQLError(
            'Table with this name has already been defined.',
            typeNode.name
          );
        }
        typeDefsMap.set(typeNode.name.value, typeNode);
      } else {
        throw new GraphQLError('Unsupported definition.', typeNode);
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
      const column = parseFieldNode(
        { typeDefsMap, enumNamesMap },
        table.name,
        fieldNode
      );
      if (
        column.name != null &&
        table.columns.some((col) => col.name === column.name)
      ) {
        throw new GraphQLError(
          `Duplicate column name "${column.name}".`,
          fieldNode.name
        );
      }
      table.columns.push(column);
    }

    tables.push(table);
  }

  const enums: SchemaEnum[] = [];
  for (const enumNode of enumNamesMap.values()) {
    enums.push(parseEnumNode(enumNode));
  }

  return {tables, enums} as ReadSchemaResult;
}

function parseEnumNode(enumNode: EnumTypeDefinitionNode) {
  const schemaEnum: SchemaEnum = {
    name: enumNode.name.value,
    enum: [],
  };
  if (enumNode.values != null ){
    if (enumNode.values.length != 1 || enumNode.values[0].name.value != "_"){
      for (const value of enumNode.values) {
        if(value.name.value == "_"){
          schemaEnum.enum.push(null);
        }else{
          schemaEnum.enum.push(value.name.value);
        }
      }
    }
  }
  return schemaEnum;
}

function parseFieldNode(
  ctx: Context,
  tableName: string,
  fieldNode: FieldDefinitionNode
): TableColumn {
  validateDirectives(fieldNode);

  const unique = isUnique(fieldNode);
  const localized = isLocalized(fieldNode);
  const refFieldName = referencesField(fieldNode);
  const fieldType = unwrapType(fieldNode);
  let references: TableColumn['references'] = null;

  if (fieldType.name === tableName) {
    references = { table: tableName };
    fieldType.name = 'row' as ColumnType;
  } else if (fieldType.name === 'rid') {
    fieldType.name = 'foreignrow' as ColumnType;
  } else if (fieldType.name === '_' && fieldType.array) {
    fieldType.name = 'array' as ColumnType;
  } else if (!ScalarTypes.has(fieldType.name)) {
    if (ctx.typeDefsMap.has(fieldType.name)) {
      references = { table: fieldType.name };
      fieldType.name = 'foreignrow' as ColumnType;
    } else if (ctx.enumNamesMap.has(fieldType.name)) {
      references = { table: fieldType.name };
      fieldType.name = 'enumrow' as ColumnType;
    } else {
      throw new GraphQLError(
        `Can't find referenced table "${fieldType.name}".`,
        fieldNode.type
      );
    }
  }

  if (refFieldName) {
    assert.ok(references?.table);
    (references as RefUsingColumn).column = refFieldName;
    const refDefNode = ctx.typeDefsMap.get(references.table);
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
      fieldType.name === 'array' ||
      fieldType.name === 'row' ||
      fieldType.name === 'foreignrow' || 
	  fieldType.name === 'enumrow'
  );

  const column: TableColumn = {
    name: fieldNode.name.value === '_' ? null : fieldNode.name.value,
    description: fieldNode.description?.value ?? null,
    array: fieldType.array,
    type: fieldType.name as ColumnType,
    unique: unique,
    localized: localized,
    references: references,
    until: null, // TODO
    file: getFileExtension(fieldNode),
    files: getFileGroupExtensions(fieldNode),
  };

  return column;
}

function isUnique(field: FieldDefinitionNode): boolean {
  return findDirective(field, DIRECTIVE_UNIQUE.NAME) != null;
}

function isLocalized(field: FieldDefinitionNode): boolean {
  return findDirective(field, DIRECTIVE_LOCALIZED.NAME) != null;
}

function referencesField(field: FieldDefinitionNode): string | undefined {
  const directive = findDirective(field, DIRECTIVE_REF.NAME);

  if (directive) {
    const { arguments: args } = directive;
    assert.ok(
      args?.length === 1 &&
        args[0].name.value === DIRECTIVE_REF.ARGS.COLUMN &&
        args[0].value.kind === 'StringValue'
    );
    return args[0].value.value;
  }
}

function unwrapType(field: FieldDefinitionNode): {
  array: boolean;
  name: string;
} {
  let array = false;

  let { type } = field;
  if (type.kind === 'ListType') {
    array = true;
    type = type.type;
  }

  if (type.kind !== 'NamedType') {
    throw new GraphQLError('Valid type expected.', field.type);
  }
  if (type.name.value === '_' && !array) {
    throw new GraphQLError(
      'Unknown type is only allowed inside an array.',
      field.type
    );
  }

  return {
    array,
    name: type.name.value,
  };
}

function getFileExtension(field: FieldDefinitionNode): string | null {
  const directive = findDirective(field, DIRECTIVE_FILE.NAME);

  if (directive) {
    const { arguments: args } = directive;
    assert.ok(
      args?.length === 1 &&
        args[0].name.value === DIRECTIVE_FILE.ARGS.EXTENSION &&
        args[0].value.kind === 'StringValue'
    );
    return args[0].value.value;
  }

  return null;
}

function getFileGroupExtensions(field: FieldDefinitionNode): string[] | null {
  const directive = findDirective(field, DIRECTIVE_FILES_GROUP.NAME);

  if (directive) {
    const { arguments: args } = directive;
    assert.ok(
      args?.length === 1 &&
        args[0].name.value === DIRECTIVE_FILES_GROUP.ARGS.EXTENSION &&
        args[0].value.kind === 'ListValue'
    );
    return args[0].value.values.map((listValue) => {
      assert.ok(listValue.kind === 'StringValue');
      return listValue.value;
    });
  }

  return null;
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

function validateDirectives(node: FieldDefinitionNode): void {
  for (const directive of node.directives ?? []) {
    switch (directive.name.value) {
      case DIRECTIVE_REF.NAME:
      case DIRECTIVE_UNIQUE.NAME:
      case DIRECTIVE_LOCALIZED.NAME:
      case DIRECTIVE_FILE.NAME:
      case DIRECTIVE_FILES_GROUP.NAME:
        break;
      default:
        throw new GraphQLError(
          `Unknown directive "${directive.name.value}".`,
          directive.name
        );
    }
  }

  let directive = findDirective(node, DIRECTIVE_UNIQUE.NAME);
  if (directive) {
    if (directive.arguments?.length) {
      throw new GraphQLError(
        `Directive doesn't accept arguments.`,
        directive.arguments
      );
    }
  }

  directive = findDirective(node, DIRECTIVE_LOCALIZED.NAME);
  if (directive) {
    if (directive.arguments?.length) {
      throw new GraphQLError(
        `Directive doesn't accept arguments.`,
        directive.arguments
      );
    }
  }

  directive = findDirective(node, DIRECTIVE_REF.NAME);
  if (directive) {
    if (!directive.arguments?.length) {
      throw new GraphQLError('Missing referenced column name.', directive);
    }
    for (const arg of directive.arguments) {
      if (arg.name.value === DIRECTIVE_REF.ARGS.COLUMN) {
        if (arg.value.kind !== 'StringValue') {
          throw new GraphQLError(`String expected.`, arg.value);
        }
      } else {
        throw new GraphQLError(
          `Unknown argument "${arg.name.value}".`,
          arg.name
        );
      }
    }
  }

  directive = findDirective(node, DIRECTIVE_FILE.NAME);
  if (directive) {
    if (!directive.arguments?.length) {
      throw new GraphQLError('Missing file extension.', directive);
    }
    for (const arg of directive.arguments) {
      if (arg.name.value === DIRECTIVE_FILE.ARGS.EXTENSION) {
        if (arg.value.kind !== 'StringValue') {
          throw new GraphQLError(`String expected.`, arg.value);
        }
      } else {
        throw new GraphQLError(
          `Unknown argument "${arg.name.value}".`,
          arg.name
        );
      }
    }
  }

  directive = findDirective(node, DIRECTIVE_FILES_GROUP.NAME);
  if (directive) {
    if (!directive.arguments?.length) {
      throw new GraphQLError('Missing file extensions.', directive);
    }
    for (const arg of directive.arguments) {
      if (arg.name.value === DIRECTIVE_FILES_GROUP.ARGS.EXTENSION) {
        if (arg.value.kind !== 'ListValue') {
          throw new GraphQLError(`List of extensions expected.`, arg.value);
        }
        // NOTE allow empty list
        // if (!arg.value.values.length) {
        //   throw new GraphQLError(`List of extensions cannot be empty.`, arg.value);
        // }
        for (const listValue of arg.value.values) {
          if (listValue.kind !== 'StringValue') {
            throw new GraphQLError(`String expected.`, listValue);
          }
        }
      } else {
        throw new GraphQLError(
          `Unknown argument "${arg.name.value}".`,
          arg.name
        );
      }
    }
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
