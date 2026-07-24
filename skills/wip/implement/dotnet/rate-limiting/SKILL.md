---
name: rate-limiting
description: ASP.NET rate limiting, quotas, and abuse controls. Use when adding or changing request throttles, per-user/IP limits, or 429 behavior on .NET APIs.
disable-model-invocation: true
metadata:
  area: wip
---

# Rate Limiting

Status: **stub** — topic list below is what to define later. Keep SKILL.md short; deep samples → `references/`.

## When to use

- Throttling public or sensitive endpoints; quotas per user/tenant/API key; abuse protection.
- **`implement`** loading this pack when designing or reviewing limits.

## Topics to fill (checklist)

### Policy design
- What we limit (global, per-IP, per-user, per-endpoint)
- Algorithms (fixed window, sliding, token bucket, concurrency) — defaults
- Limits for anonymous vs authenticated

### ASP.NET integration
- Built-in rate limiting middleware vs gateway/WAF — where the source of truth lives
- Partition keys; how we identify the client
- `429` + `Retry-After` / ProblemDetails shape (→ error-handling, endpoint-conventions)

### Distributed vs in-process
- Single-instance limits vs Redis/distributed — when required
- Align with caching (shared store) and resilience (clients backing off)

### Exemptions
- Health probes (→ health-and-readiness) must not be throttled into false unhealthy
- Internal/admin bypass — how gated

### Observability
- Metrics for throttled requests; logs without PII spam

### Align with
- security (authn before or with limit?), api-contracts (document limits), http-clients (outbound isn’t this skill)

## Don't

- Don't rate-limit readiness/liveness into deployment flaps.
- Don't use only IP limits behind a reverse proxy without trusting `X-Forwarded-For` correctly.
- Don't return 500 when the limit store is down without an explicit fail-open/fail-closed policy.

## References

Optional: `references/` for policy samples. Concrete limit numbers often live per-service in the target repo.
