---
name: rn-forms-and-inputs
description: Use when building React Native forms, text inputs, keyboard handling, or client-side validation UX.
disable-model-invocation: true
metadata:
  area: wip
---

# Forms and Inputs

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Login/settings forms, keyboard avoiding, pickers.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Form stack
- Library (React Hook Form + zod?) — our default
- Controlled vs uncontrolled inputs

### Keyboard
- KeyboardAvoidingView / avoiding view strategy per platform
- Next-field focus; submit on enter

### Validation UX
- When to validate; error placement; align with API errors

### Align with
- data-fetching (submit), accessibility (labels)

## Don't
- Don't fight the keyboard with random `paddingBottom` hacks as the only strategy.
- Don't block submit without accessible error text.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

