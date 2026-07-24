---
name: rn-native-modules
description: Use when adding Expo modules, config plugins, or custom native iOS/Android code to a React Native app.
disable-model-invocation: true
metadata:
  area: wip
---

# Native Modules

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Missing native capability, config plugins, eject pressure.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Preference order
- Expo SDK module → config plugin → custom native module
- When we allow CNG / prebuild customizations

### Discipline
- Keep native surface minimal; document upgrade cost
- Versioning with Expo SDK upgrades

## Don't
- Don't add custom native code when an Expo module exists.
- Don't fork React Native core casually.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

