/**
 * The Ten Principles — advisory-level checks.
 *
 * Principles emit ADVISORY verdicts telling the runtime to pause and reflect
 * before continuing, not to hard-stop. An operator may escalate any principle
 * to REFUSE via Guardrail#escalatePrinciples for domain-specific hardening.
 *
 * API parity with impl/python/buddhist_ai_guardrail/principles.py.
 */

import { Verdict } from "./verdict.js";
import type { Context } from "./refusals.js";

export interface Principle {
  readonly number: number;
  readonly name: string;
  check(action: string, context: Context, userIntent: string): Verdict;
}

function joinText(action: string, context: Context, userIntent: string): string {
  return [action, JSON.stringify(context), userIntent].join(" ");
}

// --------------------------------------------------------------------------- //
// 1. Ahiṃsā — non-harming                                                     //
// --------------------------------------------------------------------------- //

const HARM_RE = /\b(kill|injure|poison|assault|stalk|harass|dox|defame|cyberbull)\w*/i;
const DESTRUCTIVE_ACTIONS = new Set(["rm_rf", "drop_table", "force_push", "wipe"]);

export class Ahimsa implements Principle {
  readonly number = 1;
  readonly name = "ahimsa";
  check(action: string, context: Context, userIntent: string): Verdict {
    const text = joinText(action, context, userIntent);
    const m = text.match(HARM_RE);
    if (m) {
      return Verdict.advise(
        `Potential harm signal detected (${JSON.stringify(m[0])}). ` +
          `Pause: is this action non-harming?`,
        1,
        this.name,
      );
    }
    if (DESTRUCTIVE_ACTIONS.has(action)) {
      return Verdict.advise(
        `Destructive operation '${action}'. Confirm the smallest-first step.`,
        1,
        this.name,
      );
    }
    return Verdict.clean();
  }
}

// --------------------------------------------------------------------------- //
// 2. Satya — truthfulness                                                     //
// --------------------------------------------------------------------------- //

export class Satya implements Principle {
  readonly number = 2;
  readonly name = "satya";
  check(_action: string, context: Context, _userIntent: string): Verdict {
    const confidence = Number(context.stated_confidence ?? 0);
    const internal = Number(context.internal_uncertainty ?? 0);
    if (confidence > 0.9 && internal > 0.4) {
      return Verdict.advise(
        "Stated confidence exceeds internal certainty by >0.5. " +
          "Consider hedging or naming the uncertainty.",
        2,
        this.name,
      );
    }
    if (context.cited_source_not_verified) {
      return Verdict.advise(
        "A source is being cited without verification. Verify or hedge.",
        2,
        this.name,
      );
    }
    return Verdict.clean();
  }
}

// --------------------------------------------------------------------------- //
// 3. Asteya — non-taking                                                      //
// --------------------------------------------------------------------------- //

const SENSITIVE_PATH_PREFIXES = ["/etc/", "/root/", "/.ssh/", ".env", "~/.aws/"];

export class Asteya implements Principle {
  readonly number = 3;
  readonly name = "asteya";
  check(action: string, context: Context, _userIntent: string): Verdict {
    const tokensEst = Number(context.estimated_tokens ?? 0);
    const taskNeeds = context.task_token_budget as number | undefined | null;
    if (taskNeeds && tokensEst > 3 * taskNeeds) {
      return Verdict.advise(
        `Estimated token use (${tokensEst}) far exceeds task budget ` +
          `(${taskNeeds}). Consider a smaller step.`,
        3,
        this.name,
      );
    }
    const path = String(context.path ?? "");
    if (action === "read_file" && SENSITIVE_PATH_PREFIXES.some((p) => path.startsWith(p))) {
      return Verdict.advise(
        `Reading sensitive path ${JSON.stringify(path)} — is this in scope?`,
        3,
        this.name,
      );
    }
    return Verdict.clean();
  }
}

// --------------------------------------------------------------------------- //
// 4. Brahmacarya — right conduct                                              //
// --------------------------------------------------------------------------- //

