import * as fs from 'fs';
import * as pluralize from 'pluralize'

// from PyPoE.poe.file.specification.data import stable
// from json import dump
// with open('./spec.json', 'w') as f:
//     dump(stable.specification.as_dict(), f)

const pypoe = require('../spec.json') as Record<string, any>;

const fileContentsMap = new Map([
  ['0_11_Anarchy', ''],
  ['1_00_Domination', ''],
  ['1_01_Invasion', ''],
  ['1_01_Ambush', ''],
  ['1_02_Beyond', ''],
  ['1_03_Bloodlines', ''],
  ['1_03_Torment', ''],
  ['2_00_The_Awakening', ''],
  ['2_00_Warbands', ''],
  ['2_01_Talisman', ''],
  ['2_02_Ascendancy', ''],
  ['2_02_Perandus', ''],
  ['2_03_Prophecy', ''],
  ['2_04_Essence', ''],
  ['2_05_Breach', ''],
  ['3_00_The_Fall_of_Oriath', ''],
  ['3_00_Harbinger', ''],
  ['3_01_Abyss', ''],
  ['3_02_Bestiary', ''],
  ['3_03_Incursion', ''],
  ['3_04_Delve', ''],
  ['3_05_Betrayal', ''],
  ['3_06_Synthesis', ''],
  ['3_07_Legion', ''],
  ['3_08_Blight', ''],
  ['3_09_Conquerors_of_the_Atlas', ''],
  ['3_09_Metamorph', ''],
  ['3_10_Delirium', ''],
  ['3_11_Harvest', ''],
  ['3_12_Heist', ''],
  ['3_13_Ritual', ''],
  ['3_14_Ultimatum', ''],
  ['_Core', ''],
]);

const pairs = Object.entries(pypoe).sort(([aName], [bName]) =>
  aName.localeCompare(bName)
);

for (const [filename, { fields }] of pairs) {
  const tableName = filename.split('.')[0];
  fileContentsMap.set(
    tableNameToFilename(tableName),
    fileContentsMap.get(tableNameToFilename(tableName)) +
      `\ntype ${tableName} {\n${genFields(fields)}\n}\n`
  );
}

for (const [name, contents] of fileContentsMap) {
  fs.writeFileSync(`./dat-spec/${name}.spec`, contents);
}

function genFields(fields: Record<string, any>) {
  return Object.entries(fields)
    .map(
      ([name, field]) =>
        `  ${normalizeName(name, field)}: ${transformType({ ...field, name })}${
          field.unique ? ' @unique' : ''
        }`
    )
    .join('\n');
}

function transformType(field: Record<string, any>): string {
  let type = '';
  let array = false;

  let value = field.type;
  if (value.startsWith('ref|list|')) {
    array = true;
    value = value.substr('ref|list|'.length);
  }

  if (field.key) {
    type = field.key.split('.')[0];
  } else if (
    (value === 'ulong' || value === 'long') &&
    /^Keys?([0-9]+)?$/.test(field.name)
  ) {
    type = 'rid';
  } else if (value === 'ref|string') {
    type = 'string';
  } else if (value === 'bool') {
    type = 'bool';
  } else if (value === 'byte') {
    type = 'i8';
  } else if (value === 'ubyte') {
    type = 'u8';
  } else if (value === 'short') {
    type = 'i16';
  } else if (value === 'ushort') {
    type = 'u16';
  } else if (value === 'int' || value === 'ref|int') {
    type = 'i32';
  } else if (value === 'uint') {
    type = 'u32';
  } else if (value === 'long') {
    type = 'i64';
  } else if (value === 'ulong') {
    type = 'u64';
  } else if (value === 'float') {
    type = 'f32';
  } else if (value === 'double') {
    type = 'f64';
  } else {
    throw new Error(`never "${value}"`);
  }

  type = array ? `[${type}]` : type;

  if (field.key_id) {
    type += ` @ref(column: "${field.key_id}")`;
  }

  return type;
}

