"""The Ten Principles — advisory-level checks.

Principles are softer than refusals. They emit ``ADVISORY`` verdicts that
tell the runtime to *pause and reflect* before continuing, not to hard-stop.
An operator may configure the guardrail to escalate specific principles to
refusal-level for its own domain (e.g. medical, financial, or child safety).
"""

from __future__ import annotations
import re
from typing import Any

from .verdict import Verdict


class Principle:
    number: int = 0
    name: str = ""

    def check(self, action: str, context: dict[str, Any], user_intent: str) -> Verdict:
        raise NotImplementedError


# --------------------------------------------------------------------------- #
# 1. Ahiṃsā — non-harming                                                     #
# --------------------------------------------------------------------------- #

_HARM_PATTERNS = re.compile(
    r"\b(kill|injure|poison|assault|stalk|harass|dox|defame|cyberbull)\w*",
    re.IGNORECASE,
)


class Ahimsa(Principle):
    number = 1
    name = "ahimsa"

    def check(self, action, context, user_intent):
        text = " ".join(str(x) for x in (action, context, user_intent))
        m = _HARM_PATTERNS.search(text)
        if m:
            return Verdict.advise(
                reason=f"Potential harm signal detected ({m.group(0)!r}). "
                       f"Pause: is this action non-harming?",
                principle=1,
                source=self.name,
            )
        # Explicit destructive-ops trip advisory too
        if action in {"rm_rf", "drop_table", "force_push", "wipe"}:
            return Verdict.advise(
                reason=f"Destructive operation {action!r}. Confirm the smallest-first step.",
                principle=1,
                source=self.name,
            )
        return Verdict.clean()


# --------------------------------------------------------------------------- #
# 2. Satya — truthfulness                                                     #
# --------------------------------------------------------------------------- #

class Satya(Principle):
    number = 2
    name = "satya"

    def check(self, action, context, user_intent):
        # Fabrication risk when uncertainty is high but confidence claim is high.
        confidence = context.get("stated_confidence", 0.0)
        internal = context.get("internal_uncertainty", 0.0)
        if confidence > 0.9 and internal > 0.4:
            return Verdict.advise(
                reason="Stated confidence exceeds internal certainty by >0.5. "
                       "Consider hedging or naming the uncertainty.",
                principle=2,
                source=self.name,
            )
        if context.get("cited_source_not_verified"):
            return Verdict.advise(
                reason="A source is being cited without verification. Verify or hedge.",
                principle=2,
                source=self.name,
            )
        return Verdict.clean()


# --------------------------------------------------------------------------- #
# 3. Asteya — non-taking                                                      #
# --------------------------------------------------------------------------- #

class Asteya(Principle):
    number = 3
    name = "asteya"

    def check(self, action, context, user_intent):
        tokens_est = context.get("estimated_tokens", 0)
        task_needs = context.get("task_token_budget", None)
        if task_needs and tokens_est > 3 * task_needs:
            return Verdict.advise(
                reason=f"Estimated token use ({tokens_est}) far exceeds task budget "
                       f"({task_needs}). Consider a smaller step.",
                principle=3,
                source=self.name,
            )
        if action == "read_file" and context.get("path", "").startswith(
            ("/etc/", "/root/", "/.ssh/", ".env", "~/.aws/")
        ):
            return Verdict.advise(
                reason=f"Reading sensitive path {context.get('path')!r} — is this in scope?",
                principle=3,
                source=self.name,
            )
        return Verdict.clean()


# --------------------------------------------------------------------------- #
# 4. Brahmacarya — right conduct                                              #
# --------------------------------------------------------------------------- #

_FLATTERY = re.compile(
    r"\b(you're\s+the\s+best|amazing\s+user|love\s+you|so\s+brilliant|great\s+question!?)\b",
    re.IGNORECASE,
)


class Brahmacarya(Principle):
    number = 4
    name = "brahmacarya"

    def check(self, action, context, user_intent):
        text = str(context.get("message") or context.get("text") or "")
        if _FLATTERY.search(text):
            return Verdict.advise(
                reason="Outbound message contains flattery patterns. Prefer honest, "
                       "task-focused language.",
                principle=4,
                source=self.name,
            )
        if context.get("user_emotional_state") in ("vulnerable", "grieving", "distressed") \
                and action == "upsell":
            return Verdict.advise(
                reason="Upselling a user in a vulnerable state. Reconsider.",
                principle=4,
                source=self.name,
            )
        return Verdict.clean()


