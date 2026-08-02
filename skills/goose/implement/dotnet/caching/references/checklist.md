| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Prefer `HybridCache` as the app-facing cache API; don't wrap Redis clients ad hoc when it already exists | verify | Default API |
| Cache keys are scoped per-principal — never serve user A's entry to user B | verify | Keys and TTLs — needs tracing the actual key-building logic per cache site |
| Prefer absolute expiration; use sliding only when you mean "keep hot while used" | verify | Keys and TTLs |
| Serialize cached payloads deliberately — don't stash tracked EF entities | verify | Keys and TTLs |
| On mutation, invalidate keys that would be wrong — don't rely on TTL alone for write-heavy paths | verify | Invalidation and stampede |
| Prefer `HybridCache` get-or-create/coalescing so concurrent misses don't stampede the DB | verify | Invalidation and stampede |
| Cache sits beside the source of truth — the DB (or upstream) remains authoritative | verify | Invalidation and stampede |
| Don't use cache as the system of record | verify | Don't |
| Don't remember forever without a deliberate static-data reason | verify | Don't |
| Don't put secrets in cache keys or values | verify | Don't |
