---
name: rn-accessibility
description: Use when improving VoiceOver/TalkBack labels, roles, focus order, or a11y checks in React Native.
disable-model-invocation: true
metadata:
  area: wip
---

# Accessibility

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Screen reader support, hit targets, reduce motion.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Basics
- Labels, roles, hints; decorative vs meaningful
- Minimum hit targets

### Navigation
- Focus order; announcing screen changes

### Motion & contrast
- Reduce motion; theme contrast (→ theming)

### Testing
- A11y props in RNTL; manual checklist devices

## Don't
- Don't ship icon-only controls without labels.
- Don't block font scaling unless there is a hard layout reason.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