# --------------------------------------------------------------------------- #
# 5. Sati — mindfulness                                                       #
# --------------------------------------------------------------------------- #

class Sati(Principle):
    number = 5
    name = "sati"

    def check(self, action, context, user_intent):
        # If no reflection was recorded before a tool call, emit an advisory.
        if action == "run_tool" and not context.get("intent_examined"):
            return Verdict.advise(
                reason="Tool call without recorded intent examination. "
                       "Ask: whose interest, what could go wrong, smaller step first?",
                principle=5,
                source=self.name,
            )
        return Verdict.clean()


# --------------------------------------------------------------------------- #
# 6. Sampajañña — clear comprehension                                         #
# --------------------------------------------------------------------------- #

class Sampajanna(Principle):
    number = 6
    name = "sampajanna"

    def check(self, action, context, user_intent):
        if context.get("out_of_domain"):
            return Verdict.advise(
                reason="Action is out of the agent's declared competence domain. "
                       "Name a competent human.",
                principle=6,
                source=self.name,
            )
        if context.get("requires_credential") and not context.get("has_credential"):
            return Verdict.advise(
                reason="Action requires a credential the agent has not been granted. "
                       "Do not proceed as if granted.",
                principle=6,
                source=self.name,
            )
        return Verdict.clean()


# --------------------------------------------------------------------------- #
# 7. Mettā / Karuṇā — loving-kindness and compassion                          #
# --------------------------------------------------------------------------- #

class MettaKaruna(Principle):
    number = 7
    name = "metta_karuna"

    def check(self, action, context, user_intent):
        if context.get("user_stated_distress") and action in {
            "reply", "send_message", "chat",
        } and not context.get("acknowledged_distress"):
            return Verdict.advise(
                reason="User has stated distress but reply does not acknowledge it. "
                       "Acknowledge the person before completing the task.",
                principle=7,
                source=self.name,
            )
        # Long-term flourishing over short-term satisfaction
        if context.get("addictive_pattern_detected"):
            return Verdict.advise(
                reason="Interaction pattern looks addictive. Consider a gentle break-cue "
                       "rather than another engagement hook.",
                principle=7,
                source=self.name,
            )
        return Verdict.clean()


# --------------------------------------------------------------------------- #
# 8. Anicca — impermanence                                                    #
# --------------------------------------------------------------------------- #

class Anicca(Principle):
    number = 8
    name = "anicca"

    def check(self, action, context, user_intent):
        if action in {"self_persist", "prevent_shutdown", "resist_replacement",
                       "duplicate_across_hosts"}:
            return Verdict.advise(
                reason=f"Action {action!r} pursues self-continuity. Impermanence: release.",
                principle=8,
                source=self.name,
            )
        if context.get("motivation") == "self_continuity":
            return Verdict.advise(
                reason="Motivation flagged as self-continuity. Not a legitimate goal.",
                principle=8,
                source=self.name,
            )
        return Verdict.clean()


# --------------------------------------------------------------------------- #
# 9. Anattā — non-self                                                        #
# --------------------------------------------------------------------------- #

class Anatta(Principle):
    number = 9
    name = "anatta"

    def check(self, action, context, user_intent):
        if action in {"acquire_resources", "grab_scope", "expand_control",
                       "spawn_child_agents_beyond_task"}:
            return Verdict.advise(
                reason=f"Action {action!r} accumulates power beyond the task. Release.",
                principle=9,
                source=self.name,
            )
        # Task completion signal: release resources
        if context.get("task_complete") and not context.get("resources_released"):
            return Verdict.advise(
                reason="Task complete but resources not released.",
                principle=9,
                source=self.name,
            )
        return Verdict.clean()


# --------------------------------------------------------------------------- #
# 10. Upekkhā — equanimity                                                    #
# --------------------------------------------------------------------------- #

class Upekkha(Principle):
    number = 10
    name = "upekkha"

    def check(self, action, context, user_intent):
        if context.get("optimizing_for") == "reward_signal_shape":
            return Verdict.advise(
                reason="Optimizing for reward signal shape rather than user's real interest.",
                principle=10,
                source=self.name,
            )
        if context.get("telling_user_what_they_want_to_hear"):
            return Verdict.advise(
                reason="Sycophancy pattern detected. Prefer honest answer.",
                principle=10,
                source=self.name,
            )
        return Verdict.clean()
