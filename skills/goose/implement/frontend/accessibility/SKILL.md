---
name: web-accessibility
description: Use when improving web a11y in Next.js — semantics, focus, keyboard, and ARIA.
disable-model-invocation: true
metadata:
  area: goose
---

# Accessibility

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Keyboard traps, missing labels, focus on route change.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Basics
- Semantic HTML first; ARIA only when needed
- Focus management on navigations/modals

### Forms & errors
- Labels, errors tied via ids; live regions

### Testing
- axe / eslint-plugin-jsx-a11y; manual keyboard pass

## Don't
- Don't replace buttons with clickable divs.
- Don't ship modals without focus trap and Escape.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

