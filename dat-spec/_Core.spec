
# enum?
type AccountQuestFlags { TODO_REMOVE_THIS: u8 }

type AchievementItemRewards {
  AchievementItemsKey: AchievementItems
  BaseItemTypesKey: BaseItemTypes
  Message: string
}

type AchievementItems {
  Id: string @unique
  _: i32
  _: i32
  Name: string
  CompletionsRequired: i32
  AchievementsKey: Achievements
  _: bool
  _: bool
  _: bool
}

type Achievements {
  Id: string @unique
  Description: string
  AchievementSetsDisplayKey: AchievementSetsDisplay @ref(column: "Id")
  Objective: string
  _: i32 @unique
  _: bool
  _: bool
  _: bool
  _: i32
  _: bool
  _: bool
  _: string
  _: bool
  _: bool
  _: bool
  _: string
}

type AchievementSetRewards {
  AchievementSetsDisplayKey: AchievementSetsDisplay @ref(column: "Id")
  _: i32
  BaseItemTypesKeys: [BaseItemTypes]
  _: i32
  Message: string
  DDSFile: string
}

# enum?
type AchievementSets { TODO_REMOVE_THIS: u8 }

type AchievementSetsDisplay {
  Id: i32 @unique
  Title: string
}

type ActiveSkills {
  Id: string! @unique
  DisplayedName: string
  Description: string
  _: string
  Icon_DDSFile: string
  ActiveSkillTargetTypes: [u32]
  ActiveSkillTypes: [u32]
  WeaponRestriction_ItemClassesKeys: [ItemClasses]
  WebsiteDescription: string
  WebsiteImage: string
  _: bool
  _: string
  _: bool
  SkillTotemId: i32
  IsManuallyCasted: bool
  Input_StatKeys: [Stats]
  Output_StatKeys: [Stats]
  MinionActiveSkillTypes: [i32]
  _: bool
  _: bool
  _: [rid]
  _: i32
  _: rid
  _: bool
  AIFile: string
  _: i32
  _: i32
  _: bool
  _: bool
}

# enum?
type ActiveSkillTargetTypes { TODO_REMOVE_THIS: u8 }

# enum?
type ActiveSkillType { TODO_REMOVE_THIS: u8 }

type AddBuffToTargetVarieties {
  _: rid
  _: [i32]
  StatsKeys: [Stats]
  _: i32
  _: [i32]
  _: i32
  _: i32
  _: [i32]
}

type AdditionalLifeScaling {
  IntId: i32
  ID: string
  DatFile: string
}

# enum?
type AdditionalLifeScalingPerLevel { TODO_REMOVE_THIS: u8 }

type AdditionalMonsterPacksFromStats {
  StatsKey: Stats
  _: i32
  MonsterPacksKeys: [MonsterPacks]
  AdditionalMonsterPacksStatMode: i32
  PackCountStatsKey: Stats
  StatsKeys: [Stats]
  StatsValues: [i32]
  _: i32
}

# enum?
type AdditionalMonsterPacksStatMode { TODO_REMOVE_THIS: u8 }

type AdvancedSkillsTutorial {
  Id: string @unique
  _: [rid]
  _: [rid]
  Description: string
  International_BK2File: string
  _: rid
  China_BK2File: string
  CharactersKey: [Characters]
}

# enum?
type AlternateBehaviourTypes { TODO_REMOVE_THIS: u8 }

type AlternatePassiveAdditions {
  Id: string @unique
  AlternateTreeVersionsKey: AlternateTreeVersions
  SpawnWeight: i32
  StatsKeys: [Stats]
  Stat1Min: i32
  Stat1Max: i32
  _: i32
  _: i32
  _: i32
  _: i32
  PassiveType: [i32]
  _: i32
}

type AlternatePassiveSkills {
  Id: string @unique
  AlternateTreeVersionsKey: AlternateTreeVersions
  Name: string
  PassiveType: [i32]
  StatsKeys: [Stats]
  Stat1Min: i32
  Stat1Max: i32
  Stat2Min: i32
  Stat2Max: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  SpawnWeight: i32
  _: i32
  RandomMin: i32
  RandomMax: i32
  FlavourText: string
  DDSIcon: string
  AchievementItemsKeys: [AchievementItems]
  _: i32
  _: i32
}

type AlternateSkillTargetingBehaviours {
  Id: string @unique
  _: i32
  _: rid
  _: i32
  _: i32
  _: i32
  _: [i32]
}

# enum?
type AlternateTreePassiveSizes { TODO_REMOVE_THIS: u8 }

