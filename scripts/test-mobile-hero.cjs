// Build dist first. Uses an existing Playwright installation; no network setup.
// PLAYWRIGHT_MODULE and CHROME_PATH can select local tooling.
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright-core');
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const root = path.resolve(__dirname, '../dist');
const evidence = process.env.HERO_EVIDENCE_DIR;
const results = [];
const server = http.createServer((req, res) => {
  const file = path.resolve(root, '.' + new URL(req.url, 'http://localhost').pathname.replace(/\/$/, '/index.html'));
  if (!file.startsWith(root + path.sep) || !fs.existsSync(file)) { res.writeHead(404).end(); return; }
  const types = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.png': 'image/png', '.webp': 'image/webp' };
  res.setHeader('Content-Type', types[path.extname(file)] || 'application/octet-stream');
  fs.createReadStream(file).pipe(res);
});
(async () => {
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const origin = `http://127.0.0.1:${server.address().port}`;
  let browser;
  try {
    browser = await chromium.launch({ executablePath: process.env.CHROME_PATH, headless: true });
    if (evidence) fs.mkdirSync(evidence, { recursive: true });
    for (const [width, height] of [[320,568],[375,667],[390,844],[320,400],[375,400],[390,400],[844,390],[1366,900]]) {
      const page = await browser.newPage({ viewport: { width, height }, reducedMotion: 'reduce' });
      await page.route('**/*', route => new URL(route.request().url()).origin === origin ? route.continue() : route.abort());
      await page.goto(origin);
      const layout = await page.evaluate(() => {
        const indicator = document.querySelector('.hero-scroll');
        const box = indicator.getBoundingClientRect();
        return {
          pointerSafe: getComputedStyle(indicator).pointerEvents === 'none',
          noOverlap: [...document.querySelectorAll('.hero-btns a')].every(a => {
            const b = a.getBoundingClientRect();
            return box.right <= b.left || box.left >= b.right || box.bottom <= b.top || box.top >= b.bottom;
          }),
          noOverflow: document.documentElement.scrollWidth <= innerWidth,
        };
      });
      if (evidence) await page.locator('.hero').screenshot({ path: path.join(evidence, `hero-${width}x${height}.png`) });
      const clicks = [];
      for (const [label, target] of [['Explore Video Series', '/pages/youtube.html'], ['Explore TradeBoard', '/pages/tradeboard.html']]) {
        await page.goto(origin);
        try {
          await page.getByRole('link', { name: label }).click({ timeout: 3000 });
          clicks.push(new URL(page.url()).pathname === target);
        } catch { clicks.push(false); }
      }
      results.push({ width, height, ...layout, clicks, pass: Object.values(layout).every(Boolean) && clicks.every(Boolean) });
      await page.close();
    }
    const menuPage = await browser.newPage({ viewport: { width:390, height:844 } });
    await menuPage.route('**/*', route => new URL(route.request().url()).origin === origin ? route.continue() : route.abort());
    await menuPage.goto(origin);
    await menuPage.locator('.hamburger').click();
    await menuPage.setViewportSize({ width:1366, height:900 });
    await menuPage.waitForFunction(() => document.querySelector('.hamburger').getAttribute('aria-expanded') === 'false');
    const resizedClosed = !await menuPage.locator('.mobile-nav').isVisible();
    await menuPage.setViewportSize({ width:390, height:844 });
    await menuPage.locator('.hamburger').click();
    await menuPage.locator('.hero-btns a').first().focus();
    const focusClosed = await menuPage.locator('.hamburger').getAttribute('aria-expanded') === 'false';
    results.push({ menuResizeAndFocus: true, resizedClosed, focusClosed, pass: resizedClosed && focusClosed });
    await menuPage.close();
  } finally {
    if (browser) await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
  if (evidence) fs.writeFileSync(path.join(evidence, 'results.json'), JSON.stringify(results, null, 2));
  console.log(JSON.stringify(results, null, 2));
  if (results.some(result => !result.pass)) process.exitCode = 1;
})().catch(error => { console.error(error.message); server.close(); process.exitCode = 1; });
