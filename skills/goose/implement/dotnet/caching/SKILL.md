---
name: caching
description: Use when adding or reviewing .NET caching — HybridCache, keys, TTLs, invalidation, stampede — or when implement loads the dotnet pack for cache work.
disable-model-invocation: true
metadata:
  area: goose
---

# Caching

Goose handbook for application-level caching in .NET backends.

**Target repo wins** if `IDistributedCache` / Redis helpers are already the house style (e.g. Monetis).

Voice: **`write-like-goose`**.

## When to use

- Speeding up repeated reads; shared cache across instances
- Invalidation after writes; stampede concerns
- **`implement`** loading this pack

## Default API (greenfield)

Prefer **`HybridCache`** as the app-facing cache API (L1 in-process + L2 distributed when configured).

| Need | Approach |
|------|----------|
| Multi-instance / shared | Configure HybridCache with a distributed store (typically **Redis**) |
| Single instance / pure process-local | HybridCache can still be L1-only — don’t invent a parallel cache façade |
| Legacy target | `IDistributedCache` / `IMemoryCache` OK if that’s what the repo already uses |

Don’t wrap Redis clients ad hoc in handlers when HybridCache (or the repo’s cache abstraction) exists.

Distributed store for rate-limit global quotas → often same Redis → **`rate-limiting`**.

## Keys and TTLs

- **Explicit, stable keys** — include user/tenant (or other principal) when the payload is scoped; never serve user A’s entry to user B
- Prefer **absolute** expiration; use sliding only when you mean “keep hot while used”
- TTL budgets live per feature in the target repo — short for volatile money/state, longer for slow reference data
- Serialize cached payloads deliberately (DTO/bytes) — don’t stash tracked EF entities

## Invalidation and stampede

- On mutation: **invalidate** (remove or bump version prefix) keys that would be wrong — don’t rely on TTL alone for write-heavy paths
- Prefer HybridCache **get-or-create / coalescing** so concurrent misses don’t stampede the DB
- Cache is **beside** the source of truth — DB (or upstream) remains authoritative
- Stale-window tolerance: document how wrong a read may be; if zero tolerance, don’t cache (or invalidate aggressively)

## Don't

- Don’t use cache as the system of record
- Don’t cache authorized/private data without varying the key by principal
- Don’t remember forever without a deliberate static-data reason
- Don’t ignore invalidation on writes “because TTL is 5 minutes”
- Don’t put secrets in cache keys or values

## References

- [`references/examples.md`](references/examples.md) — HybridCache sketch

## Related

- Options / Redis connection → **`configuration`** / **`dependency-injection`**
- Shared Redis for limits → **`rate-limiting`**
- Latency/alloc evidence → **`observability`** (metrics/traces); query cost → **`db-integration`** / **`database`**
