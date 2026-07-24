---
name: messaging
description: Queues/buses, outbox, consumers, poison messages. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Messaging

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Integration events, queues, or consumers.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Topology
- Which bus/queue; message naming; versioning payloads

### Outbox / inbox
- When required (with DB transaction); dual-write ban

### Consumers
- Idempotency; ack/nack; concurrency
- Poison / DLQ handling

### Ordering & delivery
- At-least-once assumptions; what we guarantee

### Align with
- database (outbox table), resilience, background-work

## Don't
- Don't publish after SaveChanges without outbox if we require it.
- Don't assume exactly-once delivery.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.
