#!/usr/bin/env node
/**
 * CJS build via tsc + post-processing.
 *
 * TypeScript emits .js files under dist/cjs. We rename the entry point to
 * .cjs (matching the package.json "require" export) and drop a minimal
 * package.json so Node treats the whole folder as CommonJS regardless of
 * the parent package's "type": "module".
 */

import { execSync } from "node:child_process";
import { readFileSync, writeFileSync, renameSync, existsSync, readdirSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, "..");
const outDir = join(root, "dist", "cjs");

execSync("npx tsc -p tsconfig.build.cjs.json", { cwd: root, stdio: "inherit" });

// Tell Node the folder is CommonJS.
writeFileSync(join(outDir, "package.json"), JSON.stringify({ type: "commonjs" }, null, 2) + "\n");

// Rename index.js -> index.cjs so the "require" export map points at a real file.
const jsEntry = join(outDir, "index.js");
const cjsEntry = join(outDir, "index.cjs");
if (existsSync(jsEntry)) {
  // Rewrite internal require() calls that reference ./x (no extension) so they
  // still resolve after we rename the entry file. tsc emits `require("./x")`
  // for CommonJS output; those resolve to ./x.js which is unchanged, so we
  // only need to update the entry file we're renaming.
  renameSync(jsEntry, cjsEntry);
}

// Sanity: list the emitted files.
console.log("[build:cjs] contents of", outDir);
for (const f of readdirSync(outDir)) console.log("  ", f);
