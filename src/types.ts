// incremented only when breaking changes are made
export const SCHEMA_VERSION = 3;

export type ScalarType =
  | 'bool'
  | 'string'
  | 'i32'
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
  name: string;
  columns: TableColumn[];
}

export interface SchemaEnumeration {
  name: string;
  indexing: 0 | 1;
  enumerators: Array<string | null>;
}

export interface SchemaFile {
  version: number;
  createdAt: number;
  tables: SchemaTable[];
  enumerations: SchemaEnumeration[];
}
