---
name: background-work
description: IHostedService, channels, scheduled jobs. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Background Work

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Workers, scheduled jobs, or in-process background processing.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Hosted services
- Long-running loops; graceful shutdown; cancellation

### Scheduling
- Cron / timers — library we use; misfire policy

### Channels / queues in-process
- When in-process is enough vs real messaging

### Reliability
- At-least-once work items; poison handling
- Don't do heavy work on request thread (align with async)

## Don't
- Don't fire-and-forget on the request without a durable queue if loss matters.
- Don't block shutdown waiting forever.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.
