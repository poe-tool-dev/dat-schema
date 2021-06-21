type HarvestObject {
  _: ref!
  _: i16
  part: [HarvestPart] @ref(field: "name")
  part2: [HarvestPart]
  Test: string! @unique
}

type HarvestPart {
  name: string! @unique
}
