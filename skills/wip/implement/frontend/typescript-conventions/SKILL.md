---
name: web-typescript-conventions
description: Use when setting TS patterns for a Next.js/React codebase — types for props, zod boundaries, and strictness.
disable-model-invocation: true
metadata:
  area: wip
---

# TypeScript Conventions

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Shared types, zod parsers, strict mode debates.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Strictness
- `strict` / noUncheckedIndexedAccess — our bar
- `any` policy; zod at boundaries

### Sharing types
- App types vs API contract types (OpenAPI)
- Server/client type-only imports

### React types
- Props patterns; children; branded IDs if any

## Don't
- Don't weaken `strict` to silence errors.
- Don't trust query/body shapes without parsing at the boundary.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

