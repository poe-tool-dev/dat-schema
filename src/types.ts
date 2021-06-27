export const SCHEMA_VERSION = 1;

export type ScalarType =
  | 'bool'
  | 'string'
  | 'u64'
  | 'u32'
  | 'u16'
  | 'u8'
  | 'i64'
  | 'i32'
  | 'i16'
  | 'i8'
  | 'f64'
  | 'f32';

export type ColumnType = ScalarType | 'row' | 'foreignrow';

export interface TableColumn {
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

export interface SchemaTable {
  name: string;
  columns: TableColumn[];
}

// interface SchemaEnum {
//   name: string;
//   enum: string[];
// }
