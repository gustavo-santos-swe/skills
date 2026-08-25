---
name: implement
description: Build a named ticket/plan batch (TDD at seams, full pack load, dirty tree until local review). Use for implement/build work - not planning, ticket split, or opening a PR.
metadata:
  area: goose
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

1. **Name the batch at start.** Soft default: one unblocked ticket or slice. Use a larger batch only if the engineer lists it.
2. **Create a feature branch before edits.** If you are on `main` or `master`, create or switch to a conventional branch (**git-practices** naming).
3. **Keep a dirty tree until local review.** Do not commit during the build. At the done bar, pause and ask for local review. Commit and push only after the engineer OKs. Then offer **git-practices** and later **pr-raise**. **pr-iterate** follows this same rule.
4. **Source of truth is a hard gate.** Re-read the cited contract or brief (or "open - frozen here"). If it is missing or unclear, stop and ask. On drift mid-build, follow **create-tickets** grounding (ask: update SoT, drift log, or addendum). Do not invent a fourth option.
5. **Load the whole active stack pack** before coding (see [Stack packs](#stack-packs)).
6. **Stay in this skill for the build.** Open a pull request only via **pr-raise** after review OK.

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
3. Loop: one failing test, then minimal code to pass, then the next test. Prefer behaviour through public interfaces, not private guts. The interface is the test surface (**codebase-design**).
4. Skip TDD only for glue both sides call out (rename, pure wiring, generated stubs). Say so explicitly.

Work vertical slices inside the batch (one test → code → next), not “all tests then all code.”

## Optional polish (simplify)

After the batch is green, if the change feels heavier than it should, do a **clarity pass on this batch only** before the review pause. Full rules: [`references/simplify.md`](references/simplify.md).

Short form: preserve behaviour and tests; match repo conventions; clarity over cleverness; no drive-by refactors; don’t strip seams that earn their keep (**codebase-design**). Skip when already clear or you don’t understand why the code is shaped that way yet.

## Steps

1. **Confirm batch** - ticket ids / plan headings / AC. Soft default one frontier slice.
2. **Grounding** - source of truth path or frozen open contract; implement-check and review-check from the ticket/plan. Stop if missing. Drift policy → **create-tickets** grounding.
3. **Branch** - feature branch if needed; still no commits.
4. **Load pack(s)** - full load as above.
5. **Agree seams** - TDD list (or explicit glue exception).
6. **Build** - red/green; run focused verifies often; honor pack rules and source of truth.
7. **Drift?** - pause; apply create-tickets drift ask.
8. **Optional polish** - if the batch is green but muddy, simplify per above (still dirty tree).
9. **Done bar** (before review ask):
   - Batch AC satisfied
   - Ticket/plan verify steps run (or note why N/A)
   - Run **`verify`** (gate) against loaded pack skills + source of truth. Drift blocks this step until you and the engineer decide (fix now / accept and log / ticket)
   - Goose voice on new/changed comments (`write-like-goose`)
10. **Pause for local engineer review** - show what changed (diff summary / paths) plus the `verify` verdict. Wait for OK before any commit/push.
11. **After they approve** - ask before **git-practices** (commit) then **pr-raise**. If they want changes, stay in implement (still dirty tree) until the next pause.

Stop when blocked, tests won’t go green after honest attempts, or scope shifts. Ask; don’t guess.

**Done when:** named batch meets the done bar and the engineer has been offered (or completed) local review - commits only after their OK.

## Self-check (diff)

Before the review pause, skim the branch diff:

- Matches batch AC and source of truth?
- No drive-by refactors outside the batch?
- Comments are why-only, Goose voice?

Rule-by-rule pack conformance is **`verify`**'s job, not a skim - run it, don't eyeball it. Deeper PR review stays in **pr-review** after open.

## References

- [`references/done-checklist.md`](references/done-checklist.md) - pause-for-review checklist
- [`references/simplify.md`](references/simplify.md) - optional clarity polish after green

## Related

- Split work → **create-tickets** (owns grounding / drift)
- Plan only → **planning**
- Pack conformance gate → **verify** (part of the done bar, not optional)
- After approve → **git-practices** → **pr-raise**
- Trust boundary gate → **security-check** (optional)
- Module shape → **codebase-design**
- Voice → **write-like-goose**
