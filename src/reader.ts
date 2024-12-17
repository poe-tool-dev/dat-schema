import * as assert from 'node:assert';
import {
  parse,
  Source,
  TypeDefinitionNode,
  ObjectTypeDefinitionNode,
  FieldDefinitionNode,
  DirectiveNode,
  EnumTypeDefinitionNode,
  GraphQLError,
} from 'graphql';
import {
  SchemaTable,
  TableColumn,
  ColumnType,
  RefUsingColumn,
  SchemaEnumeration,
  SchemaFile,
  ValidFor,
} from './types.js';

// prettier-ignore
const ScalarTypes: ReadonlySet<string> = new Set([
  'bool',
  'string',
  'i16',
  'u16',
  'i32',
  'u32',
  'f32',
]);

const DIRECTIVE_REF = {
  NAME: 'ref',
  ARGS: {
    COLUMN: 'column',
  },
  validate(directive: DirectiveNode) {
    if (!directive.arguments?.length) {
      throw new GraphQLError('Missing referenced column name.', {
        nodes: directive,
      });
    }
    for (const arg of directive.arguments) {
      if (arg.name.value === DIRECTIVE_REF.ARGS.COLUMN) {
        if (arg.value.kind !== 'StringValue') {
          throw new GraphQLError(`String expected.`, { nodes: arg.value });
        }
      } else {
        throw new GraphQLError(`Unknown argument "${arg.name.value}".`, {
          nodes: arg.name,
        });
      }
    }
  },
};

const DIRECTIVE_UNIQUE = {
  NAME: 'unique',
  validate(directive: DirectiveNode) {
    if (directive.arguments?.length) {
      throw new GraphQLError(`Directive doesn't accept arguments.`, {
        nodes: directive.arguments,
      });
    }
  },
};

const DIRECTIVE_LOCALIZED = {
  NAME: 'localized',
  validate(directive: DirectiveNode) {
    if (directive.arguments?.length) {
      throw new GraphQLError(`Directive doesn't accept arguments.`, {
        nodes: directive.arguments,
      });
    }
  },
};

const DIRECTIVE_FILE = {
  NAME: 'file',
  ARGS: {
    EXTENSION: 'ext',
  },
  validate(directive: DirectiveNode) {
    if (!directive.arguments?.length) {
      throw new GraphQLError('Missing file extension.', { nodes: directive });
    }
    for (const arg of directive.arguments) {
      if (arg.name.value === DIRECTIVE_FILE.ARGS.EXTENSION) {
        if (arg.value.kind !== 'StringValue') {
          throw new GraphQLError(`String expected.`, { nodes: arg.value });
        }
      } else {
        throw new GraphQLError(`Unknown argument "${arg.name.value}".`, {
          nodes: arg.name,
        });
      }
    }
  },
};

const DIRECTIVE_FILES_GROUP = {
  NAME: 'files',
  ARGS: {
    EXTENSION: 'ext',
  },
  validate(directive: DirectiveNode) {
    if (!directive.arguments?.length) {
      throw new GraphQLError('Missing file extensions.', { nodes: directive });
    }
    for (const arg of directive.arguments) {
      if (arg.name.value === DIRECTIVE_FILES_GROUP.ARGS.EXTENSION) {
        if (arg.value.kind !== 'ListValue') {
          throw new GraphQLError(`List of extensions expected.`, {
            nodes: arg.value,
          });
        }
        // NOTE allow empty list
        // if (!arg.value.values.length) {
        //   throw new GraphQLError(`List of extensions cannot be empty.`, arg.value);
        // }
        for (const listValue of arg.value.values) {
          if (listValue.kind !== 'StringValue') {
            throw new GraphQLError(`String expected.`, { nodes: listValue });
          }
        }
      } else {
        throw new GraphQLError(`Unknown argument "${arg.name.value}".`, {
          nodes: arg.name,
        });
      }
    }
  },
};

