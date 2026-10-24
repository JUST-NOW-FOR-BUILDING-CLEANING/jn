// usage: node bkbook.mjs "<location text>" "<service>" "<package label>" <dayOfMonth> [--submit]
import { createRequire } from "node:module"; import { execSync } from "node:child_process";
const require = createRequire(import.meta.url);
const { chromium } = require(execSync("npm root -g").toString().trim() + "/playwright");
const BASE = "https://justnowforbuildingcleaningservicescollc.bookingkoala.com";
const [loc, svc, pkg, day, email] = process.argv.slice(2); const submit = process.argv.includes("--submit");
const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY }, args: ["--ignore-certificate-errors", "--disable-quic"] });
const ctx = await b.newContext({ ignoreHTTPSErrors: true, viewport: { width: 1440, height: 1000 }, userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" });
const page = await ctx.newPage();
await page.goto(BASE + "/booknow", { waitUntil: "domcontentloaded" }); await page.waitForTimeout(6000);
await page.locator("#locationMenu").click(); await page.waitForTimeout(600);
await page.locator(".bk-dropdown-link", { hasText: loc }).filter({ visible: true }).first().click(); await page.waitForTimeout(2500);
const sels = page.locator("select.bk-select");
await sels.nth(0).selectOption({ label: svc }); await page.waitForTimeout(2000);
await sels.nth(1).selectOption({ label: pkg }); await page.waitForTimeout(3000);
await page.locator("#dateFormControlInput").locator("xpath=..").click(); await page.waitForTimeout(3000);
const pop = page.locator("bk-schedule-calendar-popup");
const cell = pop.locator(".tjs-bcalendar__day").filter({ hasText: new RegExp("^\\s*" + day + "\\s*$") }).first();
await cell.click(); await page.waitForTimeout(4000);
console.log("popup now:", await page.evaluate(() => { const p = document.querySelector("bk-schedule-calendar-popup"); return p ? p.innerText.replace(/\s+/g, " ").slice(0, 600) : "closed"; }));
await page.screenshot({ path: "bk-book-slots.png", fullPage: true });
// slots inside popup?
const slotBtns = page.locator("bk-schedule-calendar-popup *").filter({ hasText: /\d{1,2}:\d{2} [AP]M/ }).filter({ visible: true });
const n = await slotBtns.count(); console.log("slot elements:", n);
if (n) {
  const texts = await slotBtns.allInnerTexts(); console.log("slot texts:", texts.map((t) => t.replace(/\s+/g, " ").slice(0, 60)).filter((v, i, s) => s.indexOf(v) == i).slice(0, 8).join(" | "));
  const leaf = page.locator("bk-schedule-calendar-popup").locator("xpath=//*[not(*)][contains(normalize-space(.), 'AM') or contains(normalize-space(.), 'PM')]").first();
  await leaf.click(); await page.waitForTimeout(2500);
  console.log("after slot click popup:", await page.evaluate(() => { const p = document.querySelector("bk-schedule-calendar-popup"); return p ? p.innerText.replace(/\s+/g, " ").slice(0, 400) : "closed"; }));
  const apply = page.locator("bk-schedule-calendar-popup button, .tjs-popup button").filter({ hasText: /Apply|Select|Done|Continue|Save/i }).filter({ visible: true });
  if (await apply.count()) { console.log("apply buttons:", await apply.allInnerTexts()); await apply.first().click(); await page.waitForTimeout(2500); }
}
console.log("date value:", await page.locator("#dateFormControlInput").inputValue(), "| date section:", await page.evaluate(() => document.body.innerText.replace(/\s+/g, " ").match(/Select Date[^]{0,300}/)?.[0]));
await page.screenshot({ path: "bk-book-after-slot.png", fullPage: true });
if (!submit) { await b.close(); process.exit(0); }
await page.locator("input[formcontrolname=first_name]").fill("TEST BOOKING");
await page.locator("input[formcontrolname=last_name]").fill("DELETE ME");
await page.locator("#userEmail").fill(email);
await page.locator("input[formcontrolname=phone_number]").fill("507677282");
await page.locator("input.bk-input[placeholder='Type Address']").fill("Test address – Al Majaz 2"); await page.waitForTimeout(1500); await page.keyboard.press("Escape");
await page.locator("input[formcontrolname=apt]").fill("Test 1");
await page.locator("textarea").first().fill("TEST booking created by setup automation – please ignore / delete").catch(() => {});
await page.locator("#accept_terms_and_conditions").check({ force: true }).catch(() => {}); console.log("terms checked:", await page.evaluate(() => document.querySelector("#accept_terms_and_conditions")?.checked));
await page.locator("label[for=cash]").click().catch(() => {});
console.log("summary:", await page.evaluate(() => document.body.innerText.replace(/\s+/g, " ").match(/Booking Summary[^]{0,400}/)?.[0]));
await page.locator("button", { hasText: "Save Booking" }).click(); await page.waitForTimeout(12000);
console.log("modals:", await page.evaluate(() => [...document.querySelectorAll(".modal.show, [role=dialog]")].filter((e) => e.offsetParent).map((e) => e.innerText.replace(/\s+/g, " ").slice(0, 400)).join(" || ")));
console.log("after submit url:", page.url());
console.log("after submit text:", await page.evaluate(() => document.body.innerText.replace(/\s+/g, " ").slice(0, 1200)));
console.log("errors:", await page.evaluate(() => [...document.querySelectorAll(".text-danger, .invalid-feedback, .alert, .toast")].filter((e) => e.offsetParent).map((e) => e.innerText.trim()).join(" | ")));
await page.screenshot({ path: "bk-book-submitted.png", fullPage: true });
await b.close();
