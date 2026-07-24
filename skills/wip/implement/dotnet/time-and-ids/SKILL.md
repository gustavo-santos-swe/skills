---
name: time-and-ids
description: Clocks, UTC, and identifier generation in .NET (TimeProvider, Guid/Ulid, strong IDs). Use when writing or reviewing time-dependent logic, ID creation, or testability of DateTime/new Guid in C#.
disable-model-invocation: true
metadata:
  area: wip
---

# Time and IDs

Status: **stub** — topic list below is what to define later. Keep SKILL.md short; deep samples → `references/`.

## When to use

- New entities needing IDs; scheduling; “now”; ordering/timestamps; freezing time in tests.
- **`implement`** loading this pack for a .NET change that touches clocks or ID generation.

## Topics to fill (checklist)

### Clock
- `TimeProvider` / `IClock` — our abstraction; ban `DateTime.Now` / `UtcNow` in domain/app?
- Always UTC in process and storage; local only at the UI edge
- `DateTime` vs `DateTimeOffset` vs `DateOnly` / `TimeOnly` — when each

### IDs
- Guid v4 vs v7 / Ulid / DB sequences — default per entity type
- Who generates IDs (app vs database)
- Strongly-typed IDs (wrappers) — yes/no; serialization rules (→ serialization / db-integration)

### Ordering & uniqueness
- Sortable IDs when we need time-ordering without a separate column
- Collision / uniqueness assumptions we document

### Testing
- How we fake the clock; seed IDs in tests
- Determinism requirements for snapshots/golden tests

### Align with
- domain-modeling (ID as value object), db-integration (column types), serialization (wire format)

## Don't

- Don't call `DateTime.Now` in domain/application if we standardize on a clock abstraction.
- Don't mix local and UTC timestamps in the same column/API field.
- Don't generate non-unique “pretty” IDs without a uniqueness guarantee.

## References

Optional: `references/` for ID/clock patterns. Project-specific generators stay in the target repo.
