---
name: web-server-and-client
description: Use when deciding RSC vs client components, `'use client'` boundaries, or shipping JS to the browser in Next.js.
disable-model-invocation: true
metadata:
  area: goose
---

# Server and Client

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- New component, hydration issues, accidental client bundles.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Default
- Server Components by default; client only for interactivity/state/effects
- Where the `'use client'` boundary sits (leaf vs root)

### Data & secrets
- Secrets only on server; never leak via RSC props accidentally
- Serializing props across the boundary

### Patterns
- Composition: server wrapper + client island

## Don't
- Don't sprinkle `'use client'` on layouts “just in case.”
- Don't pass non-serializable props (functions, class instances) into client children from server parents.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

