import { createRequire } from "node:module"; import { execSync } from "node:child_process"; import { readFileSync } from "node:fs";
const require = createRequire(import.meta.url);
const { chromium } = require(execSync("npm root -g").toString().trim() + "/playwright");
const BASE = "https://justnowforbuildingcleaningservicescollc.bookingkoala.com";
const [idx, file, anchor] = process.argv.slice(2);
const html = readFileSync(file, "utf8");
const name = Number(idx) === 0 ? "Terms Of Service" : "Privacy Policy";
const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY }, args: ["--ignore-certificate-errors", "--disable-quic"] });
const ctx = await b.newContext({ ignoreHTTPSErrors: true, storageState: "bk-state.json", viewport: { width: 1440, height: 1000 }, userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" });
const page = await ctx.newPage();
page.on("response", (r) => { if (r.request().method() !== "GET" && /api/.test(r.url())) console.log("XHR", r.request().method(), r.status(), r.url().replace(BASE, "").slice(0, 90)); });
const btnState = () => page.evaluate(() => { const b = [...document.querySelectorAll("button")].find((x) => /Save & Publish/.test(x.textContent)); return b ? "disabled=" + b.disabled + " cls=" + b.className.slice(0, 60) : "no btn"; });
await page.goto(BASE + "/admin/theme-builder/?theme=simple", { waitUntil: "domcontentloaded" }); await page.waitForTimeout(8000);
console.log("btn at start:", await btnState());
await page.locator("button:has-text('Page :')").click(); await page.waitForTimeout(1200);
await page.locator("text=Manage Popups").click(); await page.waitForTimeout(2500);
const i = await page.evaluate((n) => [...document.querySelectorAll("button.builder-block-menu")].findIndex((b) => b.parentElement.innerText.includes(n)), name);
await page.locator("button.builder-block-menu").nth(i).click(); await page.waitForTimeout(4000);
const p = page.locator(`text=${anchor}`).first();
const bb = await p.boundingBox(); await page.mouse.click(bb.x + 50, bb.y + 8); await page.waitForTimeout(1500);
await page.locator("button, a").filter({ hasText: /^Edit$/ }).filter({ visible: true }).first().click(); await page.waitForTimeout(3500);
await page.evaluate((h) => { const ed = tinymce.editors[0]; ed.setContent(h); ed.undoManager.add(); ed.fire("change"); ed.fire("input"); ed.save(); ed.setDirty(true); }, html);
// real keystroke inside editor to trigger angular change detection
await page.frameLocator("iframe[id^=tiny-angular]").locator("body").click(); await page.keyboard.press("End"); await page.keyboard.type(" "); await page.keyboard.press("Backspace"); await page.waitForTimeout(1500);
console.log("btn after edit:", await btnState());
console.log("builder preview has JN text?", await page.evaluate(() => document.body.innerText.includes("every booking made with Just Now")));
const close = page.locator("button", { hasText: /^Close$/ }).filter({ visible: true }).first();
if (await close.count()) { await close.click(); await page.waitForTimeout(2500); console.log("after Close modal:", await page.evaluate(() => [...document.querySelectorAll(".modal.show, [role=dialog]")].filter((e) => e.offsetParent).map((e) => e.innerText.replace(/\s+/g, " ").slice(0, 200)).join(" || "))); }
await page.screenshot({ path: `bk-popup3-${idx}-a.png` });
const saveBtn = page.locator(".modal.show button, [role=dialog] button").filter({ hasText: /Save|Yes|Keep/i }).filter({ visible: true });
if (await saveBtn.count()) { console.log("modal buttons:", await saveBtn.allInnerTexts()); await saveBtn.first().click(); await page.waitForTimeout(4000); }
console.log("btn before publish:", await btnState());
await page.locator("button", { hasText: "Save & Publish" }).click(); await page.waitForTimeout(7000);
console.log("after publish modals:", await page.evaluate(() => [...document.querySelectorAll(".modal.show, [role=dialog], .toast")].filter((e) => e.offsetParent).map((e) => e.innerText.replace(/\s+/g, " ").slice(0, 200)).join(" || ")));
const confirm = page.locator(".modal.show button, [role=dialog] button").filter({ hasText: /Publish|Yes|Confirm|Ok/i }).filter({ visible: true });
if (await confirm.count()) { console.log("confirm buttons:", await confirm.allInnerTexts()); await confirm.first().click(); await page.waitForTimeout(7000); }
await page.screenshot({ path: `bk-popup3-${idx}-b.png` });
const ctx2 = await b.newContext({ ignoreHTTPSErrors: true, viewport: { width: 1440, height: 1000 }, userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" });
const pg = await ctx2.newPage(); await pg.goto(BASE + "/booknow", { waitUntil: "domcontentloaded" }); await pg.waitForTimeout(6000);
await pg.locator("button", { hasText: Number(idx) === 0 ? "Terms & Conditions" : "Privacy Policy" }).first().click(); await pg.waitForTimeout(2500);
console.log("PUBLIC:", await pg.evaluate(() => [...document.querySelectorAll(".modal.show, [role=dialog]")].filter((e) => e.offsetParent).map((e) => e.innerText.replace(/\s+/g, " ").slice(0, 160)).join(" || ")));
await b.close();
