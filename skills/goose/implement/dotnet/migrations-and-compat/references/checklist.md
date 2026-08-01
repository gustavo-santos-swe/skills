| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Migrations live in Infrastructure (or the agreed persistence project); generate with EF tools, don't hand-author opaque diffs | verify | EF hygiene |
| An already-applied migration file is never edited after the fact — add a new migration instead | regression-test | EF hygiene — snapshot/hash comparison of `Migrations/` against the base branch |
| Don't squash/rewrite migration history that has left the developer laptop | verify | EF hygiene |
| Production/CD uses an explicit apply step (e.g. `dotnet ef database update` in the pipeline); don't rely on `Database.Migrate()` on first-instance startup under scale-out | verify | Apply |
| Expand → deploy dual-read/write app → backfill → contract, correctly sequenced across rolling deploys | verify | Expand/contract — requires reasoning about rolling-deploy timing across releases |
| Never run destructive contract steps before backfill completes | verify | Expand/contract |
| Reference/seed data uses a dedicated migration or an idempotent seed path — not one-off prod fixes buried in unrelated migrations | verify | Seed data |
| Don't auto-migrate on startup as the prod strategy | verify | Don't |
| Don't drop/rename columns in one step when old binaries are still live | verify | Don't |
| Don't point migrate at the wrong database "to save time" | verify | Don't |
