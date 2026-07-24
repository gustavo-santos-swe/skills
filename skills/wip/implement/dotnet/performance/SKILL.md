---
name: performance
description: Measure-first hot paths in .NET — allocations, ASP.NET/EF bottlenecks, budgets. Use when chasing latency, allocations, throughput, or perf regressions in C#/.NET (not schema design or cache policy alone).
disable-model-invocation: true
metadata:
  area: wip
---

# Performance

Status: **stub** — topic list below is what to define later. Keep SKILL.md short; deep samples → `references/`.

**This skill = runtime cost in process.** Schema/SQL truth → [`../../database/`](../../database/SKILL.md). EF wiring → [`../db-integration/`](../db-integration/SKILL.md). Cache *policy* → [`../caching/`](../caching/SKILL.md). Async correctness → [`../async/`](../async/SKILL.md).

## When to use

- Hot paths, allocation spikes, p95/p99 regressions, “is this N+1 / too chatty?”
- **`implement`** loading this pack for a perf-sensitive .NET change.

## Topics to fill (checklist)

### Measure first (non-negotiable)
- Tools we use: `dotnet-trace`, `dotnet-counters`, BenchmarkDotNet, app metrics/APM
- What “evidence” means before a micro-opt lands
- How we reproduce locally vs prod-like load
- Flamegraphs / alloc profiles — when each

### Budgets & SLOs
- Latency budgets (p50/p95/p99) per endpoint class if we have them
- Payload size budgets (request/response)
- Allocation budgets on hot paths (optional, only where we care)
- When to fail CI / review on budget break

### Allocations & GC
- Spans / `ReadOnlySpan` / `Memory` — when worth it
- `ArrayPool` / `ObjectPool` — rent/return discipline
- Boxing, closures, iterator allocations
- `record` / LINQ / `string` concat on hot paths — our rules
- LOH / large buffers; streaming vs buffering

### ASP.NET Core hotspots
- Middleware order cost; avoid heavy work per request in pipeline
- Model binding / JSON serialize cost (align with serialization)
- Sync-over-async / thread-pool starvation (pointer to async)
- Response buffering vs streaming large payloads
- Kestrel / limits that affect throughput (if we tune them)

### Data access (symptoms → other skills)
- N+1, over-fetch, missing projection — detect here; fix with db-integration + database
- Chatty round-trips vs one query; cartesian explosions
- Tracking vs no-tracking on read paths
- When to suggest Dapper/raw SQL (policy lives in db-integration)

### Caching & fan-out
- When missing cache is the real bug (→ caching)
- Unbounded `Task.WhenAll` / parallel fan-out (→ async + resilience)
- Stampede as a perf incident

### Concurrency & throughput
- Lock contention; `Channel` vs unbounded queues
- CPU-bound work off the request thread (→ background-work)
- Connection pool exhaustion (HTTP/DB) as a throughput killer

### Serialization & payloads
- Over-serializing graphs; anonymous DTOs vs slim projections
- Compression when it helps vs CPU tradeoff
- Align with api-contracts (don’t “optimize” by breaking shape)

### Testing performance
- When BenchmarkDotNet is required vs “smoke under load”
- Perf tests in CI — yes/no, how flaky we tolerate
- Regression gate: compare to baseline how?

### Review checklist (short)
- [ ] Measured before/after?
- [ ] Hot path or cold path?
- [ ] Clarity preserved on non-hot code?
- [ ] Cross-links: database / caching / async if the fix lives there?

## Don't

- Don't optimize before measuring.
- Don't sacrifice clarity on cold paths for micro-gains.
- Don't “fix perf” by weakening correctness, authz, or schema integrity.
- Don't tune SQL indexes here without the database skill’s rules.

## References

Optional: `references/` for BenchmarkDotNet templates, trace recipes. Project SLOs stay in the target repo.
