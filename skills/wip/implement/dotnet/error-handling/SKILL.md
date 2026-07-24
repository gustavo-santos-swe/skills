---
name: error-handling
description: Exceptions vs Result, domain errors, HTTP mapping, consistency. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Error Handling

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Error types, exception middleware, or API error shapes.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Strategy
- Exceptions vs Result/Error union — our default per layer
- Domain errors as types vs magic strings

### Mapping to HTTP
- Domain/app error → status + ProblemDetails catalog
- What becomes 400 / 401 / 403 / 404 / 409 / 422 / 500

### Infrastructure failures
- DB unique/concurrency (with db-integration); transient → resilience

### Logging
- What we log at which level; no PII in messages (observability)

### Consistency
- One pipeline for unhandled exceptions; no catch-all that swallows

## Don't
- Don't return 500 for expected business failures.
- Don't expose stack traces or internal messages to clients.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.
