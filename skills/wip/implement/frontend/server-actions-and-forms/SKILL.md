---
name: web-server-actions-and-forms
description: Use when implementing Next.js Server Actions, progressive forms, or progressive enhancement for mutations.
disable-model-invocation: true
metadata:
  area: wip
---

# Server Actions and Forms

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Form posts, mutations from RSC, useActionState/useFormStatus.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Actions
- When Server Actions vs Route Handlers
- Input validation (zod); authz inside the action
- Return shape / error model (→ error-loading-ui)

### Forms
- Progressive enhancement expectations
- Pending UI; idempotency

### Security
- Origin / CSRF posture for actions; never trust client fields for authz

## Don't
- Don't skip server-side validation because the client validated.
- Don't perform privileged writes without authz in the action.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

