---
name: rn-testing
description: Use when writing or structuring React Native / Expo tests (Jest, RNTL, Maestro/Detox).
metadata:
  area: goose
---

# Testing

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Unit/component tests, E2E smoke, testing providers.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Pyramid
- Unit vs RNTL vs E2E — what each change requires
- Providers/wrappers for tests

### Tooling
- Jest + RNTL defaults; Maestro/Detox — when
- Mocking navigation, secure store, netinfo

### Align with
- TDD process skills; don't duplicate process here

## Don't
- Don't rely only on E2E for pure logic.
- Don't snapshot entire screens as the only assertion strategy.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

