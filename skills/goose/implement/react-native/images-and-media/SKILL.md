---
name: rn-images-and-media
description: Use when loading images, picking photos/files, or playing media in React Native / Expo.
metadata:
  area: goose
---

# Images and Media

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Avatars, galleries, image picker, video/audio basics.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Images
- Fast image / Expo Image — our default
- Sizing, caching, placeholders, blurhash
- Remote vs bundled assets

### Picker / camera
- Permissions; compression; HEIC handling
- Upload handoff (→ backend file-storage)

### Align with
- lists-and-virtualization (cells), performance

## Don't
- Don't load full-resolution images into tiny thumbnails.
- Don't block the JS thread encoding huge assets on the UI path.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

