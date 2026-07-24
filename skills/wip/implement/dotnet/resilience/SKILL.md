---
name: resilience
description: Timeouts, retries, circuit breakers (Polly), idempotency. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Resilience

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Outbound calls, flaky dependencies, or retry policy design.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Timeouts
- Per dependency defaults; cancellation linkage

### Retries
- Which ops are safe; exponential backoff; jitter
- Idempotency keys for non-safe HTTP/commands

### Circuit breakers / bulkhead
- When we use them; failure thresholds

### Polly / built-in
- Standard pipelines we reuse (HttpClient, etc.)

### Align with
- http-clients, messaging, error-handling

## Don't
- Don't retry non-idempotent operations without a key/guard.
- Don't infinite-retry on the request thread.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.
