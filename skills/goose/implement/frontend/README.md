# frontend

Next.js (App Router) conventions for Goose web. Lives under **`implement`**.

Path: `skills/goose/implement/frontend/`. Preferred web stack: **Next.js**. Load from **`implement`** by concern.

**Filled:** `project-structure`, `styling` (reuse-first kit + `DESIGN.md` gate). Other skills in this pack are still stubs. Stubs list **Topics to fill**.

Backend APIs often live in [`../dotnet/`](../dotnet/); this pack is the **web tier**.

## Assumed craft skills (install upstream)

Visual craft is **not** owned here. Assume these are available when you ship UI:

| Skill | Role | Where |
|-------|------|--------|
| `frontend-design` | Distinctive UI, anti-slop | Vendored: [`../../../design/frontend-design/`](../../../design/frontend-design/) |
| `design-taste-frontend` | LP / marketing taste | Install upstream ([root README](../../../../README.md#favorite-frontend--design-skills-install-upstream--do-not-vendor)) |
| `impeccable` | Brand vs product, polish / `DESIGN.md` help | Install upstream (same README section) |

Optional finish/motion: Emil Kowalski pack, `anti-ui-slop` (same root list).

Goose owns structure and reuse (`project-structure`, `styling`). Load craft skills for look; do not copy their rules into this pack.

## Map

### Core
| Skill | Focus | Status |
|-------|--------|--------|
| [`project-structure`](./project-structure/) | App Router layout, kit vs feature UI | **filled** |
| [`server-and-client`](./server-and-client/) | RSC vs `'use client'` | stub |
| [`routing-and-layouts`](./routing-and-layouts/) | Routes, layouts, nav | stub |
| [`data-fetching`](./data-fetching/) | RSC fetch / waterfalls | stub |
| [`caching-and-revalidation`](./caching-and-revalidation/) | Tags, revalidate | stub |
| [`server-actions-and-forms`](./server-actions-and-forms/) | Actions + forms | stub |
| [`route-handlers`](./route-handlers/) | `app/api` / webhooks | stub |
| [`middleware`](./middleware/) | Edge gates / headers | stub |

### Product surfaces
| Skill | Focus | Status |
|-------|--------|--------|
| [`auth`](./auth/) | Sessions / protected routes | stub |
| [`styling`](./styling/) | Tokens, CVA, reuse ladder, `DESIGN.md` gate | **filled** |
| [`images-fonts-assets`](./images-fonts-assets/) | `next/image`, fonts | stub |
| [`metadata-and-seo`](./metadata-and-seo/) | Metadata / OG / sitemap | stub |
| [`error-loading-ui`](./error-loading-ui/) | `loading` / `error` / Suspense | stub |
| [`localization`](./localization/) | i18n routing / dictionaries | stub |
| [`state-client`](./state-client/) | Client islands state | stub |

### Quality
| Skill | Focus | Status |
|-------|--------|--------|
| [`env-and-config`](./env-and-config/) | Env boundaries | stub |
| [`typescript-conventions`](./typescript-conventions/) | TS / zod boundaries | stub |
| [`testing`](./testing/) | Vitest / RTL / Playwright | stub |
| [`performance`](./performance/) | CWV / bundles | stub |
| [`accessibility`](./accessibility/) | Web a11y | stub |
| [`security`](./security/) | XSS/CSP/headers | stub |

Out of scope here: Blazor, plain CRA without Next (add only if needed).
