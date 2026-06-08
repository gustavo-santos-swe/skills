---
name: triage-bug
description: Take a raw bug report and turn it into a clean, prioritized ticket with a title, repro steps, and severity. Use when the user says "triage this", pastes a support escalation, or asks "what's this bug".
metadata:
  area: operations
license: MIT
---

# Triage Bug

Convert a noisy bug report into a ticket someone can act on: one-line title, repro steps, severity, area.

## When to use

- Support escalates a bug.
- A teammate dumps a Slack thread or screenshot.
- The user says "triage this" or "what's this bug".

## Steps

1. **Re-read the report once, in full.** Don't start writing yet.
2. **Restate the symptom** in one sentence as a user would say it. No internal jargon.
3. **Pull out repro steps** even if the original report doesn't separate them. Number them 1, 2, 3.
4. **Note the gap** between expected and actual.
5. **Decide severity** with this rubric:
   - **S1** — production down, data loss, or security issue.
   - **S2** — common path broken, no workaround.
   - **S3** — broken with workaround.
   - **S4** — cosmetic / rare path.
6. **Identify the area** (one of: editor, billing, auth, api, infra, marketing).

## Output format

```markdown
## Title
<one line, present tense, no "bug:" prefix>

## Severity
S2

## Area
billing

## Repro
1. ...
2. ...
3. ...

## Expected vs actual
- Expected: ...
- Actual: ...

## Notes
- URLs, screenshots, affected user IDs.
```

## Don't

- Don't open with "I think the issue is..." — the title goes first.
- Don't skip severity. Every ticket gets one, even if it's a guess.
- Don't paste raw stack traces into the title. Summarize.
