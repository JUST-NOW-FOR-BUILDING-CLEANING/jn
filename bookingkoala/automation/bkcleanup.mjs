import { createRequire } from "node:module"; import { execSync } from "node:child_process";
const require = createRequire(import.meta.url);
const { chromium } = require(execSync("npm root -g").toString().trim() + "/playwright");
const BASE = "https://justnowforbuildingcleaningservicescollc.bookingkoala.com";
const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY }, args: ["--ignore-certificate-errors", "--disable-quic"] });
const ctx = await b.newContext({ ignoreHTTPSErrors: true, storageState: "bk-state.json", viewport: { width: 1440, height: 1000 }, userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" });
const page = await ctx.newPage();
const dumpDialog = () => page.evaluate(() => { const h = [...document.querySelectorAll("*")].find((e) => e.offsetParent && e.children.length <= 1 && /^(Booking summary|Cancel booking|Cancellation|Are you sure)/i.test(e.textContent.trim()) && e.textContent.trim().length < 40); let n = h; for (let i = 0; i < 6 && n && n.innerText.length < 400; i++) n = n.parentElement; return n ? n.innerText.replace(/\s+/g, " ").slice(0, 900) : [...document.querySelectorAll(".modal.show, [role=dialog]")].filter((e) => e.offsetParent).map((e) => e.innerText.replace(/\s+/g, " ").slice(0, 700)).join(" || "); });
const visButtons = () => page.evaluate(() => [...document.querySelectorAll("button, a.btn")].filter((e) => e.offsetParent && e.getBoundingClientRect().width > 0).map((e) => ({ t: e.innerText.trim().slice(0, 25), x: Math.round(e.getBoundingClientRect().x), y: Math.round(e.getBoundingClientRect().y), w: Math.round(e.getBoundingClientRect().width), h: Math.round(e.getBoundingClientRect().height) })).filter((b) => b.t));
for (let round = 0; round < 6; round++) {
  await page.goto(BASE + (process.argv[2] || "/admin/bookings/upcoming"), { waitUntil: "domcontentloaded" }); await page.waitForTimeout(7000);
  const ev = page.locator(".fc-event").filter({ hasText: /TEST BOOKING|TEST - DO NOT CONFIRM/ }).filter({ visible: true });
  const n = await ev.count(); console.log("round", round, "test events:", n);
  if (!n) break;
  await ev.first().click(); await page.waitForTimeout(3500);
  const panelTxt = await dumpDialog(); console.log("summary:", panelTxt.slice(0, 260));
  const btns = await visButtons(); console.log("panel buttons:", JSON.stringify(btns.filter((b) => b.x > 850)));
  const cb = btns.find((b) => b.t === "Cancel" && b.x > 850);
  if (!cb) { console.log("no Cancel button"); break; }
  await page.mouse.click(cb.x + cb.w / 2, cb.y + cb.h / 2); await page.waitForTimeout(3000);
  console.log("after cancel click buttons:", JSON.stringify((await visButtons()).filter((b) => b.x > 300)));
  console.log("cancel dialog:", await dumpDialog().then((t) => t.slice(-700)));
  await page.screenshot({ path: `bk-cancel-dialog-${round}.png` });
  console.log("dialog controls:", await page.evaluate(() => [...document.querySelectorAll(".modal.show input, .modal.show select, .modal.show textarea, .modal.show button, [role=dialog] input, [role=dialog] select, [role=dialog] textarea, [role=dialog] button")].filter((e) => e.offsetParent).map((e) => e.tagName + "#" + e.id + "[" + (e.name || e.getAttribute("formcontrolname") || "") + "|" + e.type + "]=" + (e.type == "checkbox" || e.type == "radio" ? e.checked : String(e.value || e.innerText).trim().slice(0, 25)) + (e.tagName == "SELECT" ? "{" + [...e.options].slice(0, 6).map((o) => o.value + ":" + o.text.trim().slice(0, 15)).join("/") + "}" : "")).join(" ;; ")));
  // pick a reason if a select/radio exists
  const sel = page.locator(".modal.show select, [role=dialog] select").filter({ visible: true }).last();
  if (await sel.count()) { const opts = await sel.evaluate((s) => [...s.options].map((o) => o.value)); const v = opts.find((o) => o && o !== "null" && o !== "undefined"); if (v) await sel.selectOption(v); }
  const radio = page.locator(".modal.show input[type=radio], [role=dialog] input[type=radio]").filter({ visible: true });
  if (await radio.count()) { const id = await radio.first().getAttribute("id"); if (id) await page.locator(`label[for="${id}"]`).first().click().catch(() => radio.first().check({ force: true })); }
  const ta = page.locator(".modal.show textarea, [role=dialog] textarea").filter({ visible: true }).first();
  if (await ta.count()) await ta.fill("Test booking created during setup. Cancelled.");
  await page.locator('label[for="9_Other"]').first().click().catch(() => page.locator('[id="9_Other"]').check({ force: true }));
  await page.locator('label[for="cancel_send_notification"]').first().click().catch(() => page.locator('#cancel_send_notification').check({ force: true }));
  await page.waitForTimeout(500);
  console.log("reason/other checked:", await page.evaluate(() => document.getElementById("9_Other")?.checked + "/" + document.getElementById("cancel_send_notification")?.checked));
  const all = await visButtons(); const cf = all.filter((b) => /^(Cancel this appointment|Yes|Confirm|Cancel booking|Submit|Proceed)/i.test(b.t)).pop();
  if (!cf) { console.log("no confirm button found"); break; }
  console.log("clicking confirm:", cf.t);
  await page.mouse.click(cf.x + cf.w / 2, cf.y + cf.h / 2); await page.waitForTimeout(4000);
  console.log("after confirm:", await page.evaluate(() => (document.body.innerText.match(/(cancel+ed|success|error|required|select)[^\n]{0,80}/gi) || []).slice(0, 4).join("; ")));
  await page.screenshot({ path: `bk-cancel-after-${round}.png` });
}
await b.close();
