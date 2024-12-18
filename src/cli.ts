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

const WATCH_MODE = process.argv.includes('--watch');

const SCHEMA_PATH =
  process.argv
    .slice(2)
    .filter((arg) => arg !== '--watch')
    .at(0) || path.join(__dirname, '../dat-schema');

function read() {
  const sources = fs.readdirSync(SCHEMA_PATH, { recursive: true, withFileTypes: true })
    .filter(entry => entry.isFile())
    .map((entry) => {
      const contents = fs.readFileSync(path.join(entry.parentPath, entry.name), {
        encoding: 'utf-8',
      });
      return new Source(contents, path.relative(SCHEMA_PATH, path.join(entry.parentPath, entry.name)));
    });

  try {
    return readSchemaSources(sources);
  } catch (e) {
    if (e instanceof GraphQLError) {
      console.error(e.toString());
      if (e.originalError instanceof GraphQLError) {
        console.error('\n-----\n' + e.originalError.toString());
      }
      return null;
    } else {
      throw e;
    }
  }
}

function runOnce(): boolean {
  const readResult = read();
  if (!readResult) return false;

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

  console.log(`[${new Date().toISOString()}] Done.`);
  return true;
}

const ok = runOnce();
if (!ok && !WATCH_MODE) {
  process.exit(1);
}

if (WATCH_MODE) {
  const watcher = await import('@parcel/watcher');
  watcher.subscribe(SCHEMA_PATH, () => {
    console.clear();
    runOnce();
  });
}
