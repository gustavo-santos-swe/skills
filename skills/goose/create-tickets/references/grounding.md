# Grounding and drift

## Find a source of truth (preflight)

Search the target repo before inventing shape:

| Situation | Look for |
|-----------|----------|
| New/changed HTTP API | OpenAPI/Swagger, proto, API ADR, existing route docs |
| Domain rules | ADR, glossary, `docs/` brief, prior tickets |
| Greenfield feature/project | Project brief, PRD, README scope, design notes |
| UI behaviour | Design doc, accepted prototype notes, existing screen copy |

If nothing fits: **stop and ask**. Options:

1. Path to an existing doc to treat as source of truth
2. Create/update a brief or ADR first (**documentation**)
3. **Open** - model proposes; freeze the contract in the epic/issue or plan slice before publish

## What “aligned” means

- Implement: acceptance criteria pass **and** behaviour matches the cited source of truth (contract test, snapshot of public surface, or explicit manual checklist).
- Review: diff vs the same source of truth - not only “code looks fine.”

## When drift appears

Drift = intentional or forced divergence from the cited source of truth (path, field, rule, UX).

**Always ask the engineer** which of:

| Choice | Use when | Example |
|--------|----------|---------|
| **Update** the source of truth | Product/API change is intentional and the doc should stay true | OpenAPI path `/orders` → `/v2/orders`; edit yaml in the PR; note on the issue |
| **Separate drift log** + follow-up | Another team owns the contract, or you must ship before the doc can change | Log entry + ticket “sync openapi”; SoT unchanged for now |
| **Addendum** on the existing doc | Keep original text; record dated exception without full rewrite | Brief keeps v1 story; addendum: “2026-07-26: gateway requires `/v2` until cutover” |

Lean if they shrug: intentional owned change → **update**; need history → **addendum**; can’t touch SoT → **log**.

Never silently rewrite the source of truth mid-slice when the change is **scope** (new endpoints, new product rules) - re-approve the breakdown or AC first.
