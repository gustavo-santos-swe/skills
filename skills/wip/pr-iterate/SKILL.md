---
name: pr-iterate
description: Handle PR feedback — verify comments, apply or push back, push fixes, re-request review. Use when the user says "iterate the PR", "address comments", "apply review feedback", or after pr-review leaves changes requested.
disable-model-invocation: true
metadata:
  area: wip
---

# PR Iterate

Status: **stub**.

Part of the `pr-*` family: **pr-raise** → **pr-review** → **pr-iterate**.

Author loop after review. Inspired by Superpowers `receiving-code-review`: verify before implementing; don't apply blindly.

## When to use

- PR has review comments / changes requested.
- User wants to respond to feedback and get back to review.

## Steps (outline)

1. **Read all feedback** without reacting.
2. **Triage** each item — apply / discuss / decline (with reason).
3. **Implement** agreed fixes (voice: `write-like-goose` on comments/commits).
4. **Push** and re-request review (or reply on declined items).

## Next

Back to **pr-review** (or done if approved).
