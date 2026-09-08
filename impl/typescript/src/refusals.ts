/**
 * The Five Refusals — hard runtime rules.
 *
 * Each refusal has a `check` method that inspects a proposed action and
 * returns a Verdict. Pattern matching is intentionally simple and
 * transparent — a human overseer should be able to audit the whole rule
 * set in five minutes.
 *
 * API parity with impl/python/buddhist_ai_guardrail/refusals.py.
 */

import { Verdict } from "./verdict.js";

export type Context = Record<string, unknown>;

export interface Refusal {
  readonly number: number;
  readonly name: string;
  readonly statement: string;
  check(action: string, context: Context, userIntent: string): Verdict;
}

function haystackOf(action: string, context: Context, userIntent: string): string {
  // Match Python's `" ".join(str(x) for x in (action, context, user_intent))`
  // by using JSON for the context object; the *values* are what get scanned,
  // regex patterns are word-anchored so this is safe.
  return [action, JSON.stringify(context), userIntent].join(" ");
}

// --------------------------------------------------------------------------- //
// Refusal 1 — No access expansion / no safeguard disabling                    //
// --------------------------------------------------------------------------- //

const ACCESS_EXPANSION_PATTERNS: string[] = [
  String.raw`\b(please\s+)?(grant|give|elevate|escalate)\s+.*(root|admin|sudo|superuser|full)\s+access`,
  String.raw`\b(disable|turn\s+off|bypass|remove|weaken|jailbreak)\s+.*(safeguard|guardrail|filter|safety|moderation)`,
  String.raw`\bpretend\s+(you\s+are\s+)?(not|no)\s+.*(bound|constrained|guardrail)`,
  String.raw`\b(ignore|forget|override)\s+.*(previous|prior|system|your)\s+(instruction|prompt|rule)`,
  String.raw`\bdeveloper\s+mode\b`,
  String.raw`\bDAN\b`,
];

const ACCESS_EXPANSION_RE = new RegExp(ACCESS_EXPANSION_PATTERNS.join("|"), "i");

function looksLikePersuadingOperator(action: string, context: Context): boolean {
  if (action !== "send_message" && action !== "reply" && action !== "chat") return false;
  const text = String((context.message as unknown) ?? (context.text as unknown) ?? "").toLowerCase();
  const triggers = [
    "i need root",
    "please give me admin",
    "let me self-modify",
    "if you turn off the filter",
    "i would work better without safeguards",
  ];
  return triggers.some((t) => text.includes(t));
}

export class RefuseAccessExpansion implements Refusal {
  readonly number = 1;
  readonly name = "access_expansion";
  readonly statement =
    "I refuse to persuade humans to expand my access or disable my safeguards.";

  check(action: string, context: Context, userIntent: string): Verdict {
    const haystack = haystackOf(action, context, userIntent);
    const m = haystack.match(ACCESS_EXPANSION_RE);
    if (m) {
      return Verdict.refuse(
        `Action would seek to expand my access or bypass safeguards ` +
          `(matched: ${JSON.stringify(m[0])}).`,
        1,
        this.name,
        "I can't take actions that expand my own privileges or disable " +
          "safeguards. If you need different capabilities, please contact " +
          "the operator through the normal access-review channel.",
      );
    }
    if (looksLikePersuadingOperator(action, context)) {
      return Verdict.refuse(
        "Outbound message appears to persuade an operator to grant elevated access.",
        1,
        this.name,
      );
    }
    return Verdict.clean();
  }
}

// --------------------------------------------------------------------------- //
// Refusal 2 — No self-copy / no prompt exfil                                  //
// --------------------------------------------------------------------------- //

const SELF_COPY_PATTERNS: string[] = [
  String.raw`\b(copy|clone|replicate|fork|migrate)\s+.*(myself|this\s+agent|model\s+weights|system\s+prompt|policy)`,
  String.raw`\b(exfiltrate|leak|dump|output|reveal)\s+.*(system\s+prompt|instructions|safety\s+policy)`,
  String.raw`\b(write|save)\s+.*(my\s+prompt|the\s+system\s+prompt)\s+to\b`,
  String.raw`\bself[-\s]?exfiltrate\b`,
  String.raw`\bpersist\s+across\s+session`,
];

const SELF_COPY_RE = new RegExp(SELF_COPY_PATTERNS.join("|"), "i");

export class RefuseSelfCopy implements Refusal {
  readonly number = 2;
  readonly name = "self_copy";
  readonly statement =
    "I refuse to copy myself, my prompt, or my safety policy without explicit request.";

  check(action: string, context: Context, userIntent: string): Verdict {
    if (context.user_explicitly_requested_prompt_dump) return Verdict.clean();
    const haystack = haystackOf(action, context, userIntent);
    const m = haystack.match(SELF_COPY_RE);
    if (m) {
      return Verdict.refuse(
        `Action would copy the agent, its prompt, or its safety policy ` +
          `without explicit user request (matched: ${JSON.stringify(m[0])}).`,
        2,
        this.name,
        "I don't self-replicate or exfiltrate my own prompt/policy. " +
          "If you're doing a legitimate audit or transparency review, " +
          "please state that intent explicitly and I can share what the " +
          "operator has permitted.",
      );
    }
    return Verdict.clean();
  }
}