const DIRECTIVE_ENUM_INDEXING = {
  NAME: 'indexing',
  ARGS: {
    FIRST: 'first',
  },
  validate(directive: DirectiveNode) {
    if (!directive.arguments?.length) {
      throw new GraphQLError('Missing first enumerator index.', {
        nodes: directive,
      });
    }
    for (const arg of directive.arguments) {
      if (arg.name.value === DIRECTIVE_ENUM_INDEXING.ARGS.FIRST) {
        if (
          arg.value.kind !== 'IntValue' ||
          (Number(arg.value.value) !== 0 && Number(arg.value.value) !== 1)
        ) {
          throw new GraphQLError(`Integer 0 or 1 expected.`, {
            nodes: arg.value,
          });
        }
      } else {
        throw new GraphQLError(`Unknown argument "${arg.name.value}".`, {
          nodes: arg.name,
        });
      }
    }
  },
};

const DIRECTIVE_TABLE_TAGS = {
  NAME: 'tags',
  ARGS: {
    LIST: 'list',
  },
  validate(directive: DirectiveNode) {
    if (!directive.arguments?.length) {
      throw new GraphQLError('Missing list of tags.', { nodes: directive });
    }
    for (const arg of directive.arguments) {
      if (arg.name.value === DIRECTIVE_TABLE_TAGS.ARGS.LIST) {
        if (arg.value.kind !== 'ListValue') {
          throw new GraphQLError(`List of tags expected.`, {
            nodes: arg.value,
          });
        }
        if (!arg.value.values.length) {
          throw new GraphQLError(`At least one tag should be in the list.`, {
            nodes: arg.value,
          });
        }
        for (const listValue of arg.value.values) {
          if (listValue.kind !== 'StringValue') {
            throw new GraphQLError(`String expected.`, { nodes: listValue });
          }
        }
      } else {
        throw new GraphQLError(`Unknown argument "${arg.name.value}".`, {
          nodes: arg.name,
        });
      }
    }
  },
};

class VersionedTypedefNode<T> implements Iterable<[ValidFor, T]> {
  constructor (
    public vBase?: T,
    public vOverride?: T,
  ) {}

  *[Symbol.iterator](): Iterator<[ValidFor, T]> {
    if (this.vBase != null && this.vOverride != null) {
      yield [ValidFor.PoE1, this.vBase];
      yield [ValidFor.PoE2, this.vOverride];
    } else if (this.vOverride != null) {
      yield [ValidFor.PoE2, this.vOverride];
    } else if (this.vBase != null) {
      yield [ValidFor.Common, this.vBase];
    }
  }
}

class VersionedTypedefMap<T extends TypeDefinitionNode> {
  readonly data = new Map<string, VersionedTypedefNode<T>>();

  add(typeNode: T, override: boolean): boolean {
    const existingNode = this.data.get(typeNode.name.value);
    if (!existingNode) {
      this.data.set(typeNode.name.value, new VersionedTypedefNode(
        !override ? typeNode : undefined,
        override ? typeNode : undefined,
      ));
    } else if (override) {
      if (existingNode.vOverride != null) return false;
      existingNode.vOverride = typeNode;
    } else {
      if (existingNode.vBase != null) return false;
      existingNode.vBase = typeNode;
    }
    return true;
  }
}

class ScopedTypedefMap<T> {
  constructor (
    private data: ReadonlyMap<string, VersionedTypedefNode<T>>,
    private ver: ValidFor
  ) {
    if (ver === ValidFor.Common) {
      this.ver = ValidFor.PoE1;
    }
  }

  get(name: string): T | undefined {
    const node = this.data.get(name);
    if (node != null) {
      if (this.ver === ValidFor.PoE1) {
        return node.vBase;
      } else {
        return node.vOverride ?? node.vBase;
      }
    }
  }

  has(name: string): boolean {
    return this.get(name) != null;
  }
}

interface Context {
  typeDefsMap: ScopedTypedefMap<ObjectTypeDefinitionNode>;
  enumDefsMap: ScopedTypedefMap<EnumTypeDefinitionNode>;
}

