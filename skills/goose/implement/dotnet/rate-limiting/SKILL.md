---
name: rate-limiting
description: Use when adding or reviewing ASP.NET request throttles, per-user/IP quotas, 429 behavior, or probe exemptions — or when implement loads the dotnet pack for rate-limit work.
disable-model-invocation: true
metadata:
  area: goose
---

# Rate Limiting

Goose handbook for abuse/quota controls on .NET APIs.

**Target repo wins** if gateway or app limits are already settled.

Voice: **`write-like-goose`**.

Concrete numbers (N req/min) live per service in the target repo — this skill is **shape**.

## When to use

- Public or sensitive endpoints need throttles
- Per-user / per-IP / per-endpoint quotas
- **`implement`** loading this pack

## Where limits live

**ASP.NET rate limiter** in the app (`AddRateLimiter` + endpoint/policy enablement) owns product quotas.

Gateway/WAF may add a coarse outer shield — don’t rely on it alone for authenticated per-user limits.

## Partitioning and algorithms

| Client | Partition |
|--------|-----------|
| Authenticated | **User id** (or stable subject) |
| Anonymous | **IP** — only with correct forwarded-headers / known proxy config |

Defaults: **fixed or sliding window** for simple quotas; **token bucket** when bursts matter. Tighter policies on auth, password reset, webhooks you don’t fully trust, expensive search, etc.

Don’t use IP-only limits for logged-in traffic behind shared NATs.

## Responses

- Exceeded → **429**
- Body: **Problem Details** (align with **`error-handling`**)
- Include **`Retry-After`** when the policy can compute it
- Document limits that clients must know → **`api-contracts`** / OpenAPI notes

## Exemptions

**Never** rate-limit liveness/readiness (`/alive`, `/health`) into deploy flaps (**`health-and-readiness`**).

Internal/admin bypass only behind real authz — not a secret query string.

## In-process vs distributed

- **Single instance:** in-process limiter is fine
- **Multi-instance / need global quotas:** shared store (e.g. Redis) — often via **`caching`** infra
- Store outage: prefer **fail-open** for availability unless the endpoint is abuse-critical — then fail-closed and **document** it. Don’t return opaque 500s without a chosen policy.

## Observability

Count throttled requests (metric). Avoid Error-logging every 429 (noise; quiet 4xx — **`observability`** / **`error-handling`**).

## Don't

- Don’t throttle health probes
- Don’t trust `X-Forwarded-For` from the open internet without a known proxy
- Don’t implement one-off counters in random handlers when a policy would do
- Don’t treat outbound HttpClient throttling as this skill (**`http-clients`** / vendor limits)

## References

- [`references/examples.md`](references/examples.md) — policy sketch + 429 note

## Related

- Problem Details → **`error-handling`**
- Probes → **`health-and-readiness`**
- Documented limits → **`api-contracts`**
