---
name: domain-modeling
description: Aggregates, value objects, invariants, domain events — C# patterns (not the Matt process skill). Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Domain Modeling

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- New entities, changing invariants, or domain events in C#.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Building blocks
- Entity vs Value Object vs Aggregate root — our criteria
- IDs (Guid, Ulid, strong types?)
- Factories / constructors — how invariants are enforced

### Invariants
- Always in domain methods, never only in validators at the edge
- What stays anemic vs rich — our line

### Domain events
- When we raise them; in-process vs outbox (point to messaging if needed)
- Naming and payload rules

### Persistence ignorance
- What the domain must not know (EF, HttpContext, ILogger?)
- Snapshots / mementos if we use them

### Relation to process skills
- Ubiquitous language / ADRs → wip `documentation` + engineering `domain-modeling` (Matt)
- This skill = **C# shape** of the domain

## Don't
- Don't put EF attributes as the only model of the domain.
- Don't create aggregates that span multiple consistency boundaries for convenience.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.
