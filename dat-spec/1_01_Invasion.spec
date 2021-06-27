
enum InvasionMonsterGroups { _ }

type InvasionMonsterRestrictions {
  Id: string @unique
  WorldAreasKey: WorldAreas
  MonsterVarietiesKeys: [MonsterVarieties]
  _: [i32]
}

enum InvasionMonsterRoles { _ }

type InvasionMonstersPerArea {
  WorldAreasKey: WorldAreas
  _: i32
  _: [i32]
  MonsterVarietiesKeys1: [MonsterVarieties]
  MonsterVarietiesKeys2: [MonsterVarieties]
  _: i32
  _: i32
  _: i32
  _: i32
}
