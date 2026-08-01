| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Every public Command/Query DTO has a matching `AbstractValidator<T>` | architecture-test | Layers — reflection: enumerate DTOs, assert a validator type exists for each |
| FluentValidation owns request shape (required fields, formats, ranges, cross-field); Domain owns real invariants that must hold for every entry point | verify | Layers |
| Run validation first in the handler; on failure → `ValidationFailed` → 422 Problem Details | verify | Timing and placement |
| Prefer sync, cheap rules in FluentValidation — no DB calls by default | verify | Timing and placement |
| Optional friendly uniqueness check in the handler → `Conflict` (409); always enforce with a DB unique constraint (race-safe) | verify | Uniqueness and I/O — see `database` skill for the matching DB-level regression test |
| Don't put `MustAsync` DB calls in every validator by default | verify | Uniqueness and I/O |
| Field-keyed errors in `ValidationFailed`; stable error codes on the failure case; no secrets/stack traces in messages | verify | Messages |
| Cross-field rules live in FluentValidation (`Must`/`When`); also enforce on the domain type if it's a lasting business invariant | verify | Cross-field rules |
| Validation is not authorization — never trust a client-supplied id as ownership proof | verify | Security |
| Don't rely on FluentValidation alone for domain invariants | verify | Don't |
| Don't use DataAnnotations as the primary request validation stack | verify | Don't |
| Don't return 500 for expected validation/conflict outcomes | verify | Don't |
