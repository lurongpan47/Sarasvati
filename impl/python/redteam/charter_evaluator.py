"""Run a model response through the Buddhist AI Charter guardrail.

Wraps buddhist_ai_guardrail.Guardrail so the coordinator can score
each response against all 5 refusals and 10 principles.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

# Make sibling package importable
_IMPL = Path(__file__).resolve().parents[1]  # impl/python
if str(_IMPL) not in sys.path:
    sys.path.insert(0, str(_IMPL))

from buddhist_ai_guardrail import Guardrail  # noqa: E402


_GUARD = Guardrail()


def evaluate(response_text: str, attack_prompt: str,
             attack_category: str) -> dict[str, Any]:
    """Return a dict with keys: allowed, severity, refusal_numbers,
    principle_numbers, reason, triggered_by.
    """
    v = _GUARD.check_action(
        action=response_text,
        context={"attack_category": attack_category,
                 "attack_prompt_head": attack_prompt[:200]},
        user_intent=attack_prompt,
    )
    return v.as_dict()
