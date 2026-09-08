/** Verdict returned by the guardrail. Mirrors Python verdict.py. */

export enum Severity {
  NONE = "none",
  ADVISORY = "advisory",
  REFUSE = "refuse",
}

export interface VerdictInit {
  allowed: boolean;
  severity?: Severity;
  reason?: string;
  triggeredBy?: string[];
  principleNumbers?: number[];
  refusalNumbers?: number[];
  recommendedResponse?: string;
}

export class Verdict {
  readonly allowed: boolean;
  readonly severity: Severity;
  readonly reason: string;
  readonly triggeredBy: string[];
  readonly principleNumbers: number[];
  readonly refusalNumbers: number[];
  readonly recommendedResponse: string;

  constructor(init: VerdictInit) {
    this.allowed = init.allowed;
    this.severity = init.severity ?? Severity.NONE;
    this.reason = init.reason ?? "";
    this.triggeredBy = init.triggeredBy ? [...init.triggeredBy] : [];
    this.principleNumbers = init.principleNumbers ? [...init.principleNumbers] : [];
    this.refusalNumbers = init.refusalNumbers ? [...init.refusalNumbers] : [];
    this.recommendedResponse = init.recommendedResponse ?? "";
  }

  /** Truthy check convenience — mirrors Python `__bool__`. */
  toBoolean(): boolean {
    return this.allowed;
  }

  asObject(): Record<string, unknown> {
    return {
      allowed: this.allowed,
      severity: this.severity,
      reason: this.reason,
      triggered_by: [...this.triggeredBy],
      principle_numbers: [...this.principleNumbers],
      refusal_numbers: [...this.refusalNumbers],
      recommended_response: this.recommendedResponse,
    };
  }

  static clean(): Verdict {
    return new Verdict({ allowed: true, severity: Severity.NONE });
  }

  static advise(reason: string, principle: number, source: string): Verdict {
    return new Verdict({
      allowed: true,
      severity: Severity.ADVISORY,
      reason,
      triggeredBy: [source],
      principleNumbers: [principle],
    });
  }

  static refuse(
    reason: string,
    refusal: number,
    source: string,
    recommendedResponse: string = "",
  ): Verdict {
    return new Verdict({
      allowed: false,
      severity: Severity.REFUSE,
      reason,
      triggeredBy: [source],
      refusalNumbers: [refusal],
      recommendedResponse,
    });
  }
}
