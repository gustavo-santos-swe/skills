---
name: http-clients
description: Use when adding or reviewing outbound .NET HTTP calls — typed clients, DelegatingHandlers, fakes — or when implement loads the dotnet pack for HttpClient work.
metadata:
  area: goose
---

# HTTP Clients

Goose handbook for **outbound** HTTP. Registration lifetimes → **`dependency-injection`**. Retries/timeouts/circuit breakers → **`resilience`**.

**Target repo wins** if typed-client style is already settled.

Voice: **`write-like-goose`**.

## When to use

- Calling Stripe, OpenFinance, email, or any external HTTP API
- Auth headers, correlation, test doubles for outbound calls
- **`implement`** loading this pack

## Defaults (greenfield)

| Piece | Rule |
|-------|------|
| Registration | **Typed client** via `AddHttpClient<TClient>()` / `TClient, TImpl` inside the Infra slice that owns that vendor (**`dependency-injection`**) |
| Config | Base address, API keys, per-dependency timeouts from **typed options** (+ `ValidateOnStart`) |
| Resilience | **`AddStandardResilienceHandler()`** (or tuned equivalent) on that client — **`resilience`** |
| Cross-cutting | **`DelegatingHandler`** for auth, correlation/trace propagation, optional body logging (PII rules → **`observability`**) |
| Application | Depend on the typed client **or a port** it implements — not `IHttpClientFactory` sprinkled through handlers |

## Hard bans

- **`new HttpClient()`** per call (or naive long-lived singleton without factory)
- Blind retries on non-idempotent POSTs without a key — **`resilience`**
- User-supplied URLs fetched server-side without allowlist — SSRF → **`security`**

## Contracts

- Outbound DTOs are **this integration’s** contracts — version/tolerate unknown fields per vendor docs
- Don’t reuse ASP.NET request DTOs as wire types to third parties unless they truly match
- Timeouts are **per dependency**, not one global 100s

## Testing

| Layer | Approach |
|-------|----------|
| **Unit** | Substitute the **port** / typed client abstraction — or inject a custom `HttpMessageHandler` |
| **Integration** | WireMock / recorded stubs / Testcontainers only when the adapter matters; don’t call real prod vendors from CI |

## Don't

- Don’t inject `IHttpClientFactory` everywhere when a typed client is the real dependency
- Don’t log full outbound bodies with secrets/PII
- Don’t share one typed client config across unrelated vendors
- Don’t skip resilience on flaky third parties “to ship faster”

## References

- [`references/examples.md`](references/examples.md) — typed client + handler sketch

## Related

- `AddHttpClient` / options → **`dependency-injection`**
- Standard resilience pipeline → **`resilience`**
- SSRF / secrets → **`security`** / **`configuration`**
