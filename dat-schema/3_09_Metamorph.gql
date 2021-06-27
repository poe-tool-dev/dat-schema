
type AlternateQualityCurrencyDecayFactors {
  BaseItemTypesKey: BaseItemTypes
  Factor: i32
}

type AlternateQualityTypes {
  StatsKey: Stats
  Description: string
  BaseItemTypesKey: BaseItemTypes
  ModsKey: Mods
}

type MetamorphLifeScalingPerLevel {
  Level: i32
  MoreLife: i32
}

type MetamorphosisMetaMonsters {
  MonsterVarietiesKey: MonsterVarieties
  _: [u64]
  _: [i32]
  Name: string
}

type MetamorphosisMetaSkills {
  _: u64
  _: u64
  _: u64
  _: [u64]
  _: [i32]
  _: u64
  _: u64
  _: [u64]
  _: [i32]
  _: i32
  _: u64
  _: [i32]
  _: i32
  _: u64
  _: i32
  _: string
  _: [u64]
  _: string
  _: i32
  _: [u64]
  _: i32
  _: i32
  _: [i32]
  _: [u64]
  _: [i32]
  _: [u64]
  _: [u64]
  _: bool
}

type MetamorphosisMetaSkillTypes {
  Id: string @unique
  Name: string
  Description: string
  UnavailableArt: string
  _: string
  AvailableArt: string
  BaseItemTypesKey: u64
  BodypartName: string
  _: i32
  AchievementItemsKeys: [AchievementItems]
  BodypartNamePlural: string
  _: i32
}

type MetamorphosisRewardTypeItemsClient {
  MetamorphosisRewardTypesKey: MetamorphosisRewardTypes
  _: i32
  Description: string
}

type MetamorphosisRewardTypes {
  Id: string @unique
  Art: string
  Name: string
  AchievementItemsKeys: [AchievementItems]
}

type MetamorphosisScaling {
  Level: i32
  StatValueMultiplier: f32
  Scaling_StatsKeys: [Stats]
  Scaling_Values: [i32]
  _: i32
}
