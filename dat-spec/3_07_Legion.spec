
type Incubators {
  BaseItemTypesKey: BaseItemTypes @unique
  _: i32
  Description: string
  Hash: i32
  AchievementItemsKeys: [AchievementItems]
}

type LegionBalancePerLevel {
  MinLevel: i32
  _: i32
  _: i32
  _: i32
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

type LegionChestCounts {
  LegionFactionsKey: LegionFactions
  LegionRanksKey: LegionRanks
  _: i32
  _: i32
  _: i32
  _: i32
  MinLevel: i32
  _: i32
}

type LegionChests {
  ChestsKey: Chests
  LegionFactionsKey: LegionFactions
  LegionRanksKey: LegionRanks
  _: rid
  _: i32
}

type LegionFactions {
  Id: string @unique
  _: i32
  _: rid
  _: f32
  _: f32
  _: rid
  _: rid
  _: rid
  _: rid
  AchievementItemsKeys1: [AchievementItems]
  _: rid
  _: rid
  _: f32
  _: f32
  AchievementItemsKeys2: [AchievementItems]
}

type LegionMonsterCounts {
  LegionFactionsKey: LegionFactions
  LegionRanksKey: LegionRanks
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

# enum?
type LegionMonsterTypes { TODO_REMOVE_THIS: u8 }

type LegionMonsterVarieties {
  MonsterVarietiesKey: MonsterVarieties
  LegionFactionsKey: LegionFactions
  _: rid
  _: i32
  _: [rid]
  _: i32
  _: i32
  _: [i32]
  _: [i32]
  _: [i32]
  _: [i32]
  _: [i32]
  _: [i32]
  _: i32
  _: i32
  _: [rid]
  _: rid
}

type LegionRanks {
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: rid
  _: i32
  _: i32
}

# enum?
type LegionRankTypes { TODO_REMOVE_THIS: u8 }

# enum?
type LegionRewardTypes { TODO_REMOVE_THIS: u8 }

type LegionRewardTypeVisuals {
  IntId: i32 @unique
  _: rid
  _: string
  MiscAnimatedKey: MiscAnimated
  _: f32
  Id: string
}
