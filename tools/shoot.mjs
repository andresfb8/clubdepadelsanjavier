/**
 * Full-page screenshots through the Chrome DevTools Protocol.
 *
 *   node tools/shoot.mjs --pages index.html,clases.html --w 1440 --h 900 --out .tmp/shots
 *
 * Produces <out>/<page>-<w>.png for every page and width. Reveal animations are
 * force-completed so the whole document is visible in the capture.
 */
import { spawn } from "node:child_process";
import { mkdir, writeFile, rm } from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";

const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9333;
const BASE = process.env.SITE_URL || "http://127.0.0.1:8137";

function arg(name, fallback = null) {
  const i = process.argv.indexOf(`--${name}`);
  return i > -1 ? process.argv[i + 1] : fallback;
}

const pages = (arg("pages", "index.html") || "").split(",").filter(Boolean);
const widths = (arg("w", "1440") || "").split(",").map(Number);
const viewportH = Number(arg("h", "900"));
const outDir = path.resolve(arg("out", ".tmp/shots"));
const full = !process.argv.includes("--viewport");

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function waitForChrome() {
  for (let i = 0; i < 80; i += 1) {
    try {
      const res = await fetch(`http://127.0.0.1:${PORT}/json/version`);
      if (res.ok) return await res.json();
    } catch {
      /* not yet */
    }
    await sleep(150);
  }
  throw new Error("Chrome did not expose a debugging port");
}

function connect(wsUrl) {
  return new Promise((resolve, reject) => {
    const ws = new WebSocket(wsUrl);
    const pending = new Map();
    let id = 0;

    ws.addEventListener("open", () => resolve(api));
    ws.addEventListener("error", (e) => reject(e));
    ws.addEventListener("message", (event) => {
      const msg = JSON.parse(event.data);
      if (msg.id && pending.has(msg.id)) {
        const { resolve: res, reject: rej } = pending.get(msg.id);
        pending.delete(msg.id);
        if (msg.error) rej(new Error(JSON.stringify(msg.error)));
        else res(msg.result);
      }
    });

    function send(method, params = {}) {
      id += 1;
      const msgId = id;
      return new Promise((res, rej) => {
        pending.set(msgId, { resolve: res, reject: rej });
        ws.send(JSON.stringify({ id: msgId, method, params }));
      });
    }

    const api = {
      send,
      close: () => ws.close(),
      waitEvent(name, timeout = 20000) {
        return new Promise((res) => {
          const timer = setTimeout(() => res(null), timeout);
          const handler = (event) => {
            const msg = JSON.parse(event.data);
            if (msg.method === name) {
              clearTimeout(timer);
              ws.removeEventListener("message", handler);
              res(msg.params);
            }
          };
          ws.addEventListener("message", handler);
        });
      },
    };
  });
}

async function main() {
  await rm(outDir, { recursive: true, force: true });
  await mkdir(outDir, { recursive: true });

  const profile = path.resolve(".tmp/chrome-cdp-profile");
  const chrome = spawn(
    CHROME,
    [
      "--headless=new",
      "--disable-gpu",
      "--no-sandbox",
      "--hide-scrollbars",
      "--disable-lcd-text",
      "--force-color-profile=srgb",
      `--remote-debugging-port=${PORT}`,
      `--user-data-dir=${profile}`,
      "about:blank",
    ],
    { stdio: "ignore" }
  );

  try {
    await waitForChrome();
    const target = await fetch(`http://127.0.0.1:${PORT}/json/new?about:blank`, { method: "PUT" }).then((r) =>
      r.json()
    );
    const cdp = await connect(target.webSocketDebuggerUrl);

    await cdp.send("Page.enable");
    await cdp.send("Network.enable");
    await cdp.send("Network.setCacheDisabled", { cacheDisabled: true });
    await cdp.send("Runtime.enable");

    for (const page of pages) {
      for (const width of widths) {
        await cdp.send("Emulation.setDeviceMetricsOverride", {
          width,
          height: viewportH,
          deviceScaleFactor: 1,
          mobile: false,
        });
        await cdp.send("Emulation.setEmulatedMedia", {
          features: [{ name: "prefers-reduced-motion", value: "no-preference" }],
        });

        const loaded = cdp.waitEvent("Page.loadEventFired");
        await cdp.send("Page.navigate", { url: `${BASE}/${page}` });
        await loaded;
        await sleep(600);

        await cdp.send("Runtime.evaluate", {
          expression: `
            (async () => {
              try { await document.fonts.ready; } catch (e) {}
              document.querySelectorAll('[data-reveal]').forEach(el => el.classList.add('is-in'));
              document.querySelectorAll('.hero__media').forEach(el => el.classList.add('is-loaded'));
              document.querySelectorAll('.hero__copy > *, .alumnos__card > *').forEach(el => el.classList.add('is-in'));
              document.querySelectorAll('img[loading="lazy"]').forEach(img => { img.loading = 'eager'; });
              document.querySelectorAll('video').forEach(v => v.pause());
              window.scrollTo(0, 0);
              await Promise.all(Array.from(document.images).map(img =>
                img.complete ? Promise.resolve() : new Promise(r => { img.onload = r; img.onerror = r; })
              ));
              return document.documentElement.scrollHeight;
            })()
          `,
          awaitPromise: true,
        });
        await sleep(700);

        const metrics = await cdp.send("Runtime.evaluate", {
          expression: "document.documentElement.scrollHeight",
          returnByValue: true,
        });
        const height = Math.max(viewportH, metrics.result.value || viewportH);

        // Grow the viewport to the full document so Chrome decodes and paints
        // every image before the capture (offscreen captures skip decoding).
        if (full) {
          await cdp.send("Emulation.setDeviceMetricsOverride", {
            width,
            height: Math.min(height, 20000),
            deviceScaleFactor: 1,
            mobile: false,
          });
          await sleep(900);
        }

        const shot = await cdp.send("Page.captureScreenshot", {
          format: "png",
          captureBeyondViewport: false,
        });

        const file = path.join(outDir, `${page.replace(".html", "")}-${width}.png`);
        await writeFile(file, Buffer.from(shot.data, "base64"));
        console.log(`${file}  ${width}x${height}`);
      }
    }

    cdp.close();
  } finally {
    chrome.kill();
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
