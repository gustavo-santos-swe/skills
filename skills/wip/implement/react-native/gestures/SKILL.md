---
name: rn-gestures
description: Use when implementing pan/pinch/swipe/long-press or Gesture Handler patterns in React Native.
disable-model-invocation: true
metadata:
  area: wip
---

# Gestures

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Custom gestures, conflicting touch handlers, drawer/sheet gestures.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Stack
- RNGH + Reanimated integration rules
- Simultaneous / native gesture conflicts

### Patterns
- Sheets, dismiss-by-swipe, list vs horizontal pager fights

### Align with
- animations; deep reference in `skills/mobile` gestures skill

## Don't
- Don't attach competing gesture handlers without an exclusive/simultaneous plan.
- Don't break scroll with accidental `gestureHandler` capture.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

