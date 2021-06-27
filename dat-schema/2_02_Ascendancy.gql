
type LabyrinthAreas {
  Id: string
  Normal_WorldAreasKeys: [WorldAreas]
  Cruel_WorldAreasKeys: [WorldAreas]
  Merciless_WorldAreasKeys: [WorldAreas]
  Endgame_WorldAreasKeys: [WorldAreas]
  _: i32
}

type LabyrinthBonusItems {
  _: rid
  _: i32
  _: string
}

type LabyrinthExclusionGroups {
  _: i32
}

type LabyrinthIzaroChests {
  Id: string @unique
  ChestsKey: Chests
  SpawnWeight: i32
  MinLabyrinthTier: i32
  MaxLabyrinthTier: i32
}

type LabyrinthNodeOverrides {
  Id1: string
  Id2: string
  _: [i32]
  _: [i32]
}

type LabyrinthRewardTypes {
  Id: string @unique
  ObjectPath: string
}

type Labyrinths {
  Tier: i32 @unique
  Name: string
  _: rid
  QuestState: i32
  _: [rid]
  AreaLevel: i32
  _: i32
  _: rid
  _: [i32]
  _: [i32]
  MinLevel: i32
  _: i32
  _: i32
  _: rid
}

type LabyrinthSecretEffects {
  Id: string
  MonsterVarietiesKey: MonsterVarieties
  Buff_BuffDefinitionsKey: BuffDefinitions
  Buff_StatValues: [i32]
  OTFile: string
}

enum LabyrinthSecretLocations { _ }

type LabyrinthSecrets {
  Id: string
  Id2: string
  _: [i32]
  _: i32
  _: i32
  LabyrinthSecretEffectsKeys0: [LabyrinthSecretEffects]
  LabyrinthSecretEffectsKeys1: [LabyrinthSecretEffects]
  LabyrinthSecretEffectsKeys2: [LabyrinthSecretEffects]
  _: i32
  LabyrinthSecretEffectsKeys3: [LabyrinthSecretEffects]
  _: i8
  _: i8
  _: i32
  _: i8
  _: i8
  _: i8
  Name: string
  AchievementItemsKey: AchievementItems
  LabyrinthTierMinimum: i32
  LabyrinthTierMaximum: i32
  _: bool
}

type LabyrinthSection {
  Id: string
  _: rid
  _: i32
  _: i32
  _: i32
  _: i32
}

type LabyrinthSectionLayout {
  LabyrinthSectionKey: LabyrinthSection
  _: i32
  LabyrinthSectionLayoutKeys: [LabyrinthSectionLayout]
  LabyrinthSecretsKey0: LabyrinthSecrets
  LabyrinthSecretsKey1: LabyrinthSecrets
  LabyrinthAreasKey: LabyrinthAreas
  Float0: f32
  Float1: f32
  LabyrinthNodeOverridesKeys: [LabyrinthNodeOverrides]
}

type LabyrinthTrials {
  WorldAreas: WorldAreas
  _: i32
  _: i32
  _: i32
  NPCTextAudioKey: NPCTextAudio
  _: string
  _: string
}

type LabyrinthTrinkets {
  BaseItemTypesKey: BaseItemTypes @unique
  LabyrinthSecretsKey: [LabyrinthSecrets]
  Buff_BuffDefinitionsKey: BuffDefinitions
  Buff_StatValues: [i32]
}
