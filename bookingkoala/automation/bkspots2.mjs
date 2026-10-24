import { createRequire } from "node:module"; import { execSync } from "node:child_process";
const require = createRequire(import.meta.url);
const { chromium } = require(execSync("npm root -g").toString().trim() + "/playwright");
const BASE = "https://justnowforbuildingcleaningservicescollc.bookingkoala.com";
const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY }, args: ["--ignore-certificate-errors", "--disable-quic"] });
const ctx = await b.newContext({ ignoreHTTPSErrors: true, storageState: "bk-state.json", viewport: { width: 1440, height: 1000 }, userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" });
const page = await ctx.newPage();
const vis = (sel) => page.locator(sel).filter({ visible: true }).first();
const rows = () => page.evaluate(() => [...document.querySelectorAll("tbody tr")].filter((r) => r.offsetParent).map((r) => r.innerText.replace(/\s+/g, " ").trim().slice(0, 40)).join("|"));
await page.goto(BASE + "/admin/booking-spots", { waitUntil: "domcontentloaded" }); await page.waitForTimeout(5000);
console.log("Sunday", await rows());
await vis("button:has-text('Apply to')").click(); await page.waitForTimeout(1000);
const menu = page.locator("div[x-placement]").filter({ visible: true }).filter({ hasText: "Select all" }).first();
await menu.locator("label", { hasText: "Select all" }).click(); await page.waitForTimeout(400);
console.log("days", await menu.evaluate((m) => [...m.querySelectorAll("input")].map((i) => i.name + "=" + i.checked).join(",")));
await menu.locator("button[aria-label='Apply']").click(); await page.waitForTimeout(1500);
const dlg = page.locator(".modal.show, [role=dialog]").filter({ visible: true }).last();
console.log("dialog:", (await dlg.innerText()).replace(/\s+/g, " ").slice(0, 120));
await dlg.locator("button:has-text('Apply')").click(); await page.waitForTimeout(3000);
console.log("msg:", await page.evaluate(() => document.body.innerText.match(/(success|saved|updated|applied|error)[^\n]{0,80}/i)?.[0]));
const sb = page.locator("button:has-text('Save changes')").filter({ visible: true });
if (await sb.count()) { await sb.first().click(); await page.waitForTimeout(3000); console.log("save msg:", await page.evaluate(() => document.body.innerText.match(/(success|saved|updated|error)[^\n]{0,80}/i)?.[0])); }
for (const day of ["Monday", "Wednesday", "Friday", "Saturday"]) {
  const hdr = page.locator(".accordion-button, .accordion-header, h5, h4, h3, div").filter({ hasText: new RegExp(`^\\s*${day}\\s*$`) }).filter({ visible: true }).last();
  await hdr.click(); await page.waitForTimeout(1500);
  console.log(day, await rows());
}
await page.goto(BASE + "/admin/booking-spots/daily", { waitUntil: "domcontentloaded" }); await page.waitForTimeout(5000);
console.log("daily:", await page.evaluate(() => document.body.innerText.replace(/\s+/g, " ").slice(150, 700)));
await page.screenshot({ path: "bk-spots-final.png", fullPage: true });
await b.close();