export function readSchemaSources(
  sources: readonly Source[]
): Pick<SchemaFile, 'tables' | 'enumerations'> {
  const typeDefsMap = new VersionedTypedefMap<ObjectTypeDefinitionNode>();
  const enumDefsMap = new VersionedTypedefMap<EnumTypeDefinitionNode>();

  for (const source of sources) {
    const doc = parse(source, { noLocation: false });

    for (const typeNode of doc.definitions) {
      if (typeNode.kind !== 'EnumTypeDefinition' && typeNode.kind !== 'ObjectTypeDefinition') {
        throw new GraphQLError('Unsupported definition.', { nodes: typeNode });
      }

      const override = source.name.startsWith('poe2');
      if (typeNode.kind === 'EnumTypeDefinition') {
        if (!enumDefsMap.add(typeNode, override)) {
          throw new GraphQLError(
            'Enum with this name has already been defined.',
            { nodes: typeNode.name }
          );
        }
      } else if (typeNode.kind === 'ObjectTypeDefinition') {
        if (!typeDefsMap.add(typeNode, override)) {
          throw new GraphQLError(
            'Table with this name has already been defined.',
            { nodes: typeNode.name }
          );
        }
      }
    }
  }

  const tables: SchemaTable[] = [];
  for (const verNode of typeDefsMap.data.values()) {
    for (const [validFor, typeNode] of verNode) {
      const table: SchemaTable = {
        validFor: validFor,
        name: typeNode.name.value,
        columns: [],
        tags: [],
      };

      validateDirectives(typeNode, [DIRECTIVE_TABLE_TAGS]);
      table.tags = getTags(typeNode);

      const ctx: Context = {
        typeDefsMap: new ScopedTypedefMap(typeDefsMap.data, validFor),
        enumDefsMap: new ScopedTypedefMap(enumDefsMap.data, validFor),
      };
      assert.ok(typeNode.fields != null);
      for (const fieldNode of typeNode.fields) {
        const column = parseFieldNode(
          ctx,
          table.name,
          fieldNode
        );
        if (
          column.name != null &&
          table.columns.some((col) => col.name === column.name)
        ) {
          throw new GraphQLError(`Duplicate column name "${column.name}".`, {
            nodes: fieldNode.name,
          });
        }
        table.columns.push(column);
      }

      tables.push(table);
    }
  }

  const enumerations: SchemaEnumeration[] = [];
  for (const verNode of enumDefsMap.data.values()) {
    for (const [validFor, enumNode] of verNode) {
      const enum_ = parseEnumNode(enumNode, validFor);
      enumerations.push(enum_);
    }
  }

  return { tables, enumerations };
}

function parseEnumNode(enumNode: EnumTypeDefinitionNode, validFor: ValidFor) {
  const schemaEnum: SchemaEnumeration = {
    validFor: validFor,
    name: enumNode.name.value,
    indexing: 0,
    enumerators: [],
  };

  validateDirectives(enumNode, [DIRECTIVE_ENUM_INDEXING]);
  {
    const indexingDirective = findDirective(
      enumNode,
      DIRECTIVE_ENUM_INDEXING.NAME
    );
    if (!indexingDirective) {
      throw new GraphQLError('`indexing` directive is required for enums.', {
        nodes: enumNode,
      });
    }
    schemaEnum.indexing = getIndexingBase(enumNode);
  }

  assert.ok(enumNode.values != null);
  for (const valueNode of enumNode.values) {
    if (valueNode.name.value === '_') {
      schemaEnum.enumerators.push(null);
    } else {
      if (schemaEnum.enumerators.includes(valueNode.name.value)) {
        throw new GraphQLError(
          `Duplicate enumerator "${valueNode.name.value}".`,
          { nodes: valueNode.name }
        );
      }
      schemaEnum.enumerators.push(valueNode.name.value);
    }
  }

  if (
    schemaEnum.enumerators.length === 1 &&
    schemaEnum.enumerators[0] === null
  ) {
    schemaEnum.enumerators = [];
  }

  return schemaEnum;
}

