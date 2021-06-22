import * as path from 'path';
import * as process from 'process';
import { readdirSync, readFileSync } from 'fs';
import { Source } from 'graphql/language/source';
import { GraphQLError, printError } from 'graphql/error';
import { readSpecs } from './read/reader';

const SPEC_PATH = path.join(__dirname, './dat-spec');

let schema: unknown;
{
  const sources = readdirSync(SPEC_PATH).map((entryName) => {
    const contents = readFileSync(path.join(SPEC_PATH, entryName), {
      encoding: 'utf-8',
    });
    return new Source(contents, entryName);
  });

  try {
    schema = readSpecs(sources);
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

console.log(schema);
