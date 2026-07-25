---
name: background-work
description: Use when adding or reviewing .NET Hangfire jobs, hosted services, in-process channels, or deferred work off the request thread — or when implement loads the dotnet pack for background work.
disable-model-invocation: true
metadata:
  area: wip
---

# Background Work

Goose handbook for deferred work **inside this application**. Cross-process events/queues → **`messaging`**. Ask which one you need before wiring.

**Target repo wins** if job infra is already settled (Monetis = Hangfire).

Voice: **`write-like-goose`**.

## When to use

- “Do this later” in the same app: email, sync, cleanup, PDF, orphan GC
- Scheduled/cron work; graceful shutdown of loops
- **`implement`** loading this pack

## What goes where

| Need | Tool |
|------|------|
| Durable unit-of-work job (retry, delay, schedule) | **Hangfire** (+ SQL/Postgres storage) |
| Continuous listener / long-running receive loop | **`BackgroundService` / `IHostedService`** (also **`messaging`** for bus consumers) |
| In-process handoff; OK to lose on crash | `Channel<T>` / similar |
| Another service must react to a fact | **`messaging`** — not Hangfire-as-bus |

## Hangfire (greenfield default for jobs)

- Enqueue or schedule from the handler/host after the decision is made — not heavy work on the request thread
- Persist job storage (Postgres/SQL) — don’t run memory-only storage in production
- Retries: assume **at-least-once** → job body **idempotent** when re-run
- Dashboard: **authz-gated** (not public on the internet)
- Prefer recurring jobs via Hangfire schedule over ad-hoc `while` + `Task.Delay` for cron-like work

## Atomicity with DB (Hangfire outbox)

`SaveChanges()` then `BackgroundJob.Enqueue(...)` is a **dual-write** — Hangfire’s SQL storage usually uses its **own connection**, so enqueue is not automatically in your EF transaction.

When the business write and “must run this job” must succeed or fail together:

1. In the **same EF transaction**: write business rows + an **outbox job** row (type + payload/args)
2. A **dispatcher** (Hangfire recurring job or `BackgroundService`) reads pending rows → `Enqueue` → mark dispatched

The durable intent is the **outbox table**; Hangfire executes. Don’t rely on enlisting Hangfire’s internal tables in your transaction unless you’ve proven the provider setup.

Loss-tolerant work: enqueue after save is fine. Integration events across processes → **`messaging`** outbox, not Hangfire-as-bus.

## Hosted services

- Long-running loops use linked **`CancellationToken`** and shut down promptly
- Don’t block host shutdown waiting forever
- Don’t start background loops from controllers/endpoints

## Request-path rules

- **No fire-and-forget** (`Task.Run`, discarded tasks) when losing the work matters — enqueue Hangfire (or a real queue)
- Align with **`async`**: no sync-over-async; pass cancellation into job work when the API supports it
- Keep the HTTP handler thin: validate → enqueue → return

## Don't

- Don’t use Hangfire as a multi-service integration bus
- Don’t do CPU/IO-heavy work synchronously in the request
- Don’t leave the Hangfire dashboard anonymous in shared/prod environments
- Don’t assume a job runs exactly once
- Don’t dual-write `SaveChanges` + `Enqueue` when losing the job is unacceptable — use the Hangfire outbox pattern
- Don’t ignore orphan/cleanup jobs when uploads create abandoned blobs (**`file-storage`**)

## References

- [`references/examples.md`](references/examples.md) — enqueue vs F&F sketch

## Related

- Integration events / outbox → **`messaging`**
- Cancellation / no F&F → **`async`**
- Orphan file cleanup → **`file-storage`**
