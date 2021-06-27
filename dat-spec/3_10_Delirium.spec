
type AfflictionBalancePerLevel {
  _: i32
  _: f32
  _: f32
  _: f32
  _: f32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: f32
  _: f32
}

type AfflictionEndgameWaveMods {
  ModsKey: Mods
  _: i32
  _: i32
  _: i32
}

type AfflictionFixedMods {
  _: rid
  ModsKey: Mods
}

type AfflictionRandomModCategories {
  Id: string @unique
  _: i8
}

type AfflictionRewardMapMods {
  ModsKey: Mods
}

# enum?
type AfflictionRewardTypes { TODO_REMOVE_THIS: u8 }

type AfflictionRewardTypeVisuals {
  AfflictionRewardTypes: AfflictionRewardTypes
  Id: string @unique
  Name: string
}

type AfflictionSplitDemons {
  _: i32
  MonsterVarietiesKey: MonsterVarieties
  AfflictionRandomModCategoriesKey: AfflictionRandomModCategories
}

type AfflictionStartDialogue {
  _: rid
  NPCTextAudioKey: NPCTextAudio
  _: [u64]
}
