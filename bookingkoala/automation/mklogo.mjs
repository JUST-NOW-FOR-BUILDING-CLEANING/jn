import { createRequire } from "node:module"; import { execSync } from "node:child_process"; import { readFileSync } from "node:fs";
const require = createRequire(import.meta.url);
const { chromium } = require(execSync("npm root -g").toString().trim() + "/playwright");
const b64 = readFileSync("dl/fb-logo.jpg").toString("base64");
const html = `<html><body style="margin:0;background:#fff"><div id="l" style="width:225px;height:50px;display:flex;align-items:center;gap:8px;font-family:Arial,Helvetica,sans-serif;background:#fff">
<img src="data:image/jpeg;base64,${b64}" style="width:50px;height:50px;border-radius:8px;display:block">
<div style="line-height:1.05"><div style="font-size:19px;font-weight:700;color:#111;letter-spacing:.2px">Just Now</div><div style="font-size:9.5px;color:#444;margin-top:2px">Deep Cleaning Services · UAE</div></div></div></body></html>`;
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 300, height: 100 }, deviceScaleFactor: 1 });
await p.setContent(html); await p.waitForTimeout(500);
await p.locator("#l").screenshot({ path: "dl/jn-logo-225x50.png", omitBackground: false });
const p2 = await b.newPage({ viewport: { width: 300, height: 100 }, deviceScaleFactor: 2 });
await p2.setContent(html); await p2.waitForTimeout(500);
await p2.locator("#l").screenshot({ path: "dl/jn-logo-450x100.png" });
await b.close(); console.log("ok");
