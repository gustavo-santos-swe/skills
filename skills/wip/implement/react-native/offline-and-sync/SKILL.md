---
name: rn-offline-and-sync
description: Use when designing offline-first behavior, mutation queues, or sync conflict handling in React Native.
disable-model-invocation: true
metadata:
  area: wip
---

# Offline and Sync

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Offline mode, retry queues, conflict UX.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Model
- Read-through cache vs true offline-first — our ambition level
- Mutation queue; idempotency keys (align with backend)

### Connectivity
- NetInfo usage; UX when offline
- Conflict resolution (last-write, server-wins, manual)

### Storage
- What we persist for offline; size limits; encryption needs

## Don't
- Don't pretend optimistic UI is durable without a queue.
- Don't sync unbounded payloads on every reconnect.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

