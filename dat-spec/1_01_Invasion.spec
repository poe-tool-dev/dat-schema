
# enum?
type InvasionMonsterGroups { TODO_REMOVE_THIS: u8 }

type InvasionMonsterRestrictions {
  Id: string @unique
  WorldAreasKey: WorldAreas
  MonsterVarietiesKeys: [MonsterVarieties]
  _: [i32]
}

# enum?
type InvasionMonsterRoles { TODO_REMOVE_THIS: u8 }

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
