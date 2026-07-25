---
name: resilience
description: Use when designing or reviewing .NET retries, timeouts, circuit breakers, or idempotent outbound calls — Polly/standard Http resilience — or when implement loads the dotnet pack for resilience work.
disable-model-invocation: true
metadata:
  area: wip
---

# Resilience

Goose handbook for surviving flaky dependencies without duplicating side effects.

**Target repo wins** if resilience wiring is already settled.

Voice: **`write-like-goose`**.

## When to use

- Typed HttpClients, third-party APIs, transient failures
- Choosing retry vs fail-fast; idempotency for commands
- **`implement`** loading this pack

## Stack (greenfield)

Prefer **`Microsoft.Extensions.Http.Resilience`** / Aspire **`AddStandardResilienceHandler()`** on typed clients (timeouts, retries, circuit breaker as a pipeline).

- Tune **per client** when a vendor needs different budgets
- Don’t hand-roll Polly in every call site
- Don’t infinite-retry on the request thread

Typed client registration → **`dependency-injection`** / **`http-clients`**.

## What to retry

| Safe by default | Only with a guard |
|-----------------|-------------------|
| GET and other idempotent/safe HTTP | POST/PUT/PATCH/commands that create side effects |
| Documented idempotent APIs | Payments, charges, “create X” without a key |

For non-safe commands: retry only with an **idempotency key** or **natural key** (**`application-layer`**), or when the remote API is explicitly idempotent. No blind retry of charge/payment effects.

## Timeouts and cancellation

- Each outbound dependency gets an **explicit timeout** in the resilience pipeline (not “infinite HttpClient”)
- Always flow **`CancellationToken`** from the incoming request (**`async`**)
- Prefer per-dependency budgets over one giant global timeout

## Where pipelines apply

| Surface | Approach |
|---------|----------|
| **Outbound HTTP / similar** | Standard resilience handler on the typed client |
| **EF / DB** | Provider + EF **execution strategy** for transient faults when enabled — don’t Polly-wrap every `SaveChanges` on top of HTTP retries |
| **Messaging consumers** | **`messaging`** (ack/retry/poison) |

Avoid nested retry stamps (HTTP pipeline + ad-hoc loop + EF strategy fighting each other). Know which layer owns the retry.

## Circuit breakers

Comes with the standard pipeline. Use open/break to shed load when a dependency is down; don’t disable the breaker to “make tests pass” in production configs.

## Don't

- Don’t retry non-idempotent operations without a key/guard
- Don’t catch-and-retry forever inside a handler
- Don’t apply the same aggressive retry to every client without looking at the vendor
- Don’t hide business failures (4xx) behind retries — retry **transient** faults

## References

- [`references/examples.md`](references/examples.md) — standard handler + idempotency note

## Related

- Typed HttpClients → **`http-clients`** / **`dependency-injection`**
- Natural-key idempotency → **`application-layer`**
- Failure mapping → **`error-handling`**
- Cancellation → **`async`**
