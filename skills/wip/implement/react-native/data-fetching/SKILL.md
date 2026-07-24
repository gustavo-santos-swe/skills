---
name: rn-data-fetching
description: Use when wiring API clients, TanStack Query/React Query, mutations, or offline-aware fetches in React Native.
disable-model-invocation: true
metadata:
  area: wip
---

# Data Fetching

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- New endpoints on mobile, loading/error UX, cache keys.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Client
- Fetch wrapper / OpenAPI client — base URL, auth headers, timeouts
- Error normalization shape

### Cache
- Query keys; staleTimes; invalidation after mutations
- Optimistic updates — when allowed

### UX states
- Loading / empty / error / retry patterns per screen type

### Align with
- offline-and-sync, auth-and-secure-storage, backend api-contracts

## Don't
- Don't fetch in random `useEffect` spaghetti if we standardize on a query library.
- Don't ignore cancellation / screen unmount.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

