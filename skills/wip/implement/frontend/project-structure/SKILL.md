---
name: web-project-structure
description: Use when laying out or changing a Next.js App Router repo — folders, feature modules, shared UI, or monorepo boundaries.
disable-model-invocation: true
metadata:
  area: wip
---

# Project Structure

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Scaffold, moving routes/features, shared packages.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### App Router layout
- `app/` segments; route groups; where features live (`src/features`?)
- `components/ui` vs feature components

### Boundaries
- What client components may import
- Shared package rules in monorepos

### Tooling
- ESLint/TS config ownership; path aliases

## Don't
- Don't put everything under `components/`.
- Don't import server-only modules into client components.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

