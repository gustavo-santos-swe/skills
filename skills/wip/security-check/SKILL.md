---
name: security-check
description: Security pass on a change or PR — auth, secrets, input boundaries, dependency risk. Use when the ticket touches auth/PII/payments/public APIs, before shipping, or when the user says "security check", "secure this", "OWASP pass".
disable-model-invocation: true
metadata:
  area: wip
---

# Security Check

Status: **stub**.

Optional gate (not every ticket). Run when the change hits a trust boundary; otherwise skip.

Inspired by Addy Osmani `security-and-hardening` — tailor later to our stack (.NET / APIs / mobile).

## When to use

- Ticket/PR involves auth, sessions, tokens, secrets, PII, payments, file upload, or public HTTP APIs.
- User asks for a security pass before `pr-raise` / merge.
- After a security-related review comment.

## When not to

- Pure refactors with no trust-boundary change.
- Docs-only / copy-only changes.

## Steps (outline)

1. **Scope the boundary** — what crosses trust? (user input, authz, data at rest, outbound calls).
2. **Checklist pass** — secrets in diff? authz on new endpoints? validation at boundary? unsafe deserialization? SSRF/path traversal if relevant?
3. **Deps** — new packages: known issues / unexpected privilege?
4. **Report** — findings by severity (block / should-fix / fyi); no finding → explicit “no security blockers for this scope”.

## Next

Blockers → back to **implement**. Clean → **git-practices** / **pr-raise** (or **pr-iterate** if already in review).