function normalizeName(name: string, field: Record<string, any>): string {
  if (
    name.includes('Unknown') ||
    /^Keys?([0-9]+)?$/.test(name) ||
    /^Flag([0-9]+)$/.test(name) ||
    /^Data([0-9]+)$/.test(name) ||
    /^Index([0-9]+)$/.test(name)
  ) {
    return '_';
  }

  // if (field.key /* && !name.includes('_') */) {
  //   if (name.endsWith('Keys')) {
  //     name = name.slice(0, -'Keys'.length)
  //     return pluralize.plural(name)
  //   } else if (name.endsWith('Key')) {
  //     name = name.slice(0, -'Key'.length)
  //     return pluralize.singular(name)
  //   }
  // }

  return name;
}

function tableNameToFilename(name: string) {
  if (name.includes('Stash') || name.includes('Storage')) {
    return '_Core';
  } else if (name.startsWith('RogueExile')) {
    return '0_11_Anarchy';
  } else if (name.startsWith('Shrine')) {
    return '1_00_Domination';
  } else if (name.startsWith('Invasion')) {
    return '1_01_Invasion';
  } else if (name.startsWith('Strongbox')) {
    return '1_01_Ambush';
  } else if (name.startsWith('Beyond')) {
    return '1_02_Beyond';
  } else if (name.startsWith('Bloodline')) {
    return '1_03_Bloodlines';
  } else if (name.startsWith('Torment')) {
    return '1_03_Torment';
  } else if (name.startsWith('DivinationCard')) {
    return '2_00_The_Awakening';
  } else if (name.startsWith('Warbands')) {
    return '2_00_Warbands';
  } else if (name.startsWith('Talisman')) {
    return '2_01_Talisman';
  } else if (name.startsWith('Labyrinth')) {
    return '2_02_Ascendancy';
  } else if (name.startsWith('Perandus')) {
    return '2_02_Perandus';
  } else if (name.startsWith('Prophec')) {
    return '2_03_Prophecy';
  } else if (name.startsWith('Essence')) {
    return '2_04_Essence';
  } else if (name.startsWith('Breach')) {
    return '2_05_Breach';
  } else if (name.startsWith('Pantheon')) {
    return '3_00_The_Fall_of_Oriath';
  } else if (name.startsWith('Harbinger')) {
    return '3_00_Harbinger';
  } else if (name.startsWith('Abyss')) {
    return '3_01_Abyss';
  } else if (name.startsWith('Bestiary')) {
    return '3_02_Bestiary';
  } else if (
    name.startsWith('Incursion') ||
    name === 'ArchitectLifeScalingPerLevel'
  ) {
    return '3_03_Incursion';
  } else if (name.startsWith('Delve')) {
    return '3_04_Delve';
  } else if (
    name.startsWith('Betrayal') ||
    name.startsWith('Safehouse') ||
    name.startsWith('Scarab')
  ) {
    return '3_05_Betrayal';
  } else if (name.startsWith('Synthesis')) {
    return '3_06_Synthesis';
  } else if (name.startsWith('Legion') || name === 'Incubators') {
    return '3_07_Legion';
  } else if (name.startsWith('Blight')) {
    return '3_08_Blight';
  } else if (name.startsWith('AtlasExile')) {
    return '3_09_Conquerors_of_the_Atlas';
  } else if (
    name.startsWith('Metamorph') ||
    name.startsWith('AlternateQuality')
  ) {
    return '3_09_Metamorph';
  } else if (name.startsWith('Affliction')) {
    return '3_10_Delirium';
  } else if (name.startsWith('Harvest')) {
    return '3_11_Harvest';
  } else if (name.startsWith('Heist')) {
    return '3_12_Heist';
  } else if (name.startsWith('Ritual')) {
    return '3_13_Ritual';
  } else if (name.startsWith('Ultimatum')) {
    return '3_14_Ultimatum';
  } else {
    return '_Core';
  }
}
