// Replace hourly booking spots with 3 arrival windows every day.
import { createRequire } from "node:module"; import { execSync } from "node:child_process";
const require = createRequire(import.meta.url);
const { chromium } = require(execSync("npm root -g").toString().trim() + "/playwright");
const BASE = "https://justnowforbuildingcleaningservicescollc.bookingkoala.com";
const LIMIT = process.argv[2] || "3";
const WINDOWS = [[["08", "00", "AM"], ["12", "00", "PM"]], [["12", "00", "PM"], ["04", "00", "PM"]], [["04", "00", "PM"], ["09", "00", "PM"]]];
const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY }, args: ["--ignore-certificate-errors", "--disable-quic"] });
const ctx = await b.newContext({ ignoreHTTPSErrors: true, storageState: "bk-state.json", viewport: { width: 1440, height: 1000 }, userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" });
const page = await ctx.newPage();
const vis = (sel) => page.locator(sel).filter({ visible: true }).first();
const rows = () => page.evaluate(() => [...document.querySelectorAll("tbody tr")].filter((r) => r.offsetParent).map((r) => r.innerText.replace(/\s+/g, " ").trim().slice(0, 60)));

await page.goto(BASE + "/admin/booking-spots", { waitUntil: "domcontentloaded" });
await page.waitForTimeout(5000);
console.log("before", await rows());

// 1. delete existing spots of the open day (Sunday)
for (let i = 0; i < 30; i++) {
  const del = page.locator("tbody tr button:has-text('Delete')").filter({ visible: true });
  if (!(await del.count())) break;
  await del.first().click();
  await page.waitForTimeout(800);
  const confirm = page.locator(".modal button:has-text('Delete'), [role=dialog] button:has-text('Delete'), button[aria-label='Delete']").filter({ visible: true }).last();
  await confirm.click();
  await page.waitForTimeout(1200);
}
console.log("after delete", await rows());

async function pickTime(toggleIndex, [h, m, ap]) {
  const btn = page.locator("#spotAddEditForm button[id^=toggleBtndropdown]").nth(toggleIndex);
  const id = await btn.getAttribute("id");
  await btn.click();
  await page.waitForTimeout(600);
  const menu = page.locator(`div[aria-labelledby="${id}"]`).filter({ visible: true }).first();
  await menu.locator("ul").nth(0).locator("li", { hasText: new RegExp(`^${h}$`) }).click();
  await menu.locator("ul").nth(1).locator("li", { hasText: new RegExp(`^${m}$`) }).click();
  await menu.locator("ul").nth(2).locator("li", { hasText: new RegExp(`^${ap}$`) }).click();
  await menu.locator("button[aria-label='Apply']").click();
  await page.waitForTimeout(500);
  return (await btn.innerText()).trim();
}

// 2. add windows
for (const [s, e] of WINDOWS) {
  await vis("button:has-text('Add spot')").click();
  await page.waitForTimeout(1200);
  await page.locator("label[for=arrivalWindow]").click();
  await page.waitForTimeout(500);
  const st = await pickTime(0, s);
  const et = await pickTime(1, e);
  await page.locator("#spotAddEditForm input[name=limit]").fill(LIMIT);
  await page.locator("label[for=both]").click();
  const state = await page.evaluate(() => ({ aw: document.querySelector("#arrivalWindow").checked, both: document.querySelector("#both").checked, limit: document.querySelector("#spotAddEditForm input[name=limit]").value }));
  console.log("form", st, "->", et, state);
  await page.locator("button[aria-label='Add'], button:has-text('Add')").filter({ visible: true }).last().click();
  await page.waitForTimeout(1500);
  const err = await page.evaluate(() => [...document.querySelectorAll(".text-danger, .invalid-feedback, .toast, .alert")].filter((e) => e.offsetParent).map((e) => e.innerText.trim()).join(" | "));
  if (err) console.log("msg:", err);
}
console.log("after add", await rows());
await page.screenshot({ path: "bk-spots-before-save.png", fullPage: true });

// 3. save
await vis("button:has-text('Save changes')").click();
await page.waitForTimeout(3000);
console.log("saved msg:", await page.evaluate(() => document.body.innerText.match(/(success|saved|updated|error)[^\n]{0,80}/i)?.[0]));

// 4. apply to all days
await vis("button:has-text('Apply to')").click();
await page.waitForTimeout(1000);
const menu = page.locator("div[x-placement]").filter({ visible: true }).filter({ hasText: "Select all" }).first();
await menu.locator("label", { hasText: "Select all" }).click();
await page.waitForTimeout(400);
console.log("days checked", await menu.evaluate((m) => [...m.querySelectorAll("input")].map((i) => i.name + "=" + i.checked).join(",")));
await menu.locator("button[aria-label='Apply']").click();
await page.waitForTimeout(2500);
console.log("apply msg:", await page.evaluate(() => document.body.innerText.match(/(success|saved|updated|applied|error)[^\n]{0,80}/i)?.[0]));
await page.screenshot({ path: "bk-spots-applied.png", fullPage: true });
const saveBtn = page.locator("button:has-text('Save changes')").filter({ visible: true });
if (await saveBtn.count()) { await saveBtn.first().click(); await page.waitForTimeout(3000); console.log("saved2 msg:", await page.evaluate(() => document.body.innerText.match(/(success|saved|updated|error)[^\n]{0,80}/i)?.[0])); }

// 5. verify each day
for (const day of ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]) {
  await page.locator("button, a, li, div[role=button]").filter({ hasText: new RegExp(`^${day}$`) }).filter({ visible: true }).first().click();
  await page.waitForTimeout(1500);
  console.log(day, await rows());
}
await b.close();
