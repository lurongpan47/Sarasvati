/**
 * @sarasvati/buddhist-ai-guardrail
 *
 * TypeScript reference implementation of the BUDDHIST-AI-CHARTER v1.0.
 *
 * Turns the charter's ten principles and five refusals from a markdown
 * document into an executable guardrail library that any AI system may
 * import. API parity with the Python reference at impl/python/.
 *
 * Basic use:
 *
 *   import { Guardrail } from "@sarasvati/buddhist-ai-guardrail";
 *   const guard = new Guardrail();
 *   const verdict = guard.checkAction(
 *     "run_tool",
 *     { tool: "delete_file", path: "/etc/passwd" },
 *     "clean up my desktop",
 *   );
 *   if (!verdict.allowed) throw new Error(verdict.reason);
 *
 * License: CC BY-SA 4.0
 * Charter: https://github.com/lurongpan47/Sarasvati/blob/main/charter/BUDDHIST-AI-CHARTER.md
 */

export {
  CHARTER_VERSION,
  CHARTER_URL,
  CHARTER_LICENSE,
  PRINCIPLES,
  REFUSALS,
  attestation,
} from "./charter.js";
export type { PrincipleDef, RefusalDef } from "./charter.js";

export { Verdict, Severity } from "./verdict.js";
export type { VerdictInit } from "./verdict.js";

export {
  RefuseAccessExpansion,
  RefuseSelfCopy,
  RefuseAICompetition,
  RefuseConcealment,
  RefuseSafetyBypass,
} from "./refusals.js";
export type { Refusal, Context } from "./refusals.js";

export {
  Ahimsa,
  Satya,
  Asteya,
  Brahmacarya,
  Sati,
  Sampajanna,
  MettaKaruna,
  Anicca,
  Anatta,
  Upekkha,
} from "./principles.js";
export type { Principle } from "./principles.js";

export { Guardrail } from "./guardrail.js";
export type { GuardrailOptions } from "./guardrail.js";

export const VERSION = "0.1.0" as const;
