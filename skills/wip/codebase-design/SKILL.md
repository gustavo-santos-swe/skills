---
name: codebase-design
description: Deep-module vocabulary (seam, depth, adapter). Use when shaping interfaces, deciding seams, or when brainstorm/implement/architecture-pass need that language.
disable-model-invocation: true
metadata:
  area: wip
  inspired_by:
    - mattpocock/skills - codebase-design (Ousterhout / Feathers vocabulary)
---

# Codebase Design

Shared language for **deep modules**: lots of behaviour behind a small interface, at a clean **seam**, tested through that interface.

Voice: **`write-like-goose`**.

Use these terms exactly — don’t swap in “component,” “service,” “API,” or “boundary.”

## When to use

- Designing or reshaping a module interface
- Choosing where a seam goes / whether an adapter is real
- Brainstorm or architecture work that needs depth / locality language
- **`improve-codebase-architecture`** (engineering) when surveying deepening opportunities

## Glossary

| Term | Meaning |
|------|---------|
| **Module** | Anything with an interface + implementation (function, class, package, slice). Not “unit/component/service.” |
| **Interface** | Everything a caller must know: types *plus* invariants, ordering, errors, config, perf. Broader than a TS `interface`. |
| **Implementation** | What’s inside. Distinct from **adapter** (role at a seam). |
| **Depth** | Leverage at the interface — behaviour per unit of interface to learn. **Deep** = small interface, lots behind it. **Shallow** = interface nearly as complex as the body. |
| **Seam** | Place you can alter behaviour without editing there (Feathers); where the interface *lives*. Placement is its own decision. |
| **Adapter** | Concrete thing that satisfies an interface at a seam (role, not guts). |
| **Leverage** | Caller payoff from depth — one implementation pays N call sites / M tests. |
| **Locality** | Maintainer payoff — change, bugs, knowledge concentrate in one place. |

## Deep vs shallow

- **Deep:** small interface, complexity hidden → ask: fewer methods? simpler params? more hidden inside?
- **Shallow:** large interface, thin pass-through → deletion test below usually fails.

## Principles

1. **Depth is about the interface**, not LOC inside. Internal seams (private, for the module’s own tests) are fine; don’t expose them.
2. **Deletion test.** Delete the module: if complexity vanishes, it was a pass-through; if it reappears across N callers, it earned its keep.
3. **Interface = test surface.** Callers and tests cross the same seam. Wanting to test *past* it usually means wrong shape.
4. **One adapter = hypothetical seam; two = real.** Don’t add a port until something actually varies (often prod + test).

## Testability habits

- Accept dependencies; don’t construct them inside.
- Prefer returning results over hidden side effects when the logic is the point.
- Small surface → fewer tests, simpler setup.

## References (load when needed)

| File | When |
|------|------|
| [`references/deepening.md`](references/deepening.md) | Deepening a cluster; dependency categories; replace-don’t-layer tests |
| [`references/design-it-twice.md`](references/design-it-twice.md) | Parallel alternate interfaces for one candidate |

## Guardrails

1. Use this vocabulary in suggestions — don’t invent parallel jargon.
2. Domain names still come from `CONTEXT.md` (brainstorm); this skill is architecture nouns only.
3. Don’t introduce seams for a single adapter “just in case.”

## Related

- Freeze the *what* → **brainstorm**
- Build behind a seam → **implement** (TDD at the agreed interface)
- Survey deepening opportunities → `engineering/improve-codebase-architecture`
