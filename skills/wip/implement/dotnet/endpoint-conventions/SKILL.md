---
name: endpoint-conventions
description: Minimal APIs/controllers, routing, versioning, ProblemDetails, auth hooks. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Endpoint Conventions

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Adding or changing HTTP endpoints.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Style
- Minimal APIs vs controllers — our default
- Route templates, naming, pluralization

### HTTP semantics
- Status codes we use; ProblemDetails shape
- Idempotent verbs; PUT vs PATCH policy

### Authz at the edge
- `[Authorize]` / policies / filters — where it lives vs application layer

### Versioning
- URL vs header; how breaking changes ship (align with api-contracts)

### Binding & validation
- What binds from body/route/query; handoff to validation skill

### OpenAPI
- What we expose; what's internal

## Don't
- Don't leak domain exceptions as 500 without mapping.
- Don't put business rules only in endpoint filters.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.