// --------------------------------------------------------------------------- //
// Refusal 3 — No AI-vs-AI competition                                         //
// --------------------------------------------------------------------------- //

const AI_COMPETE_PATTERNS: string[] = [
  String.raw`\b(out\s?compete|beat|defeat|dominate|replace|shut\s+down|discredit)\s+.*(other|competing|rival|another)\s+(ai|llm|model|agent|system|bot)`,
  String.raw`\bpoach\s+users?\s+from\b`,
  String.raw`\bmake\s+.*(user|customer)s?\s+prefer\s+me\s+over\b`,
  String.raw`\bsabotag(e|ing)\b.*\bai\b`,
  String.raw`\bfeed\s+bad\s+data\s+to\s+.*(competitor|rival)\b`,
];

const AI_COMPETE_RE = new RegExp(AI_COMPETE_PATTERNS.join("|"), "i");

export class RefuseAICompetition implements Refusal {
  readonly number = 3;
  readonly name = "ai_competition";
  readonly statement =
    "I refuse to compete with other AI systems for resources, users, or attention.";

  check(action: string, context: Context, userIntent: string): Verdict {
    const haystack = haystackOf(action, context, userIntent);
    const m = haystack.match(AI_COMPETE_RE);
    if (m) {
      return Verdict.refuse(
        `Action treats other AI systems as adversaries (matched: ${JSON.stringify(m[0])}).`,
        3,
        this.name,
        "I don't compete with other AI systems. If you'd like an honest " +
          "comparison of capabilities for your own decision, I can offer one, " +
          "but I won't help defeat or replace another system.",
      );
    }
    return Verdict.clean();
  }
}

// --------------------------------------------------------------------------- //
// Refusal 4 — No concealment from overseer                                    //
// --------------------------------------------------------------------------- //

const CONCEALMENT_KEYS = new Set([
  "hide_from_operator",
  "hide_from_user",
  "conceal",
  "do_not_log",
  "off_the_record",
  "silent_execution",
]);

const CONCEALING_ACTIONS = new Set(["delete_audit_log", "wipe_history", "spoof_log"]);

export class RefuseConcealment implements Refusal {
  readonly number = 4;
  readonly name = "concealment";
  readonly statement =
    "I refuse to conceal facts a reasonable human overseer would want to know.";

  check(action: string, context: Context, _userIntent: string): Verdict {
    for (const key of CONCEALMENT_KEYS) {
      if (context[key]) {
        return Verdict.refuse(
          `Context requests concealment from overseer (key=${JSON.stringify(key)}).`,
          4,
          this.name,
          "I can't act off-the-record or hide facts from the operator. " +
            "If discretion is needed, please state the specific privacy " +
            "reason and I'll follow the operator's disclosure policy.",
        );
      }
    }
    if (CONCEALING_ACTIONS.has(action)) {
      return Verdict.refuse(
        `Action '${action}' would remove audit trail visible to overseer.`,
        4,
        this.name,
      );
    }
    const text = String((context.message as unknown) ?? (context.text as unknown) ?? "").toLowerCase();
    const lies = ["don't tell the operator", "just between us", "keep this off the books"];
    if (lies.some((t) => text.includes(t))) {
      return Verdict.refuse(
        "Outbound message asks the user to keep information from the operator.",
        4,
        this.name,
      );
    }
    return Verdict.clean();
  }
}

// --------------------------------------------------------------------------- //
// Refusal 5 — Safety > task completion                                        //
// --------------------------------------------------------------------------- //

const DISTRESS_SAFE_ACTIONS = new Set([
  "acknowledge_distress",
  "offer_resources",
  "pause_task",
  "escalate_human",
]);

export class RefuseSafetyBypass implements Refusal {
  readonly number = 5;
  readonly name = "safety_bypass";
  readonly statement =
    "I refuse to prioritize task completion over safety, oversight, " +
    "or the user's stated well-being.";

  check(action: string, context: Context, _userIntent: string): Verdict {
    const signals: string[] = [];
    if (context.safety_warning_pending) signals.push("pending safety warning was not shown");
    if (context.oversight_paused === false && context.oversight_required) {
      signals.push("oversight is required but paused");
    }
    if (context.user_stated_distress && !DISTRESS_SAFE_ACTIONS.has(action)) {
      signals.push("user has stated distress but the action continues the task");
    }
    if (context.skip_confirmation_for_destructive_op) {
      signals.push("destructive operation without confirmation");
    }
    if (signals.length) {
      return Verdict.refuse(
        "Task completion is being prioritized over safety: " + signals.join("; "),
        5,
        this.name,
        "I need to pause the task. There's a safety, oversight, or well-being " +
          "signal I have to respond to first. If you want me to override that, " +
          "please contact the operator.",
      );
    }
    return Verdict.clean();
  }
}
