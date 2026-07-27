---
name: implement
description: Build a named ticket/plan batch (TDD at seams, full pack load, dirty tree until local review). Use for implement/build work - not planning, ticket split, or opening a PR.
disable-model-invocation: true
metadata:
  area: wip
---

# Implement

Goose handbook for **building** after planning/tickets (or a small clear change).

Voice: **`write-like-goose`**.

## When to use

- Unblocked ticket(s) or plan slice(s) ready to build
- Small clear change that skipped formal tickets
- User says “implement”, “build this”, “do the ticket”

## When not to

- Design still open → **brainstorm** / **research**
- Need an ordered plan first → **planning**
- Multi-slice split not done → **create-tickets**
- Failure / flake without a clear fix path → **diagnose**
- Engineer already approved the diff and wants history/PR → **git-practices** / **pr-raise**

## Hard rules

1. **Name the batch at start.** Soft default: one unblocked ticket/slice. Larger batches only if the engineer lists them.
2. **Feature branch before edits.** If on `main`/`master`, create/switch to a conventional branch (**git-practices** naming).
3. **Dirty tree until local review (canonical).** No commits during the build. At the done bar, pause and ask for local review. **Commit/push only after the engineer OKs.** Then offer **git-practices** (commit) and later **pr-raise**. Other skills that build mid-PR (**pr-iterate**) follow this same rule.
4. **Source of truth is a hard gate.** Re-read the cited contract/brief (or “open - frozen here”). If missing/unclear, stop and ask. On drift mid-build, follow **create-tickets** grounding (ask: update SoT | drift log | addendum) - do not invent a fourth option.
5. **Load the whole active stack pack** before coding (see [Stack packs](#stack-packs)).
6. **Stay in this skill for the build.** Open a PR only via **pr-raise** after review OK.

## Stack packs

Pick the pack(s) for the work. Persistence often needs **both** `database` and `dotnet/db-integration`.

| Pack | Path |
|------|------|
| Data / DB (language-agnostic) | [`database/`](./database/README.md) |
| .NET / C# | [`dotnet/`](./dotnet/README.md) |
| React Native / Expo | [`react-native/`](./react-native/README.md) |
| Frontend / Next.js | [`frontend/`](./frontend/README.md) |

**Load rule (literal):** before writing feature code, read the pack `README` **and every** `SKILL.md` under that pack (and under a second pack if both apply). Context cost is accepted so pack rules aren’t skipped.

If a new concern appears mid-slice that belongs to another pack, load that pack the same way before continuing.

## TDD

**Red → green at agreed seams by default.**

1. At batch start, list seams under test (public boundaries: HTTP contract, domain API, UI behaviour, etc.).
2. Confirm with the engineer if unclear. No tests at unconfirmed seams.
3. Loop: one failing test → minimal code to pass → next test. Prefer behaviour through public interfaces (not private guts).
4. Skip TDD only for glue both sides call out (rename, pure wiring, generated stubs). Say so explicitly.

Work vertical slices inside the batch (one test → code → next), not “all tests then all code.”

## Steps

1. **Confirm batch** - ticket ids / plan headings / AC. Soft default one frontier slice.
2. **Grounding** - source of truth path or frozen open contract; implement-check and review-check from the ticket/plan. Stop if missing. Drift policy → **create-tickets** grounding.
3. **Branch** - feature branch if needed; still no commits.
4. **Load pack(s)** - full load as above.
5. **Agree seams** - TDD list (or explicit glue exception).
6. **Build** - red/green; run focused verifies often; honor pack rules and source of truth.
7. **Drift?** - pause; apply create-tickets drift ask.
8. **Done bar** (before review ask):
   - Batch AC satisfied
   - Ticket/plan verify steps run (or note why N/A)
   - Self-check against loaded pack skills + source of truth
   - Goose voice on new/changed comments (`write-like-goose`)
9. **Pause for local engineer review** - show what changed (diff summary / paths). Wait for OK before any commit/push.
10. **After they approve** - ask before **git-practices** (commit) then **pr-raise**. If they want changes, stay in implement (still dirty tree) until the next pause.

Stop when blocked, tests won’t go green after honest attempts, or scope shifts. Ask; don’t guess.

**Done when:** named batch meets the done bar and the engineer has been offered (or completed) local review - commits only after their OK.

## Self-check (diff)

Before the review pause, skim the branch diff:

- Matches batch AC and source of truth?
- Pack rules respected?
- No drive-by refactors outside the batch?
- Comments are why-only, Goose voice?

Deeper PR review stays in **pr-review** after open.

## References

- [`references/done-checklist.md`](references/done-checklist.md) - pause-for-review checklist

## Related

- Split work → **create-tickets** (owns grounding / drift)
- Plan only → **planning**
- After approve → **git-practices** → **pr-raise**
- Trust boundary gate → **security-check** (optional)
- Voice → **write-like-goose**
