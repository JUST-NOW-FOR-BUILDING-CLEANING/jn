import { createRequire } from "node:module"; import { execSync } from "node:child_process";
const require = createRequire(import.meta.url);
const { chromium } = require(execSync("npm root -g").toString().trim() + "/playwright");
const BASE = "https://justnowforbuildingcleaningservicescollc.bookingkoala.com";
const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY }, args: ["--ignore-certificate-errors", "--disable-quic"] });
const ctx = await b.newContext({ ignoreHTTPSErrors: true, viewport: { width: 1440, height: 1000 }, userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" });
const page = await ctx.newPage();
await page.goto(BASE + "/booknow", { waitUntil: "domcontentloaded" }); await page.waitForTimeout(6000);
await page.locator("#locationMenu").click(); await page.waitForTimeout(800);
const locs = await page.evaluate(() => [...document.querySelectorAll(".bk-dropdown-link")].filter(e => e.offsetParent).map(e => e.innerText.trim()));
await page.keyboard.press("Escape");
console.log("LOCS", locs);
const out = {};
for (const loc of locs) {
  await page.locator("#locationMenu").click(); await page.waitForTimeout(600);
  await page.locator(".bk-dropdown-link", { hasText: loc }).filter({ visible: true }).first().click(); await page.waitForTimeout(2500);
  out[loc] = {};
  const svcSel = page.locator("select.bk-select").first();
  const svcs = await svcSel.evaluate(s => [...s.options].map(o => [o.value, o.text.trim()]));
  for (const [val, name] of svcs) {
    if (!val) continue;
    await svcSel.selectOption(val); await page.waitForTimeout(2000);
    const opts = await page.evaluate(() => [...document.querySelectorAll("select.bk-select")].slice(1).filter(s => s.offsetParent).map(s => [...s.options].map(o => o.text.trim()).filter(Boolean)));
    const heads = await page.evaluate(() => [...document.querySelectorAll("label, h5, h6, .fw-bold")].filter(e => e.offsetParent && /package/i.test(e.innerText)).map(e => e.innerText.trim()));
    out[loc][name] = { heads, opts };
  }
}
console.log(JSON.stringify(out, null, 1));
await b.close();
