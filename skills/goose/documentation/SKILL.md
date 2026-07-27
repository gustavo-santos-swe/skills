---
name: documentation
description: ADRs before build; ship-docs after. Use when a decision or public/ops surface needs a durable written trail.
metadata:
  area: goose
---

# Documentation

Goose handbook for durable project docs. Two branches: **`adr`** (why) and **`ship-docs`** (how to use/operate).

Voice: **`write-like-goose`**. Project paths may be overridden by the target repo’s `AGENTS.md`.

## Branches

| Branch | When in the lifecycle | Answers |
|--------|----------------------|---------|
| **`adr`** | During **design → plan**, before **implement** | *Why* we chose X (and what we rejected) |
| **`ship-docs`** | During/after **implement**, before **pr-raise** when the public or ops surface changed | *How* it works / how to use or operate it |

```
design → [documentation:adr?] → plan → … → implement → [documentation:ship-docs?] → pr-raise
```

## References

| File | Contents |
|------|----------|
| [`references/adr-format.md`](references/adr-format.md) | When to ADR, template, numbering, what qualifies |
| Glossary / CONTEXT | Owned by **`brainstorm`** - [`../brainstorm/references/context-format.md`](../brainstorm/references/context-format.md) |

## Branch: adr

1. Confirm the triple gate (hard to reverse + surprising + real trade-off). See [`adr-format.md`](references/adr-format.md).
2. Write the ADR (paragraph-first template; optional sections only if needed).
3. Link it from the plan, ticket, or brainstorm freeze so it stays discoverable.

**Done when:** decision is written, discoverable, and referenced from the plan or issue.

## Branch: ship-docs

### When required

Run this branch if **any** of these changed:

- Public HTTP/API contract or user-facing behaviour
- Onboarding / setup steps
- Operator runbook, alerts, or deploy steps
- README “how to run” (or equivalent) for the changed area

Skip when the PR is internal-only (pure refactor, tests, private helpers) with no reader- or operator-facing surface change.

### What to touch

1. Prefer the **target repo’s** existing docs paths for that surface.
2. Else under `docs/`: API notes, `docs/runbooks/`, or the relevant README section.
3. Keep prose outcome-oriented - not a line-by-line code restatement.

### DoD

- [ ] A newcomer can use or operate the changed surface without reading the PR diff
- [ ] No line-by-line code dump
- [ ] Linked from the PR body References (or the ticket) when a PR exists

**Done when:** the checklist is green.

## Hard rules

1. ADR only when the triple gate passes (see adr-format).
2. Ship-docs only when a reader/ops surface changed.
3. Ubiquitous-language terms → `CONTEXT.md` via **brainstorm**, not ADRs.

## Related

- Freeze the what → **brainstorm**
- Plan → **planning**
- Build → **implement**
- Open PR → **pr-raise**
