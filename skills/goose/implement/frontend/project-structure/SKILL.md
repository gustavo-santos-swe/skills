---
name: web-project-structure
description: Use when laying out or changing a Next.js App Router repo (folders, feature modules, shared UI kit, or monorepo boundaries), or when implement loads the frontend pack for where code should live.
metadata:
  area: goose
---

# Project Structure

Goose defaults for Next.js App Router layout and **where UI lives**. Reuse rules and tokens live in **`styling`**. This skill owns folders and import boundaries.

**Target repo wins:** if the project already has a clear App Router layout, follow it unless the user asks to migrate.

Voice: **`write-like-goose`**. Target-repo `AGENTS.md` may override paths and names.

## When to use

- Scaffold, move routes or features, or add shared packages
- Decide kit vs feature component placement
- **`implement`** loading this pack

## When not to

- Variants, tokens, `DESIGN.md` gate → **`styling`**
- RSC vs client choice alone → **`server-and-client`**
- Route segment behavior alone → **`routing-and-layouts`**

## Monorepo placement

When the product also has a .NET (or other) backend — Monetis / Goose default:

| Surface | Path |
|---------|------|
| Next.js web | **`src/frontend/`** |
| .NET API | `src/backend/` (see **`solution-structure`**) |
| Expo / RN | `src/mobile/` when Mobile is in |

Do **not** put the Next app at repo-root `web/` beside a backend-only `src/`. Inside `src/frontend/`, use the app tree below (`src/frontend/src/app/…` when the package already uses a nested `src/`).

Standalone Next-only repos may keep the app at the package root; target repo wins.

## Default tree (inside the Next package)

Prefer a nested `src/` when the package already uses it. Otherwise keep the same root the package uses.

```
src/                   # inside src/frontend/ (or the Next package root)
  app/                 # routes, layouts, route handlers
  components/
    ui/                # shared kit primitives (Button, Input, …)
  features/            # optional: feature modules with local UI + logic
  lib/                 # shared non-UI helpers (cn, clients)
```

Small apps may skip `features/` and colocate under `app/`. Do not put kit primitives only under a single route folder.

## Kit vs feature UI

| Kind | Lives in | Examples |
|------|----------|----------|
| **Kit primitive** | `components/ui` (or repo kit path) | Button, Input, Dialog, Select |
| **Feature UI** | `features/<name>/` or next to the route | PricingTable, CheckoutForm shell |
| **Route files** | `app/` | `page.tsx`, `layout.tsx`, loading/error UI |

### Placement rules

1. If the control is a **role** (button, input, dialog) and will repeat, put it in the **kit**.
2. If the control is a **product composition** of kit pieces, keep it in the feature or route.
3. Do not grow a second informal kit inside `features/` (local `Button.tsx` that mirrors `ui/button`).
4. When **`styling`** says "add a kit primitive", add it under the kit path here.

## App Router notes

- Use route groups `(group)` for layout splits without URL segments.
- Keep route handlers under `app/api` (or the repo convention). Deep handler rules → **`route-handlers`**.
- Prefer feature folders for multi-file product slices. Prefer route colocation for tiny pages.

## Import boundaries

- Client components must not import server-only modules (`server-only`, private server libs).
- Kit primitives stay free of feature imports (no `components/ui` → `features/…`).
- Features may import kit + `lib`. Features must not import other features' internals without a shared extract.

## Tooling

- Path aliases (`@/`) owned with the repo TS config.
- ESLint / TS config ownership stays at repo root (or the package that already owns them).

## Don't

- Do not put everything under `components/`
- Do not hide a new kit role only under one feature folder
- Do not import server-only modules into client components
- Do not invent a monorepo package for one shared button
- Do not scaffold polyglot greenfield as root `web/` + backend-only `src/` — use `src/frontend/`

## References

- [`references/layout-sketch.md`](references/layout-sketch.md): example trees

## Related

- Reuse ladder, tokens, CVA → **`styling`**
- RSC / `'use client'` → **`server-and-client`**
- Routes and layouts → **`routing-and-layouts`**
