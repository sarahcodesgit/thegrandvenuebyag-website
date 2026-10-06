import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { renderRoute } from '../src/ssg';
import { canonicalFor, navigation, routes, type RouteKey } from '../src/data/site';

const distDirectory = join(process.cwd(), 'dist');
const routeKeys: RouteKey[] = ['home', 'venue', 'weddings', 'events', 'gallery', 'contact', 'notFound'];

function escapeAttribute(value: string): string {
  return value.replaceAll('&', '&amp;').replaceAll('"', '&quot;').replaceAll('<', '&lt;').replaceAll('>', '&gt;');
}

function extractAssetTags(viteDocument: string): string {
  const tags = viteDocument.match(/<(?:script|link)\b[^>]*(?:\/assets\/)[^>]*(?:><\/script>|\/?>)/g) ?? [];
  if (tags.length === 0) throw new Error('Could not find Vite-built asset tags in dist/index.html.');
  return tags.join('\n    ');
}

function noScriptNavigation(currentPath: string): string {
  const links = navigation.map((item) => `<a href="${item.href}"${item.href === currentPath ? ' aria-current="page"' : ''}>${item.label}</a>`).join('');
  return `<noscript><nav class="noscript-nav" aria-label="Primary navigation">${links}</nav></noscript>`;
}

function createDocument(route: RouteKey, assetTags: string): string {
  const page = routes[route];
  const canonical = canonicalFor(page);
  const robots = page.noindex ? '    <meta name="robots" content="noindex,follow">\n' : '';
  const body = renderRoute(route);

  return `<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#171513">
    <title>${escapeAttribute(page.title)}</title>
    <meta name="description" content="${escapeAttribute(page.description)}">
${robots}    <link rel="canonical" href="${canonical}">
    <meta property="og:type" content="website">
    <meta property="og:title" content="${escapeAttribute(page.title)}">
    <meta property="og:description" content="${escapeAttribute(page.description)}">
    <meta property="og:url" content="${canonical}">
    <meta property="og:site_name" content="The AG Grand Venue">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="${escapeAttribute(page.title)}">
    <meta name="twitter:description" content="${escapeAttribute(page.description)}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Jost:wght@400;500;600&display=swap" rel="stylesheet">
    <script>document.documentElement.classList.add('js')</script>
    ${assetTags}
  </head>
  <body class="${page.bodyClass}">
    ${noScriptNavigation(page.path)}
    <div id="root">${body}</div>
  </body>
</html>
`;
}

async function main() {
  const viteDocument = await readFile(join(distDirectory, 'index.html'), 'utf8');
  const assetTags = extractAssetTags(viteDocument);

  await Promise.all(routeKeys.map(async (route) => {
    const page = routes[route];
    const output = route === 'home'
      ? join(distDirectory, 'index.html')
      : route === 'notFound'
        ? join(distDirectory, '404.html')
        : join(distDirectory, page.path.slice(1), 'index.html');
    await mkdir(dirname(output), { recursive: true });
    await writeFile(output, createDocument(route, assetTags));
  }));
}

void main();
