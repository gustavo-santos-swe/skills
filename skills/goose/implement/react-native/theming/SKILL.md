---
name: rn-theming
description: Use when adding dark mode, brand themes, or dynamic color schemes in a React Native / Expo app.
disable-model-invocation: true
metadata:
  area: goose
---

# Theming

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Light/dark mode, theme provider, system appearance.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Model
- Theme tokens shape; light/dark (and more?) 
- Follow system vs in-app toggle — persistence

### Implementation
- Provider placement; avoiding flash of wrong theme
- StatusBar / navigation theme sync

### Align with
- styling, accessibility (contrast)

## Don't
- Don't hardcode absolute colors outside tokens on product screens.
- Don't ignore contrast when inventing dark surfaces.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

