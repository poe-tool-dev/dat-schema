import * as path from 'path';
import * as process from 'process';
import * as fs from 'fs';
import { Source } from 'graphql/language/source';
import { GraphQLError, printError } from 'graphql/error';
import { readSpecs } from './reader';
import { SchemaTable, SCHEMA_VERSION } from './types';

const SPEC_PATH = path.join(__dirname, '../dat-spec');

function read(): SchemaTable[] {
  const sources = fs.readdirSync(SPEC_PATH).map((entryName) => {
    const contents = fs.readFileSync(path.join(SPEC_PATH, entryName), {
      encoding: 'utf-8',
    });
    return new Source(contents, entryName);
  });

  try {
    return readSpecs(sources);
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
    tables: read(),
  })
);
