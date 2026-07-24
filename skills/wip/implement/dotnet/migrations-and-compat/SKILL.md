---
name: migrations-and-compat
description: EF migrations hygiene, expand/contract, schema compatibility. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Migrations and Compat

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- EF migrations, expand/contract in .NET, deploy order.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### EF mechanics
- Where migrations live; how we generate/apply in CI and local
- Idempotent scripts? bundle?

### Hygiene
- Never edit applied migrations
- Seed data policy

### Expand / contract
- Principles in [`../../database/`](../../database/SKILL.md); here = EF steps for dual columns, backfill jobs

### Multi-instance
- Rolling deploy + migration order

## Don't
- Don't squash or rewrite history that's in prod.
- Don't run destructive contract steps before backfill completes.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.
