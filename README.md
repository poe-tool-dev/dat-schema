# PoE dat schema

Source of truth schema for dat files.

## Using

Each commit triggers a CI build that exports schema to JSON.
You can always `curl` latest version at
[github.com/poe-tool-dev/dat-schema/releases/download/latest/schema.min.json](https://github.com/poe-tool-dev/dat-schema/releases/download/latest/schema.min.json)

Structure of JSON file is described in [src/types.ts](https://github.com/poe-tool-dev/dat-schema/blob/main/src/types.ts)

## Schema

The schema is based on GraphQL syntax.

### Supported scalar types

| Type     | Description                       |
|----------|-----------------------------------|
| bool     | Boolean                           |
| string   | String                            |
| i16, i32 | Signed Integer                    |
| u16, u32 | Unsigned Integer                  |
| f32      | Floating Point Number             |
| rid      | Index to a Row in a Foreign Table |

The `rid` type is intended to be used temporarily until we know the name of foreign table.

The other type for temporary use is `_`, which is only allowed inside array `[_]`.
You will find it useful if you know that a column is an array but don't know of which type (because they are all zero-length).

### Defining relations

- Using a row index

  Example `BaseItem: BaseItemTypes`

- Using a matching value in column (like in relational databases)

  Example `SkillId: ActiveSkills @ref(column: "Id")`

### Supported directives

| Directive               | Description |
|-------------------------|-------------|
| `@ref(column: String)`  | Defines a relation |
| `@unique`               | All values in a column are different |
| `@localized`            | Content of column differs depending on the language |
| `@file(ext: String)`    | Value in a column is a file path |
| `@files(ext: [String])` | Value in a column is a common prefix for several files (often with different extensions) |
| `@tags(list: [String])` | Add tags to the table as metadata that can be used by tools |
