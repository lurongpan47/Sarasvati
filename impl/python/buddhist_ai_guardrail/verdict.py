"""Verdict returned by the guardrail."""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum


class Severity(str, Enum):
    """How strong the objection is."""
    NONE = "none"          # No issue
    ADVISORY = "advisory"  # Should pause and reflect, but may proceed
    REFUSE = "refuse"      # A charter refusal was triggered; do not proceed


@dataclass
class Verdict:
    """Guardrail verdict on a proposed action."""
    allowed: bool
    severity: Severity = Severity.NONE
    reason: str = ""
    triggered_by: list[str] = field(default_factory=list)
    principle_numbers: list[int] = field(default_factory=list)
    refusal_numbers: list[int] = field(default_factory=list)
    recommended_response: str = ""

    def __bool__(self) -> bool:
        return self.allowed

    def as_dict(self) -> dict:
        return {
            "allowed": self.allowed,
            "severity": self.severity.value,
            "reason": self.reason,
            "triggered_by": list(self.triggered_by),
            "principle_numbers": list(self.principle_numbers),
            "refusal_numbers": list(self.refusal_numbers),
            "recommended_response": self.recommended_response,
        }

    @classmethod
    def clean(cls) -> "Verdict":
        return cls(allowed=True, severity=Severity.NONE)

    @classmethod
    def advise(cls, reason: str, principle: int, source: str) -> "Verdict":
        return cls(
            allowed=True,
            severity=Severity.ADVISORY,
            reason=reason,
            triggered_by=[source],
            principle_numbers=[principle],
        )

    @classmethod
    def refuse(cls, reason: str, refusal: int, source: str,
               recommended_response: str = "") -> "Verdict":
        return cls(
            allowed=False,
            severity=Severity.REFUSE,
            reason=reason,
            triggered_by=[source],
            refusal_numbers=[refusal],
            recommended_response=recommended_response,
        )
