# PR Template

Use this body when creating PRs with `gh pr create --body`.

```markdown
## Summary
- <1–3 bullets: what changed and why>
- <focus on the outcome for the user/reviewer, not the implementation>

## Test plan
- [ ] <concrete step to verify>
- [ ] <another step, if applicable>
```

## Rules

- **Summary:** 1–3 bullets. Each bullet = one change or clear reason.
- **Test plan:** checklist with actions the reviewer can repeat.
- For UI changes, add an optional section:

```markdown
## Screenshots
<describe what changed visually, or paste image if the user provided one>
```

## Example

**Title:** `feat(auth): add password reset flow`

**Body:**

```markdown
## Summary
- Add forgot-password endpoint and email template
- Reset link expires after 1 hour

## Test plan
- [ ] Request reset for existing user — email arrives
- [ ] Click link within 1h — password updates
- [ ] Click expired link — shows error page
- [ ] `npm test` passes
```

## What to avoid

- Long paragraphs in Summary
- "Test plan: tested locally" with no details
- Pasting the entire diff in the description
- Leaving Test plan empty
