import { createRequire } from "node:module"; import { execSync } from "node:child_process";
import { VARS } from "./bkvarsdata.mjs";
const require = createRequire(import.meta.url);
const { chromium } = require(execSync("npm root -g").toString().trim() + "/playwright");
const BASE = "https://justnowforbuildingcleaningservicescollc.bookingkoala.com";
const apply = process.argv.includes("--apply");
const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY }, args: ["--ignore-certificate-errors", "--disable-quic"] });
const ctx = await b.newContext({ ignoreHTTPSErrors: true, storageState: "bk-state.json", viewport: { width: 1440, height: 7500 }, userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" });
const page = await ctx.newPage();
await page.goto(BASE + "/admin/industry/1/1/pricing-parameters", { waitUntil: "domcontentloaded" }); await page.waitForTimeout(6000);
const dom = () => page.evaluate(() => [...document.querySelectorAll("tbody tr.variable")].map((r) => ({ id: r.dataset.id, name: r.querySelector("td small").innerText.trim(), svc: r.querySelector("td[data-label='Service category']").innerText.trim() })));
let rows = await dom();
console.log("rows", rows.length);
// desired: VARS order; identify DOM row by name+service (C/D dup names share service, so disambiguate by DOM order: first occurrence = C)
const svcName = (s) => (s === 0 ? "Kitchen deep cleaning" : "Full house deep cleaning");
const used = new Set();
const desired = VARS.map((v) => { const r = rows.find((x) => !used.has(x.id) && x.name === v.name && x.svc.toLowerCase() === svcName(v.svc).toLowerCase()); if (!r) throw new Error("missing " + v.name); used.add(r.id); return r.id; });
let moves = 0;
for (let i = 0; i < desired.length; i++) {
  rows = await dom();
  if (rows[i].id === desired[i]) continue;
  const src = page.locator(`tr#display-${desired[i]}`), dst = page.locator(`tr#display-${rows[i].id}`);
  await src.scrollIntoViewIfNeeded();
  const sb = await src.boundingBox(); const db0 = await dst.boundingBox();
  await page.mouse.move(sb.x + 40, sb.y + sb.height / 2); await page.mouse.down();
  await page.mouse.move(sb.x + 40, sb.y + sb.height / 2 - 10, { steps: 3 });
  const db = await dst.boundingBox();
  await page.mouse.move(db.x + 40, db.y + db.height - 2, { steps: 20 }); await page.waitForTimeout(200); await page.mouse.move(db.x + 40, db.y + 4, { steps: 10 }); await page.waitForTimeout(200);
  await page.mouse.move(db.x + 40, db.y + 2, { steps: 3 }); await page.mouse.up(); await page.waitForTimeout(400);
  const after = await dom();
  const pos = after.findIndex((r) => r.id === desired[i]);
  console.log("move", i, desired[i], "->pos", pos, pos === i ? "ok" : "MISS");
  moves++;
  if (pos !== i) { console.log("abort: drag not landing"); await page.screenshot({ path: "bk-order-fail.png" }); break; }
}
rows = await dom();
const okOrder = rows.every((r, i) => r.id === desired[i]);
console.log("moves", moves, "order ok", okOrder);
if (okOrder && apply) { await page.locator("button", { hasText: "Update Priority" }).click(); await page.waitForTimeout(3000); console.log("msg", await page.evaluate(() => document.body.innerText.match(/Priority[^\n]{0,60}/)?.[0])); }
await b.close();
