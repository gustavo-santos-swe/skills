---
name: brainstorm-with-docs
description: Brainstorm a plan with relentless Q&A while sharpening domain language and updating CONTEXT.md and ADRs inline. Use when user wants to stress-test a design, align on terminology, build a shared glossary, or says "brainstorm with docs", "grill the plan", or needs domain language before implementation. Pairs with brainstorming — use this when CONTEXT.md/ADRs matter; use brainstorming for the full spec-to-plan flow.
metadata:
  area: product
  upstream:
    repo: mattpocock/skills
    path: skills/engineering/grill-with-docs
    url: https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs
    synced_at: "2026-06-07"
    commit: be55a7970319ede7965edbb02b5e41cba1ca82c9
    note: Renomeada de grill-with-docs; complementa brainstorming.
---

# Brainstorm With Docs

Grilling session that aligns the plan with the project's domain language and documents decisions as they crystallise.

**Announce at start:** "Estou usando a skill brainstorm-with-docs."

## When to use

| Situação | Skill |
|----------|-------|
| Feature nova, fluxo completo (spec → plan) | `brainstorming` |
| Plano/ideia existe, precisa alinhar linguagem e docs | **esta skill** |
| Repo já tem `CONTEXT.md` / ADRs e decisões precisam ser validadas | **esta skill** |

## The session

Interview the user relentlessly about every aspect of the plan until you reach shared understanding. Walk down each branch of the design tree, resolving dependencies one-by-one. For each question, provide your recommended answer.

- Ask **one question at a time** — wait for feedback before continuing.
- If a question can be answered by exploring the codebase, explore the codebase instead.

## Domain awareness

During codebase exploration, look for existing documentation.

### File structure

Most repos have a single context:

```
/
├── CONTEXT.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

If `CONTEXT-MAP.md` exists at the root, the repo has multiple contexts — read the map to find each `CONTEXT.md`.

Create files lazily — only when you have something to write.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with `CONTEXT.md`, call it out. "Your glossary defines 'cancellation' as X, but you seem to mean Y — which is it?"

### Sharpen fuzzy language

When the user uses vague terms, propose a precise canonical term. "You said 'account' — do you mean Customer or User?"

### Discuss concrete scenarios

Stress-test domain relationships with specific edge-case scenarios.

### Cross-reference with code

When the user states how something works, check whether the code agrees. Surface contradictions explicitly.

### Update CONTEXT.md inline

When a term is resolved, update `CONTEXT.md` immediately — don't batch. Format: `references/context-format.md`.

`CONTEXT.md` is a **glossary only** — no implementation details, no spec, no scratch pad.

### Offer ADRs sparingly

Only when all three are true:

1. **Hard to reverse**
2. **Surprising without context**
3. **Result of a real trade-off**

Format: `references/adr-format.md`.

## Handoff to implementation

When the session is complete and terminology is aligned:

- If a full spec is still needed → invoke `brainstorming` or proceed to `writing-plans`
- If the plan is clear → invoke `writing-plans` directly

## References

- `references/context-format.md`
- `references/adr-format.md`