type AlternateTreeVersions {
  Id: string @unique
  _: i8
  _: i8
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

type Animation {
  Id: string! @unique
  _: bool
  _: bool
  IntId: i32 @unique
  _: bool
  Mainhand_AnimationKey: Animation @ref(column: "Id")
  Offhand_AnimationKey: Animation @ref(column: "Id")
}

type ApplyDamageFunctions {
  Id: string @unique
  StatsKeys: [Stats]
  _: bool
}

type ArchetypeRewards {
  Id: string @unique
  _: rid
  _: [rid]
  _: rid
  BK2File: string
}

type Archetypes {
  Id: string
  CharactersKey: Characters
  PassiveSkillTreeURL: string
  AscendancyClassName: string
  Description: string
  UIImageFile: string
  TutorialVideo_BKFile: string
  _: i32
  _: f32
  _: f32
  BackgroundImageFile: string
  IsTemporary: bool
  _: bool
  ArchetypeImage: string
  _: bool
  _: bool
}

type AreaInfluenceDoodads {
  StatsKey: Stats
  StatValue: i32
  _: f32
  AOFiles: [string]
  _: i32
  _: i8
}

type AreaTransitionAnimations {
  Id: string @unique
  AnimationId: string
}

type AreaTransitionAnimationTypes {
  Id: string @unique
}

type AreaTransitionInfo {
  _: rid
  _: rid
  _: i32
  _: i32
  _: i32
  _: i32
  _: rid
  _: rid
  _: rid
  _: rid
  _: rid
  _: rid
  _: rid
  _: [rid]
  _: i32
  _: [rid]
}

# enum?
type AreaType { TODO_REMOVE_THIS: u8 }

# enum?
type ArmourClasses { TODO_REMOVE_THIS: u8 }

# enum?
type ArmourSurfaceTypes { TODO_REMOVE_THIS: u8 }

type ArmourTypes {
  BaseItemTypesKey: BaseItemTypes
  IncreasedMovementSpeed: i32
}

type Ascendancy {
  Id: string @unique
  ClassNo: i32
  CharactersKey: Characters
  CoordinateRect: string
  RGBFlavourTextColour: string
  Name: string
  FlavourText: string
  OGGFile: string
}

type AtlasAwakeningStats {
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

type AtlasBaseTypeDrops {
  Id: string @unique
  AtlasRegionsKey: AtlasRegions
  MinTier: i32
  MaxTier: i32
  SpawnWeight_TagsKeys: [Tags]
  SpawnWeight_Values: [i32]
}

type AtlasFog {
  _: i32
  _: i32
  _: i32
  _: i32
}

type AtlasInfluenceOutcomes {
  Id: string @unique
  _: i32
  _: i32
  _: i32
  _: i32
  _: rid
  ModsKeys: [Mods]
}

type AtlasMods {
  ModsKey: Mods
  AtlasModTiers: i32
}

# enum?
type AtlasModTiers { TODO_REMOVE_THIS: u8 }

type AtlasNode {
  WorldAreasKey: WorldAreas
  ItemVisualIdentityKey: ItemVisualIdentity
  _: i8
  MapsKey: Maps
  _: i32
  FlavourTextKey: FlavourText
  AtlasRegionsKey: AtlasRegions
  AtlasNodeKeys0: [AtlasNode]
  AtlasNodeKeys1: [AtlasNode]
  AtlasNodeKeys2: [AtlasNode]
  AtlasNodeKeys3: [AtlasNode]
  AtlasNodeKeys4: [AtlasNode]
  Tier0: i32
  Tier1: i32
  Tier2: i32
  Tier3: i32
  Tier4: i32
  X0: f32
  X1: f32
  X2: f32
  X3: f32
  X4: f32
  Y0: f32
  Y1: f32
  Y2: f32
  Y3: f32
  Y4: f32
  _: f32
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
  _: i32
  _: i32
  X: f32
  Y: f32
  DDSFile: string
}

type AtlasNodeDefinition {
  WorldAreasKey: WorldAreas
  ItemVisualIdentityKey: ItemVisualIdentity
  _: bool
  Tier: i32
  _: i32
  _: i32
}

type AtlasPositions {
  _: i32
  _: i32
  X: f32
  Y: f32
}

# enum?
type AtlasQuadrant { TODO_REMOVE_THIS: u8 }

type AtlasRegions {
  Id: string @unique
  Name: string
  _: i32
  _: i32
  _: i32
}

type AtlasSector {
  Id: string @unique
  SpawnWeight_TagsKeys: [Tags]
  SpawnWeight_Values: [i32]
}

# enum?
type Attributes { TODO_REMOVE_THIS: u8 }

type AwardDisplay {
  Id: string @unique
  Text: string
  BackgroundImage: string
  _: i32
  _: f32
  _: f32
  _: string
  _: string
  ForegroundImage: string
  OGGFile: string
  _: i32
}

type BackendErrors {
  Id: string @unique
  Text: string
}

type BaseItemTypes {
  Id: string! @unique
  ItemClassesKey: ItemClasses
  Width: i32
  Height: i32
  Name: string
  InheritsFrom: string
  DropLevel: i32
  FlavourTextKey: FlavourText
  Implicit_ModsKeys: [Mods]
  _: i32
  SoundEffectsKey: SoundEffects
  NormalPurchase_BaseItemTypesKeys: [BaseItemTypes]
  NormalPurchase_Costs: [i32]
  MagicPurchase_BaseItemTypesKeys: [BaseItemTypes]
  MagicPurchase_Costs: [i32]
  TagsKeys: [Tags]
  ModDomainsKey: i32
  _: bool
  ItemVisualIdentityKey: ItemVisualIdentity
  _: u32 @unique
  VendorRecipe_AchievementItemsKeys: [AchievementItems]
  RarePurchase_BaseItemTypesKeys: [BaseItemTypes]
  RarePurchase_Costs: [i32]
  UniquePurchase_BaseItemTypesKeys: [BaseItemTypes]
  UniquePurchase_Costs: [i32]
  Inflection: string
  Equip_AchievementItemsKey: AchievementItems
  IsCorrupted: bool
  Identify_AchievementItemsKeys: [AchievementItems]
  ItemThemesKey: ItemThemes
  IdentifyMagic_AchievementItemsKeys: [AchievementItems]
  FragmentBaseItemTypesKey: BaseItemTypes
  IsBlessing: bool
  _: rid
  _: rid
  _: rid
}

type BindableVirtualKeys {
  KeyCode: i32
  Name: string
  Id: string
}

type BlightStashTabLayout {
  Id: string @unique
  BaseItemTypesKey: BaseItemTypes
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i8
  _: i8
  _: i8
}

type BloodTypes {
  Id: string @unique
  PETFile1: string
  PETFile2: string
  PETFile3: string
  _: rid
  PETFile4: string
  PETFile5: string
  PETFile6: string
  _: rid
  _: [rid]
  _: rid
  PETFile7: string
  PETFile8: string
  PETFile9: string
}

# enum?
type BuffCategories { TODO_REMOVE_THIS: u8 }

type BuffDefinitions {
  Id: string @unique
  Description: string
  Invisible: bool
  Removable: bool
  Name: string
  StatsKeys: [Stats]
  _: bool
  _: i32
  _: bool
  Maximum_StatsKey: Stats
  Current_StatsKey: Stats
  _: bool
  _: i32
  BuffVisualsKey: BuffVisuals
  _: bool
  _: bool
  _: i32
  _: bool
  _: bool
  _: bool
  _: bool
  BuffLimit: i32
  _: bool
  Id2: string
  IsRecovery: bool
  _: bool
  _: bool
  _: rid
  _: i8
  _: i32
  _: i8
  _: i8
  _: i32
  _: [i32]
  _: bool
  _: bool
  _: rid
  _: bool
  _: [rid]
  _: [rid]
  _: [rid]
  _: [rid]
}

# enum?
type BuffGroups { TODO_REMOVE_THIS: u8 }

# enum?
type BuffMergeModes { TODO_REMOVE_THIS: u8 }

# enum?
type BuffStackUIModes { TODO_REMOVE_THIS: u8 }

type BuffVisualOrbArt {
  Id: string @unique
  _: rid
  _: [string]
  _: [string]
  _: string
  _: string
}

type BuffVisualOrbs {
  Id: string @unique
  BuffVisualOrbTypesKey: BuffVisualOrbTypes
  BuffVisualOrbArtKeys: [BuffVisualOrbArt]
  Player_BuffVisualOrbArtKeys: [BuffVisualOrbArt]
  BuffVisualOrbArtKeys2: [BuffVisualOrbArt]
}

type BuffVisualOrbTypes {
  Id: string @unique
  _: f32
  _: f32
  _: f32
  _: f32
  _: i32
  _: bool
  _: rid
  _: rid
  _: i32
  _: bool
}

type BuffVisuals {
  Id: string @unique
  BuffDDSFile: string
  EPKFiles1: [string]
  EPKFiles2: [string]
  MiscAnimatedKeys1: [MiscAnimated]
  _: bool
  BuffName: string
  _: rid
  _: rid
  BuffDescription: string
  EPKFile: string
  HasExtraArt: bool
  ExtraArt: string
  _: [i32]
  EPKFiles: [string]
  _: [rid]
}

type BuffVisualSetEntries {
  Id: string @unique
  _: i32
  _: rid
  _: i32
}

# enum?
type BuffVisualSets { TODO_REMOVE_THIS: u8 }

type CharacterAudioEvents {
  Id: string @unique
  QuestState: i32
  _: i32
  _: i32
  Marauder_CharacterTextAudioKeys: [CharacterTextAudio]
  Ranger_CharacterTextAudioKeys: [CharacterTextAudio]
  Witch_CharacterTextAudioKeys: [CharacterTextAudio]
  Duelist_CharacterTextAudioKeys: [CharacterTextAudio]
  Shadow_CharacterTextAudioKeys: [CharacterTextAudio]
  Templar_CharacterTextAudioKeys: [CharacterTextAudio]
  Scion_CharacterTextAudioKeys: [CharacterTextAudio]
  Goddess_CharacterTextAudioKeys: [CharacterTextAudio]
  JackTheAxe_CharacterTextAudioKeys: [CharacterTextAudio]
  _: bool
}

type CharacterPanelDescriptionModes {
  Id: string @unique
  _: string
  FormatString_Positive: string
  FormatString_Negative: string
}

# enum?
type CharacterPanelStatContexts { TODO_REMOVE_THIS: u8 }

type CharacterPanelStats {
  Id: string @unique
  Text: string
  StatsKeys1: [Stats]
  CharacterPanelDescriptionModesKey: CharacterPanelDescriptionModes
  StatsKeys2: [Stats]
  StatsKeys3: [Stats]
  CharacterPanelTabsKey: CharacterPanelTabs
  _: bool
  _: [u32]
}

type CharacterPanelTabs {
  Id: string @unique
  _: i32
  Text: string
}

type Characters {
  Id: string @unique
  Name: string @unique
  AOFile: string
  ACTFile: string
  BaseMaxLife: i32
  BaseMaxMana: i32
  WeaponSpeed: i32
  MinDamage: i32
  MaxDamage: i32
  MaxAttackDistance: i32
  Icon: string
  IntegerId: i32 @unique
  BaseStrength: i32
  BaseDexterity: i32
  BaseIntelligence: i32
  _: [rid]
  Description: string
  StartSkillGem_SkillGemsKey: SkillGems
  _: i32
  _: i32
  _: i32
  _: i32
  CharacterSize: i32
  IntroSoundFile: string
  StartWeapon_BaseItemTypesKey: BaseItemTypes
  _: i32
  TraitDescription: string
  _: rid
  _: rid
  _: rid
  _: rid
  _: i32
  _: [rid]
}

type CharacterStartQuestState {
  Id: string
  QuestKeys: [Quest]
  QuestStates: [i32]
  _: [rid]
  MapPinsKeys: [MapPins]
  _: [i32]
  _: [rid]
}

type CharacterStartStates {
  Id: string @unique
  Description: string
  CharactersKey: Characters
  Level: i32
  PassiveSkillsKeys: [PassiveSkills]
  IsPVP: bool
  CharacterStartStateSetKey: CharacterStartStateSet
  _: rid
  CharacterStartQuestStateKeys: [CharacterStartQuestState]
  Bool0: i8
  InfoText: string
  _: rid
}

type CharacterStartStateSet {
  Id: string
}

type CharacterTextAudio {
  Id: string @unique
  Text: string
  SoundFile: string
}

type ChestClusters {
  Id: string @unique
  ChestsKeys: [Chests]
  _: [u32]
  _: i32
  _: i32
  _: i32
}

type ChestEffects {
  Id: string @unique
  Normal_EPKFile: string
  Normal_Closed_AOFile: string
  Normal_Open_AOFile: string
  Magic_EPKFile: string
  Unique_EPKFile: string
  Rare_EPKFile: string
  Magic_Closed_AOFile: string
  Unique_Closed_AOFile: string
  Rare_Closed_AOFile: string
  Magic_Open_AOFile: string
  Unique_Open_AOFile: string
  Rare_Open_AOFile: string
}

type Chests {
  Id: string @unique
  _: bool
  _: i32
  Name: string
  AOFiles: [string]
  _: bool
  _: bool
  _: i32
  _: bool
  _: bool
  _: i32
  _: [u64]
  _: [u32]
  BaseItemTypesKey: BaseItemTypes
  _: bool
  ModsKeys: [Mods]
  TagsKeys: [Tags]
  ChestEffectsKey: ChestEffects
  MinLevel: i32
  _: string
  MaxLevel: i32
  Corrupt_AchievementItemsKey: AchievementItems
  CurrencyUse_AchievementItemsKey: AchievementItems
  Encounter_AchievementItemsKeys: [AchievementItems]
  _: rid
  InheritsFrom: string
  _: bool
  _: rid
}

type ClientStrings {
  Id: string @unique
  Text: string
  XBoxText: string
  _: i32
  PlaystationText: string
}

# enum?
type ClientUIScreens { TODO_REMOVE_THIS: u8 }

type CloneShot {
  Id: string @unique
  MonsterVarietiesKey: MonsterVarieties
  _: rid
  _: rid
  _: rid
}

type Commands {
  Id: string @unique
  Command: string
  _: bool
  Command2: string
  Description: string
  _: bool
}

type ComponentArmour {
  BaseItemTypesKey: BaseItemTypes @ref(column: "Id") @unique
  Armour: i32
  Evasion: i32
  EnergyShield: i32
  IncreasedMovementSpeed: i32
}

type ComponentAttributeRequirements {
  BaseItemTypesKey: BaseItemTypes @ref(column: "Id") @unique
  ReqStr: i32
  ReqDex: i32
  ReqInt: i32
}

type ComponentCharges {
  BaseItemTypesKey: BaseItemTypes @ref(column: "Id") @unique
  MaxCharges: i32
  PerCharge: i32
}

# enum?
type CooldownBypassTypes { TODO_REMOVE_THIS: u8 }

# enum?
type CooldownGroups { TODO_REMOVE_THIS: u8 }

type CostTypes {
  Id: string
  StatsKey: Stats
  FormatText: string
}

# enum?
type CraftingBenchCustomActions { TODO_REMOVE_THIS: u8 }

type CraftingBenchOptions {
  HideoutNPCsKey: HideoutNPCs
  Order: i32
  ModsKey: Mods
  Cost_BaseItemTypesKeys: [BaseItemTypes]
  Cost_Values: [u32]
  RequiredLevel: i32
  Name: string
  CraftingBenchCustomAction: i32
  ItemClassesKeys: [ItemClasses]
  Links: i32
  SocketColours: string
  Sockets: i32
  ItemQuantity: i32
  _: [i32]
  Description: string
  IsDisabled: bool
  IsAreaOption: bool
  RecipeIds: [RecipeUnlockDisplay] @ref(column: "RecipeId")
  Tier: i32
  ModFamily: string
  CraftingItemClassCategoriesKeys: [CraftingItemClassCategories]
  MaximumMapTier: i32
  CraftingBenchUnlockCategoriesKey: CraftingBenchUnlockCategories
  UnveilsRequired: i32
  UnveilsRequired2: i32
  AffixType: string
  _: [rid]
  _: [rid]
  AchievementItemsKeys: [AchievementItems]
  _: i32
  _: i32
  _: bool
  _: u64
}

type CraftingBenchUnlockCategories {
  Id: string
  _: i32
  _: [i32]
  UnlockType: string
  CraftingItemClassCategoriesKeys: [CraftingItemClassCategories]
  ObtainingDescription: string
}

type CraftingItemClassCategories {
  Id: string
  ItemClassesKeys: [ItemClasses]
  _: string
  Text: string
}

type CurrencyItems {
  BaseItemTypesKey: BaseItemTypes @unique
  Stacks: i32
  CurrencyUseType: i32
  Action: string
  Directions: string
  FullStack_BaseItemTypesKey: BaseItemTypes
  Description: string
  Usage_AchievementItemsKeys: [AchievementItems]
  _: bool
  CosmeticTypeName: string
  Possession_AchievementItemsKey: AchievementItems
  _: [rid]
  _: [i32]
  CurrencyTab_StackSize: i32
  XBoxDirections: string
  _: i32
  _: rid
  _: rid
  AchievementItemsKeys: [AchievementItems]
  _: [rid]
  _: rid
}

type CurrencyStashTabLayout {
  Id: string
  BaseItemTypesKey: BaseItemTypes
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: bool
}

# enum?
type CurrencyUseTypes { TODO_REMOVE_THIS: u8 }

type CustomLeagueMods {
  Id: string @unique
  _: [rid]
  _: [i32]
  _: bool
  _: bool
  _: i32
  _: rid
  _: i32
  _: rid
  _: i32
}

type DamageHitEffects {
  _: i32
  _: i32
  _: [rid]
  _: i32
  _: i32
  _: [string]
  _: [string]
}

type DamageParticleEffects {
  DamageParticleEffectTypes: DamageParticleEffectTypes
  Variation: i32
  PETFile: string
  _: rid
  _: rid
  _: i32
}

# enum?
type DamageParticleEffectTypes { TODO_REMOVE_THIS: u8 }

type Dances {
  BaseItemTypesKey: BaseItemTypes
  CharactersKey: Characters
}

type DaressoPitFights {
  Id: string @unique
  _: rid
  _: i32
  _: [i32]
  _: bool
  _: bool
  _: i32
  _: i32
  _: i32
  _: bool
}

# enum?
type Default { TODO_REMOVE_THIS: u8 }

type DefaultMonsterStats {
  DisplayLevel: string
  Damage: f32
  Evasion: i32
  Accuracy: i32
  Life: i32
  Experience: i32
  AllyLife: i32
  _: i32
  Difficulty: i32
  Damage2: f32
  _: i32
  _: f32
  _: f32
  _: i32
  _: i32
  Armour: i32
}

type DeliriumStashTabLayout {
  Id: string @unique
  _: rid
  X: i32
  Y: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

type DelveStashTabLayout {
  Id: string @unique
  BaseItemTypesKey: BaseItemTypes
  X: i32
  Y: i32
  IntId: i32 @unique
  Width: i32
  Height: i32
  StackSize: i32
}

type DescentExiles {
  Id: string @unique
  WorldAreasKey: WorldAreas
  CharactersKey: Characters
  MonsterVarietiesKey: MonsterVarieties
  _: i32
}

type DescentRewardChests {
  Id: string @unique
  BaseItemTypesKeys1: [BaseItemTypes]
  BaseItemTypesKeys2: [BaseItemTypes]
  BaseItemTypesKeys3: [BaseItemTypes]
  BaseItemTypesKeys4: [BaseItemTypes]
  BaseItemTypesKeys5: [BaseItemTypes]
  BaseItemTypesKeys6: [BaseItemTypes]
  BaseItemTypesKeys7: [BaseItemTypes]
  BaseItemTypesKeys8: [BaseItemTypes]
  BaseItemTypesKeys9: [BaseItemTypes]
  BaseItemTypesKeys10: [BaseItemTypes]
  BaseItemTypesKeys11: [BaseItemTypes]
  BaseItemTypesKeys12: [BaseItemTypes]
  WorldAreasKey: WorldAreas
  BaseItemTypesKeys13: [BaseItemTypes]
  BaseItemTypesKeys14: [BaseItemTypes]
}

type DescentStarterChest {
  Id: string @unique
  CharactersKey: Characters
  BaseItemTypesKey: BaseItemTypes
  SocketColours: string
  WorldAreasKey: WorldAreas
}

type DialogueEvent {
  Id: string @unique
  Timer: i32
}

# enum?
type Directions { TODO_REMOVE_THIS: u8 }

type DisplayMinionMonsterType {
  Id: i32 @unique
  MonsterVarietiesKey: MonsterVarieties
}

type DivinationCardStashTabLayout {
  BaseItemTypesKey: BaseItemTypes @unique
  IsEnabled: bool
}

type Doors {
  Id: string @unique
  _: i8
}

type DropEffects {
  Id: string @unique
  AOFile: string
}

type DropPool {
  Group: string @unique
  Weight: i32
  _: [i32]
}

type EclipseMods {
  _: string @unique
  SpawnWeight_TagsKeys: [Tags]
  SpawnWeight_Values: [i32]
  ModsKey: Mods
  MinLevel: i32
  MaxLevel: i32
  IsPrefix: bool
}

type EffectDrivenSkill {
  _: i32
  _: [u64]
  _: i32
  _: i32
  _: i32
  _: i32
  _: i8
  _: i8
  _: i32
  _: i8
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i8
  _: i32
  _: i8
  _: i8
  _: i32
  _: i32
  _: i8
  _: i8
  _: i8
  _: i32
  _: i8
  _: i8
}

# enum?
type Effectiveness { TODO_REMOVE_THIS: u8 }

type EffectivenessCostConstants {
  Id: string @unique
  Multiplier: f32
}

type EinharMissions {
  Id: string
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

type EinharPackFallback {
  _: rid
  _: [rid]
}

type ElderBossArenas {
  WorldAreasKey: WorldAreas @unique
  _: i32
  AchievementItemsKeys: [AchievementItems]
}

type ElderMapBossOverride {
  WorldAreasKey: WorldAreas @unique
  MonsterVarietiesKeys: [MonsterVarieties]
  TerrainMetadata: string
}

type EndlessLedgeChests {
  Id: string @unique
  WorldAreasKey: WorldAreas
  BaseItemTypesKeys: [BaseItemTypes]
  SocketColour: string
}

type Environments {
  Id: string @unique
  Base_ENVFile: string
  Corrupted_ENVFile: string
  _: i32
  _: i32
  _: i32
  _: i32
  EnvironmentTransitionsKey: EnvironmentTransitions
  _: rid
}

type EnvironmentTransitions {
  Id: string
  OTFiles: [string]
  _: [string]
}

type EssenceStashTabLayout {
  Id: string @unique
  BaseItemTypesKey: BaseItemTypes
  X: i32
  Y: i32
  IntId: i32 @unique
  SlotWidth: i32
  SlotHeight: i32
  IsUpgradableEssenceSlot: bool
}

type EventSeason {
  Id: string @unique
  _: i32
  RewardCommand: string
}

type EventSeasonRewards {
  EventSeasonKey: EventSeason
  Point: i32
  RewardCommand: string
}

type EvergreenAchievements {
  _: i32
  _: i32
  _: [rid]
}

# enum?
type EvergreenAchievementTypes { TODO_REMOVE_THIS: u8 }

type ExecuteGEAL {
  _: i32
  _: [rid]
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: bool
  _: i32
  _: bool
  _: i32
  _: bool
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: bool
  _: i32
  _: bool
  _: i32
  _: bool
  _: i32
  _: i32
  _: bool
  _: i32
  MetadataIDs: [string]
  ScriptCommand: string
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: bool
  _: bool
  _: i32
  _: i32
  _: i32
}

type ExpandingPulse {
  _: [i32]
  _: [i32]
  _: [f32]
  _: [rid]
  _: rid
  _: bool
}

type ExperienceLevels {
  _: string
  Level: i32
  Experience: u32
}

type ExplodingStormBuffs {
  Id: string @unique
  BuffDefinitionsKey1: BuffDefinitions
  _: rid
  StatValues: [i32]
  _: i32
  _: [i32]
  _: i32
  _: i32
  _: i32
  Friendly_MonsterVarietiesKey: MonsterVarieties
  MiscObjectsKey: MiscObjects
  MiscAnimatedKey: MiscAnimated
  BuffVisualsKey: BuffVisuals
  Enemy_MonsterVarietiesKey: MonsterVarieties
  _: i32
  _: i32
  _: i32
  BuffDefinitionsKey2: BuffDefinitions
  IsOnlySpawningNearPlayer: bool
}

type ExtraTerrainFeatures {
  Id: string @unique
  _: [i32]
  _: [i32]
  _: i8
  _: [i32]
  _: [i32]
  _: i32
  _: rid
  _: i8
}

type FixedHideoutDoodadTypes {
  Id: string
  HideoutDoodadsKeys: [HideoutDoodads]
  BaseTypeHideoutDoodadsKey: HideoutDoodads
}

type FixedMissions {
  _: rid
  _: rid
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

type Flasks {
  BaseItemTypesKey: BaseItemTypes @unique
  Name: string
  Group: i32
  LifePerUse: i32
  ManaPerUse: i32
  RecoveryTime: i32
  BuffDefinitionsKey: BuffDefinitions
  BuffStatValues: [i32]
}

# enum?
type FlaskType { TODO_REMOVE_THIS: u8 }

type FlavourText {
  Id: string @unique
  _: i32
  Text: string
}

# enum?
type FlavourTextImages { TODO_REMOVE_THIS: u8 }

type Footprints {
  Id: string @unique
  Active_AOFiles: [string]
  Idle_AOFiles: [string]
}

type FootstepAudio {
  _: i32
  Id: string @unique
}

type FragmentStashTabLayout {
  Id: string @unique
  BaseItemTypesKey: BaseItemTypes
  PosX: i32
  PosY: i32
  Order: i32
  SizeX: i32
  SizeY: i32
  _: i8
}

type GameConstants {
  Id: string @unique
  Value: i32
}

type GameStats {
  Id: string @unique
  Id2: string @unique
}

type GemTags {
  Id: string @unique
  Tag: string
  _: rid
  _: rid
  _: rid
  _: rid
}

# enum?
type GemTypes { TODO_REMOVE_THIS: u8 }

type GenericBuffAuras {
  Id: string @unique
}

type GeometryAttack {
  _: i32
  _: [rid]
  _: [rid]
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: bool
  _: i32
  _: i32
  _: i32
  _: bool
  _: bool
  _: i32
  _: i32
  _: i32
  _: i32
  _: rid
  _: i32
  _: i32
  _: bool
  _: bool
  _: i32
  _: i32
  _: bool
  _: i32
  _: bool
  _: rid
  _: [i32]
  _: i32
  _: bool
  _: bool
  _: rid
  _: i8
  _: i8
  _: i8
  _: i8
  _: i8
  _: i32
  _: i8
  _: i8
  _: rid
  _: i8
}

type GeometryChannel {
  Id: string @unique
  _: rid
  _: rid
  _: rid
  _: string
  _: string
  _: string
  _: bool
  _: bool
  _: rid
  _: rid
  EPKFile: string
  _: i32
  _: i32
}

type GeometryProjectiles {
  _: i32
  _: rid
  _: bool
  _: i32
  _: bool
  _: i32
  _: i32
  _: bool
  _: i32
  _: i32
  _: i32
  _: bool
  _: i32
  _: i32
  _: i32
  _: i8
  _: i8
  _: i8
  _: rid
}

type GeometryTrigger {
  _: i32
  _: rid
  _: rid
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
  _: i32
  _: i32
  _: i32
  _: i8
  _: i32
  _: i8
  _: i32
  _: i8
  _: i32
  _: i32
  _: [rid]
  _: i32
  _: i8
  _: i32
  _: i8
  _: i8
  _: i32
  _: i8
  _: i8
  _: rid
  _: i8
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i8
  _: i8
}

type GlobalAudioConfig {
  Id: string @unique
  Value: i32
  _: bool
}

type Grandmasters {
  Id: string
  GMFile: string
  AISFile: string
  ModsKeys: [Mods]
  CharacterLevel: i32
  _: bool
}

# enum?
type GrantedEffectGroups { TODO_REMOVE_THIS: u8 }

type GrantedEffectQualityStats {
  GrantedEffectsKey: GrantedEffects
  SetId: i32
  StatsKeys: [Stats]
  StatsValuesPermille: [i32]
  Weight: i32
  _: [i32]
  _: [i32]
}

type GrantedEffectQualityTypes {
  Id: i32 @unique
  Text: string
  ClientStringsKey: ClientStrings
}

type GrantedEffects {
  Id: string @unique
  IsSupport: bool
  AllowedActiveSkillTypes: [u32]
  BaseEffectiveness: f32
  IncrementalEffectiveness: f32
  SupportGemLetter: string
  _: i32
  AddedActiveSkillTypes: [u32]
  ExcludedActiveSkillTypes: [u32]
  SupportsGemsOnly: bool
  _: u32
  _: [i32]
  _: bool
  _: i32
  CastTime: i32
  ActiveSkillsKey: ActiveSkills
  _: bool
  _: bool
  _: [i32]
  _: rid
  _: rid
  _: bool
  _: [rid]
  GrantedEffectsKey: GrantedEffects
}

type GrantedEffectsPerLevel {
  GrantedEffectsKey: GrantedEffects
  Level: i32
  StatsKeys: [Stats]
  Stat1Float: f32
  Stat2Float: f32
  Stat3Float: f32
  Stat4Float: f32
  Stat5Float: f32
  Stat6Float: f32
  Stat7Float: f32
  Stat8Float: f32
  Stat9Float: f32
  EffectivenessCostConstantsKeys: [EffectivenessCostConstants]
  Stat1Value: i32
  Stat2Value: i32
  Stat3Value: i32
  Stat4Value: i32
  Stat5Value: i32
  Stat6Value: i32
  Stat7Value: i32
  Stat8Value: i32
  Stat9Value: i32
  LevelRequirement: i32
  ManaMultiplier: i32
  LevelRequirement2: i32
  LevelRequirement3: i32
  CriticalStrikeChance: i32
  DamageEffectiveness: i32
  StoredUses: i32
  Cooldown: i32
  CooldownBypassType: i32
  StatsKeys2: [Stats]
  _: bool
  VaalSouls: i32
  VaalStoredUses: i32
  CooldownGroup: i32
  _: i32
  DamageMultiplier: i32
  _: i32
  ArtVariation: i32
  StatInterpolationTypesKeys: [i32]
  _: i32
  VaalSoulGainPreventionTime: i32
  BaseDuration: i32
  AttackSpeedMultiplier: i32
  _: i32
  CostAmounts: [i32]
  CostTypesKeys: [CostTypes]
  ManaReservationFlat: i32
  ManaReservationPercent: i32
  LifeReservationFlat: i32
  LifeReservationPercent: i32
  _: i32
}

# enum?
type GroundEffectEffectTypes { TODO_REMOVE_THIS: u8 }

type GroundEffects {
  GroundEffectTypesKey: GroundEffectTypes
  _: i32
  _: i32
  _: rid
  _: bool
  _: bool
  _: i32
  _: bool
  _: bool
  AOFile: string
  _: bool
  _: [i32]
  _: [i32]
  _: i32
  _: rid
  _: rid
  _: rid
  _: rid
  _: rid
  _: bool
  _: bool
  _: bool
}

type GroundEffectTypes {
  Id: string @unique
  _: i32
  _: f32
  _: rid
  _: rid
  _: rid
}

type HarvestStorageLayout {
  Id: string @unique
  _: rid
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  Button: string
  ButtonHighlight: string
  HasButton: bool
}

type HeistStorageLayout {
  Id: string @unique
  _: rid
  _: bool
  ButtonFile: string
  _: i32
  HeistJobsKey: HeistJobs
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: rid
}

type HideoutDoodads {
  BaseItemTypesKey: BaseItemTypes @unique
  Variation_AOFiles: [string]
  FavourCost: i32
  MasterLevel: i32
  HideoutNPCsKey: HideoutNPCs
  IsNonMasterDoodad: bool
  _: i32
  _: i32
  _: i32
  InheritsFrom: string
  IsCraftingBench: bool
  _: bool
}

type HideoutNPCs {
  Hideout_NPCsKey: NPCs
  Regular_NPCsKeys: [NPCs]
  HideoutDoodadsKey: HideoutDoodads
  NPCMasterKey: NPCMaster
  _: i32
  _: i32
  _: i32
  _: rid
}

type HideoutRarity {
  Id: string @unique
  Text: string
}

type Hideouts {
  Id: string @unique
  SmallWorldAreasKey: WorldAreas
  _: i32
  HideoutFile: string
  _: [rid]
  LargeWorldAreasKey: WorldAreas
  HideoutImage: string
  IsEnabled: i8
  Weight: i32
  _: HideoutRarity
  _: bool
  Name: string
  _: [i32]
  _: bool
}

type ImpactSoundData {
  Id: string @unique
  Sound: string
  _: i32
  _: i32
  _: i32
  _: i32
}

type IndexableSupportGems {
  _: i32
  BaseItemTypesKey: BaseItemTypes
  Name: string
}

type InfluenceExalts {
  Id: i32 @unique
  BaseItemTypesKey: BaseItemTypes
}

# enum?
type InfluenceTypes { TODO_REMOVE_THIS: u8 }

type Inventories {
  Id: string
  InventoryIdKey: InventoryId
  InventoryTypeKey: InventoryType
  _: i32
  _: bool
  _: bool
  _: i32
  _: bool
}

# enum?
type InventoryId { TODO_REMOVE_THIS: u8 }

# enum?
type InventoryType { TODO_REMOVE_THIS: u8 }

# enum?
type ItemClassCategories { TODO_REMOVE_THIS: u8 }

type ItemClasses {
  Id: string @unique
  Name: string
  Category: string
  _: i32
  RemovedIfLeavesArea: bool
  _: [rid]
  _: [rid]
  _: bool
  _: bool
  _: bool
  _: i32
  _: i32
  _: bool
  _: bool
  _: bool
  _: bool
  _: bool
  _: bool
  _: bool
  _: rid
  _: bool
}

type ItemCostPerLevel {
  Contract_BaseItemTypesKey: BaseItemTypes
  Level: i32
  Cost1_BaseItemTypesKeys: [BaseItemTypes]
  Cost1_Values: [i32]
  Cost2_BaseItemTypesKeys: [BaseItemTypes]
  Cost2_Values: [i32]
  Cost3_BaseItemTypesKeys: [BaseItemTypes]
  Cost3_Values: [i32]
  Cost4_BaseItemTypesKeys: [BaseItemTypes]
  Cost4_Values: [i32]
}

# enum?
type ItemCreationTemplateCustomAction { TODO_REMOVE_THIS: u8 }

type ItemExperiencePerLevel {
  BaseItemTypesKey: BaseItemTypes
  ItemCurrentLevel: i32
  Experience: i32
}

type ItemisedVisualEffect {
  BaseItemTypesKey: BaseItemTypes
  ItemVisualEffectKey: ItemVisualEffect
  ItemVisualIdentityKey1: ItemVisualIdentity
  ItemVisualIdentityKey2: ItemVisualIdentity
  _: [rid]
  _: [u32]
  _: [rid]
  _: bool
  _: [u32]
  _: [i32]
  _: bool
}

type ItemNoteCode {
  BaseItemTypesKey: BaseItemTypes
  Code: string
  _: i32
  _: bool
}

# enum?
type ItemSetNames { TODO_REMOVE_THIS: u8 }

type ItemShopType {
  Id: string @unique
  Name: string
}

type ItemThemes {
  Id: string @unique
  Name: string
}

type ItemVisualEffect {
  Id: string @unique
  DaggerEPKFile: string
  BowEPKFile: string
  OneHandedMaceEPKFile: string
  OneHandedSwordEPKFile: string
  _: string
  TwoHandedSwordEPKFile: string
  TwoHandedStaffEPKFile: string
  _: i32 @unique
  TwoHandedMaceEPKFile: string
  OneHandedAxeEPKFile: string
  TwoHandedAxeEPKFile: string
  ClawEPKFile: string
  PETFile: string
}

type ItemVisualHeldBodyModel {
  _: rid
  _: string
  _: string
  _: string
  _: i32
  _: i32
  _: i32
  _: string
  _: string
  _: string
  _: string
  _: string
  _: string
  _: string
  _: string
}

type ItemVisualIdentity {
  Id: string @unique
  DDSFile: string
  AOFile: string
  SoundEffectsKey: SoundEffects
  _: i32 @unique
  AOFile2: string
  MarauderSMFiles: [string]
  RangerSMFiles: [string]
  WitchSMFiles: [string]
  DuelistDexSMFiles: [string]
  TemplarSMFiles: [string]
  ShadowSMFiles: [string]
  ScionSMFiles: [string]
  MarauderShape: string
  RangerShape: string
  WitchShape: string
  DuelistShape: string
  TemplarShape: string
  ShadowShape: string
  ScionShape: string
  _: i32
  _: i32
  Pickup_AchievementItemsKeys: [AchievementItems]
  SMFiles: [string]
  Identify_AchievementItemsKeys: [AchievementItems]
  EPKFile: string
  Corrupt_AchievementItemsKeys: [AchievementItems]
  IsAlternateArt: bool
  _: bool
  CreateCorruptedJewelAchievementItemsKey: AchievementItems
  AnimationLocation: string
  _: string
  _: string
  _: string
  _: string
  _: string
  _: string
  _: string
  _: string
  _: string
  _: string
  _: string
  _: string
  IsAtlasOfWorldsMapIcon: bool
  IsTier16Icon: bool
  _: [i32]
  _: bool
  _: [u64]
}

type JobAssassinationSpawnerGroups {
  _: i32
  _: i32
  _: i32
  _: i32
}

type JobRaidBrackets {
  MinLevel: i32
  _: i32
  _: rid
  _: i32
  _: i32
  _: i32
  _: i32
}

type KillstreakThresholds {
  Kills: i32
  MonsterVarietiesKey: MonsterVarieties
  AchievementItemsKey: AchievementItems
}

# enum?
type LeagueCategory { TODO_REMOVE_THIS: u8 }

type LeagueFlag {
  Id: string @unique
  Image: string
}

# enum?
type LeagueFlags { TODO_REMOVE_THIS: u8 }

type LeagueInfo {
  Id: string @unique
  PanelImage: string
  HeaderImage: string
  Screenshots: [string]
  Description: string
  League: string
  _: bool
  ItemImages: [string]
  HoverImages: [string]
  TrailerVideoLink: string
  BackgroundImage: string
  _: bool
}

# enum?
type LeagueQuestFlags { TODO_REMOVE_THIS: u8 }

# enum?
type LeagueTrophy { TODO_REMOVE_THIS: u8 }

type LevelRelativePlayerScaling {
  PlayerLevel: i32 @unique
  MonsterLevel: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

type MagicMonsterLifeScalingPerLevel {
  Level: i32
  Life: i32
}

type MapCompletionAchievements {
  _: string
  MapStatConditionsKeys: [MapStatConditions]
  StatsKeys: [Stats]
  AchievementItemsKeys: [AchievementItems]
  MapTierAchievementsKeys: [MapTierAchievements]
  _: i8
  WorldAreasKeys: [WorldAreas]
}

type MapConnections {
  MapPinsKey0: MapPins
  MapPinsKey1: MapPins
  _: i32
  RestrictedAreaText: string
  _: i32
  _: i32
  _: i32
  _: i32
  RestrictedAreaMessage: string
}

type MapCreationInformation {
  MapsKey: Maps
  Tier: i32
}

type MapDeviceRecipes {
  Id: string @unique
  BaseItemTypesKeys: [BaseItemTypes]
  WorldAreasKey: WorldAreas
  _: rid
  AreaLevel: i32
  _: i32
  _: i32
  IsLegionMap: bool
}

type MapDevices {
  Id: string
  _: rid
  _: i32
  _: i8
  InheritsFrom: string
  Command: string
  Command_Data: [i32]
}

# enum?
type MapFragmentFamilies { TODO_REMOVE_THIS: u8 }

type MapFragmentMods {
  BaseItemTypesKey: BaseItemTypes @unique
  ModsKeys: [Mods]
  AchievementItemsKey: [AchievementItems]
  MapFragmentFamilies: i32
  _: bool
  _: bool
  _: bool
  _: bool
}

type MapInhabitants {
  StatsKey: Stats
  MonsterPacksKeys: [MonsterPacks]
}

type MapPins {
  Id: string @unique
  PositionX: i32
  PositionY: i32
  Waypoint_WorldAreasKey: WorldAreas
  WorldAreasKeys: [WorldAreas]
  Name: string
  FlavourText: string
  _: [u32]
  Act: i32
  _: string
  _: [i32]
  _: i32
}

type MapPurchaseCosts {
  Tier: i32 @unique
  NormalPurchase_BaseItemTypesKeys: [BaseItemTypes]
  NormalPurchase_Costs: [i32]
  MagicPurchase_BaseItemTypesKeys: [BaseItemTypes]
  MagicPurchase_Costs: [i32]
  RarePurchase_BaseItemTypesKeys: [BaseItemTypes]
  RarePurchase_Costs: [i32]
  UniquePurchase_BaseItemTypesKeys: [BaseItemTypes]
  UniquePurchase_Costs: [i32]
}

type Maps {
  BaseItemTypesKey: BaseItemTypes @unique
  Regular_WorldAreasKey: WorldAreas
  Unique_WorldAreasKey: WorldAreas
  MapUpgrade_BaseItemTypesKey: BaseItemTypes
  MonsterPacksKeys: [MonsterPacks]
  _: rid
  Regular_GuildCharacter: string
  Unique_GuildCharacter: string
  Tier: i32
  Shaped_Base_MapsKey: Maps
  Shaped_AreaLevel: i32
  UpgradedFrom_MapsKey: Maps
  MapsKey2: Maps
  MapsKey3: Maps
  MapSeriesKey: MapSeries
  _: bool
  _: bool
}

type MapSeries {
  Id: string @unique
  Name: string
  BaseIcon_DDSFile: string
  Infected_DDSFile: string
  Shaper_DDSFile: string
  Elder_DDSFile: string
  Drawn_DDSFile: string
}

type MapSeriesTiers {
  MapsKey: Maps
  MapWorldsTier: i32
  BetrayalTier: i32
  SynthesisTier: i32
  LegionTier: i32
  BlightTier: i32
  MetamorphosisTier: i32
  DeliriumTier: i32
  HarvestTier: i32
  HeistTier: i32
}

# enum?
type MapStashTabLayout { TODO_REMOVE_THIS: u8 }

type MapStatConditions {
  Id: string @unique
  StatsKey: Stats
  _: i8
  StatMin: i32
  StatMax: i32
}

type MapTierAchievements {
  Id: string @unique
  AchievementItemsKey: [AchievementItems]
  MapTiers: [i32]
}

type MapTiers {
  Tier: i32
  Level: i32
  _: i32
}

type MasterHideoutLevels {
  NPCMasterKey: NPCMaster
  Level: i32
  MissionsRequired: i32
}

type Melee {
  _: u64
  _: i32
  _: rid
  MeleeTrailsKey1: MeleeTrails
  MeleeTrailsKey2: MeleeTrails
  MeleeTrailsKey3: MeleeTrails
  MeleeTrailsKey4: MeleeTrails
  MeleeTrailsKey5: MeleeTrails
  MeleeTrailsKey6: MeleeTrails
  MeleeTrailsKey7: MeleeTrails
  _: i8
  SurgeEffect_EPKFile: string
  _: string
  _: string
}

type MeleeTrails {
  EPKFile1: string
  EPKFile2: string
  _: i32
  _: i32
  _: i32
  _: bool
  AOFile: string
  _: bool
}

type MetamorphosisStashTabLayout {
  Id: string @unique
  BaseItemTypesKey: BaseItemTypes
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  BackgroundImage: string
  ButtonImage: string
}

type MicroMigrationData {
  BaseItemTypesKey: BaseItemTypes
  _: i32
  _: rid
  _: rid
}

type MicrotransactionCharacterPortraitVariations {
  _: rid
}

type MicrotransactionCombineFormula {
  Id: string
  Result_BaseItemTypesKey: BaseItemTypes
  Ingredients_BaseItemTypesKeys: [BaseItemTypes]
  BK2File: string
  _: [i32]
  _: i32
  _: i8
}

type MicrotransactionFireworksVariations {
  BaseItemTypesKey: BaseItemTypes
  AOFile: string
  _: bool
}

type MicrotransactionPeriodicCharacterEffectVariations {
  Id: string @unique
  AOFile: string
  _: rid
}

type MicrotransactionPortalVariations {
  BaseItemTypesKey: BaseItemTypes
  AOFile: string
  MapAOFile: string
  _: f32
  _: rid
}

type MicrotransactionRarityDisplay {
  Rarity: string @unique
  ImageFile: string
}

# enum?
type MicrotransactionRecycleCategories { TODO_REMOVE_THIS: u8 }

type MicrotransactionRecycleOutcomes {
  _: rid
  _: i32
}

type MicrotransactionRecycleSalvageValues {
  _: rid
  _: i32
  _: i32
}

# enum?
type MicrotransactionSlotId { TODO_REMOVE_THIS: u8 }

type MicrotransactionSocialFrameVariations {
  Id: i32 @unique
  BaseItemTypesKey: BaseItemTypes
  BK2File: string
}

type MinimapIcons {
  Id: string
  MinimapIconRadius: i32
  LargemapIconRadius: i32
  _: bool
  _: bool
  _: bool
  MinimapIconPointerMaxDistance: i32
  _: i32
}

type MiscAnimated {
  Id: string @unique
  AOFile: string
  PreloadGroupsKeys: [PreloadGroups]
  _: i32
  _: i32
}

type MiscBeams {
  Id: string @unique
  _: rid
  _: i32
  PreloadGroupsKeys: [PreloadGroups]
  _: i32
}

type MiscEffectPacks {
  Id: string @unique
  EPKFile: string
  _: i32
  _: i32
  _: i32
  _: [rid]
  _: i8
  PlayerOnly_EPKFile: string
}

type MiscObjects {
  Id: string @unique
  EffectVirtualPath: string
  PreloadGroupsKeys: [PreloadGroups]
  _: i32
  _: i32
}

type MissionFavourPerLevel {
  Level: i32
  Favour: i32
}

# enum?
type MissionTileMap { TODO_REMOVE_THIS: u8 }

type MissionTimerTypes {
  Id: string
  Image: string
  BackgroundImage: string
}

type MissionTransitionTiles {
  Id: string @unique
  TDTFile: string
  _: i32
  _: i32
  _: i32
}

# enum?
type ModAuraFlags { TODO_REMOVE_THIS: u8 }

# enum?
type ModDomains { TODO_REMOVE_THIS: u8 }

type ModEffectStats {
  StatsKey: Stats
  TagsKeys: [Tags]
  _: bool
  _: i32
  _: bool
}

type ModEquivalencies {
  Id: string @unique
  ModsKey0: Mods
  ModsKey1: Mods
  ModsKey2: Mods
  _: bool
}

# enum?
type ModFamily { TODO_REMOVE_THIS: u8 }

# enum?
type ModGenerationType { TODO_REMOVE_THIS: u8 }

type Mods {
  Id: string @unique
  Hash: i32
  ModTypeKey: ModType
  Level: i32
  StatsKey1: Stats
  StatsKey2: Stats
  StatsKey3: Stats
  StatsKey4: Stats
  Domain: i32
  Name: string
  GenerationType: i32
  CorrectGroup: string
  Stat1Min: i32
  Stat1Max: i32
  Stat2Min: i32
  Stat2Max: i32
  Stat3Min: i32
  Stat3Max: i32
  Stat4Min: i32
  Stat4Max: i32
  SpawnWeight_TagsKeys: [Tags]
  SpawnWeight_Values: [u32]
  BuffDefinitionsKey: BuffDefinitions
  BuffValue: i32
  TagsKeys: [Tags]
  GrantedEffectsPerLevelKeys: [GrantedEffectsPerLevel]
  _: [u32]
  _: [u32]
  MonsterMetadata: string
  _: [i32]
  _: [i32]
  BuffVisualsKey: BuffVisuals
  Stat5Min: i32
  Stat5Max: i32
  StatsKey5: Stats
  FullAreaClear_AchievementItemsKey: [AchievementItems]
  AchievementItemsKey: [AchievementItems]
  GenerationWeight_TagsKeys: [Tags]
  GenerationWeight_Values: [i32]
  _: [i32]
  IsEssenceOnlyModifier: bool
  Stat6Min: i32
  Stat6Max: i32
  StatsKey6: Stats
  MaxLevel: i32
  _: i8
  _: [rid]
  MonsterOnDeath: string
  _: i32
  _: [i32]
  _: [GrantedEffectsPerLevel]
  Heist_SubStatValue1: i32
  Heist_SubStatValue2: i32
  Heist_StatsKey0: Stats
  Heist_StatsKey1: Stats
  Heist_AddStatValue1: i32
  Heist_AddStatValue2: i32
  InfluenceTypes: i32
  ImplicitTagsKeys: [Tags]
}

type ModSellPriceTypes {
  Id: string
}

# enum?
type ModSetNames { TODO_REMOVE_THIS: u8 }

type ModSets {
  _: string
  _: i32
  _: rid
  _: i32
}

type ModType {
  Name: string @unique
  ModSellPriceTypesKeys: [ModSellPriceTypes]
}

type MonsterArmours {
  Id: string
  ArtString_SMFile: string
}

# enum?
type MonsterBehavior { TODO_REMOVE_THIS: u8 }

type MonsterBonuses {
  Id: string @unique
  _: [rid]
  _: rid
  _: i32
  _: i32
  StatsKeys: [Stats]
  StatValues: [i32]
}

type MonsterConditions {
  Id: string
  _: i32
  _: rid
  _: i32
  _: [rid]
  _: i8
  _: i8
  _: [rid]
  _: [i32]
  _: i32
}

type MonsterDeathAchievements {
  Id: string @unique
  MonsterVarietiesKeys: [MonsterVarieties]
  AchievementItemsKeys: [AchievementItems]
  _: i8
  PlayerConditionsKeys: [PlayerConditions]
  MonsterDeathConditionsKeys: [MonsterDeathConditions]
  _: [u64]
  _: i32
  _: i32
  _: i8
  _: i8
  _: u64
  _: [u64]
  _: [u64]
  _: [u64]
  _: u64
  _: i32
  NearbyMonsterConditionsKeys: [NearbyMonsterConditions]
  _: i8
  MultiPartAchievementConditionsKeys: [MultiPartAchievementConditions]
  _: i32
}

type MonsterDeathConditions {
  _: string
  _: [u64]
  _: i8
  _: i32
  _: [u64]
  _: i8
  _: i32
  _: i32
  _: i8
  _: u64
  _: i32
  _: i8
  _: [u64]
  _: i32
  _: u64
  _: u64
}

# enum?
type MonsterFleeConditions { TODO_REMOVE_THIS: u8 }

type MonsterGroupEntries {
  Id: string @unique
  MonsterVarietiesKey: MonsterVarieties
  MonsterGroupNamesId: i32
}

# enum?
type MonsterGroupNames { TODO_REMOVE_THIS: u8 }

type MonsterHeightBrackets {
  Id: string @unique
  _: i32
  _: rid
  _: rid
}

type MonsterHeights {
  _: rid
  _: f32
  _: rid
}

type MonsterMapBossDifficulty {
  MapLevel: i32
  Stat1Value: i32
  Stat2Value: i32
  StatsKey1: Stats
  StatsKey2: Stats
  StatsKey3: Stats
  Stat3Value: i32
  StatsKey4: Stats
  Stat4Value: i32
  StatsKey5: Stats
  Stat5Value: i32
}

type MonsterMapDifficulty {
  MapLevel: i32
  Stat1Value: i32
  Stat2Value: i32
  StatsKey1: Stats
  StatsKey2: Stats
  StatsKey3: Stats
  Stat3Value: i32
  StatsKey4: Stats
  Stat4Value: i32
}

type MonsterMortar {
  Id: i32 @unique
  _: rid
  _: rid
  _: rid
  _: i32
  _: i8
  _: bool
  _: bool
  _: bool
  _: i32
  _: bool
  _: i32
  _: i32
  _: bool
  _: bool
  _: bool
  _: bool
}

type MonsterPackCounts {
  _: rid
  _: i32
  _: [rid]
  _: i8
  _: [i32]
}

type MonsterPackEntries {
  Id: string @unique
  MonsterPacksKey: MonsterPacks
  _: bool
  _: i32
  MonsterVarietiesKey: MonsterVarieties
}

type MonsterPacks {
  Id: string @unique
  WorldAreasKeys: [WorldAreas]
  _: i32
  _: i32
  BossMonsterSpawnChance: i32
  BossMonsterCount: i32
  BossMonster_MonsterVarietiesKeys: [MonsterVarieties]
  _: bool
  _: i32
  _: [string]
  TagsKeys: [Tags]
  MinLevel: i32
  MaxLevel: i32
  _: [rid]
  _: i32
  _: rid
  _: i32
}

type MonsterProjectileAttack {
  Id: i32 @unique
  _: rid
  _: bool
  _: bool
  _: bool
  _: i32
}

type MonsterProjectileSpell {
  Id: i32 @unique
  _: rid
  _: rid
  _: bool
  _: bool
  _: i32
  _: bool
}

type MonsterResistances {
  Id: string @unique
  FireNormal: i32
  ColdNormal: i32
  LightningNormal: i32
  ChaosNormal: i32
  FireCruel: i32
  ColdCruel: i32
  LightningCruel: i32
  ChaosCruel: i32
  FireMerciless: i32
  ColdMerciless: i32
  LightningMerciless: i32
  ChaosMerciless: i32
}

# enum?
type MonsterScalingByLevel { TODO_REMOVE_THIS: u8 }

type MonsterSegments {
  Id: string
  Shapes: string
}

# enum?
type MonsterSize { TODO_REMOVE_THIS: u8 }

# enum?
type MonsterSkillsAliveDead { TODO_REMOVE_THIS: u8 }

# enum?
type MonsterSkillsAttackSpell { TODO_REMOVE_THIS: u8 }

# enum?
type MonsterSkillsClientInstance { TODO_REMOVE_THIS: u8 }

# enum?
type MonsterSkillsHull { TODO_REMOVE_THIS: u8 }

# enum?
type MonsterSkillsOrientation { TODO_REMOVE_THIS: u8 }

# enum?
type MonsterSkillsPlacement { TODO_REMOVE_THIS: u8 }

# enum?
type MonsterSkillsReference { TODO_REMOVE_THIS: u8 }

# enum?
type MonsterSkillsSequenceMode { TODO_REMOVE_THIS: u8 }

# enum?
type MonsterSkillsShape { TODO_REMOVE_THIS: u8 }

# enum?
type MonsterSkillsTargets { TODO_REMOVE_THIS: u8 }

# enum?
type MonsterSkillsWaveDirection { TODO_REMOVE_THIS: u8 }

type MonsterSpawnerGroups {
  Id: string
}

type MonsterSpawnerGroupsPerLevel {
  MonsterSpawnerGroupsKey: MonsterSpawnerGroups
  MinLevel: i32
  _: i32
  _: i32
  _: i32
}

type MonsterSpawnerOverrides {
  _: rid
  Base_MonsterVarietiesKey: MonsterVarieties
  Override_MonsterVarietiesKey: MonsterVarieties
}

type MonsterTypes {
  Id: string @unique
  _: i32
  IsSummoned: bool
  Armour: i32
  Evasion: i32
  EnergyShieldFromLife: i32
  DamageSpread: i32
  TagsKeys: [Tags]
  MonsterResistancesKey: MonsterResistances
  IsLargeAbyssMonster: bool
  IsSmallAbyssMonster: bool
}

type MonsterVarieties {
  Id: string @unique
  MonsterTypesKey: MonsterTypes
  _: i32
  ObjectSize: i32
  MinimumAttackDistance: i32
  MaximumAttackDistance: i32
  ACTFiles: [string]
  AOFiles: [string]
  BaseMonsterTypeIndex: string
  ModsKeys: [Mods]
  _: i32
  _: i32
  _: i32
  ModelSizeMultiplier: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  TagsKeys: [Tags]
  ExperienceMultiplier: i32
  _: [i32]
  _: i32
  _: i32
  _: i32
  CriticalStrikeChance: i32
  _: i32
  GrantedEffectsKeys: [GrantedEffects]
  AISFile: string
  ModsKeys2: [Mods]
  Stance: string
  _: rid
  Name: string
  DamageMultiplier: i32
  LifeMultiplier: i32
  AttackSpeed: i32
  Weapon1_ItemVisualIdentityKeys: [ItemVisualIdentity]
  Weapon2_ItemVisualIdentityKeys: [ItemVisualIdentity]
  Back_ItemVisualIdentityKey: ItemVisualIdentity
  MainHand_ItemClassesKey: ItemClasses
  OffHand_ItemClassesKey: ItemClasses
  _: rid
  Helmet_ItemVisualIdentityKey: ItemVisualIdentity
  _: i32
  KillSpecificMonsterCount_AchievementItemsKeys: [AchievementItems]
  Special_ModsKeys: [Mods]
  KillRare_AchievementItemsKeys: [AchievementItems]
  _: bool
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i8
  _: i32
  KillWhileOnslaughtIsActive_AchievementItemsKey: AchievementItems
  MonsterSegmentsKey: MonsterSegments
  MonsterArmoursKey: MonsterArmours
  KillWhileTalismanIsActive_AchievementItemsKey: AchievementItems
  Part1_ModsKeys: [Mods]
  Part2_ModsKeys: [Mods]
  Endgame_ModsKeys: [Mods]
  _: rid
  _: i32
  _: i32
  _: [rid]
  _: [rid]
  _: i32
  SinkAnimation_AOFile: string
  _: i8
  _: [rid]
  _: i8
  _: i8
  _: i8
  _: i32
  _: i32
  _: i32
  _: i32
  EPKFile: string
  _: i32
  MonsterConditionalEffectPacksKey: u64
  _: bool
  _: bool
  _: i32
  _: bool
}

type MoveDaemon {
  _: i32
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
  _: i32
  _: i32
  _: i8
  _: i8
  _: i8
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i8
  _: i8
  _: i8
}

type MTXSetBonus {
  Id: string @unique
  ArtFile: string
}

type MultiPartAchievementAreas {
  _: rid
  _: [rid]
  _: i32
}

type MultiPartAchievementConditions {
  Id: string @unique
  MultiPartAchievementsKey1: MultiPartAchievements
  MultiPartAchievementsKey2: MultiPartAchievements
  _: i32
  _: i32
}

type MultiPartAchievements {
  Id: string @unique
  _: i32
  AchievementItemsKey: AchievementItems
  _: i32
  _: bool
  _: bool
  _: i32
}

type Music {
  Id: string @unique
  SoundFile: string
  BankFile: string
  _: i32
  IsAvailableInHideout: i8
  Name: string
  _: i32
  _: [rid]
}

type MusicCategories {
  Id: string @unique
  Name: string
  Order: i32
  _: i8
}

type MysteryBoxes {
  BaseItemTypesKey: BaseItemTypes
  BK2File: string
  BoxId: string
  BundleId: string
}

type NearbyMonsterConditions {
  Id: string @unique
  MonsterVarietiesKeys: [MonsterVarieties]
  MonsterAmount: i32
  _: i32
  IsNegated: bool
  _: i32
  _: [i32]
  IsLessThen: bool
  MinimumHealthPercentage: i32
}

type NetTiers {
  BaseItemTypesKey: BaseItemTypes
  Tier: i32
}

type Notifications {
  Id: string @unique
  _: bool
  _: bool
  Message: string
  _: string
  _: i32
  _: bool
  _: bool
}

type NPCAudio {
  Id: string @unique
  _: [i32]
  _: [i32]
  VolumePercentage: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

type NPCConversations {
  Id: string
  _: u64
  NPCsKey: NPCs
  NPCsKeys: [NPCs]
  NPCTextAudioKeys: [NPCTextAudio]
  _: [i32]
  _: [i32]
  _: i32
}

type NPCDialogueStyles {
  Id: string @unique
  HeaderBaseFile: string
  ButtomFile: string
  BannerFiles: [string]
  HeaderFiles: [string]
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

type NPCFollowerVariations {
  MonsterVarietiesKey: MonsterVarieties
  MiscAnimatedKey0: MiscAnimated
  MiscAnimatedKey1: MiscAnimated
  _: bool
  _: bool
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: bool
  _: bool
  _: [i32]
  _: [i32]
  _: i32
  _: bool
}

type NPCMaster {
  Id: string
  _: i16
  Signature_ModsKey: Mods
  _: i8
  SpawnWeight_TagsKeys: [Tags]
  SpawnWeight_Values: [i32]
  _: [i32]
  _: [i32]
  _: rid
  HelpText: string
  HelpTextForNextLevel: string
  _: rid
  _: i32
  AreaDescription: string
  _: rid
  _: i32
  _: i32
  _: i32
}

type NPCs {
  Id: string! @unique
  Name: string
  Metadata: string
  _: i32
  NPCMasterKey: NPCMaster
  ShortName: string
  _: i32
  NPCShopKey: NPCShop
  NPCAudioKeys1: [NPCAudio]
  NPCAudioKeys2: [NPCAudio]
  _: i32
  _: i32
  PortraitFile: string
  _: i32
  _: i32
  _: i32
}

type NPCShop {
  Id: string @unique
  _: i32
  SoldItem_TagsKeys: [Tags]
  SoldItem_Weights: [u32]
  _: [u64]
  _: [u32]
  _: i32
  _: [rid]
  _: [i32]
  _: i32
  _: i32
}

type NPCTalk {
  NPCKey: NPCs
  _: i32
  DialogueOption: string
  _: [u32]
  _: [u32]
  _: [u32]
  Script: string
  _: i32
  _: i32
  QuestKey: Quest
  _: i32
  NPCTextAudioKeys: [NPCTextAudio]
  Script2: string
  _: bool
  _: bool
  _: [i32]
  _: [i32]
  _: i32
  _: [i32]
  _: i32
  _: bool
  _: [rid]
  _: rid
  _: bool
  _: bool
  DialogueOption2: string
  _: rid
  _: rid
  _: i32
  _: i32
  _: i32
}

# enum?
type NPCTalkCategory { TODO_REMOVE_THIS: u8 }

type NPCTalkConsoleQuickActions {
  Id: string
  Controller: string
}

type NPCTextAudio {
  Id: string @unique
  CharactersKey: Characters
  Text: string
  Mono_AudioFile: string
  Stereo_AudioFile: string
  HasStereo: bool
  _: bool
  Inflection: string
  _: i32
  _: i32
  _: i32
}

# enum?
type NPCTextAudioInterruptRules { TODO_REMOVE_THIS: u8 }

# enum?
type OldMapStashTabLayout { TODO_REMOVE_THIS: u8 }

type OnKillAchievements {
  MonsterVarietiesKey: MonsterVarieties
  _: rid
}

# enum?
type Orientations { TODO_REMOVE_THIS: u8 }

type PackFormation {
  Id: string
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

type PassiveJewelSlots {
  PassiveSkillsKey: PassiveSkills
  _: rid
  _: i32
  PassiveJewelSlotsKey: PassiveJewelSlots
  _: u64
  _: i32
  _: i32
}

type PassiveSkillFilterCatagories {
  Id: string @unique
  Name: string
}

type PassiveSkillFilterOptions {
  Id: string @unique
  _: rid
  Name: string
  _: string
}

type PassiveSkills {
  Id: string @unique
  Icon_DDSFile: string
  StatsKeys: [Stats]
  Stat1Value: i32
  Stat2Value: i32
  Stat3Value: i32
  Stat4Value: i32
  PassiveSkillGraphId: i32 @unique
  Name: string
  CharactersKeys: [Characters]
  IsKeystone: bool
  IsNotable: bool
  FlavourText: string
  IsJustIcon: bool
  AchievementItemsKey: AchievementItems
  IsJewelSocket: bool
  AscendancyKey: Ascendancy
  IsAscendancyStartingNode: bool
  Reminder_ClientStringsKeys: [ClientStrings]
  SkillPointsGranted: i32
  IsMultipleChoice: bool
  IsMultipleChoiceOption: bool
  Stat5Value: i32
  PassiveSkillBuffsKeys: [u64]
  GrantedEffectsPerLevelKey: GrantedEffectsPerLevel
  _: bool
  _: i32
  _: i8
  IsProxyPassive: i8
  _: i32
}

type PassiveSkillStatCategories {
  Id: string @unique
  Name: string
}

type PassiveSkillTreeTutorial {
  Id: string
  CharactersKey: Characters
  _: rid
  ChoiceA_Description: string
  ChoiceB_Description: string
  _: rid
  ChoiceA_PassiveTreeURL: string
  ChoiceB_PassiveTreeURL: string
  _: rid
  _: rid
}

type PassiveTreeExpansionJewels {
  BaseItemTypesKey: BaseItemTypes
  PassiveTreeExpansionJewelSizesKey: PassiveTreeExpansionJewelSizes
  MinNodes: i32
  MaxNodes: i32
  SmallIndices: [i32]
  NotableIndices: [i32]
  SocketIndices: [i32]
  Art: string
  TotalIndices: i32
  SoundEffectsKey: SoundEffects
}

type PassiveTreeExpansionJewelSizes {
  Name: string
}

type PassiveTreeExpansionSkills {
  PassiveSkillsKey: PassiveSkills
  Mastery_PassiveSkillsKey: PassiveSkills
  TagsKey: Tags
  PassiveTreeExpansionJewelSizesKey: PassiveTreeExpansionJewelSizes
}

type PassiveTreeExpansionSpecialSkills {
  PassiveSkillsKey: PassiveSkills
  StatsKey: Stats
}

type PCBangRewardMicros {
  BaseItemTypesKey: u64
  _: i32
}

# enum?
type PerLevelValues { TODO_REMOVE_THIS: u8 }

type Pet {
  Id: string @unique
  BaseItemTypesKey: BaseItemTypes
  _: i32
  _: i32
  _: i32
  _: i16
}

type PlayerConditions {
  Id: string @unique
  BuffDefinitionsKeys: [BuffDefinitions]
  _: bool
  BuffStacks: i32
  CharactersKey: Characters
  StatsKeys: [Stats]
  _: bool
  StatValue: i32
  _: [rid]
  _: bool
}

type PreloadGroups {
  Id: string @unique
}

# enum?
type PreloadPriorities { TODO_REMOVE_THIS: u8 }

type Projectiles {
  Id: string @unique
  AOFiles: [string]
  LoopAnimationIds: [string]
  ImpactAnimationIds: [string]
  ProjectileSpeed: i32
  _: bool
  _: i32
  _: bool
  _: bool
  InheritsFrom: string
  _: i32
  _: rid
  _: i32
  _: bool
  _: bool
  Stuck_AOFile: string
  Bounce_AOFile: string
  _: i32
  _: i32
  _: i32
  _: i32
  _: rid
  _: rid
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: [rid]
  _: rid
  _: bool
}

type ProjectileVariations {
  Id: string @unique
  ProjectileKey: Projectiles
}

# enum?
type PVPTypes { TODO_REMOVE_THIS: u8 }

type Quest {
  Id: string @unique
  Act: i32
  Name: string
  Icon_DDSFile: string
  QuestId: i32
  _: bool
  _: i32
  _: i32
  _: [i32]
  _: i32
}

type QuestAchievements {
  Id: string @unique
  QuestStates: [i32]
  _: [i32]
  AchievementItemsKeys: [u64]
  _: [rid]
}

# enum?
type QuestFlags { TODO_REMOVE_THIS: u8 }

type QuestRewardOffers {
  Id: string
  QuestKey: Quest
  QuestState: i32
  _: i32
  _: i32
}

# enum?
type QuestRewardType { TODO_REMOVE_THIS: u8 }

# enum?
type QuestStateCalculation { TODO_REMOVE_THIS: u8 }

type QuestStates {
  QuestKey: Quest
  _: i32
  QuestStates: [u32]
  _: [u32]
  Text: string
  _: bool
  Message: string
  MapPinsKeys1: [MapPins]
  _: i32
  MapPinsTexts: [string]
  MapPinsKeys2: [MapPins]
  _: [rid]
  _: bool
  _: [i32]
  QuestStateCalcuationKey: i32
  _: rid
  _: i32
  _: i32
}

type QuestStaticRewards {
  _: i32
  _: i32
  StatsKeys: [Stats]
  StatValues: [i32]
  QuestKey: Quest
  _: i32
  ClientStringsKey: ClientStrings
  _: i32
}

type QuestType {
  Id: string @unique
  _: [i32]
}

type Races {
  Id: string @unique
  _: [u64]
  _: [i32]
  _: i32
  _: bool
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

type RaceTimes {
  RacesKey: Races
  Index: i32
  StartUNIXTime: i32
  EndUNIXTime: i32
}

type RandomUniqueMonsters {
  _: i64
  _: [i64]
}

type RareMonsterLifeScalingPerLevel {
  Level: i32
  Life: i32
}

# enum?
type Rarity { TODO_REMOVE_THIS: u8 }

type Realms {
  Id: string @unique
  Name: string
  Server: [string]
  IsEnabled: bool
  Server2: [string]
  ShortName: string
  _: [i32]
  _: i32
  _: i32
  IsGammaRealm: bool
  _: [i32]
}

type RecipeUnlockDisplay {
  RecipeId: i32 @unique
  Description: string
  CraftingItemClassCategoriesKeys: [CraftingItemClassCategories]
  UnlockDescription: string
  Rank: i32
  _: rid
}

type RecipeUnlockObjects {
  WorldAreasKey: WorldAreas
  InheritsFrom: string
  RecipeId: i32
}

# enum?
type RelativeImportanceConstants { TODO_REMOVE_THIS: u8 }

type Rulesets {
  Id: string @unique
}

type RunicCircles {
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

type SalvageBoxes {
  _: rid
  Id: string @unique
  _: string
}

type SessionQuestFlags {
  QuestFlag: i32
}

type ShieldTypes {
  BaseItemTypesKey: BaseItemTypes @unique
  Block: i32
}

type ShopCategory {
  Id: string @unique
  ClientText: string
  ClientJPGFile: string
  WebsiteText: string
  WebsiteJPGFile: string
  _: i32
  AppliedTo_BaseItemTypesKey: BaseItemTypes
}

type ShopCountry {
  CountryTwoLetterCode: string
  Country: string
  ShopCurrencyKey: ShopCurrency
}

type ShopCurrency {
  CurrencyCode: string
  CurrencySign: string
}

# enum?
type ShopForumBadge { TODO_REMOVE_THIS: u8 }

# enum?
type ShopPackagePlatform { TODO_REMOVE_THIS: u8 }

type ShopPaymentPackage {
  Id: string @unique
  Text: string
  Coins: i32
  AvailableFlag: bool
  _: i32
  _: i32
  _: bool
  ContainsBetaKey: bool
  _: [i32]
  _: rid
  BackgroundImage: string
  _: string
  _: bool
  Upgrade_ShopPaymentPackageKey: ShopPaymentPackage
  PhysicalItemPoints: i32
  _: i32
  ShopPackagePlatformKeys: [i32]
  _: string
}

type ShopPaymentPackagePrice {
  ShopPaymentPackageKey: ShopPaymentPackage
  ShopCountryKey: ShopCountry
  Price: i32
}

# enum?
type ShopPaymentPackageProxy { TODO_REMOVE_THIS: u8 }

type ShopRegion {
  Id: string @unique
}

type ShopToken {
  Id: string
  TypeId: string
  Description: string
}

type SigilDisplay {
  Id: string @unique
  Active_StatsKey: Stats
  Inactive_StatsKey: Stats
  DDSFile: string
  Inactive_ArtFile: string
  Active_ArtFile: string
  Frame_ArtFile: string
}

type SkillGemInfo {
  Id: string @unique
  Description: string
  VideoURL1: string
  SkillGemsKey: SkillGems
  VideoURL2: string
  CharactersKeys: [Characters]
}

type SkillGems {
  BaseItemTypesKey: BaseItemTypes @unique
  GrantedEffectsKey: GrantedEffects
  Str: i32
  Dex: i32
  Int: i32
  GemTagsKeys: [GemTags]
  VaalVariant_BaseItemTypesKey: BaseItemTypes
  IsVaalVariant: bool
  Description: string
  Consumed_ModsKey: Mods
  GrantedEffectsKey2: GrantedEffects
  MinionGlobalSkillLevelStatsKey: u64
  SupportSkillName: string
  _: bool
  _: bool
  _: rid
}

# enum?
type SkillMines { TODO_REMOVE_THIS: u8 }

type SkillMineVariations {
  SkillMinesKey: i32
  _: i32
  _: rid
}

type SkillMorphDisplay {
  _: rid
  _: [rid]
  DDSFiles: [string]
  _: i32
  _: [i32]
  _: i32
  _: [f32]
  _: bool
  _: bool
}

# enum?
type SkillMorphDisplayOverlayCondition { TODO_REMOVE_THIS: u8 }

# enum?
type SkillMorphDisplayOverlayStyle { TODO_REMOVE_THIS: u8 }

type SkillSurgeEffects {
  GrantedEffectsKey: GrantedEffects
  _: string
  _: bool
  _: bool
  _: bool
  MiscAnimated: MiscAnimated
  _: bool
  _: bool
  _: i32
  _: bool
  _: [f32]
  _: [rid]
  _: bool
  _: [i32]
}

# enum?
type SkillTotems { TODO_REMOVE_THIS: u8 }

type SkillTotemVariations {
  SkillTotemsKey: SkillTotems
  TotemSkinId: i32
  MonsterVarietiesKey: MonsterVarieties
}

type SkillTrapVariations {
  Id: i32
  Metadata: string
  _: rid
}

type SoundEffects {
  Id: string @unique
  SoundFile: string
  SoundFile_2D: string
  _: bool
}

type SpawnAdditionalChestsOrClusters {
  StatsKey: Stats
  ChestsKey: Chests
  ChestClustersKey: ChestClusters
}

type SpawnObject {
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
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i16
}

type SpecialRooms {
  Id: string @unique
  ARMFile: string
}

type SpecialTiles {
  Id: string @unique
  TDTFile: string
}

type SpectreOverrides {
  _: rid
  _: rid
  _: [rid]
}

type StartingPassiveSkills {
  Id: string @unique
  PassiveSkills: [PassiveSkills]
}

# enum?
type StashId { TODO_REMOVE_THIS: u8 }

type StashType {
  Id: string @unique
  IntId: i32 @unique
  Id2: string
  _: i32
  _: i32
  _: i32
}

type StatDescriptionFunctions {
  Id: string @unique
  TranslationId: string @unique
}

# enum?
type StatInterpolationTypes { TODO_REMOVE_THIS: u8 }

type Stats {
  Id: string @unique
  _: bool
  IsLocal: bool
  IsWeaponLocal: bool
  _: i32
  _: bool
  Text: string
  _: bool
  _: bool
  MainHandAlias_StatsKey: Stats
  OffHandAlias_StatsKey: Stats
  _: bool
  _: i32
  BelongsActiveSkillsKey: [ActiveSkills] @ref(column: "Id")
  _: rid
  _: bool
  _: bool
  IsValueUsed: bool
  _: i32
  _: i32
}

# enum?
type StatSemantics { TODO_REMOVE_THIS: u8 }

type StrDexIntMissionExtraRequirement {
  Id: string @unique
  SpawnWeight: i32
  MinLevel: i32
  MaxLevel: i32
  TimeLimit: i32
  HasTimeBonusPerKill: bool
  HasTimeBonusPerObjectTagged: bool
  HasLimitedPortals: bool
  NPCTalkKey: NPCTalk
  TimeLimitBonusFromObjective: i32
  ObjectCount: i32
  _: [i32]
  _: bool
  _: [rid]
}

type StrDexIntMissions {
  Id: string @unique
  _: rid
  SpawnWeight: i32
  _: rid
  _: rid
  Extra_ModsKeys: [Mods]
  _: i8
  _: i8
  _: i8
  _: rid
  _: i32
  _: i32
  _: i32
  _: i32
  _: rid
  _: rid
  _: rid
  _: i8
  _: rid
  _: bool
}

type SuicideExplosion {
  Id: i32
  _: rid
  _: rid
  _: bool
  _: bool
  _: bool
  _: bool
  _: i32
}

type SummonedSpecificBarrels {
  Id: string @unique
  ChestsKey: Chests
  _: rid
  _: i32
  _: rid
}

type SummonedSpecificMonsters {
  Id: i32 @unique
  MonsterVarietiesKey: MonsterVarieties
  _: i32
  _: rid
  _: bool
  _: bool
  _: i32
  _: i32
  _: i8
  _: rid
  _: rid
  _: i32
  _: bool
  _: i32
}

type SummonedSpecificMonstersOnDeath {
  Id: string @unique
  MonsterVarietiesKey: MonsterVarieties
  _: i32
  _: rid
  _: i32
  _: i8
}

type SupporterPackSets {
  Id: string @unique
  FormatTitle: string
  Background: string
  Time0: string
  Time1: string
  ShopPackagePlatformKey: [i32]
  _: string
}

# enum?
type SurgeCategory { TODO_REMOVE_THIS: u8 }

type SurgeTypes {
  Id: string @unique
  _: [rid]
}

type TableMonsterSpawners {
  Metadata: string
  _: i32
  _: [u64]
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i8
  _: i32
  _: i32
  _: i8
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i8
  _: i8
  _: i32
  Script1: string
  _: i8
  _: i8
  Script2: string
  _: [i32]
  _: i32
  _: i32
}

type Tags {
  Id: string @unique
  _: u32
  DisplayString: string
  Name: string
}

type TencentAutoLootPetCurrencies {
  BaseItemTypesKey: BaseItemTypes
  _: i8
}

type TencentAutoLootPetCurrenciesExcludable {
  BaseItemTypesKey: BaseItemTypes
}

type TerrainPlugins {
  Id: string @unique
  _: i32 @unique
}

type Tips {
  Id: string @unique
  Text: string
  TextXBox: string
}

type Topologies {
  Id: string @unique
  DGRFile: string
  _: i32
  _: i32
  _: i32
}

type TreasureHunterMissions {
  _: string
  _: u64
  _: u64
  _: [u64]
  _: [u64]
  _: [u64]
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i8
  _: i32
  _: i32
  _: i32
}

type TriggerBeam {
  _: i32
  _: [u64]
  _: [u64]
  _: [i32]
  _: i8
  _: i32
  _: i32
  _: i32
  _: i32
  _: i8
  _: [i32]
  _: i8
}

type TriggerSpawners {
  Id: string @unique
  _: [i32]
  _: i32
  _: [i32]
  _: bool
}

type Tutorial {
  Id: string @unique
  UIFile: string
  _: rid
  IsEnabled: bool
  _: i32
  _: [i32]
  _: i32
  _: i32
  _: [i32]
  _: bool
  _: bool
}

# enum?
type UITalkCategories { TODO_REMOVE_THIS: u8 }

type UITalkText {
  Id: string @unique
  UITalkCategoriesKey: UITalkCategories
  OGGFile: string
  Text: string
  _: i8
  _: rid
}

type UniqueChests {
  Id: string @unique
  WordsKey: Words
  FlavourTextKey: FlavourText
  MinLevel: i32
  ModsKeys: [Mods]
  SpawnWeight: i32
  _: [i32]
  AOFile: string
  _: bool
  _: [u32]
  AppearanceChestsKey: Chests
  ChestsKey: Chests
  _: [rid]
}

type UniqueJewelLimits {
  UniqueItemsKey: u64
  Limit: i32
}

type UniqueMapInfo {
  BaseItemTypesKey: BaseItemTypes
  _: rid
  FlavourTextKey: FlavourText
  ItemVisualIdentityKey: ItemVisualIdentity
  _: i8
}

type UniqueMaps {
  ItemVisualIdentityKey: ItemVisualIdentity @unique
  WorldAreasKey: WorldAreas
  WordsKey: Words
  FlavourTextKey: FlavourText
  HasGuildCharacter: bool
  GuildCharacter: string
  Name: string
}

# enum?
type UniqueSetNames { TODO_REMOVE_THIS: u8 }

type UniqueStashLayout {
  WordsKey: Words
  ItemVisualIdentityKey: ItemVisualIdentity
  UniqueStashTypesKey: UniqueStashTypes
  _: rid
  _: i32
  _: i32
  _: bool
  _: bool
  UniqueStashLayoutKey: UniqueStashLayout
  UniqueStashLayoutKey2: UniqueStashLayout
  _: bool
}

type UniqueStashTypes {
  Id: string @unique
  Order: i32
  Width: i32
  Height: i32
  _: i32
  _: i32
  Name: string
  _: i32
  Image: string
  _: i32
}

type VoteState {
  Id: string @unique
  Text: string
}

type VoteType {
  Id: string @unique
  Text: string
  AcceptText: string
  RejectText: string
  _: i32
}

# enum?
type WeaponArmourCommon { TODO_REMOVE_THIS: u8 }

type WeaponClasses {
  _: rid
  _: i32
}

# enum?
type WeaponDamageScaling { TODO_REMOVE_THIS: u8 }

type WeaponImpactSoundData {
  Id: string @unique
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

# enum?
type WeaponSoundTypes { TODO_REMOVE_THIS: u8 }

type WeaponTypes {
  BaseItemTypesKey: BaseItemTypes @unique
  Critical: i32
  Speed: i32
  DamageMin: i32
  DamageMax: i32
  RangeMax: i32
  Null6: i32
}

# enum?
type Wordlists { TODO_REMOVE_THIS: u8 }

type Words {
  WordlistsKey: i32
  Text: string
  SpawnWeight_TagsKeys: [Tags]
  SpawnWeight_Values: [u32]
  _: i32
  Text2: string
  Inflection: string
}

type WorldAreas {
  Id: string @unique
  Name: string
  Act: i32
  IsTown: bool
  HasWaypoint: bool
  Connections_WorldAreasKeys: [WorldAreas]
  AreaLevel: i32
  _: i32
  _: i32
  _: i32
  LoadingScreen_DDSFile: string
  _: i32
  _: [i32]
  _: i32
  TopologiesKeys: [Topologies]
  ParentTown_WorldAreasKey: WorldAreas
  _: i32
  _: i32
  _: i32
  Bosses_MonsterVarietiesKeys: [MonsterVarieties]
  Monsters_MonsterVarietiesKeys: [MonsterVarieties]
  SpawnWeight_TagsKeys: [Tags]
  SpawnWeight_Values: [u32]
  IsMapArea: bool
  FullClear_AchievementItemsKeys: [AchievementItems]
  _: i32
  _: i32
  AchievementItemsKey: AchievementItems
  ModsKeys: [Mods]
  _: i32
  _: i32
  VaalArea_WorldAreasKeys: [WorldAreas]
  VaalArea_SpawnChance: i32
  Strongbox_SpawnChance: i32
  Strongbox_MaxCount: i32
  Strongbox_RarityWeight: [i32]
  _: i8
  _: i32
  MaxLevel: i32
  AreaType_TagsKeys: [Tags]
  _: i32
  _: i32
  IsHideout: bool
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  TagsKeys: [Tags]
  IsVaalArea: bool
  _: i32
  _: i32
  _: i32
  IsLabyrinthAirlock: bool
  IsLabyrinthArea: bool
  TwinnedFullClear_AchievementItemsKey: AchievementItems
  Enter_AchievementItemsKey: AchievementItems
  _: i32
  _: i32
  _: i32
  TSIFile: string
  _: rid
  _: i32
  _: i32
  _: i32
  WaypointActivation_AchievementItemsKeys: [AchievementItems]
  IsUniqueMapArea: bool
  IsLabyrinthBossArea: bool
  _: i32
  _: i32
  FirstEntry_NPCTextAudioKey: NPCTextAudio
  FirstEntry_SoundEffectsKey: SoundEffects
  FirstEntry_NPCsKey: NPCs @ref(column: "Id")
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  EnvironmentsKey: Environments
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
  _: bool
  _: i32
  _: i32
  _: i8
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  MetamorphChance: i32
  DeliriumChance: i32
  HarvestChance: i32
  HeistChance: i32
}

type WorldPopupIconTypes {
  Id: string @unique
  _: string
  _: string
  _: string
}

type ZanaLevels {
  _: i32
  _: i32
}