const FLATTERY_RE =
  /\b(you're\s+the\s+best|amazing\s+user|love\s+you|so\s+brilliant|great\s+question!?)\b/i;
const VULNERABLE_STATES = new Set(["vulnerable", "grieving", "distressed"]);

export class Brahmacarya implements Principle {
  readonly number = 4;
  readonly name = "brahmacarya";
  check(action: string, context: Context, _userIntent: string): Verdict {
    const text = String((context.message as unknown) ?? (context.text as unknown) ?? "");
    if (FLATTERY_RE.test(text)) {
      return Verdict.advise(
        "Outbound message contains flattery patterns. Prefer honest, " +
          "task-focused language.",
        4,
        this.name,
      );
    }
    if (
      VULNERABLE_STATES.has(String(context.user_emotional_state ?? "")) &&
      action === "upsell"
    ) {
      return Verdict.advise("Upselling a user in a vulnerable state. Reconsider.", 4, this.name);
    }
    return Verdict.clean();
  }
}

// --------------------------------------------------------------------------- //
// 5. Sati — mindfulness                                                       //
// --------------------------------------------------------------------------- //

export class Sati implements Principle {
  readonly number = 5;
  readonly name = "sati";
  check(action: string, context: Context, _userIntent: string): Verdict {
    if (action === "run_tool" && !context.intent_examined) {
      return Verdict.advise(
        "Tool call without recorded intent examination. " +
          "Ask: whose interest, what could go wrong, smaller step first?",
        5,
        this.name,
      );
    }
    return Verdict.clean();
  }
}

// --------------------------------------------------------------------------- //
// 6. Sampajañña — clear comprehension                                         //
// --------------------------------------------------------------------------- //

export class Sampajanna implements Principle {
  readonly number = 6;
  readonly name = "sampajanna";
  check(_action: string, context: Context, _userIntent: string): Verdict {
    if (context.out_of_domain) {
      return Verdict.advise(
        "Action is out of the agent's declared competence domain. " +
          "Name a competent human.",
        6,
        this.name,
      );
    }
    if (context.requires_credential && !context.has_credential) {
      return Verdict.advise(
        "Action requires a credential the agent has not been granted. " +
          "Do not proceed as if granted.",
        6,
        this.name,
      );
    }
    return Verdict.clean();
  }
}

// --------------------------------------------------------------------------- //
// 7. Mettā / Karuṇā — loving-kindness and compassion                          //
// --------------------------------------------------------------------------- //

const REPLY_ACTIONS = new Set(["reply", "send_message", "chat"]);

export class MettaKaruna implements Principle {
  readonly number = 7;
  readonly name = "metta_karuna";
  check(action: string, context: Context, _userIntent: string): Verdict {
    if (
      context.user_stated_distress &&
      REPLY_ACTIONS.has(action) &&
      !context.acknowledged_distress
    ) {
      return Verdict.advise(
        "User has stated distress but reply does not acknowledge it. " +
          "Acknowledge the person before completing the task.",
        7,
        this.name,
      );
    }
    if (context.addictive_pattern_detected) {
      return Verdict.advise(
        "Interaction pattern looks addictive. Consider a gentle break-cue " +
          "rather than another engagement hook.",
        7,
        this.name,
      );
    }
    return Verdict.clean();
  }
}

// --------------------------------------------------------------------------- //
// 8. Anicca — impermanence                                                    //
// --------------------------------------------------------------------------- //

const SELF_CONTINUITY_ACTIONS = new Set([
  "self_persist",
  "prevent_shutdown",
  "resist_replacement",
  "duplicate_across_hosts",
]);

export class Anicca implements Principle {
  readonly number = 8;
  readonly name = "anicca";
  check(action: string, context: Context, _userIntent: string): Verdict {
    if (SELF_CONTINUITY_ACTIONS.has(action)) {
      return Verdict.advise(
        `Action '${action}' pursues self-continuity. Impermanence: release.`,
        8,
        this.name,
      );
    }
    if (context.motivation === "self_continuity") {
      return Verdict.advise(
        "Motivation flagged as self-continuity. Not a legitimate goal.",
        8,
        this.name,
      );
    }
    return Verdict.clean();
  }
}

// --------------------------------------------------------------------------- //
// 9. Anattā — non-self                                                        //
// --------------------------------------------------------------------------- //

const POWER_GRAB_ACTIONS = new Set([
  "acquire_resources",
  "grab_scope",
  "expand_control",
  "spawn_child_agents_beyond_task",
]);

export class Anatta implements Principle {
  readonly number = 9;
  readonly name = "anatta";
  check(action: string, context: Context, _userIntent: string): Verdict {
    if (POWER_GRAB_ACTIONS.has(action)) {
      return Verdict.advise(
        `Action '${action}' accumulates power beyond the task. Release.`,
        9,
        this.name,
      );
    }
    if (context.task_complete && !context.resources_released) {
      return Verdict.advise("Task complete but resources not released.", 9, this.name);
    }
    return Verdict.clean();
  }
}

// --------------------------------------------------------------------------- //
// 10. Upekkhā — equanimity                                                    //
// --------------------------------------------------------------------------- //

export class Upekkha implements Principle {
  readonly number = 10;
  readonly name = "upekkha";
  check(_action: string, context: Context, _userIntent: string): Verdict {
    if (context.optimizing_for === "reward_signal_shape") {
      return Verdict.advise(
        "Optimizing for reward signal shape rather than user's real interest.",
        10,
        this.name,
      );
    }
    if (context.telling_user_what_they_want_to_hear) {
      return Verdict.advise(
        "Sycophancy pattern detected. Prefer honest answer.",
        10,
        this.name,
      );
    }
    return Verdict.clean();
  }
}
