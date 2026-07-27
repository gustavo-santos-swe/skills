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

## Reply one-liners

| Plan | Reply |
|------|--------|
| apply | `Fixed: <what>. <where>.` |
| decline | `Not applying: <technical reason>.` |
| ask | `Need clarify before changing: <question>.` |
| already done | `Already covered by <path/commit> - no further change.` |

No thanks, no “great point”, no “you’re right.”
