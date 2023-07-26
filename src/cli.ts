import * as path from 'node:path';
import { fileURLToPath } from 'node:url';
import * as process from 'node:process';
import * as fs from 'node:fs';
import { Source, GraphQLError } from 'graphql';
import { readSchemaSources } from './reader.js';
import {
  SchemaFile,
  SchemaLine,
  SchemaMetadata,
  SCHEMA_VERSION,
} from './types.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const SCHEMA_PATH = path.join(__dirname, '../dat-schema');

function read() {
  const sources = fs.readdirSync(SCHEMA_PATH).map((entryName) => {
    const contents = fs.readFileSync(path.join(SCHEMA_PATH, entryName), {
      encoding: 'utf-8',
    });
    return new Source(contents, entryName);
  });

  try {
    return readSchemaSources(sources);
  } catch (e) {
    if (e instanceof GraphQLError) {
      console.error(e.toString());
      if (e.originalError instanceof GraphQLError) {
        console.error('\n-----\n' + e.originalError.toString());
      }
      process.exit(1);
    } else {
      throw e;
    }
  }
}

const readResult = read();

const metadata: SchemaMetadata = {
  version: SCHEMA_VERSION,
  createdAt: Math.floor(Date.now() / 1000),
};

fs.writeFileSync(
  path.join(process.cwd(), './schema.min.json'),
  JSON.stringify({ ...metadata, ...readResult } satisfies SchemaFile)
);

fs.writeFileSync(
  path.join(process.cwd(), './schema.jsonl'),
  [metadata, ...readResult.tables, ...readResult.enumerations]
    .map((line: SchemaLine) => JSON.stringify(line))
    .join('\n') + '\n'
);
