
type BlightBalancePerLevel {
  Level: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

type BlightBossLifeScalingPerLevel {
  Level: i32
  MoreLife: i32
}

type BlightChestTypes {
  ChestsKey: Chests
}

type BlightCraftingItems {
  BaseItemTypesKey: BaseItemTypes @unique
  Tier: i32
  AchievementItemsKeys: [AchievementItems]
}

type BlightCraftingRecipes {
  Id: string @unique
  BlightCraftingItemsKeys: [BlightCraftingItems]
  BlightCraftingResultsKey: BlightCraftingResults
  BlightCraftingTypesKey: BlightCraftingTypes
}

type BlightCraftingResults {
  Id: string @unique
  ModsKey: Mods
  PassiveSkillsKey: PassiveSkills
}

type BlightCraftingTypes {
  Id: string @unique
  _: i32
  _: bool
}

type BlightCraftingUniques {
  _: u64
}

type BlightedSporeAuras {
  _: rid
  _: [i32]
  _: i32
  _: [i32]
  _: i32
}

type BlightEncounterTypes {
  Id: string @unique
  Icon: string
  IsGeneric: i8
  Weight: i32
}

type BlightEncounterWaves {
  MonsterSpawnerId: string
  _: rid
  _: i32
  _: i32
  _: i32
  _: i32
}

type BlightRewardTypes {
  Id: string @unique
  Icon: string
}

type BlightTopologies {
  Id: string @unique
  _: rid
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

type BlightTopologyNodes {
  Id: string @unique
  _: [i32]
  Size: i32
  Type: string
  _: [i32]
  _: [i32]
  _: [i32]
  _: [i32]
  _: [i32]
  _: [i32]
}

type BlightTowerAuras {
  Id: i32 @unique
  BuffDefinitionsKey: BuffDefinitions
  _: i32
  MiscAnimatedKey: MiscAnimated
}

type BlightTowers {
  Id: string @unique
  Name: string
  Description: string
  Icon: string
  _: [i32]
  _: i32
  Tier: string
  Radius: i32
  _: i32
  SpendResourceAchievementItemsKey: AchievementItems
  StatsKey: Stats
  StatsKeys: [Stats]
  _: [rid]
  _: bool
}

type BlightTowersPerLevel {
  BlightTowersKey: BlightTowers
  _: i32
  MonsterVarietiesKey: MonsterVarieties
  Cost: i32
  _: i32
}
