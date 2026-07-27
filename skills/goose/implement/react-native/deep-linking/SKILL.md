---
name: rn-deep-linking
description: Use when configuring Universal Links / App Links, Expo linking, or in-app deep link routing.
disable-model-invocation: true
metadata:
  area: goose
---

# Deep Linking

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Share links into screens, email magic links, deferred deep links.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Config
- Scheme / associated domains; Expo linking config
- Mapping URLs → routes (→ navigation)

### Security
- Signed/expiring links; don't trust open redirects
- Auth-gated deep links

### Testing
- How we verify links on iOS/Android

## Don't
- Don't deep-link into privileged screens without re-checking auth.
- Don't ship undocumented URL schemes.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

