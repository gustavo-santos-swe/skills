---
name: rn-error-and-boundaries
description: Use when defining error UI, ErrorBoundaries, crash reporting, or user-visible failure patterns in React Native.
disable-model-invocation: true
metadata:
  area: wip
---

# Error and Boundaries

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Crash redboxes in prod, failed screens, reporting.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Boundaries
- Where ErrorBoundaries wrap (root / feature)
- Fallback UI standards

### Reporting
- Sentry/Crashlytics — what we send; PII scrubbing
- Fatal vs non-fatal

### User messaging
- Retryable vs dead-end errors; align with data-fetching

## Don't
- Don't swallow errors silently in production.
- Don't show raw exception messages to users.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

