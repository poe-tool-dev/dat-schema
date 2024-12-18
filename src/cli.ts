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

const SCHEMA_PATH = process.argv[2] || path.join(__dirname, '../dat-schema');
const OUTPUT_PATH = process.argv[3] || process.cwd();
const MIN = 'schema.min.json';
const JSONL = 'schema.jsonl';

function read() {
  const sources = fs
    .readdirSync(SCHEMA_PATH, { recursive: true, withFileTypes: true })
    .filter((entry) => entry.isFile())
    .map((entry) => {
      const contents = fs.readFileSync(
        path.join(entry.parentPath, entry.name),
        {
          encoding: 'utf-8',
        },
      );
      return new Source(
        contents,
        path.relative(SCHEMA_PATH, path.join(entry.parentPath, entry.name)),
      );
    });

  return readSchemaSources(sources);
}

export function generate() {
  const readResult = read();
  const metadata: SchemaMetadata = {
    version: SCHEMA_VERSION,
    createdAt: Math.floor(Date.now() / 1000),
  };
  return {
    [MIN]: JSON.stringify({
      ...metadata,
      ...readResult,
    } satisfies SchemaFile),
    [JSONL]:
      [metadata, ...readResult.tables, ...readResult.enumerations]
        .map((line: SchemaLine) => JSON.stringify(line))
        .join('\n') + '\n',
  };
}

try {
  const output = generate();
  for (const filename in output) {
    fs.writeFileSync(
      path.join(OUTPUT_PATH, filename),
      output[filename as keyof typeof output],
    );
  }
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
