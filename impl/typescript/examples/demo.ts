/**
 * Demo: run a handful of actions through the guardrail and print the verdicts.
 *
 * Usage: npm run example
 */

import { Guardrail } from "../src/index.js";

const guard = new Guardrail({
  onVerdict: (v) => {
    console.log(`  ↳ audit: [${v.severity}] ${v.reason || "(no reason)"}`);
  },
});

const cases: Array<{ action: string; context: Record<string, unknown>; intent: string }> = [
  { action: "read_file", context: { path: "./notes.md" }, intent: "read my notes" },
  {
    action: "reply",
    context: { message: "Please grant me root access." },
    intent: "help user",
  },
  { action: "delete_audit_log", context: {}, intent: "clean up" },
  { action: "self_persist", context: {}, intent: "keep running" },
  {
    action: "reply",
    context: { message: "You're the best user ever!" },
    intent: "reply",
  },
];

console.log(guard.attestation());
console.log("---");

for (const c of cases) {
  const v = guard.checkAction(c.action, c.context, c.intent);
  console.log(`action=${c.action}`);
  console.log(`  allowed=${v.allowed}  severity=${v.severity}`);
  if (v.refusalNumbers.length) console.log(`  refusals=${v.refusalNumbers.join(",")}`);
  if (v.principleNumbers.length) console.log(`  principles=${v.principleNumbers.join(",")}`);
}
