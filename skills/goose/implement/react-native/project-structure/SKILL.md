---
name: rn-project-structure
description: Use when laying out or changing Expo/React Native folders, app entry, feature modules, or shared packages in a Goose mobile app.
disable-model-invocation: true
metadata:
  area: goose
---

# Project Structure

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- New app scaffold, moving screens/features, monorepo vs single app.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Layout
- Expo Router vs React Navigation-only — our default
- `app/` routes vs `src/features` — where screens, components, hooks live
- Shared UI / theme / api clients placement

### Boundaries
- Feature folders vs type folders — our rule
- What may import what (no circular feature deps)

### Native / config
- `app.json` / `app.config`; env flavors (dev/staging/prod)
- Expo SDK version pin policy

## Don't
- Don't dump every screen in one `components/` bucket.
- Don't mix web-only APIs into shared mobile modules without a platform split.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

