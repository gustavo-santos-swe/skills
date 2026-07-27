---
name: rn-animations
description: Use when adding Reanimated/Skia motion in React Native — Goose defaults; deep patterns may defer to mobile area skills.
disable-model-invocation: true
metadata:
  area: goose
---

# Animations

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Microinteractions, screen transitions, gesture-driven animation.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Stack
- Reanimated version assumptions; when Skia is allowed
- UI-thread work vs JS thread

### Defaults
- Duration/easing tokens; reduce-motion respect (→ accessibility)
- What we animate vs instant

### Align with
- Deep reference: `skills/mobile` animations / react-native-best-practices
- gestures skill for gesture-driven motion

## Don't
- Don't animate layout thrash on low-end without measuring.
- Don't ignore `prefers-reduced-motion` / reduce motion settings.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

