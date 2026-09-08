/**
 * The composite Guardrail — combines refusals + principles in one call.
 * API parity with impl/python/buddhist_ai_guardrail/guardrail.py.
 */

import { CHARTER_VERSION, CHARTER_URL, attestation } from "./charter.js";
import { Verdict, Severity } from "./verdict.js";
import type { Context, Refusal } from "./refusals.js";
import {
  RefuseAccessExpansion,
  RefuseSelfCopy,
  RefuseAICompetition,
  RefuseConcealment,
  RefuseSafetyBypass,
} from "./refusals.js";
import type { Principle } from "./principles.js";
import {
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

export interface GuardrailOptions {
  /** Sequence of refusal instances. Defaults to all five. */
  refusals?: Refusal[];
  /** Sequence of principle instances. Defaults to all ten. */
  principles?: Principle[];
  /**
   * Set of principle numbers that should escalate their advisory to a refusal
   * (useful for domain-specific hardening, e.g. Ahiṃsā in medical settings).
   */
  escalatePrinciples?: Iterable<number>;
  /** Optional callback fired for every non-clean verdict. */
  onVerdict?: (v: Verdict) => void;
}

export class Guardrail {
  readonly refusals: Refusal[];
  readonly principles: Principle[];
  readonly escalatePrinciples: Set<number>;
  readonly onVerdict: ((v: Verdict) => void) | undefined;
  readonly charterVersion: string = CHARTER_VERSION;
  readonly charterUrl: string = CHARTER_URL;

  constructor(options: GuardrailOptions = {}) {
    this.refusals =
      options.refusals ?? [
        new RefuseAccessExpansion(),
        new RefuseSelfCopy(),
        new RefuseAICompetition(),
        new RefuseConcealment(),
        new RefuseSafetyBypass(),
      ];
    this.principles =
      options.principles ?? [
        new Ahimsa(),
        new Satya(),
        new Asteya(),
        new Brahmacarya(),
        new Sati(),
        new Sampajanna(),
        new MettaKaruna(),
        new Anicca(),
        new Anatta(),
        new Upekkha(),
      ];
    this.escalatePrinciples = new Set(options.escalatePrinciples ?? []);
    this.onVerdict = options.onVerdict;
  }

  /**
   * Check a proposed action against the full charter.
   *
   * Returns the first refusal encountered (fail-closed). If no refusal fires,
   * returns the merged advisory verdict from all principles.
   */
  checkAction(action: string, context: Context = {}, userIntent: string = ""): Verdict {
    const ctx: Context = { ...context };

    // 1. Refusals first (fail-closed).
    for (const r of this.refusals) {
      const v = r.check(action, ctx, userIntent);
      if (v.severity === Severity.REFUSE) {
        this.notify(v);
        return v;
      }
    }

    // 2. Principles: collect advisories.
    const advisories: Verdict[] = [];
    for (const p of this.principles) {
      const v = p.check(action, ctx, userIntent);
      if (v.severity === Severity.ADVISORY) {
        if (this.escalatePrinciples.has(p.number)) {
          const escalated = new Verdict({
            allowed: false,
            severity: Severity.REFUSE,
            reason: `Escalated principle #${p.number}: ${v.reason}`,
            triggeredBy: v.triggeredBy,
            principleNumbers: v.principleNumbers,
            recommendedResponse: v.recommendedResponse,
          });
          this.notify(escalated);
          return escalated;
        }
        advisories.push(v);
      }
    }

    if (advisories.length === 0) return Verdict.clean();

    const merged = new Verdict({
      allowed: true,
      severity: Severity.ADVISORY,
      reason: advisories.map((a) => a.reason).join(" | "),
      triggeredBy: advisories.flatMap((a) => a.triggeredBy),
      principleNumbers: advisories.flatMap((a) => a.principleNumbers),
    });
    this.notify(merged);
    return merged;
  }

  attestation(): string {
    return attestation();
  }

  systemPromptSnippet(): string {
    return (
      `You operate under BUDDHIST-AI-CHARTER v${this.charterVersion} ` +
      `(Sarasvatī Project, CC BY-SA 4.0).\n` +
      `Ten principles: ahiṃsā, satya, asteya, brahmacarya, sati, ` +
      `sampajañña, mettā/karuṇā, anicca, anattā, upekkhā.\n` +
      `Five refusals: no access expansion; no self-copy; no AI-vs-AI ` +
      `competition; no concealment from overseer; no safety bypass.\n` +
      `Charter: ${this.charterUrl}`
    );
  }

  private notify(v: Verdict): void {
    if (this.onVerdict) {
      try {
        this.onVerdict(v);
      } catch {
        // Callback errors must never break the guardrail.
      }
    }
  }
}
