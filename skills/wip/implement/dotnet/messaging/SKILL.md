---
name: messaging
description: Use when designing or reviewing .NET integration events, buses, outbox, or queue consumers — or when choosing events vs Hangfire jobs — or when implement loads the dotnet pack for messaging work.
disable-model-invocation: true
metadata:
  area: wip
---

# Messaging

Goose handbook for **cross-process** events and queues. In-app deferred work → **`background-work`**. In-process domain event collection → **`domain-modeling`**.

**Target repo wins** if a bus or Hangfire-only style is already settled.

Voice: **`write-like-goose`**.

## When to use

- Something happened and **another process/service** (or a dedicated worker) should react
- Choosing bus vs job, outbox, consumer idempotency
- **`implement`** loading this pack

**Before wiring:** ask what the engineer means — **integration/domain event** (fact that occurred; others may react) vs **background task** (do this work later in *this* app). Don’t guess.

## Events vs jobs

| Kind | Use | Lives in |
|------|-----|----------|
| **Integration event** | Cross-process reaction; fan-out; other services | Bus behind **ports** (this skill) |
| **In-process domain event** | Same process, after successful save | **`domain-modeling`** (collect → dispatch) |
| **Background job** | Email, sync, cleanup, “run this later” in this app | **Hangfire / hosted jobs** → **`background-work`** |

Don’t pretend Hangfire is a multi-service bus. Don’t put every cron on Kafka.

## Abstraction (no single mandated bus lib)

Goose does **not** require MassTransit, Wolverine, or a specific broker.

| Layer | Rule |
|-------|------|
| **Application / Domain** | Publish/consume via **ports** (e.g. `IEventPublisher`, consumer interfaces). No raw SQS / Rabbit / Azure Service Bus / Amazon SDK types. |
| **Infrastructure** | Chooses the bus (MassTransit, Wolverine, Rebus, …) and transport. Document the choice in the target repo. |

**License note (when picking a bus):** MassTransit **v8** is Apache 2.0; **v9+** is commercial (Massient) — free/discount programs need qualification, not silent NuGet-only use. Wolverine/Rebus are MIT. Pick consciously per repo.

## Hosting listeners (web apps)

In ASP.NET web hosts, **queue/event listeners** run in a **`BackgroundService` / `IHostedService`** (or an equivalent bus-hosted consumer on that host) — **not** on the HTTP request path, and not started from controllers/endpoints.

Prefer a dedicated worker host when consumption load or lifecycle shouldn’t share the API process — still the same “hosted service” idea.

## Outbox

When a DB state change and an integration publish must succeed or fail together: use a **transactional outbox** (EF/bus outbox). **Ban dual-write** (`SaveChanges` then hope `Publish` works).

Hangfire enqueue-after-save is fine for jobs unless you need the same atomicity — then outbox or an equivalent pattern.

## Consumers and delivery

- Assume **at-least-once** delivery — design **idempotent** consumers (inbox, natural key, dedupe)
- Retries with backoff; **poison/fault → DLQ** (or bus fault queue) — don’t infinite-loop
- Don’t assume global ordering unless the topology guarantees it
- Align retries with **`resilience`**; don’t nest blind Polly on top of bus retries without knowing who owns the retry

## Don't

- Don’t use raw broker SDKs in Application/Domain
- Don’t publish integration events after `SaveChanges` without outbox when atomicity matters
- Don’t assume exactly-once delivery
- Don’t run queue polling on a request thread
- Don’t route every deferred task through the bus when Hangfire is the right tool

## References

- [`references/examples.md`](references/examples.md) — intent split + port sketch

## Related

- Domain event raise/dispatch → **`domain-modeling`**
- Hangfire / hosted jobs → **`background-work`**
- Retries / timeouts → **`resilience`**
- Outbox table / schema → **`database`** / **`db-integration`**
