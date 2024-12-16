// incremented only when breaking changes are made
export const SCHEMA_VERSION = 5;

export type ScalarType =
  | 'bool'
  | 'string'
  | 'i16'
  | 'u16'
  | 'i32'
  | 'u32'
  | 'f32';

export type ColumnType =
  | ScalarType
  // column is an array of unknown type
  | 'array'
  // row index (references column in same table)
  | 'row'
  // row index (references column in foreign table)
  | 'foreignrow'
  // row index (references foreign table with no columns)
  | 'enumrow';

export interface RefUsingRowIndex {
  table: string;
}

export interface RefUsingColumn {
  table: string;
  column: string;
}

export type FileExtension = string;

// Bitmask
export enum ValidFor {
  PoE1 = 0x01,
  PoE2 = 0x02,
  Common = 0x03,
};

export interface TableColumn {
  name: string | null;
  description: string | null;
  array: boolean;
  type: ColumnType;
  unique: boolean;
  localized: boolean;
  until: string | null;
  references: RefUsingRowIndex | RefUsingColumn | null;
  file: FileExtension | null;
  files: FileExtension[] | null;
}

export interface SchemaTable {
  validFor: ValidFor;
  name: string;
  columns: TableColumn[];
  tags: string[];
}

export interface SchemaEnumeration {
  validFor: ValidFor;
  name: string;
  indexing: 0 | 1;
  enumerators: Array<string | null>;
}

export interface SchemaMetadata {
  version: number;
  createdAt: number;
}

// exported as "schema.min.json"
export interface SchemaFile extends SchemaMetadata {
  tables: SchemaTable[];
  enumerations: SchemaEnumeration[];
}

// exported as "schema.jsonl"
export type SchemaLine =
  | SchemaMetadata
  | SchemaTable
  | SchemaEnumeration;
