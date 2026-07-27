---
name: web-localization
description: Use when adding Next.js i18n routing, dictionaries, or locale-aware formatting.
metadata:
  area: goose
---

# Localization

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Multi-language routes, next-intl/similar, locale switcher.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Routing
- Locale prefix strategy; default locale; detection
- Shared with marketing vs app

### Messages
- Dictionary layout; missing-key policy
- Format dates/numbers with locale; store invariant

### Align with
- metadata-and-seo (hreflang), routing-and-layouts

## Don't
- Don't localize logs/telemetry.
- Don't store locale-formatted values as source of truth.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

