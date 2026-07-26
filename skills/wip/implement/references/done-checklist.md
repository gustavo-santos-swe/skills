# Implement - pause for local review

Use before asking the engineer to read the diff. Still **no commit / push**.

## Batch

- [ ] Named batch only (ticket ids / plan slices) - nothing extra snuck in
- [ ] Feature branch (not `main` / `master`)
- [ ] Working tree dirty on purpose - no commits yet

## Grounding

- [ ] Source of truth re-read (or open contract frozen in ticket/plan)
- [ ] Behaviour matches that source of truth
- [ ] If drift happened: engineer chose update / drift log / addendum; noted on ticket or plan

## Build quality

- [ ] Seams agreed; TDD loop used (or glue exception stated)
- [ ] Acceptance criteria for the batch pass
- [ ] Verify steps from ticket/plan run (or N/A with reason)
- [ ] Active pack(s): every `SKILL.md` was loaded before coding; self-check against those rules
- [ ] `write-like-goose` on comments / durable notes added

## Hand-off lines (chat)

- What batch finished
- Key paths touched
- How to run verifies
- Ready for **local review** - ask before **git-practices** / **pr-raise**
