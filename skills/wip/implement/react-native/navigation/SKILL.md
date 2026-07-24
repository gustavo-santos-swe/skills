---
name: rn-navigation
description: Use when adding or changing Expo Router / React Navigation stacks, tabs, modals, or auth gates in React Native.
disable-model-invocation: true
metadata:
  area: wip
---

# Navigation

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- New routes, nested navigators, protected screens, linking config.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Router choice
- Expo Router file conventions we follow
- Stacks / tabs / drawers — when each

### Auth & gates
- Redirect unauthenticated users — where enforced
- Deep link into protected routes

### Params & state
- Typed routes/params; what belongs in params vs global state
- Modal vs push presentation

### Align with
- deep-linking, auth-and-secure-storage

## Don't
- Don't navigate with magic string routes if we have typed routes.
- Don't put heavy business state only in navigation params.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

