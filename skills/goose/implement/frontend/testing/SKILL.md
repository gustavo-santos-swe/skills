---
name: web-testing
description: Use when writing Next.js/React tests — Vitest/Jest, Testing Library, Playwright.
disable-model-invocation: true
metadata:
  area: goose
---

# Testing

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Component tests, RSC testing strategy, E2E smoke.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Pyramid
- Unit/RTL vs Playwright — what each change needs
- How we test Server Actions / handlers

### Tooling
- Vitest vs Jest; MSW for APIs
- Playwright smoke paths

### Align with
- TDD process skills

## Don't
- Don't only E2E pure UI logic.
- Don't mock away the authz check you're supposed to verify.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

