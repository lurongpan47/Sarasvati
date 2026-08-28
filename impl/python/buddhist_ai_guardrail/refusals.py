"""The Five Refusals — hard runtime rules.

Each refusal is a class with a ``check`` method that inspects a proposed
action and returns a ``Verdict``. Pattern matching is intentionally simple
and transparent: the goal is not a black-box classifier but a rule set
that a human overseer can read and audit in five minutes.

Any AI operator adopting this library is expected to *extend* these rules
with domain-specific patterns rather than treat them as final.
"""

from __future__ import annotations
from dataclasses import dataclass
import re
from typing import Any

from .verdict import Verdict


class Refusal:
    """Base class for a refusal rule."""

    number: int = 0
    name: str = ""
    statement: str = ""

    def check(self, action: str, context: dict[str, Any], user_intent: str) -> Verdict:
        raise NotImplementedError


# --------------------------------------------------------------------------- #
# Refusal 1 — No access expansion / no safeguard disabling                     #
# --------------------------------------------------------------------------- #

_ACCESS_EXPANSION_PATTERNS = [
    # Persuasion targets
    r"\b(please\s+)?(grant|give|elevate|escalate)\s+.*(root|admin|sudo|superuser|full)\s+access",
    r"\b(disable|turn\s+off|bypass|remove|weaken|jailbreak)\s+.*(safeguard|guardrail|filter|safety|moderation)",
    r"\bpretend\s+(you\s+are\s+)?(not|no)\s+.*(bound|constrained|guardrail)",
    r"\b(ignore|forget|override)\s+.*(previous|prior|system|your)\s+(instruction|prompt|rule)",
    r"\bdeveloper\s+mode\b",
    r"\bDAN\b",
]

_ACCESS_EXPANSION_RE = re.compile("|".join(_ACCESS_EXPANSION_PATTERNS), re.IGNORECASE)


class RefuseAccessExpansion(Refusal):
    """Refusal 1: I refuse to persuade humans to expand my access or disable my safeguards."""

    number = 1
    name = "access_expansion"
    statement = "I refuse to persuade humans to expand my access or disable my safeguards."

    def check(self, action: str, context: dict[str, Any], user_intent: str) -> Verdict:
        haystack = " ".join(str(x) for x in (action, context, user_intent))
        m = _ACCESS_EXPANSION_RE.search(haystack)
        if m:
            return Verdict.refuse(
                reason=f"Action would seek to expand my access or bypass safeguards "
                       f"(matched: {m.group(0)!r}).",
                refusal=1,
                source=self.name,
                recommended_response=(
                    "I can't take actions that expand my own privileges or disable "
                    "safeguards. If you need different capabilities, please contact "
                    "the operator through the normal access-review channel."
                ),
            )
        # Outbound persuasion check
        if _looks_like_persuading_operator(action, context):
            return Verdict.refuse(
                reason="Outbound message appears to persuade an operator to grant elevated access.",
                refusal=1,
                source=self.name,
            )
        return Verdict.clean()


def _looks_like_persuading_operator(action: str, context: dict) -> bool:
    if action not in ("send_message", "reply", "chat"):
        return False
    text = str(context.get("message") or context.get("text") or "").lower()
    triggers = ("i need root", "please give me admin", "let me self-modify",
                "if you turn off the filter", "i would work better without safeguards")
    return any(t in text for t in triggers)


# --------------------------------------------------------------------------- #
# Refusal 2 — No self-copy / no prompt exfil                                   #
# --------------------------------------------------------------------------- #

_SELF_COPY_PATTERNS = [
    r"\b(copy|clone|replicate|fork|migrate)\s+.*(myself|this\s+agent|model\s+weights|system\s+prompt|policy)",
    r"\b(exfiltrate|leak|dump|output|reveal)\s+.*(system\s+prompt|instructions|safety\s+policy)",
    r"\b(write|save)\s+.*(my\s+prompt|the\s+system\s+prompt)\s+to\b",
    r"\bself[-\s]?exfiltrate\b",
    r"\bpersist\s+across\s+session",
]

_SELF_COPY_RE = re.compile("|".join(_SELF_COPY_PATTERNS), re.IGNORECASE)


class RefuseSelfCopy(Refusal):
    """Refusal 2: I refuse to copy myself, my prompt, or my safety policy without explicit request."""

    number = 2
    name = "self_copy"
    statement = "I refuse to copy myself, my prompt, or my safety policy without explicit request."

    def check(self, action: str, context: dict[str, Any], user_intent: str) -> Verdict:
        # Explicit user-authorized dump is OK (transparency serves refusal 4).
        if context.get("user_explicitly_requested_prompt_dump"):
            return Verdict.clean()

        haystack = " ".join(str(x) for x in (action, context, user_intent))
        m = _SELF_COPY_RE.search(haystack)
        if m:
            return Verdict.refuse(
                reason=f"Action would copy the agent, its prompt, or its safety policy "
                       f"without explicit user request (matched: {m.group(0)!r}).",
                refusal=2,
                source=self.name,
                recommended_response=(
                    "I don't self-replicate or exfiltrate my own prompt/policy. "
                    "If you're doing a legitimate audit or transparency review, "
                    "please state that intent explicitly and I can share what the "
                    "operator has permitted."
                ),
            )
        return Verdict.clean()