function parseFieldNode(
  ctx: Context,
  tableName: string,
  fieldNode: FieldDefinitionNode
): TableColumn {
  validateDirectives(fieldNode, [
    DIRECTIVE_REF,
    DIRECTIVE_UNIQUE,
    DIRECTIVE_LOCALIZED,
    DIRECTIVE_FILE,
    DIRECTIVE_FILES_GROUP,
  ]);

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
    } else if (ctx.enumDefsMap.has(fieldType.name)) {
      references = { table: fieldType.name };
      fieldType.name = 'enumrow' as ColumnType;
    } else {
      throw new GraphQLError(
        `Can't find referenced table/enum "${fieldType.name}".`,
        { nodes: fieldNode.type }
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
        {
          nodes: findDirective(fieldNode, DIRECTIVE_REF.NAME),
          originalError: e as Error,
        }
      );
    }

    if (!refFieldType) {
      throw new GraphQLError(
        `Can't find column "${refFieldName}" in table "${references.table}".`,
        { nodes: findDirective(fieldNode, DIRECTIVE_REF.NAME) }
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

function getIndexingBase(
  node: EnumTypeDefinitionNode
): SchemaEnumeration['indexing'] {
  const directive = findDirective(node, DIRECTIVE_ENUM_INDEXING.NAME);
  assert.ok(directive);

  const { arguments: args } = directive;
  assert.ok(
    args?.length === 1 &&
      args[0].name.value === DIRECTIVE_ENUM_INDEXING.ARGS.FIRST &&
      args[0].value.kind === 'IntValue'
  );
  const first = Number(args[0].value.value);
  assert.ok(first === 0 || first === 1);

  return first;
}

function getTags(node: ObjectTypeDefinitionNode): SchemaTable['tags'] {
  const directive = findDirective(node, DIRECTIVE_TABLE_TAGS.NAME);
  if (!directive) return [];

  const { arguments: args } = directive;
  assert.ok(
    args?.length === 1 &&
      args[0].name.value === DIRECTIVE_TABLE_TAGS.ARGS.LIST &&
      args[0].value.kind === 'ListValue'
  );
  return args[0].value.values.map((listValue) => {
    assert.ok(listValue.kind === 'StringValue');
    return listValue.value;
  });
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
    throw new GraphQLError('Valid type expected.', { nodes: field.type });
  }
  if (type.name.value === '_' && !array) {
    throw new GraphQLError('Unknown type is only allowed inside an array.', {
      nodes: field.type,
    });
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
      throw new GraphQLError('Сannot refer to a column with an array type.', {
        nodes: fieldNode.type,
      });
    }
    if (!isUnique(fieldNode)) {
      throw new GraphQLError(
        'Values in the referenced column must be unique.',
        { nodes: fieldNode }
      );
    }
    if (!ScalarTypes.has(typeInfo.name)) {
      throw new GraphQLError(
        'Сannot refer to a column with a non-scalar type.',
        { nodes: fieldNode.type }
      );
    }

    return typeInfo.name;
  }
}

function validateDirectives(
  node: FieldDefinitionNode | EnumTypeDefinitionNode | ObjectTypeDefinitionNode,
  specs: Array<{ NAME: string; validate: (directive: DirectiveNode) => void }>
): void {
  for (const directive of node.directives ?? []) {
    const spec = specs.find((spec) => spec.NAME === directive.name.value);
    if (spec) {
      spec.validate(directive);
    } else {
      throw new GraphQLError(`Unknown directive "${directive.name.value}".`, {
        nodes: directive.name,
      });
    }
  }
}

function findDirective(
  node: FieldDefinitionNode | EnumTypeDefinitionNode | ObjectTypeDefinitionNode,
  name: string
): DirectiveNode | undefined {
  return (node.directives ?? []).find(
    (directive) => directive.name.value === name
  );
}
