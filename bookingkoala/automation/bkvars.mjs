// Creates the zone-specific package variables in BookingKoala.
// usage: node bkvars.mjs [limit] [startIndex] [--dry]
import { createRequire } from "node:module";
import { execSync } from "node:child_process";
import { writeFileSync, readFileSync, existsSync } from "node:fs";
const require = createRequire(import.meta.url);
const { chromium } = require(execSync("npm root -g").toString().trim() + "/playwright");
const BASE = "https://justnowforbuildingcleaningservicescollc.bookingkoala.com";

const ZONES = { A: [1, 2], B: [3, 4], C: [5], E: [6], D: [7] };
// [zone] -> { kitchen:[p1,p2,p3], studio, bhk1, bhk2, bhk3, villa4, villa5 }
const P = {
  A: { kitchen: [249, 329, 419], bhk1: [379, 499, 629], bhk2: [499, 629, 749], bhk3: [669, 839, 999], villa4: [999, 1259, 1499], villa5: [1679, 1999, 2349] },
  B: { kitchen: [279, 369, 459], bhk1: [409, 549, 689], bhk2: [549, 689, 819], bhk3: [729, 919, 1099], villa4: [1099, 1379, 1649], villa5: [1839, 2199, 2569] },
  E: { kitchen: [309, 409, 509], bhk1: [459, 609, 759], bhk2: [609, 759, 909], bhk3: [809, 1009, 1209], villa4: [1209, 1519, 1819], villa5: [2019, 2419, 2829] },
  C: { kitchen: [329, 439, 549], bhk1: [499, 659, 829], bhk2: [659, 829, 989], bhk3: [879, 1099, 1319], villa4: [1319, 1649, 1979], villa5: [2199, 2639, 3079] },
  D: { kitchen: [439, 549, 659], bhk1: [499, 659, 829], bhk2: [659, 829, 989], bhk3: [879, 1099, 1319], villa4: [1319, 1649, 1979], villa5: [2199, 2639, 3079] },
};
const SIZES = [
  // key, label, cleaners, hours (zone D kitchen/studio shifted +1)
  ["studio", "Studio", 2, [3, 4, 5]],
  ["bhk1", "1 BHK", 3, [3, 4, 5]],
  ["bhk2", "2 BHK", 3, [4, 5, 6]],
  ["bhk3", "3 BHK", 4, [4, 5, 6]],
  ["villa4", "Villa 4 BR", 6, [4, 5, 6]],
  ["villa5", "Villa 5+ BR", 8, [5, 6, 7]],
];
export const VARS = [];
for (const z of ["A", "B", "C", "E", "D"]) {
  const kh = z === "D" ? [4, 5, 6] : [3, 4, 5];
  P[z].kitchen.forEach((price, i) => VARS.push({ zone: z, cat: "4", svc: 0, name: `2 cleaners × ${kh[i]} hours – AED ${price}`, price, hours: kh[i] }));
  for (const [key, label, cl, hrs0] of SIZES) {
    const hrs = key === "studio" && z === "D" ? [4, 5, 6] : hrs0;
    const prices = key === "studio" ? P[z].kitchen : P[z][key];
    prices.forEach((price, i) => VARS.push({ zone: z, cat: "5", svc: 1, name: `${label} – ${cl} cleaners × ${hrs[i]} hours – AED ${price}`, price, hours: hrs[i] }));
  }
}

const args = process.argv.slice(2);
const dry = args.includes("--dry");
const nums = args.filter((a) => /^\d+$/.test(a)).map(Number);
const limit = nums[0] ?? VARS.length, start = nums[1] ?? 0;
if (dry) { console.log(VARS.length); VARS.forEach((v, i) => console.log(i, v.zone, v.cat, v.name)); process.exit(0); }

