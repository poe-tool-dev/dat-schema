// incremented only when breaking changes are made
export const SCHEMA_VERSION = 2;

export type ScalarType =
  | 'bool'
  | 'string'
  | 'u32'
  | 'i32'
  | 'f32';

export type ColumnType =
  | ScalarType
  // column is an array of unknown type
  | 'array'
  // row index (references column in same table)
  | 'row'
  // row index (references column in foreign table)
  | 'foreignrow';

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

// interface SchemaEnum {
//   name: string;
//   enum: string[];
// }

export interface SchemaFile {
  version: number;
  createdAt: number;
  tables: SchemaTable[];
}
