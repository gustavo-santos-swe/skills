---
name: rn-push-notifications
description: Use when adding Expo notifications, FCM/APNs, channels, or notification tap routing in React Native.
disable-model-invocation: true
metadata:
  area: goose
---

# Push Notifications

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Push opt-in, categories, open-from-notification.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Permissions
- When we ask; soft-ask UX; settings deep link

### Payload
- Shape we expect; localization; sensitive data rules
- Tap → navigation mapping

### Channels / importance (Android)
- Defaults we use

### Align with
- backend messaging; deep-linking for targets

## Don't
- Don't put secrets in push payloads.
- Don't spam push for events the user didn't opt into.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

