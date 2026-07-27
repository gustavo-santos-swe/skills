---
name: web-data-fetching
description: Use when fetching data in Next.js — RSC fetch, cache options, Suspense, or client queries.
metadata:
  area: goose
---

# Data Fetching

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- New data on a page, waterfalls, cache confusion.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Server fetch
- `fetch` cache defaults we rely on; `cache` / `next.revalidate` / `tags`
- Direct DAL / DB access from server vs HTTP-to-ourselves

### Waterfalls
- Compose in one server tree; avoid request waterfalls
- `Promise.all` / deferred streaming patterns

### Client fetch
- When TanStack Query on client is allowed (highly interactive islands)

### Align with
- caching-and-revalidation, server-and-client

## Don't
- Don't call our own public HTTP routes from RSC when a DAL works.
- Don't cache personalized data as static.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

