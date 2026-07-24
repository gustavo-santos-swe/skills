---
name: web-error-loading-ui
description: Use when adding Next.js `loading.tsx`, `error.tsx`, `not-found`, or Suspense fallbacks.
disable-model-invocation: true
metadata:
  area: wip
---

# Error and Loading UI

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Route-level pending/error UX, digests, not-found.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Files
- When to add `loading` / `error` / `not-found` per segment
- Error boundary reset patterns

### Suspense
- Granularity of fallbacks; skeleton standards

### User messaging
- Safe messages vs digests; reporting (Sentry)

## Don't
- Don't expose stack traces to end users.
- Don't wrap the entire app in one coarse spinner if segments can stream.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

