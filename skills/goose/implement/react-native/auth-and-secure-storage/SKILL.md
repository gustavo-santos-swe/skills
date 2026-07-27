---
name: rn-auth-and-secure-storage
description: Use when implementing login sessions, tokens, biometrics, or secure storage in React Native / Expo.
metadata:
  area: goose
---

# Auth and Secure Storage

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Auth flows, token refresh, storing secrets on device.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Session
- Token types; refresh strategy; logout everywhere
- Where session lives (memory + secure store)

### Storage
- SecureStore / Keychain vs AsyncStorage — what may go where
- Wipe on logout

### Biometrics / PIN
- When we offer; fallback paths

### Align with
- navigation (gates), security-check process skill, backend auth

## Don't
- Don't store refresh tokens in AsyncStorage/plaintext.
- Don't log tokens or PII.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

