# PoE dat schema

Source of truth schema for dat files.

## Using

TODO

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

NOTE: the `rid` type is intended to be used temporarily until we know the name of foreign table.

### Defining relations

- Using a row index

  Example `BaseItem: BaseItemTypes`

- Using a matching value (like in relational databases)

  Example `SkillId: ActiveSkills @ref(column: "Id")`

### Supported directives

| Directive | Arguments | Description |
|-----------|-----------|-------------|
| @ref      | column: "STRING" - name of referenced column | Defines relation |
| @unique   | -         | All values in a column are different |
