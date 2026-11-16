import assert from 'node:assert/strict';
import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
const root = 'dist';
const walk = (dir) => readdirSync(dir, { withFileTypes: true }).flatMap(e => e.isDirectory() ? walk(join(dir, e.name)) : [join(dir, e.name)]);
const files = walk(root);
const html = files.filter(f => f.endsWith('.html'));
const routes = ['index.html', 'research/index.html', 'publications/index.html', 'publications/scrapmem/index.html', 'publications/hu2026ondeviceagentmemory/index.html', 'publications/specgan/index.html', 'projects/embodied/index.html', 'blog/index.html', 'blog/admission-memoir/index.html', 'cv/index.html', 'news/index.html', '404.html', 'rss.xml', 'sitemap.xml', 'pagefind/pagefind.js', 'assets/pdf/jiale-chang-cv.pdf'];
for (const route of routes) assert.ok(existsSync(join(root, route)), `Missing ${route}`);
for (const draft of ['publishing-guide']) assert.ok(!files.some(f => f.includes(draft)), `Draft leaked: ${draft}`);
let checked = 0;
for (const file of html) {
 const body = readFileSync(file, 'utf8');
 assert.ok(!/Albert Einstein|einstein@example|qc6CJjYAAAAJ|18434539751|求职意向/.test(body), `Demo or private data: ${file}`);
 assert.ok(body.includes('https://changjiale444.github.io'), `Wrong site origin: ${file}`);
 for (const m of body.matchAll(/(?:href|src)="(\/[^"?#]*)(?:[?#][^"]*)?"/g)) {
  const path = decodeURIComponent(m[1]);
  assert.ok(!path.startsWith('/as-folio'), `Template base: ${file}`);
  const target = join(root, path);
  assert.ok(existsSync(target) || existsSync(join(target, 'index.html')), `Broken local resource ${path} in ${file}`);
  checked++;
 }
 for (const tag of body.matchAll(/<a\b[^>]*href="https?:[^>]+>/g)) {
  assert.ok(tag[0].includes('target="_blank"') && /rel="[^"]*noopener/.test(tag[0]) && /rel="[^"]*noreferrer/.test(tag[0]), `Unsafe external link in ${file}: ${tag[0]}`);
 }
}
const home = readFileSync(join(root, 'index.html'), 'utf8');
assert.ok(home.includes('2026.11') && home.includes('2026.10') && home.includes('Month TBD'), 'News date precision lost');
assert.ok(home.includes('<strong>Jiale Chang</strong>'), 'Author emphasis missing');
const rss = readFileSync(join(root, 'rss.xml'), 'utf8');
assert.ok(rss.includes('/blog/admission-memoir/'), 'Published first post missing from RSS');
assert.ok(!rss.includes('publishing-guide'), 'Draft leaked into RSS');
assert.ok(home.includes('/blog/admission-memoir/'), 'First post missing from homepage');
assert.ok(readFileSync(join(root, 'sitemap.xml'), 'utf8').includes('/blog/admission-memoir/'), 'Published post missing from sitemap');
console.log(`Verified ${html.length} HTML pages, ${checked} local resource references, required routes, external link attributes, date precision, author emphasis, and draft exclusion.`);
