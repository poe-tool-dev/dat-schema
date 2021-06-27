
type HeistAreaFormationLayout {
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
  _: bool
  _: i32
  _: i32
}

type HeistAreas {
  Id: string @unique
  WorldAreasKeys: [WorldAreas]
  _: i32
  EnvironmentsKey1: Environments
  EnvironmentsKey2: Environments
  HeistJobsKeys: [HeistJobs]
  Contract_BaseItemTypesKey: BaseItemTypes
  Blueprint_BaseItemTypesKey: BaseItemTypes
  DGRFile: string
  _: i32
  _: i32
  _: bool
  _: bool
  Blueprint_DDSFile: string
  AchievementItemsKeys: [AchievementItems]
  AchievementItemsKeys2: [AchievementItems]
  ClientStringsKey: ClientStrings
}

type HeistBalancePerLevel {
  Level: i32
  _: f32
  _: f32
  _: i32
  _: i32
  _: f32
  _: f32
  _: rid
  _: rid
  _: rid
  _: rid
  _: rid
  _: f32
  _: f32
  _: f32
  _: f32
  _: rid
  _: rid
  _: f32
  _: f32
  _: i32
}

enum HeistBlueprintWindowTypes { _ }

type HeistChestRewardTypes {
  Id: string @unique
  Art: string
  RewardTypeName: string
  _: i32
  RewardRoomName: string
  MinLevel: i32
  MaxLevel: i32
  Weight: i32
  RewardRoomName2: string
  _: [rid]
  _: i32
}

type HeistChests {
  ChestsKey: Chests
  Weight: i32
  _: [rid]
  HeistChestTypesKey: HeistChestTypes
}

enum HeistChestTypes { _ }

type HeistChokepointFormation {
  _: rid
  _: i32
  _: [i32]
  _: [rid]
  _: rid
  _: i32
  _: i8
  _: i32
  _: i32
  _: i32
  _: i32
}

type HeistConstants {
  Id: string @unique
  Value: f32
}

type HeistContracts {
  BaseItemTypesKey: BaseItemTypes @unique
  HeistAreasKey: HeistAreas
  _: i32
}

type HeistDoodadNPCs {
  _: rid
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  AOFile: string
  Stance: string
  _: rid
}

type HeistDoors {
  Id: string @unique
  _: string
  _: rid
  _: rid
  _: string
  _: [string]
  _: [string]
  _: i32
  _: rid
}

type HeistEquipment {
  BaseItemTypesKey: BaseItemTypes @unique
  RequiredJob_HeistJobsKey: HeistJobs
  RequiredLevel: i32
}

enum HeistFormationMarkerType { _ }

type HeistGeneration {
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

type HeistIntroAreas {
  Id: string @unique
  _: rid
  _: i32
  _: i32
  DGRFile: string
  _: i32
  _: i32
  _: i8
  _: i32
  _: i32
  _: i32
}

type HeistJobs {
  Id: string @unique
  Name: string
  RequiredSkillIcon: string
  SkillIcon: string
  _: f32
  _: i32
  MapIcon: string
  Level_StatsKey: Stats
  Alert_StatsKey: Stats
  Alarm_StatsKey: Stats
  Cost_StatsKey: Stats
  ExperienceGain_StatsKey: Stats
}

type HeistJobsExperiencePerLevel {
  HeistJobsKey: HeistJobs
  Tier: i32
  Experience: i32
  MinLevel: i32
  _: [rid]
}

type HeistLockType {
  Id: string @unique
  HeistJobsKey: HeistJobs
  SkillIcon: string
}

type HeistNPCAuras {
  StatsKey: Stats
  _: u64
}

type HeistNPCBlueprintTypes {
  _: rid
  _: i32
}

type HeistNPCDialogue {
  _: rid
  _: rid
  _: [rid]
  _: [rid]
  _: i32
}

type HeistNPCs {
  NPCsKey: NPCs
  MonsterVarietiesKey: MonsterVarieties
  SkillLevel_HeistJobsKeys: [HeistJobs]
  PortraitFile: string
  HeistNPCStatsKeys: [HeistNPCStats]
  StatValues: [f32]
  _: f32
  SkillLevel_Values: [i32]
  Name: string
  _: i32
  SilhouetteFile: string
  _: i32
  _: i32
  HeistNPCsKey: HeistNPCs
  StatValues2: [f32]
  Ally_NPCsKey: NPCs
  ActiveNPCIcon: string
  HeistJobsKey: HeistJobs
  Equip_AchievementItemsKeys: [AchievementItems]
  AOFile: string
}

type HeistNPCStats {
  StatsKey: Stats
  _: bool
  _: bool
  _: bool
  _: bool
}

type HeistObjectives {
  key0: u64
  _: f32
  Name: string
}

type HeistObjectiveValueDescriptions {
  _: i32
  _: i32
  _: i32
}

type HeistPatrolPacks {
  MonsterPacksKey: MonsterPacks
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i8
}

type HeistQuestContracts {
  _: rid
  _: rid
  _: [rid]
  _: rid
  _: i32
  _: i32
  _: i32
  _: i8
  _: rid
  _: rid
  _: i8
  _: i8
  _: i32
  _: i32
  _: i8
  _: i8
  _: i32
  _: i8
  _: i32
  _: i32
  _: i32
  _: i8
  _: i8
  Objective: string
  _: i8
  _: rid
  _: i8
  _: rid
  _: i32
  _: rid
  _: string
}

type HeistRevealingNPCs {
  NPCsKey: NPCs
  PortraitFile: string
  _: [rid]
  _: i32
}

type HeistRooms {
  HeistJobsKey: HeistJobs
  Id: i32
  ARMFile: string
  _: rid
  _: rid
  _: i32
  _: i32
  _: i32
  _: i32
  _: f32
  _: i8
  _: i8
}

enum HeistRoomTypes { _ }

type HeistValueScaling {
  Id: string @unique
  _: f32
  _: f32
}
