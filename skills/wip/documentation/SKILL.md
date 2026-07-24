---
name: documentation
description: Write or update durable docs — ADRs before build, and system/API/runbook docs after implementation. Use when the user says "ADR", "document this", "update the docs", or a decision/public surface needs a written trail.
disable-model-invocation: true
metadata:
  area: wip
  inspired_by:
    - addyosmani/agent-skills — documentation-and-adrs
    - mattpocock/skills — domain-modeling (ADR format)
---

# Documentation

Status: **partial stub** — `adr` has a format; `ship-docs` still TODO. Project paths may be overridden by the target repo’s `AGENTS.md`.

Voice: durable prose — **`write-like-goose`**.

## Branches

Pick one (or both in order on a long feature):

| Branch | When in the lifecycle | Answers |
|--------|----------------------|---------|
| **`adr`** | During **design → plan**, before **implement** | *Why* we chose X (and what we rejected) |
| **`ship-docs`** | During/after **implement**, before **pr-raise** when the public surface changed | *How* it works / how to use it |

```
design → [documentation:adr?] → plan → … → implement → [documentation:ship-docs?] → pr-raise
```

## References

| File | Contents |
|------|----------|
| [`references/adr-format.md`](references/adr-format.md) | When to ADR, template, numbering, what qualifies |
| Glossary / CONTEXT | Owned by **`brainstorm`** — [`../brainstorm/references/context-format.md`](../brainstorm/references/context-format.md) |

## Branch: adr

1. Confirm the triple gate (hard to reverse + surprising + real trade-off). See [`adr-format.md`](references/adr-format.md).
2. Write the ADR (paragraph-first template; optional sections only if needed).
3. Link it from the plan, ticket, or brainstorm freeze so it stays discoverable.

Done when: decision is written, discoverable, and referenced from the plan or issue.

## Branch: ship-docs

_TODO: when required (API contract, onboarding, runbook, README surface), what to touch, DoD._

Done when: a newcomer can use or operate the changed surface without reading the PR diff.

## Don't

- Don't write an ADR for reversible trivia.
- Don't write ship-docs that only restate the code line-by-line.
- Don't block every PR on docs — only when the reader-facing or operator-facing surface changed.
- Don't put ubiquitous-language terms in ADRs — those go in `CONTEXT.md` via **brainstorm**.
