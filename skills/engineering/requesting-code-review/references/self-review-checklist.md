# Self-Review Checklist

Use this when running `requesting-code-review` on your own work.

## What to Check

**Plan alignment:**
- Does the implementation match the plan / requirements?
- Are deviations justified improvements, or problematic departures?
- Is all planned functionality present?

**Code quality:**
- Clean separation of concerns?
- Proper error handling?
- Type safety where applicable?
- DRY without premature abstraction?
- Edge cases handled?

**Architecture:**
- Sound design decisions?
- Reasonable scalability and performance?
- Security concerns?
- Integrates cleanly with surrounding code?

**Testing:**
- Tests verify real behavior, not mocks?
- Edge cases covered?
- Integration tests where they matter?
- All tests passing?

**Production readiness:**
- Migration strategy if schema changed?
- Backward compatibility considered?
- Documentation complete?
- No obvious bugs?

## Output Format

```markdown
### Strengths
[What's well done? Be specific with file:line.]

### Issues

#### Critical (Must Fix)
[Bugs, security, data loss, broken functionality]

#### Important (Should Fix)
[Architecture problems, missing features, test gaps]

#### Minor (Nice to Have)
[Style, polish, non-blocking improvements]

For each issue: file:line, what's wrong, why it matters, how to fix.

### Assessment

**Ready for PR?** [Yes | No | With fixes]

**Reasoning:** [1-2 sentences]
```

## Calibration

- Categorize by actual severity — not everything is Critical
- Acknowledge strengths before listing issues
- Flag intentional deviations from the plan explicitly
- Give a clear verdict — don't hedge