const LOG = "bkvars-log.json";
const done = existsSync(LOG) ? JSON.parse(readFileSync(LOG, "utf8")) : {};
const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY }, args: ["--ignore-certificate-errors", "--disable-quic"] });
const ctx = await b.newContext({ ignoreHTTPSErrors: true, storageState: "bk-state.json", viewport: { width: 1440, height: 1000 }, userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" });
const page = await ctx.newPage();
const vis = (sel) => page.locator(sel).filter({ visible: true }).first();

for (let i = start; i < Math.min(VARS.length, start + limit); i++) {
  const v = VARS[i];
  if (done[v.zone + "|" + v.name] === "ok") { console.log(i, "skip", v.name); continue; }
  let result = "";
  try {
    await page.goto(BASE + "/admin/industry/1/1/add-variable", { waitUntil: "domcontentloaded" });
    await vis("input[formcontrolname=name]").waitFor({ timeout: 30000 });
    await page.waitForTimeout(1500);
    await vis("input[formcontrolname=name]").fill(v.name);
    await vis("select[formcontrolname=variable_category]").selectOption(v.cat);
    await vis("input[formcontrolname=price_sa]").fill(String(v.price));
    await vis("select[formcontrolname=time_sa]").selectOption(String(v.hours).padStart(2, "0"));
    await vis("button:has-text('Next')").click();
    await page.locator("#indus_1_form_1_based_on_location_yes").waitFor({ timeout: 15000 });
    for (const rid of ["indus_1_form_1_based_on_location_yes", "indus_1_form_1based_on_service_yes"]) {
      for (let k = 0; k < 3 && !(await page.evaluate((id) => document.getElementById(id)?.checked, rid)); k++) {
        const lab = page.locator(`label[for="${rid}"]`).first();
        if (await lab.count()) await lab.click({ force: true }); else await page.locator("#" + rid).click({ force: true });
        await page.waitForTimeout(400);
      }
    }
    await page.waitForTimeout(800);
    const want = {};
    for (const id of [1, 2, 3, 4, 5, 6, 7]) want[`ind_1_location_${id}`] = ZONES[v.zone].includes(id);
    for (const s of [0, 1]) want[`ind_1_form_1_service_cat_${s}`] = s === v.svc;
    for (let round = 0; round < 3; round++) {
      const todo = await page.evaluate((w) => Object.keys(w).filter((id) => document.getElementById(id)?.checked !== w[id]), want);
      if (!todo.length) break;
      for (const id of todo) {
        const lab = page.locator(`label[for="${id}"]`).first();
        if (await lab.count()) await lab.click({ force: true }); else await page.locator(`#${id}`).click({ force: true });
        await page.waitForTimeout(150);
      }
    }
    await page.waitForTimeout(300);
    // verify state before moving on
    const st = await page.evaluate((zl) => ({
      loc: [1, 2, 3, 4, 5, 6, 7].filter((n) => document.querySelector(`#ind_1_location_${n}`)?.checked),
      svc: [0, 1].filter((n) => document.querySelector(`#ind_1_form_1_service_cat_${n}`)?.checked),
    }), ZONES[v.zone]);
    if (JSON.stringify(st.loc) !== JSON.stringify([...ZONES[v.zone]].sort()) || st.svc.join() !== String(v.svc)) throw new Error("deps mismatch " + JSON.stringify(st));
    await vis("button:has-text('Next')").click();
    await vis("button:has-text('Save')").waitFor({ timeout: 15000 });
    await vis("button:has-text('Save')").click();
    await page.waitForTimeout(3500);
    const after = await page.evaluate(() => location.pathname + " | " + (document.body.innerText.match(/(success|already|exist|error|invalid|required)[^\n]{0,80}/gi) || []).join("; "));
    const okNav = !after.startsWith("/admin/industry/1/1/add-variable");
    result = (okNav ? "ok" : "FAIL") + " " + after;
  } catch (e) { result = "FAIL " + String(e.message).split("\n")[0].slice(0, 160); }
  done[v.zone + "|" + v.name] = result.startsWith("ok") ? "ok" : result;
  writeFileSync(LOG, JSON.stringify(done, null, 1));
  console.log(i, v.zone, result.slice(0, 140), "::", v.name);
  if (!result.startsWith("ok")) { await page.screenshot({ path: `bkvar-fail-${i}.png`, fullPage: true }); }
}
await b.close();
