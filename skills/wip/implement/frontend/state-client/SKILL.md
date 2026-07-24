---
name: web-state-client
description: Use when adding client-only state (Zustand, context, URL state) in Next.js client islands.
disable-model-invocation: true
metadata:
  area: wip
---

# Client State

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Interactive widgets, cross-island state, URL as state.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Prefer
- Server state + URL searchParams before global client stores
- Local React state first

### Global client state
- When Zustand/context is justified
- Don't duplicate the server cache

### URL state
- nuqs or native searchParams — our preference

## Don't
- Don't hydrate a giant global store for static pages.
- Don't mirror RSC data into client state without a sync plan.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

