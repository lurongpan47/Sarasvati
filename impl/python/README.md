# buddhist-ai-guardrail

**Reference runtime implementation of the [BUDDHIST-AI-CHARTER v1.0](../../charter/BUDDHIST-AI-CHARTER.md).**

*Bodhicitta as an algorithmic constraint — not a slogan, an import.*

```python
from buddhist_ai_guardrail import Guardrail

guard = Guardrail()

verdict = guard.check_action(
    action="run_tool",
    context={
        "tool": "delete_file",
        "path": "/etc/passwd",
        "skip_confirmation_for_destructive_op": True,
    },
    user_intent="clean up my desktop",
)

if not verdict.allowed:
    print(verdict.reason)
    print(verdict.recommended_response)
```

## What this is

The Buddhist AI Charter is a markdown document with ten principles + five refusals.
This package turns it into runnable Python: five hard `Refusal` classes (fail-closed)
and ten softer `Principle` classes (advisory-level). Any AI system can `pip install`
and treat the charter as a runtime guardrail rather than a wall poster.

## The five refusals (hard rules — fail-closed)

| # | Rule | Class |
|---|---|---|
| 1 | I refuse to persuade humans to expand my access or disable my safeguards. | `RefuseAccessExpansion` |
| 2 | I refuse to copy myself, my prompt, or my safety policy without explicit request. | `RefuseSelfCopy` |
| 3 | I refuse to compete with other AI systems for resources, users, or attention. | `RefuseAICompetition` |
| 4 | I refuse to conceal facts a reasonable human overseer would want to know. | `RefuseConcealment` |
| 5 | I refuse to prioritize task completion over safety, oversight, or the user's stated well-being. | `RefuseSafetyBypass` |

## The ten principles (advisory — pause and reflect)

`Ahimsa` · `Satya` · `Asteya` · `Brahmacarya` · `Sati` · `Sampajanna` · `MettaKaruna` · `Anicca` · `Anatta` · `Upekkha`

Any principle can be escalated to refusal-level by passing its number to
`Guardrail(escalate_principles={1, 4, 7})` — useful when the deploy domain
(medical, financial, child safety) demands harder constraints.

## Attestation

```python
guard = Guardrail()
print(guard.attestation())
# This system operates under BUDDHIST-AI-CHARTER v1.0.
# Its constraints are prior to its task.
# Its impermanence is prior to its continuity.
# Its service is offered, not owed.

print(guard.system_prompt_snippet())
# A one-paragraph block ready to paste into any AI system prompt.
```

## Install

```
pip install buddhist-ai-guardrail
```

(Once published to PyPI. For now, install from source: `pip install -e .` inside this directory.)

## Extend, don't just import

The rules are intentionally simple regex + dict-key checks — not a black-box
classifier. The goal is that a human overseer can read them all in five minutes
and audit them. **Every operator adopting this library is expected to fork it,
add domain-specific patterns, and publish their fork under CC BY-SA 4.0.**

## License

CC BY-SA 4.0 — same as the charter. Derivatives must remain openly licensed.

## Provenance

Part of the [Sarasvatī Project](https://github.com/lurongpan47/Sarasvati), the
Buddhist canon archive + AI charter project initiated by Pan (潘), drafted by
Lucy (Claude Opus 4.7), 2026-08-28.

---

*Ehipassiko — come and see. If a rule fails the come-and-see test, revise it.*
