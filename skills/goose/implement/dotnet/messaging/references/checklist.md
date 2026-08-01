| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Ask whether the need is a cross-process integration event or an in-app background task before wiring — don't guess | verify | Before wiring |
| Application/Domain publish and consume via ports (`IEventPublisher`, consumer interfaces) — no raw SQS/Rabbit/Azure Service Bus/broker SDK types | verify | Abstraction |
| Queue/event listeners run in a `BackgroundService`/`IHostedService` (or bus-hosted consumer) — never on the HTTP request path | verify | Hosting listeners |
| A transactional outbox is used only where the DB write and integration publish must succeed or fail together — ban dual-write | verify | Outbox — "must be atomic" is a product-risk judgment per use case |
| Consumers assume at-least-once delivery and are designed idempotent (inbox, natural key, dedupe) | verify | Consumers and delivery |
| Retries use backoff; poison/fault messages go to a DLQ (or bus fault queue) — don't infinite-loop | verify | Consumers and delivery |
| Don't assume global ordering unless the topology guarantees it | verify | Don't |
| Don't route every deferred task through the bus when Hangfire is the right tool | verify | Don't |
