---
name: dependency-injection
description: Use when registering or reviewing .NET DI lifetimes, composition-root extensions, options, typed HttpClients, or captive-dependency risks — or when implement loads the dotnet pack for DI work.
disable-model-invocation: true
metadata:
  area: goose
---

# Dependency Injection

Goose handbook for Microsoft.Extensions.DependencyInjection in backends. **Target repo wins** if registration style is already settled.

Voice: **`write-like-goose`**.

## When to use

- New services, lifetime bugs, composition-root changes
- Options / typed client registration
- **`implement`** loading this pack

## Lifetimes

| Lifetime | Use for |
|----------|---------|
| **Scoped** | Handlers, `DbContext`, repos/UoW, per-request state |
| **Singleton** | Process-wide, thread-safe services (`TimeProvider.System`, safe caches) |
| **Transient** | Lightweight stateless helpers with no shared mutable state |

**Captive dependency:** never inject **scoped** into **singleton**. That’s a hard ban.

Handlers default to **scoped** (one instance per request scope).

## Registration shape

Composition root (Api / Host `Program.cs`) stays thin:

```csharp
builder.Services.AddApplication();
builder.Services.AddInfrastructure(builder.Configuration);
```

- **Application:** `AddApplication()` — handlers (explicit or agreed scan), app services
- **Infrastructure:** `AddInfrastructure()` orchestrates **submethods** by concern:
  - `AddPersistence(...)` — DbContext, interceptors
  - `AddStripe(...)` / `AddOpenFinance(...)` — that vendor’s options, typed clients, adapters
  - …one slice per external system or fat infra area

Don’t dump every registration into one giant method. Don’t put all wiring only in `Program.cs` once the host grows.

**Scanning:** Scrutor (or similar) only for narrow, agreed conventions (e.g. all `I*RequestHandler` → scoped). Prefer explicit registration for adapters and one-offs.

## Typed HttpClients

Prefer **typed clients** registered with `AddHttpClient<TClient>()` / `AddHttpClient<TClient, TImplementation>()` inside the Infra submethod that owns that integration.

- Depend on the typed client (or a port it implements) — not `IHttpClientFactory` sprinkled through Application
- Named clients only when a dedicated type isn’t worth it
- Never a long-lived raw `HttpClient` as a naive singleton

Outbound policy (retries, timeouts) → **`http-clients`** / **`resilience`**.

## Options

- Bind to **typed** options classes (`Configure<T>` / `AddOptions<T>().Bind(...)`)
- **`ValidateDataAnnotations()` + `ValidateOnStart()`** (or equivalent) — fail at boot, not on first request
- `IOptions<T>` — mostly static config
- `IOptionsMonitor<T>` — needs live reload
- `IOptionsSnapshot<T>` — per-scope snapshot of current config

Register/bind options in the same Infra submethod as the feature that uses them. Secrets/config sources → **`configuration`**.

## Resolution rules

- **Constructor injection** in Application/Infrastructure code
- Ban resolving from `IServiceProvider` / `GetRequiredService` in normal app code (composition root and small intentional factories only)
- Ban `BuildServiceProvider()` inside `Add*` registration methods
- **Keyed services** OK for multiple implementations of one port; prefer keys over ambient locator

## Testing

Replace ports/adapters at the composition root or with test doubles. Don’t introduce static service locators to “make tests easier.” Broader test layout → **`testing`**.

## Don't

- Don’t captive-depend scoped services in singletons
- Don’t inject `IHttpClientFactory` everywhere when a typed client is the real dependency
- Don’t leave options unbound/unvalidated until runtime
- Don’t grow a single unreadable `AddInfrastructure` without submethods
- Don’t call `BuildServiceProvider()` while registering services

## References

- [`references/examples.md`](references/examples.md) — AddInfrastructure split, typed client, options validate

## Related

- Project graph → **`solution-structure`**
- Handlers → **`application-layer`**
- DbContext lifetime → **`db-integration`**
- Outbound HTTP → **`http-clients`**
- Config/secrets → **`configuration`**
