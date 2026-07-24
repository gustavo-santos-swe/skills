---
name: caching
description: Memory/distributed cache, invalidation, stampede. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Caching

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Adding or changing caches.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Layers
- IMemoryCache vs distributed (Redis?) — when each

### Keys & TTLs
- Naming; TTL defaults; absolute vs sliding

### Invalidation
- Event-based vs TTL-only; stampede (lock / coalescing)

### Consistency
- What may be stale; cache beside source of truth

## Don't
- Don't cache authorized data without varying by principal when needed.
- Don't use cache as the system of record.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.
