---
name: rn-styling
description: Use when styling React Native screens — StyleSheet, NativeWind/Uniwind, design tokens, or spacing/typography conventions.
disable-model-invocation: true
metadata:
  area: wip
---

# Styling

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- New UI styling, restyling a screen, choosing styling approach.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Approach
- StyleSheet vs NativeWind/Tamagui/etc. — our default
- Design tokens (color, space, type) — source of truth

### Patterns
- Variants / sizes; avoid one-off magic numbers
- Platform-specific styles (`Platform.select`) — when allowed

### Align with
- theming; aesthetic direction → `skills/mobile/react-native-design` + design area when needed

## Don't
- Don't invent a second spacing scale in one screen.
- Don't copy web CSS patterns that break on native (unless the stack explicitly supports them).

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

