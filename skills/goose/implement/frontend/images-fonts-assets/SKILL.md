---
name: web-images-fonts-assets
description: Use when configuring next/image, next/font, static assets, or remote image patterns in Next.js.
metadata:
  area: goose
---

# Images, Fonts, and Assets

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Hero images, font loading, remote image hosts.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Images
- `next/image` defaults; sizes/remotePatterns
- Priority / LCP images

### Fonts
- `next/font` setup; subsetting; CLS avoidance

### Static assets
- `public/` vs imported assets; cache headers assumptions

## Don't
- Don't use raw `<img>` for LCP heroes without a reason.
- Don't host unbounded remote image domains in `remotePatterns`.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

