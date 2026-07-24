---
name: application-layer
description: Use cases/handlers, DTOs, orchestration without leaking I/O into domain. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Application Layer

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Adding or changing application use cases / handlers.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Use cases / handlers
- One handler = one use case? naming (`XCommand` / `XHandler`)
- MediatR (or not) — our choice and pipeline behaviors

### DTOs vs domain
- Request/response types at the edge; no domain entities over the wire
- Mapping style (manual, Mapperly, etc.)

### Orchestration
- What the handler may call (repos, clock, id generator)
- Transactions: opened here or in infrastructure? (align with db-integration)

### Cross-cutting in pipeline
- Logging, validation, authz behaviors — order of pipeline

### Idempotency
- Commands that must be safe to retry — how we model that

## Don't
- Don't put SQL or HttpClient calls in domain.
- Don't return tracked EF entities from handlers.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.
