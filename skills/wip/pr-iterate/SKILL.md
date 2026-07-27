---
name: pr-iterate
description: Handle PR review feedback - triage all comments first, apply or decline with reasons, fix small items (or hand large scope to implement), dirty tree until local engineer review, then commit/push/reply/re-request. Use when addressing PR comments, changes requested, or iterating after pr-review.
disable-model-invocation: true
metadata:
  area: wip
---

# PR Iterate

Goose handbook for the **author loop** after review. Part of `pr-*`: **pr-raise** → **pr-review** → **pr-iterate**.

Voice: **`write-like-goose`** on comments, commits, and durable notes.

## When to use

- PR has review comments or “changes requested”
- User says “iterate the PR”, “address comments”, “apply review feedback”
- After **pr-review** left work for the author

## When not to

- No PR yet → **implement** / **pr-raise**
- First-pass review of someone else’s PR → **pr-review**
- Greenfield slice unrelated to feedback → **implement**

## Hard rules

1. **Triage before code.** Read every open thread. No edits until each item is **apply** / **ask** / **decline**. If anything is unclear, stop and clarify those items before implementing the rest.
2. **Dirty tree until local engineer review.** Same as **implement**: apply the agreed batch uncommitted → pause for their look → only then commit, push, reply, re-request.
3. **Size split for coding.** Small/mechanical fixes stay here. Larger than ~one vertical slice or new product behaviour → hand the named batch to **implement**, then return here for push/replies.
4. **No performative agreement.** No “great point”, “thanks for catching”, “you’re absolutely right.” Technical restatement, fix, or reasoned decline.

## Steps

### 1. Fetch feedback

Identify the PR (URL, number, or current branch). Load review threads + CI via GitHub MCP or `gh` (same discovery order as **pr-raise**). Read **all** comments without reacting.

### 2. Triage (required table)

Present a short triage to the engineer before coding:

| # | Thread / ask | Plan | Notes |
|---|--------------|------|--------|
| 1 | … | apply / ask / decline | … |

- **apply** - will change code (or already satisfied - say so)
- **ask** - need clarification; block coding that depends on it
- **decline** - won’t do; technical reason ready for the reply

Order applies later: blockers/security first, then simple fixes, then larger ones (or route large to **implement**).

Get explicit go-ahead on the triage (especially declines and asks).

### 3. Build the apply set

| Scope | Where |
|-------|--------|
| Typo, null check, small test, localised authz fix, reply-only | **This skill** |
| New behaviour, multi-layer slice, pack-heavy work | **implement** (name the batch; keep dirty-tree + review rules) |

While coding here:

- Honor source of truth / drift ask from the ticket or PR (same three options as **create-tickets** / **implement**)
- TDD at seams when the fix is behavioural (not pure glue)
- Load pack security/testing skills if the comment touches those concerns
- `write-like-goose` on new comments

### 4. Pause for local review

When the apply batch is ready (still uncommitted):

- Summarise what changed (paths + intent)
- **Do not** commit or push yet
- Wait for engineer OK

### 5. Commit, push, reply, re-request

After OK:

1. **git-practices** - conventional commits for the batch (ask before rewriting published history)
2. `git push` (no force unless they ask)
3. **Thread replies** (template below) - each handled item; declines can go earlier if discussion was needed pre-code
4. Re-request review / mark ready for review (MCP or `gh`). Don’t merge.

### 6. Next

Back to **pr-review** (or human merge when approved). If new comments arrive, run this skill again.

## Reply shape

Keep short. Same facts in chat and on GitHub.

**Applied:**

```text
Fixed: <what>. <path or test name if useful>.
```

**Declined:**

```text
Not applying: <reason for this codebase>. <alternative if any>.
```

**Ask:**

```text
Need clarify before changing: <question>.
```

## Don't

- Don’t implement before triage is settled
- Don’t commit/push before local engineer review
- Don’t swallow large scope inside “address comments” - use **implement**
- Don’t merge the PR
- Don’t thank / flatter the reviewer in thread replies
- Don’t leave declined threads unanswered when you push the rest

## References

- [`references/triage-template.md`](references/triage-template.md) - triage table + reply lines

## Related

- Reviewer side → **pr-review**
- Open PR → **pr-raise**
- Large fix batch → **implement**
- Branch/commit shape → **git-practices**
