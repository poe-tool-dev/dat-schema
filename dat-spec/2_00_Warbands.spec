
type WarbandsGraph {
  WorldAreasKey: WorldAreas
  Connections: [i32]
}

type WarbandsMapGraph {
  WorldAreasKey: WorldAreas
  Connections: [i32]
}

type WarbandsPackMonsters {
  Id: string @unique
  _: i64
  _: i32
  Tier4_MonsterVarietiesKeys: [MonsterVarieties]
  Tier3_MonsterVarietiesKeys: [MonsterVarieties]
  Tier2_MonsterVarietiesKeys: [MonsterVarieties]
  Tier1_MonsterVarietiesKeys: [MonsterVarieties]
  Tier1Name: string
  Tier2Name: string
  Tier3Name: string
  Tier4Name: string
  Tier1Art: string
  Tier2Art: string
  Tier3Art: string
  Tier4Art: string
}

type WarbandsPackNumbers {
  Id: string @unique
  SpawnChance: i32
  MinLevel: i32
  MaxLevel: i32
  Tier4Number: i32
  _: i32
  Tier3Number: i32
  _: i32
  Tier2Number: i32
  _: i32
  Tier1Number: i32
}
