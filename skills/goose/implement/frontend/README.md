# frontend

Next.js (App Router) conventions for Goose web. Lives under **`implement`**.

Path: `skills/goose/implement/frontend/`. Preferred web stack: **Next.js**. Load from **`implement`** by concern. Stubs list **Topics to fill**.

Visual craft may also pull [`../../../design/`](../../../design/) / frontend-design. Backend APIs often live in [`../dotnet/`](../dotnet/); this pack is the **web tier**.

## Map

### Core
| Skill | Focus |
|-------|--------|
| [`project-structure`](./project-structure/) | App Router layout |
| [`server-and-client`](./server-and-client/) | RSC vs `'use client'` |
| [`routing-and-layouts`](./routing-and-layouts/) | Routes, layouts, nav |
| [`data-fetching`](./data-fetching/) | RSC fetch / waterfalls |
| [`caching-and-revalidation`](./caching-and-revalidation/) | Tags, revalidate |
| [`server-actions-and-forms`](./server-actions-and-forms/) | Actions + forms |
| [`route-handlers`](./route-handlers/) | `app/api` / webhooks |
| [`middleware`](./middleware/) | Edge gates / headers |

### Product surfaces
| Skill | Focus |
|-------|--------|
| [`auth`](./auth/) | Sessions / protected routes |
| [`styling`](./styling/) | Tailwind / tokens |
| [`images-fonts-assets`](./images-fonts-assets/) | `next/image`, fonts |
| [`metadata-and-seo`](./metadata-and-seo/) | Metadata / OG / sitemap |
| [`error-loading-ui`](./error-loading-ui/) | `loading` / `error` / Suspense |
| [`localization`](./localization/) | i18n routing / dictionaries |
| [`state-client`](./state-client/) | Client islands state |

### Quality
| Skill | Focus |
|-------|--------|
| [`env-and-config`](./env-and-config/) | Env boundaries |
| [`typescript-conventions`](./typescript-conventions/) | TS / zod boundaries |
| [`testing`](./testing/) | Vitest / RTL / Playwright |
| [`performance`](./performance/) | CWV / bundles |
| [`accessibility`](./accessibility/) | Web a11y |
| [`security`](./security/) | XSS/CSP/headers |

Out of scope here: Blazor, plain CRA without Next (add only if needed).
