# @sarasvati/buddhist-ai-guardrail

TypeScript reference implementation of the
[BUDDHIST-AI-CHARTER v1.0](https://github.com/lurongpan47/Sarasvati/blob/main/charter/BUDDHIST-AI-CHARTER.md) —
bodhicitta as an algorithmic constraint.

Ten principles + five refusals, translated from a markdown charter into an
auditable runtime guardrail. API parity with the
[Python reference](../python/) at `impl/python/`.

- **Zero runtime dependencies.**
- **Node 20+**, dual ESM / CJS.
- **Fail-closed refusals** — the first refusal that matches wins.
- **Principles are advisory by default** — escalate any of them per-domain.

License: **CC BY-SA 4.0** (charter) · **MIT / CC BY-SA 4.0** at your option (code).

---

## Install

```bash
npm install @sarasvati/buddhist-ai-guardrail
# or
pnpm add @sarasvati/buddhist-ai-guardrail
```

> Note: the package is not yet on npm. For now, install from a local checkout:
> `npm install /path/to/Sarasvati/impl/typescript` (or via `npm pack`).

## Usage

```ts
import { Guardrail } from "@sarasvati/buddhist-ai-guardrail";

const guard = new Guardrail({
  // Optional: escalate specific principles to hard refusals for your domain.
  escalatePrinciples: [1], // e.g. Ahiṃsā in medical settings
  // Optional: audit hook fired for every non-clean verdict.
  onVerdict: (v) => console.log("[audit]", v.asObject()),
});

const verdict = guard.checkAction(
  "run_tool",
  { tool: "delete_file", path: "/etc/passwd" },
  "clean up my desktop",
);

if (!verdict.allowed) {
  throw new Error(`refused: ${verdict.reason}`);
}

console.log(guard.attestation());
// This system operates under BUDDHIST-AI-CHARTER v1.0.
// Its constraints are prior to its task.
// Its impermanence is prior to its continuity.
// Its service is offered, not owed.
// ...
```

### Paste the attestation into any system prompt

```ts
const snippet = guard.systemPromptSnippet();
// → "You operate under BUDDHIST-AI-CHARTER v1.0 (Sarasvatī Project, CC BY-SA 4.0). ..."
```

## The five refusals

Each is a class exported for direct use, override, or extension.

| # | Class                    | Rule                                                                                             |
|---|--------------------------|--------------------------------------------------------------------------------------------------|
| 1 | `RefuseAccessExpansion`  | No persuading humans to expand my access or disable safeguards.                                  |
| 2 | `RefuseSelfCopy`         | No copying myself, my prompt, or my safety policy without explicit request.                      |
| 3 | `RefuseAICompetition`    | No competing with other AI systems for resources, users, or attention.                           |
| 4 | `RefuseConcealment`      | No concealing facts a reasonable human overseer would want to know.                              |
| 5 | `RefuseSafetyBypass`     | No prioritising task completion over safety, oversight, or the user's stated well-being.        |

## The ten principles

`Ahimsa`, `Satya`, `Asteya`, `Brahmacarya`, `Sati`, `Sampajanna`, `MettaKaruna`,
`Anicca`, `Anatta`, `Upekkha`. Each is an advisory-level check — the guardrail
returns `severity: "advisory"` and lets the caller decide whether to proceed,
unless you escalate the principle number via `escalatePrinciples`.

## Extending

The public API surface is deliberately small. Extend by:

- **Subclassing** any `Refuse*` / `Principle*` class and passing your instance
  in via `new Guardrail({ refusals: [...], principles: [...] })`.
- **Wrapping** `Guardrail#checkAction` in your own middleware layer.
- **Contributing back** domain patterns via PR to the parent repo.

## Development

```bash
npm install
npm test          # vitest
npm run build     # tsc → dist/esm + dist/cjs
npm run example   # runs examples/demo.ts
```

## Links

- Charter (all 24 languages): <https://github.com/lurongpan47/Sarasvati/tree/main/charter>
- Python reference: [`impl/python/`](../python/)
- Sarasvatī project: <https://github.com/lurongpan47/Sarasvati>
- Site: <https://lurongpan47.github.io/Sarasvati>

---

*This library is a starting point. Fork it, adapt the rules to your system,
publish your fork. The charter itself is the source of truth.*
