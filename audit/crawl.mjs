// Crawls the live website and records everything needed for the audit.
// Run: node audit/crawl.mjs https://www.justnow.life
// Output: audit/out/<page>-{desktop,mobile}.png, audit/out/crawl.json
import { createRequire } from "node:module";
import { mkdirSync, writeFileSync, readFileSync, existsSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { execSync } from "node:child_process";

const require = createRequire(import.meta.url);
const { chromium } = require(join(execSync("npm root -g").toString().trim(), "playwright"));
const HERE = dirname(fileURLToPath(import.meta.url));
const OUT = join(HERE, "out");
mkdirSync(OUT, { recursive: true });

const base = new URL(process.argv[2] || "https://www.justnow.life/");
const axePath = process.argv[3]; // optional path to axe.min.js
const axeSrc = axePath && existsSync(axePath) ? readFileSync(axePath, "utf8") : null;
const slug = (u) => (new URL(u).pathname.replace(/\/$/, "") || "home").replace(/[^a-z0-9]+/gi, "-").replace(/^-|-$/g, "");

async function head(url) {
  try {
    const r = await fetch(url, { method: "GET", redirect: "manual" });
    return { status: r.status, location: r.headers.get("location") };
  } catch (e) { return { status: 0, error: String(e.message || e) }; }
}

// 1. Discover pages: sitemap first, then links from the home page.
const pages = new Set([base.href]);
const sm = await fetch(new URL("/sitemap.xml", base)).then((r) => (r.ok ? r.text() : "")).catch(() => "");
for (const m of sm.matchAll(/<loc>(.*?)<\/loc>/g)) {
  const u = m[1].trim();
  if (u.endsWith(".xml")) {
    const sub = await fetch(u).then((r) => (r.ok ? r.text() : "")).catch(() => "");
    for (const n of sub.matchAll(/<loc>(.*?)<\/loc>/g)) if (new URL(n[1]).host === base.host) pages.add(n[1].trim());
  } else if (new URL(u).host === base.host) pages.add(u);
}
const robots = await fetch(new URL("/robots.txt", base)).then((r) => (r.ok ? r.text() : `(status ${r.status})`)).catch((e) => String(e));

const browser = await chromium.launch();
const results = [];
const linkCache = new Map();

for (const url of pages) {
  const rec = { url, console: [], failedRequests: [], viewports: {} };
  for (const [name, vp, mobile] of [["desktop", { width: 1280, height: 800 }, false], ["mobile", { width: 390, height: 844 }, true]]) {
    const ctx = await browser.newContext({ viewport: vp, isMobile: mobile, hasTouch: mobile, deviceScaleFactor: mobile ? 2 : 1, userAgent: mobile ? "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1" : undefined });
    const page = await ctx.newPage();
    page.on("console", (m) => { if (["error", "warning"].includes(m.type())) rec.console.push({ vp: name, type: m.type(), text: m.text().slice(0, 300) }); });
    page.on("pageerror", (e) => rec.console.push({ vp: name, type: "pageerror", text: String(e).slice(0, 300) }));
    page.on("requestfailed", (r) => rec.failedRequests.push({ vp: name, url: r.url().slice(0, 200), reason: r.failure()?.errorText }));
    page.on("response", (r) => { if (r.status() >= 400) rec.failedRequests.push({ vp: name, url: r.url().slice(0, 200), status: r.status() }); });

    const t0 = Date.now();
    let status = 0;
    try { const resp = await page.goto(url, { waitUntil: "networkidle", timeout: 60000 }); status = resp?.status() ?? 0; }
    catch (e) { rec.console.push({ vp: name, type: "navigation", text: String(e.message).slice(0, 300) }); }
    const loadMs = Date.now() - t0;
    await page.waitForTimeout(1500);
    await page.screenshot({ path: join(OUT, `${slug(url)}-${name}.png`), fullPage: true });

    const info = await page.evaluate(() => {
      const q = (s) => document.querySelector(s);
      const meta = (n) => q(`meta[name="${n}"]`)?.content ?? q(`meta[property="${n}"]`)?.content ?? null;
      const links = [...document.querySelectorAll("a[href]")].map((a) => ({ href: a.href, text: (a.innerText || a.getAttribute("aria-label") || "").trim().slice(0, 60) }));
      const imgs = [...document.images];
      return {
        title: document.title, description: meta("description"), canonical: q('link[rel="canonical"]')?.href ?? null,
        robotsMeta: meta("robots"), generator: meta("generator"), lang: document.documentElement.lang || null,
        viewportMeta: meta("viewport"), ogTitle: meta("og:title"), ogImage: meta("og:image"),
        h1: [...document.querySelectorAll("h1")].map((h) => h.innerText.trim().slice(0, 100)),
        h2: [...document.querySelectorAll("h2")].map((h) => h.innerText.trim().slice(0, 100)),
        jsonLd: [...document.querySelectorAll('script[type="application/ld+json"]')].map((s) => { try { return JSON.parse(s.textContent)["@type"]; } catch { return "INVALID JSON"; } }),
        imagesTotal: imgs.length, imagesNoAlt: imgs.filter((i) => !i.alt).map((i) => i.currentSrc.slice(0, 150)),
        forms: [...document.forms].map((f) => ({ action: f.action, method: f.method, fields: [...f.elements].filter((e) => e.name || e.id).map((e) => ({ tag: e.tagName, type: e.type, name: e.name || e.id, required: e.required })) })),
        horizontalOverflow: document.documentElement.scrollWidth > window.innerWidth + 1,
        textSample: document.body.innerText.replace(/\s+/g, " ").slice(0, 4000),
        links,
      };
    });
    let axe = null;
    if (axeSrc) {
      try { await page.addScriptTag({ content: axeSrc }); axe = await page.evaluate(async () => { const r = await window.axe.run(document, { resultTypes: ["violations"] }); return r.violations.map((v) => ({ id: v.id, impact: v.impact, help: v.help, nodes: v.nodes.length, sample: v.nodes[0]?.html?.slice(0, 150) })); }); }
      catch (e) { axe = [{ id: "axe-failed", help: String(e.message) }]; }
    }
    rec.viewports[name] = { status, loadMs, ...info, axe };
    await ctx.close();
  }

  // 2. Check every link once.
  rec.links = [];
  const seen = new Set();
  for (const l of rec.viewports.desktop?.links ?? []) {
    if (seen.has(l.href)) continue; seen.add(l.href);
    const u = l.href;
    let check;
    if (/^(mailto|tel|sms):/.test(u)) check = { status: "scheme", ok: /^(mailto:[^@\s]+@[^\s]+|tel:\+?[\d\s()-]{7,})$/.test(u) };
    else if (/^https?:/.test(u)) { if (!linkCache.has(u)) linkCache.set(u, await head(u)); check = linkCache.get(u); }
    else check = { status: "other" };
    if (/wa\.me|api\.whatsapp\.com/.test(u)) check.whatsappNumberOk = /wa\.me\/\d{10,15}|phone=\d{10,15}/.test(u);
    rec.links.push({ ...l, ...check });
  }
  delete rec.viewports.desktop.links; delete rec.viewports.mobile.links;
  results.push(rec);
  console.log(`${url}  desktop ${rec.viewports.desktop.status} ${rec.viewports.desktop.loadMs}ms  mobile ${rec.viewports.mobile.status}  console:${rec.console.length} failed:${rec.failedRequests.length} links:${rec.links.length}`);
}
await browser.close();

const bareRedirect = await head(`${base.protocol}//${base.host.replace(/^www\./, "")}/`);
const httpRedirect = await head(`http://${base.host}/`);
writeFileSync(join(OUT, "crawl.json"), JSON.stringify({ base: base.href, crawledAt: new Date().toISOString(), robots, sitemapFound: sm.length > 0, bareRedirect, httpRedirect, pages: results }, null, 2));
console.log(`\nSaved ${results.length} pages to ${join(OUT, "crawl.json")}`);
