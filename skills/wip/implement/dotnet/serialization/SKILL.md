---
name: serialization
description: System.Text.Json conventions, enums/dates, polymorphism. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Serialization

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- JSON contract or serializer configuration changes.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Defaults
- STJ settings (naming, nulls, comments); Newtonsoft — banned or not

### Types
- DateTime/DateTimeOffset (UTC); enums as string vs int
- Decimal / money

### Polymorphism
- Discriminators; when we allow it

### Contracts
- What must stay stable (align with api-contracts)

## Don't
- Don't silently change enum/date formats on public APIs.
- Don't serialize domain entities with cycles/nav properties by accident.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.
