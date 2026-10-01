# PR iterate - triage + replies

## Triage table (chat, before code)

```markdown
## Triage - <repo>#<n>

| # | Comment (short) | Plan | Notes |
|---|-----------------|------|--------|
| 1 | … | apply | … |
| 2 | … | ask | … |
| 3 | … | decline | … |

**Apply here:** …
**Route to implement:** … (or none)
**Blocked on ask:** …
```

Wait for engineer confirmation before editing.

## After local review OK

1. Commit (conventional) → push  
2. Reply on threads  
3. Re-request review  

## Replies

One or two short paragraphs each, written as you'd say it to the reviewer. What was happening in the code, then what changed (or why not). Examples in the skill's [Reply shape](../SKILL.md#reply-shape).

| Plan | First sentence carries |
|------|------------------------|
| apply | what the code was doing wrong |
| decline | the reason it stays, for this codebase |
| ask | the decision the reviewer has to make, with the stake |
| already done | where it is already covered |

No `Fixed:` / `Confirmed.` openers, no SHA as a sentence, no praise, no bullets.
