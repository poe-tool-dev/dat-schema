
type AtlasExileBossArenas {
  AtlasExilesKey: AtlasExiles
  _: i32
  WorldAreasKey: WorldAreas
}

type AtlasExileInfluence {
  AtlasExilesKey: AtlasExiles
  _: i32
  AtlasExileInfluenceSetsKeys: [AtlasExileInfluenceSets]
}

type AtlasExileInfluenceData {
  AtlasExileInfluenceOutcomeTypesKey: AtlasExileInfluenceOutcomeTypes
  _: [u64]
  _: u64
  _: [u64]
  _: i32
  _: [i32]
  _: [i32]
}

type AtlasExileInfluenceOutcomes {
  Id: string @unique
  _: i32
  AtlasExileInfluenceOutcomeTypesKey: i32
}

enum AtlasExileInfluenceOutcomeTypes { _ }

type AtlasExileInfluenceSets {
  Id: string @unique
  AtlasExileInfluencePacksKey: [u64]
}

type AtlasExileRegionQuestFlags {
  AtlasExilesKey: AtlasExiles
  AtlasRegionsKey: AtlasRegions
  _: i32
  _: rid
  QuestState: i32
}

type AtlasExiles {
  Id: string @unique
  MonsterVarietiesKey: MonsterVarieties
  Art: string
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: rid
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
}
