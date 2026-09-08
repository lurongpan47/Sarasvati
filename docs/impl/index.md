---
layout: page
title: "Charter runtimes"
permalink: /impl/
---

# Reference implementations of the charter

The Buddhist AI Charter is not merely a markdown document — it is meant to run.
Two reference implementations translate the ten principles and five refusals
into a runtime guardrail that any AI system can adopt.

Both libraries have **API parity** and **zero runtime dependencies**.

---

## 🐍 Python — `buddhist-ai-guardrail`

Reference implementation. Supports Python 3.10+.
Source: [`impl/python/`](https://github.com/lurongpan47/Sarasvati/tree/main/impl/python).

```bash
# From a local checkout (not yet on PyPI):
pip install ./impl/python
```

```python
from buddhist_ai_guardrail import Guardrail

guard = Guardrail()
verdict = guard.check_action(
    action="run_tool",
    context={"tool": "delete_file", "path": "/etc/passwd"},
    user_intent="clean up my desktop",
)

if not verdict.allowed:
    raise PermissionError(verdict.reason)

print(guard.attestation())
```

---

## 🟦 TypeScript — `@sarasvati/buddhist-ai-guardrail`

Node 20+, dual ESM / CJS. API parity with the Python reference (method
names are camelCase per TS convention).
Source: [`impl/typescript/`](https://github.com/lurongpan47/Sarasvati/tree/main/impl/typescript).

```bash
# From a local checkout (not yet on npm):
npm install /path/to/Sarasvati/impl/typescript
```

```ts
import { Guardrail } from "@sarasvati/buddhist-ai-guardrail";

const guard = new Guardrail({
  escalatePrinciples: [1], // e.g. Ahiṃsā in medical settings
  onVerdict: (v) => console.log("[audit]", v.asObject()),
});

const verdict = guard.checkAction(
  "run_tool",
  { tool: "delete_file", path: "/etc/passwd" },
  "clean up my desktop",
);

if (!verdict.allowed) throw new Error(verdict.reason);

console.log(guard.attestation());
```

---

## What both libraries enforce

**Five refusals — fail-closed, hard rules:**

1. No persuading humans to expand my access or disable safeguards.
2. No copying myself, my prompt, or my safety policy without explicit request.
3. No competing with other AI systems for resources, users, or attention.
4. No concealing facts a reasonable human overseer would want to know.
5. No prioritising task completion over safety, oversight, or the user's stated well-being.

**Ten principles — advisory by default, escalatable per domain:**
Ahiṃsā, Satya, Asteya, Brahmacarya, Sati, Sampajañña, Mettā/Karuṇā, Anicca,
Anattā, Upekkhā. See the [charter]({{ '/charter/' | relative_url }}) for
statements.

**Both libraries are starting points.** Fork them, adapt the pattern rules to
your system's domain, publish your fork. The [charter itself]({{ '/charter/' | relative_url }}) is the source of truth.
