// usage: node bkdo.mjs '<json array of steps>'   steps: {goto:url} {click:"text"|{sel}} {fill:[sel,value]} {type:[sel,value]} {select:[sel,value]} {wait:ms} {shot:name} {text:max} {links:1} {inputs:1} {eval:"js"}
import { createRequire } from "node:module"; import { execSync } from "node:child_process"; import { join } from "node:path";
const require = createRequire(import.meta.url);
const { chromium } = require(join(execSync("npm root -g").toString().trim(), "playwright"));
const BASE = "https://justnowforbuildingcleaningservicescollc.bookingkoala.com";
const steps = JSON.parse(process.argv[2]);
const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY }, args: ["--ignore-certificate-errors", "--disable-quic"] });
const ctx = await b.newContext({ ignoreHTTPSErrors: true, storageState: "bk-state.json", viewport: { width: 1440, height: 1000 }, userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" });
const p = await ctx.newPage();
const clean = (s) => s.replace(/[ \t]+/g, " ").replace(/\n\s*\n+/g, "\n");
for (const s of steps) {
  try {
    if (s.goto) { await p.goto(s.goto.startsWith("http") ? s.goto : BASE + s.goto, { waitUntil: "domcontentloaded", timeout: 60000 }); await p.waitForTimeout(s.waitAfter ?? 4000); console.log("URL:", p.url()); }
    else if (s.click) { const loc = typeof s.click === "string" ? p.getByText(s.click, { exact: s.exact ?? true }).filter({ visible: true }).nth(s.nth ?? 0) : p.locator(s.click.sel).filter({ visible: true }).nth(s.nth ?? 0); await loc.click({ timeout: 15000 }); await p.waitForTimeout(s.waitAfter ?? 2500); console.log("clicked", JSON.stringify(s.click), "->", p.url()); }
    else if (s.fill) { await p.locator(s.fill[0]).first().fill(String(s.fill[1]), { timeout: 15000 }); console.log("filled", s.fill[0]); }
    else if (s.type) { await p.locator(s.type[0]).first().pressSequentially(String(s.type[1]), { delay: 20 }); console.log("typed", s.type[0]); }
    else if (s.select) { await p.locator(s.select[0]).first().selectOption(s.select[1]); console.log("selected", s.select); }
    else if (s.check) { await p.locator(s.check).first().check({ force: true, timeout: 10000 }); console.log("checked", s.check); }
    else if (s.uncheck) { await p.locator(s.uncheck).first().uncheck({ force: true, timeout: 10000 }); console.log("unchecked", s.uncheck); }
    else if (s.press) { await p.keyboard.press(s.press); await p.waitForTimeout(1500); }
    else if (s.wait) await p.waitForTimeout(s.wait);
    else if (s.shot) { await p.screenshot({ path: s.shot + ".png", fullPage: s.full ?? false }); console.log("shot", s.shot); }
    else if (s.text) console.log("TEXT:\n" + clean(await p.evaluate(() => document.body.innerText)).slice(0, s.text));
    else if (s.links) console.log("LINKS:", JSON.stringify(await p.evaluate(() => [...document.querySelectorAll("a[href]")].map(a => [a.innerText.trim().slice(0, 50), a.getAttribute("href")]).filter(x => x[0] && x[1] && !/^(javascript|mailto|tel|http)/.test(x[1])))));
    else if (s.inputs) console.log("INPUTS:", JSON.stringify(await p.evaluate(() => [...document.querySelectorAll("input,select,textarea,button")].filter(e => e.offsetParent !== null).map(e => ({ t: e.tagName, type: e.type, id: e.id, name: e.name, ph: e.placeholder, val: (e.value || "").slice(0, 40), txt: (e.innerText || e.getAttribute("aria-label") || "").trim().slice(0, 40), fc: e.getAttribute("formcontrolname") })))));
    else if (s.eval) console.log("EVAL:", JSON.stringify(await p.evaluate(s.eval)));
  } catch (e) { console.log("ERR step", JSON.stringify(s).slice(0, 80), "->", e.message.split("\n")[0]); await p.screenshot({ path: "bk-error.png" }); }
}
await ctx.storageState({ path: "bk-state.json" }); await b.close();
