---
name: web-routing-and-layouts
description: Use when adding Next.js routes, layouts, parallel/intercepting routes, or navigational UX.
disable-model-invocation: true
metadata:
  area: wip
---

# Routing and Layouts

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- New pages, nested layouts, modals as routes.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Conventions
- File names (`page`, `layout`, `template`, `default`)
- Route groups; when to use parallel/intercepting routes

### Navigation
- `Link` / `useRouter`; scroll & prefetch policy
- Auth-gated segments (→ auth, middleware)

### Align with
- metadata-and-seo, error-loading-ui

## Don't
- Don't duplicate chrome in every page when a layout fits.
- Don't overuse intercepting routes for simple modals unless we standardize on them.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

