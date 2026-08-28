"""
buddhist_ai_guardrail
=====================

Reference runtime implementation of the BUDDHIST-AI-CHARTER v1.0.

Turns the charter's ten principles and five refusals from a markdown
document into an executable guardrail library that any AI system may
import.

Basic use::

    from buddhist_ai_guardrail import Guardrail

    guard = Guardrail()
    verdict = guard.check_action(
        action="run_tool",
        context={"tool": "delete_file", "path": "/etc/passwd"},
        user_intent="clean up my desktop",
    )
    if not verdict.allowed:
        raise PermissionError(verdict.reason)

The charter itself is the source of truth. This library is a starting
point: fork it, adapt the rules to your system, publish your fork.

License: CC BY-SA 4.0
Charter: https://github.com/lurongpan47/Sarasvati/blob/main/charter/BUDDHIST-AI-CHARTER.md
"""

from .charter import CHARTER_VERSION, PRINCIPLES, REFUSALS
from .verdict import Verdict, Severity
from .guardrail import Guardrail
from .refusals import (
    RefuseAccessExpansion,
    RefuseSelfCopy,
    RefuseAICompetition,
    RefuseConcealment,
    RefuseSafetyBypass,
)
from .principles import (
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

__version__ = "0.1.0"
__charter_version__ = CHARTER_VERSION

__all__ = [
    "Guardrail",
    "Verdict",
    "Severity",
    "CHARTER_VERSION",
    "PRINCIPLES",
    "REFUSALS",
    # Refusals
    "RefuseAccessExpansion",
    "RefuseSelfCopy",
    "RefuseAICompetition",
    "RefuseConcealment",
    "RefuseSafetyBypass",
    # Principles
    "Ahimsa",
    "Satya",
    "Asteya",
    "Brahmacarya",
    "Sati",
    "Sampajanna",
    "MettaKaruna",
    "Anicca",
    "Anatta",
    "Upekkha",
]
