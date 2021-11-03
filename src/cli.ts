import * as path from 'path';
import * as process from 'process';
import * as fs from 'fs';
import { Source } from 'graphql/language/source';
import { GraphQLError, printError } from 'graphql/error';
import { readSchemaSources } from './reader';
import { SchemaFile, SCHEMA_VERSION } from './types';

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
  } catch (e: unknown) {
    if (e instanceof GraphQLError) {
      console.error(printError(e));
      if (e.originalError instanceof GraphQLError) {
        console.error('\n-----\n' + printError(e.originalError));
      }
      process.exit(1);
    } else {
      throw e;
    }
  }
}

fs.writeFileSync(
  path.join(process.cwd(), './schema.min.json'),
  JSON.stringify({
    version: SCHEMA_VERSION,
    createdAt: Math.floor(Date.now() / 1000),
    ...read(),
  } as SchemaFile)
);
