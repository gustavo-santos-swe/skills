---
name: rn-performance
description: Use when chasing JS/UI jank, TTI, re-renders, or bundle size in React Native / Expo.
disable-model-invocation: true
metadata:
  area: wip
---

# Performance

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Dropped frames, slow startup, re-render storms.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Measure
- Perf monitor, why-did-you-render, bundle analysis — our tools
- Evidence before micro-opts

### Hotspots
- Re-renders; lists; images; heavy JS on UI thread
- Bridge / JSI awareness (pointer to mobile best-practices)

### Budgets
- TTI / frame budgets if we define them

### Align with
- lists-and-virtualization, animations, `skills/mobile/react-native-performance`

## Don't
- Don't optimize cold paths blindly.
- Don't add memo everywhere without a measured re-render problem.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

