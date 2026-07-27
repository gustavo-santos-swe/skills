# Smell baseline (Guidelines axis)

Judgement-call heuristics from Fowler (*Refactoring*, ch. 3). Use on the **diff**, not the whole repo.

**Rules that bind:**

1. **Repo wins.** Documented project standards override this list.
2. **Always a judgement call.** Label as a possible smell, never a hard Block by itself.
3. **Skip tooling.** Anything CI/analyzers already enforce stays out of the review.

| Smell | What it is | Typical fix |
|-------|------------|-------------|
| Mysterious Name | Name hides what it does/holds | Rename; if no honest name, design is murky |
| Duplicated Code | Same logic shape in more than one hunk | Extract shared shape |
| Feature Envy | Method reaches into another object's data more than its own | Move toward the data |
| Data Clumps | Same few fields/params travel together | Bundle into a type |
| Primitive Obsession | Primitive standing in for a domain concept | Small dedicated type |
| Repeated Switches | Same switch/cascade on one type across the change | Polymorphism or one shared map |
| Shotgun Surgery | One logical change scatters across many files | Gather what changes together |
| Divergent Change | One module edited for unrelated reasons | Split by reason-to-change |
| Speculative Generality | Abstraction for needs the spec doesn't have | Delete until a real need |
| Message Chains | Long `a.b().c().d()` the caller shouldn't know | Hide behind one method |
| Middle Man | Mostly delegates onward | Call the real target |
| Refused Bequest | Subclass ignores most of what it inherits | Prefer composition |

**How to report:** under Guidelines, name the smell, quote the hunk, keep it Should-fix or Nit unless it also fails Correctness/Spec.
