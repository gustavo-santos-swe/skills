---
name: pr-iterate
description: Author loop on PR feedback: triage, fix, local review, then commit/push/reply/re-request. Use when addressing review comments or changes requested.
metadata:
  area: goose
---

# PR Iterate

Goose handbook for the **author loop** after review. Part of `pr-*`: **pr-raise** → **pr-review** → **pr-iterate**.

Voice: **`write-like-goose`**.

## When to use

- PR has review comments or “changes requested”
- User says “iterate the PR”, “address comments”, “apply review feedback”
- After **pr-review** left work for the author

## When not to

- No PR yet → **implement** / **pr-raise**
- First-pass review of someone else’s PR → **pr-review**
- Greenfield slice unrelated to feedback → **implement**

## Hard rules

1. **Triage before code.** Read every open thread. No edits until each item is **apply** / **ask** / **decline**. If anything is unclear, clarify those items before implementing the rest.
2. **Dirty tree until local review.** Same rule as **implement**: apply the agreed batch uncommitted → pause for engineer look → only then commit, push, reply, re-request.
3. **Size split for coding.** Small/mechanical fixes stay here. Larger than ~one vertical slice or new product behaviour → hand the named batch to **implement**, then return here for push/replies.
4. **Technical replies only.** What was happening, what changed, or the reason for not changing. No praise, no agreement ritual, no status opener. Shape in [Reply shape](#reply-shape).
5. **Human merges.** Re-request review; do not merge the PR from this skill.

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
| New behaviour, multi-layer slice, pack-heavy work | **implement** (name the batch; keep implement dirty-tree + review rules) |

While coding here:

- Drift / SoT → **create-tickets** grounding
- TDD at seams when the fix is behavioural (not pure glue)
- Load pack security/testing skills if the comment touches those concerns
- Goose voice on new comments

### 4. Pause for local review

When the apply batch is ready (still uncommitted):

- Summarise what changed (paths + intent)
- Wait for engineer OK before any commit/push

### 5. Commit, push, reply, re-request

After OK:

1. **git-practices** - conventional commits for the batch (ask before rewriting published history)
2. `git push` (force only if they ask)
3. **Thread replies** (shape below) - each handled item; declines can go earlier if discussion was needed pre-code
4. Re-request review / mark ready for review (MCP or `gh`)

### 6. Next

Back to **pr-review** (or human merge when approved). If new comments arrive, run this skill again.

**Done when:** triage settled, agreed applies landed (or routed), engineer reviewed the dirty tree, commits pushed, threads replied, review re-requested.

## Reply shape

Write the reply the way you would say it to the reviewer at your desk. Prose, one or two short paragraphs. Same facts in chat and on GitHub.

Open with what was actually happening in the code, in plain words. Then what you changed and why that closes it. Name a test or a file when it helps the reviewer verify, not as proof of work. GitHub already shows the commits, so a SHA is not a sentence.

**Applied:**

> The empty string was turning into null during binding, so the validator never saw it and the request fell into the release-everything path. I added `DisplayFormat(ConvertEmptyStringToNull = false)` to the property so a blank reaches the validator and gets a 400. There's a behavioral test hitting the endpoint with `ChannelAddress=` now.

**Declined:**

> I'd keep the retry on the worker. The webhook is already idempotent on `providerPaymentId`, and a webhook retry can capture twice when the provider marked it paid in between. If you'd rather have it on the webhook, I can add the unique index first.

**Ask:**

> Before I change this: do you want blank and omitted to mean the same thing here? Today omitted releases every email channel on the tier. If blank should do that too, the validator rule goes away and the docs change.

**Partly open:**

> Fixed the DELETE side: the detaching tier unlinks its own sub-account and it goes into retention when that was its last channel. What I couldn't solve here is the teardown, since the cron works off channels and this sub-account has none. That needs a sub-account sweep.

Not in a reply: status openers (`Confirmed.`, `Fixed.`, `Right on both counts.`), praise (`good catch`, `great point`, `thanks for checking`), agreement rituals (`you're right`), bullets, a SHA as the subject of a sentence. Agreement shows in the fix.

When you push the apply set, reply on declined threads too so nothing stays silent.

## References

- [`references/triage-template.md`](references/triage-template.md) - triage table + reply lines

## Related

- Reviewer side → **pr-review**
- Open PR → **pr-raise**
- Large fix batch → **implement** (owns dirty-tree rule)
- Drift / SoT → **create-tickets**
- Branch/commit shape → **git-practices**
