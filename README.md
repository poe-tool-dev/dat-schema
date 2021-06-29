# PoE dat schema

Source of truth schema for dat files.

## Using

Each commit triggers a CI build that exports schema to JSON.
You can always `curl` latest version at
[github.com/poe-tool-dev/dat-schema/releases/download/latest/schema.min.json](https://github.com/poe-tool-dev/dat-schema/releases/download/latest/schema.min.json)

## Schema

The schema is based on GraphQL syntax.

### Supported scalar types

| Non-nullable type | Nullable type |      Description      |
|-------------------|---------------|-----------------------|
| bool              | -             | Boolean               |
| string!           | string        | String                |
| u64, u32, u16, u8 | -             | Unsigned Integer      |
| i64, i32, i16, i8 | -             | Signed Integer        |
| f64, f32          | -             | Floating Point Number |
| rid!              | rid           | Index to a Row in a Foreign Table |

The `rid` type is intended to be used temporarily until we know the name of foreign table.

The other type for temporary use is `_`, which is only allowed inside array `[_]`.
You will find it useful if you know that a column is an array but don't know of which type (because they are all zero-length).

### Defining relations

- Using a row index

  Example `BaseItem: BaseItemTypes`

- Using a matching value in column (like in relational databases)

  Example `SkillId: ActiveSkills @ref(column: "Id")`

### Supported directives

| Directive  | Arguments | Description |
|------------|-----------|-------------|
| @ref       | column: "STRING" - name of referenced column | Defines relation |
| @unique    | -         | All values in a column are different |
| @localized | -         | Content of column differs depending on the language |
