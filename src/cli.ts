import { readdirSync, readFileSync } from 'fs';
import * as path from 'path';
import { readFiles } from './read/reader';

const schema = readFiles(
  readdirSync(path.join(__dirname, './dat-spec')).map((filename) => ({
    name: filename,
    contents: readFileSync(path.join(__dirname, './dat-spec', filename), {
      encoding: 'utf-8',
    }),
  }))
);

console.log(schema);
