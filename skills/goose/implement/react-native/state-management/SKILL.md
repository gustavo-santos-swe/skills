---
name: rn-state-management
description: Use when choosing or changing client state (server cache, Zustand/context, form state) in a React Native app.
disable-model-invocation: true
metadata:
  area: goose
---

# State Management

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Global store debates, cache vs UI state, prop drilling pain.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Layers
- Server/async state (TanStack Query / similar) vs client UI state
- Form state stays local when possible

### Global store
- When Zustand/context is allowed; what never goes global
- Persistence (secure vs async storage) — split with auth-and-secure-storage

### Patterns
- Selectors to limit re-renders; avoid mega-contexts

## Don't
- Don't put server entities only in a global store if we standardize on a query cache.
- Don't persist secrets in AsyncStorage (→ auth-and-secure-storage).

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

