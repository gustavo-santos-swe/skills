---
name: web-metadata-and-seo
description: Use when setting Next.js Metadata API, Open Graph, sitemaps, robots, or JSON-LD.
metadata:
  area: goose
---

# Metadata and SEO

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Titles/descriptions, OG images, SEO routes.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Metadata API
- Per-route vs layout defaults; dynamic metadata
- OG/twitter images

### Discoverability
- `sitemap.ts` / `robots.ts`; canonical URLs
- Indexing rules for app vs marketing routes

### Align with
- routing-and-layouts; localization if i18n routes exist

## Don't
- Don't ship duplicate titles/descriptions across key pages.
- Don't noindex marketing pages by accident.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

