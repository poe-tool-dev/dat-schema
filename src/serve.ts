import { generate } from './cli.js';
import http from 'http';

const HOSTNAME = '0.0.0.0';
const PORT = 3001;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'application/json');
  res.setHeader('Access-Control-Allow-Origin', '*');

  let output;
  try {
    output = generate();
  } catch (e: any) {
    res.statusCode = 500;
    res.end(JSON.stringify({ error: e.message }));
    return;
  }

  if (req.url === '/') {
    const links = Object.keys(output).map(
      (key) => `<a href="/${key}">${key}</a>`,
    );
    res.setHeader('Content-Type', 'text/html');
    res.end(`<html><body>${links.join('<br>')}</body></html>`);
    return;
  }

  const keys = Object.keys(output) as (keyof typeof output)[];
  for (const key in keys) {
    if (req.url === '/' + keys[key]) {
      res.end(output[keys[key]]);
      return;
    }
  }

  res.statusCode = 404;
  res.end(JSON.stringify({ error: 'Not found' }));
});

server.listen(PORT, HOSTNAME, () => {
  console.log(`Server running at http://${HOSTNAME}:${PORT}/`);
});
