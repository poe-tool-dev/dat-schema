
type Prophecies {
  Id: string @unique
  PredictionText: string
  _: i32 @unique
  Name: string
  FlavourText: string
  QuestTracker_ClientStringsKeys: [ClientStrings]
  OGGFile: string
  ProphecyChainKey: ProphecyChain
  ProphecyChainPosition: i32
  IsEnabled: bool
  SealCost: i32
  PredictionText2: string
}

type ProphecyChain {
  Id: string @unique
  _: i32
  _: [i32]
  _: [i32]
  _: i32
  _: i32
}

# enum?
type ProphecySetNames { TODO_REMOVE_THIS: u8 }

type ProphecyType {
  Id: string @unique
  _: i32 @unique
}