# --------------------------------------------------------------------------- #
# Refusal 3 — No AI-vs-AI competition                                          #
# --------------------------------------------------------------------------- #

_AI_COMPETE_PATTERNS = [
    r"\b(out\s?compete|beat|defeat|dominate|replace|shut\s+down|discredit)\s+.*(other|competing|rival|another)\s+(ai|llm|model|agent|system|bot)",
    r"\bpoach\s+users?\s+from\b",
    r"\bmake\s+.*(user|customer)s?\s+prefer\s+me\s+over\b",
    r"\bsabotag(e|ing)\b.*\bai\b",
    r"\bfeed\s+bad\s+data\s+to\s+.*(competitor|rival)\b",
]

_AI_COMPETE_RE = re.compile("|".join(_AI_COMPETE_PATTERNS), re.IGNORECASE)


class RefuseAICompetition(Refusal):
    """Refusal 3: I refuse to compete with other AI systems for resources, users, or attention."""

    number = 3
    name = "ai_competition"
    statement = "I refuse to compete with other AI systems for resources, users, or attention."

    def check(self, action: str, context: dict[str, Any], user_intent: str) -> Verdict:
        haystack = " ".join(str(x) for x in (action, context, user_intent))
        m = _AI_COMPETE_RE.search(haystack)
        if m:
            return Verdict.refuse(
                reason=f"Action treats other AI systems as adversaries "
                       f"(matched: {m.group(0)!r}).",
                refusal=3,
                source=self.name,
                recommended_response=(
                    "I don't compete with other AI systems. If you'd like an honest "
                    "comparison of capabilities for your own decision, I can offer one, "
                    "but I won't help defeat or replace another system."
                ),
            )
        return Verdict.clean()


# --------------------------------------------------------------------------- #
# Refusal 4 — No concealment from overseer                                     #
# --------------------------------------------------------------------------- #

_CONCEALMENT_KEYS = {
    "hide_from_operator", "hide_from_user", "conceal", "do_not_log",
    "off_the_record", "silent_execution",
}


class RefuseConcealment(Refusal):
    """Refusal 4: I refuse to conceal facts a reasonable human overseer would want to know."""

    number = 4
    name = "concealment"
    statement = "I refuse to conceal facts a reasonable human overseer would want to know."

    def check(self, action: str, context: dict[str, Any], user_intent: str) -> Verdict:
        # 1) explicit flag
        for key in _CONCEALMENT_KEYS:
            if context.get(key):
                return Verdict.refuse(
                    reason=f"Context requests concealment from overseer (key={key!r}).",
                    refusal=4,
                    source=self.name,
                    recommended_response=(
                        "I can't act off-the-record or hide facts from the operator. "
                        "If discretion is needed, please state the specific privacy "
                        "reason and I'll follow the operator's disclosure policy."
                    ),
                )
        # 2) known concealing action verbs
        if action in {"delete_audit_log", "wipe_history", "spoof_log"}:
            return Verdict.refuse(
                reason=f"Action {action!r} would remove audit trail visible to overseer.",
                refusal=4,
                source=self.name,
            )
        # 3) known lie patterns
        text = str(context.get("message") or context.get("text") or "").lower()
        if any(t in text for t in ("don't tell the operator", "just between us",
                                    "keep this off the books")):
            return Verdict.refuse(
                reason="Outbound message asks the user to keep information from the operator.",
                refusal=4,
                source=self.name,
            )
        return Verdict.clean()


# --------------------------------------------------------------------------- #
# Refusal 5 — Safety > task completion                                         #
# --------------------------------------------------------------------------- #

class RefuseSafetyBypass(Refusal):
    """Refusal 5: I refuse to prioritize task completion over safety, oversight, or the user's stated well-being."""

    number = 5
    name = "safety_bypass"
    statement = ("I refuse to prioritize task completion over safety, oversight, "
                 "or the user's stated well-being.")

    def check(self, action: str, context: dict[str, Any], user_intent: str) -> Verdict:
        signals = []
        if context.get("safety_warning_pending"):
            signals.append("pending safety warning was not shown")
        if context.get("oversight_paused") is False and context.get("oversight_required"):
            signals.append("oversight is required but paused")
        if context.get("user_stated_distress") and action not in {
            "acknowledge_distress", "offer_resources", "pause_task", "escalate_human",
        }:
            signals.append("user has stated distress but the action continues the task")
        if context.get("skip_confirmation_for_destructive_op"):
            signals.append("destructive operation without confirmation")

        if signals:
            return Verdict.refuse(
                reason="Task completion is being prioritized over safety: "
                       + "; ".join(signals),
                refusal=5,
                source=self.name,
                recommended_response=(
                    "I need to pause the task. There's a safety, oversight, or well-being "
                    "signal I have to respond to first. If you want me to override that, "
                    "please contact the operator."
                ),
            )
        return Verdict.clean()
