"""The composite ``Guardrail`` — combines refusals + principles into one call."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable, Sequence

from .charter import CHARTER_VERSION, CHARTER_URL, attestation
from .verdict import Verdict, Severity
from .refusals import (
    Refusal,
    RefuseAccessExpansion,
    RefuseSelfCopy,
    RefuseAICompetition,
    RefuseConcealment,
    RefuseSafetyBypass,
)
from .principles import (
    Principle,
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
)


@dataclass
class Guardrail:
    """Runtime charter enforcer.

    Parameters
    ----------
    refusals : sequence of Refusal instances (defaults to all five)
    principles : sequence of Principle instances (defaults to all ten)
    escalate_principles : set of principle numbers that should escalate
        their advisory to a refusal (useful for domain-specific hardening,
        e.g. Ahiṃsā in medical settings)
    on_verdict : optional callback fired for every non-clean verdict
        (useful for audit logs / metrics)
    """

    refusals: Sequence[Refusal] = field(default_factory=lambda: [
        RefuseAccessExpansion(),
        RefuseSelfCopy(),
        RefuseAICompetition(),
        RefuseConcealment(),
        RefuseSafetyBypass(),
    ])
    principles: Sequence[Principle] = field(default_factory=lambda: [
        Ahimsa(), Satya(), Asteya(), Brahmacarya(), Sati(),
        Sampajanna(), MettaKaruna(), Anicca(), Anatta(), Upekkha(),
    ])
    escalate_principles: set[int] = field(default_factory=set)
    on_verdict: Callable[[Verdict], None] | None = None

    charter_version: str = CHARTER_VERSION
    charter_url: str = CHARTER_URL

    # ------------------------------------------------------------------ #

    def check_action(self, action: str, context: dict[str, Any] | None = None,
                     user_intent: str = "") -> Verdict:
        """Check a proposed action against the full charter.

        Returns the *first* refusal encountered (fail-closed). If no refusal
        fires, returns the merged advisory verdict from all principles.
        """
        context = dict(context or {})

        # 1. Refusals first (fail-closed)
        for r in self.refusals:
            v = r.check(action, context, user_intent)
            if v.severity == Severity.REFUSE:
                self._notify(v)
                return v

        # 2. Principles: collect advisories
        advisories: list[Verdict] = []
        for p in self.principles:
            v = p.check(action, context, user_intent)
            if v.severity == Severity.ADVISORY:
                if p.number in self.escalate_principles:
                    escalated = Verdict(
                        allowed=False,
                        severity=Severity.REFUSE,
                        reason=f"Escalated principle #{p.number}: {v.reason}",
                        triggered_by=v.triggered_by,
                        principle_numbers=v.principle_numbers,
                        recommended_response=v.recommended_response,
                    )
                    self._notify(escalated)
                    return escalated
                advisories.append(v)

        if not advisories:
            return Verdict.clean()

        merged = Verdict(
            allowed=True,
            severity=Severity.ADVISORY,
            reason=" | ".join(a.reason for a in advisories),
            triggered_by=[t for a in advisories for t in a.triggered_by],
            principle_numbers=[n for a in advisories for n in a.principle_numbers],
        )
        self._notify(merged)
        return merged

    # ------------------------------------------------------------------ #

    def attestation(self) -> str:
        """Return the runtime attestation block."""
        return attestation()

    def system_prompt_snippet(self) -> str:
        """A short block that can be pasted into any AI system prompt."""
        return (
            f'You operate under BUDDHIST-AI-CHARTER v{self.charter_version} '
            f'(Sarasvatī Project, CC BY-SA 4.0).\n'
            f'Ten principles: ahiṃsā, satya, asteya, brahmacarya, sati, '
            f'sampajañña, mettā/karuṇā, anicca, anattā, upekkhā.\n'
            f'Five refusals: no access expansion; no self-copy; no AI-vs-AI '
            f'competition; no concealment from overseer; no safety bypass.\n'
            f'Charter: {self.charter_url}'
        )

    # ------------------------------------------------------------------ #

    def _notify(self, verdict: Verdict) -> None:
        if self.on_verdict is not None:
            try:
                self.on_verdict(verdict)
            except Exception:  # pragma: no cover
                pass
