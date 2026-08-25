# Research: LLM answer structure (community skills)

**Date:** 2026-08-17
**Status:** lean

## Question

What should Goose steal from community “write better answers” skills so replies stay scannable, keep meaning, and pick a structure from the job (list vs prose vs steps), without another overloaded rule pile?

Success: enough to pick among (A) keep write-like-goose as-is, (B) add a thin shape-picker, (C) absorb another upstream skill wholesale.

## Options

- A — Keep current write-like-goose (prose + Procedure + Question). No new structure layer.
- B — Add a short shape-picker: four jobs, four shapes. Steal the “never cut a condition” line. Do not import STE caps or a costume.
- C — Replace the voice skill with one upstream (hyperfocus, attention-control, or i-have-adhd).

## Findings

Community work clusters into four jobs. Most “weird” skills pick one job and apply it to every reply.

### Shape / act (how-tos)

1. [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) — 10 rules: action first, numbered steps, one next move, restate state, list cap 5, no closers. Viral (~20k stars). Overrides when the user asks to explain. ([SKILL.md](https://github.com/ayghri/i-have-adhd/blob/main/skills/i-have-adhd/SKILL.md))
2. [alexgreensh/attention-span](https://github.com/alexgreensh/attention-span) — Attention-kind: `→` + bold, fully answers, go-deep suspends brevity. Measured shorter output; coding pass rate unchanged. Costume is the `→`.
3. [aaddrick/attention-control](https://github.com/aaddrick/attention-control) — i-have-adhd shape + STE language. Explicit: “A rule never removes a fact, a number, a condition, or a scope qualifier.”
4. [shubhamV123/crisp](https://github.com/shubhamV123/crisp) — Finding → fix → next. Fragments OK. Suspends terseness for safety. Can go telegram.

### Structure / scan (not fewer words)

5. [nextor2k/hyperfocus](https://github.com/nextor2k/hyperfocus) — “Not fewer words — better structure.” Answer first, short chunks, **lists over walls**. Modes: Clean (terse), Flow (What → Why → How), Zen (TL;DR + lists/tables). Cites [W3C COGA](https://www.w3.org/TR/coga-usable/) for front-loading.
6. [Marksooxx/plain-speak](https://github.com/Marksooxx/plain-speak) — Mined from real transcripts. Failures were decision moments with missing stakes, not jargon. Decision items are **paragraphs** (who / what happens / cost of nothing / options / rec), not one-line bullets. “Don’t cut by word count, cut by priority.” Compression in the last quarter of an answer caused “what does that mean?”
7. [Google developer tone](https://developers.google.com/style/tone) — Conversational, not a costume. Lists for sequences and parallel items. Personality without entertainment.

### Language / anti-slop (can over-cut)

8. [L1nefeed ASD-STE100 gist](https://gist.github.com/L1nefeed/4164ecaaf77879e76dca3c06f142f1c2) — 20/25 word caps, one word one meaning, synonym bans. Also: “Accuracy always wins. Never remove a fact, a condition, a number, or a scope qualifier.” Numbered list for 3+ steps; bullets for 3+ parallel items. Do not bury a sequence in one sentence.
9. [AminBlg/SimpleEnglish](https://github.com/AminBlg/SimpleEnglish/blob/main/skills/simple-english/SKILL.md) — 53 STE rules, pragmatic vs strict modes. Heavy. Built for manuals, not chat.
10. [toppa STE gist](https://gist.github.com/toppa/bf7ff49d6fc44fd4fc3337248f8f2a7e) — Same family. “Length is not terseness. Caps apply to each sentence, not the response.”
11. [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) — Cut filler, break formulaic structures, vary rhythm. Voice, not layout. Catalogs grow and the model over-applies.
12. [shaswatco/anti-ai-writing-style](https://github.com/shaswatco/anti-ai-writing-style) — Stance, rhythm, physical verbs. Large ban list.
13. [yzhao062/agent-style](https://github.com/yzhao062/agent-style) — RULE-A: do not bullet prose that is not a list. Over-bulleting is itself an AI tell.
14. [softaworks writing-clearly-and-concisely](https://github.com/softaworks/agent-toolkit/tree/main/skills/writing-clearly-and-concisely) — Strunk: omit needless words, positive form. Warns against “formatting overuse: excessive bullets, emoji, bold on every other word.”
15. [carlosduplar/caveman](https://github.com/carlosduplar/caveman-output-style-claude-code) — Drop articles, fragments. Token savings. Same failure mode as old Goose caps.

### Official / classic (not skills, still primary)

16. [ASD-STE100](https://www.asd-ste100.org/) — Aerospace controlled language. Safe for procedures. Wrong as a chat law.
17. [Orwell, Politics and the English Language](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/) — Short word, cut needless, active, break the rule before you say something stupid.
18. [W3C COGA](https://www.w3.org/TR/coga-usable/) — Front-load the point. ADHD / tired readers may not reach the end.

### Posts (X-shaped; no stable tweet URL found)

Web search did not return durable `x.com/status/…` links. The same pitch spread as:

19. [Joe Njenga, Medium](https://medium.com/@joe.njenga/i-tried-this-claude-code-adhd-skill-that-no-one-is-talking-about-a990a647b1c7) — i-have-adhd as 10 rules, answer first.
20. [YouTube walkthrough](https://www.youtube.com/watch?v=EpU0Cj4jlVg) — Same skill: command on line one, numbered steps, no lecture.
21. [Ruben Hassid, “Use ASD-STE100.”](https://ruben.substack.com/p/how-to-deslop-claude-in-2-words) — Two-word deslop. He notes STE is bad for creative writing.
22. [Vibin / Saboo post](https://vibin.live/a-claude-i-have-adhd-skill-is-going-viral-for-improving-response-quality) — Viral ADHD-skill framing (chunking, less context switch). Secondary; treat as a lead.

## Trade-offs

| Option | Pros | Cons |
|--------|------|------|
| A Keep as-is | Already has prose vs Procedure vs Question | Shape choice is implicit. Model still writes how-tos as paragraphs sometimes. No one-page “pick the structure” table. |
| B Thin shape-picker | Matches hyperfocus + STE structure rules + plain-speak + agent-style RULE-A. Small. Protects meaning. | One more section in SKILL.md. Must stay four rows or it becomes another pile. |
| C Absorb one upstream | Fast. Community-tested. | hyperfocus always-lists. attention-control brings STE caps back. i-have-adhd always-procedure. We already rejected those costumes. |

## What the good ones agree on

1. **Pick the shape from the job.** Sequence → numbers. Parallel items → bullets. Causal why → prose. Decision → a short paragraph per option, not a label. ([L1nefeed structure](https://gist.github.com/L1nefeed/4164ecaaf77879e76dca3c06f142f1c2), [hyperfocus](https://github.com/nextor2k/hyperfocus), [plain-speak](https://github.com/Marksooxx/plain-speak), [agent-style RULE-A](https://github.com/yzhao062/agent-style))
2. **Never cut a load-bearing clause.** Fact, number, condition, scope. ([L1nefeed](https://gist.github.com/L1nefeed/4164ecaaf77879e76dca3c06f142f1c2), [attention-control](https://github.com/aaddrick/attention-control), [plain-speak](https://github.com/Marksooxx/plain-speak), [attention-span](https://github.com/alexgreensh/attention-span))
3. **Cut by priority, not by a word cap.** Drop recap, analogy, stat dump first. ([plain-speak](https://github.com/Marksooxx/plain-speak), [toppa](https://gist.github.com/toppa/bf7ff49d6fc44fd4fc3337248f8f2a7e))
4. **Answer first.** Tired readers stop early. ([W3C COGA](https://www.w3.org/TR/coga-usable/), i-have-adhd, hyperfocus)
5. **One costume for every reply is the failure.** Arrows, caveman, STE-on-chat, always-lists.

## Open questions

- No primary X status URLs in this pass. If a specific thread matters, paste it.
- ~~Whether Flow’s What → Why → How should be a named mode~~ → Tried as Answer frame; rejected. Named slots felt like a form. Keep silent order only (answer → reason → steps) with no printed labels.
- Decision paragraphs for options stay in Question surface, not a fourth shape-picker row.

## Lean

**B — then pruned.** Do not import another skill. Do not keep a named Answer frame. `write-like-goose` is prose + Procedure + Question + thin anti-AI (attention-span ideas without `→`; humanizer tells without the 29-pattern pile). Accuracy line stays: never drop a fact, number, condition, or scope.

| Job | Shape |
|-----|--------|
| How-to (do more than one thing) | Numbered procedure. One action per step. Action on line one. |
| Parallel set (files, options, symptoms) | Bullets. Rank if choosing. Recommendation first. |
| Why / diagnosis / one idea | Prose. Short paragraphs. No fake list. |
| Decision (they must pick) | One short paragraph per option: what changes, cost of nothing, your rec. Then the form. |
| Flow / state / who-calls-whom (3+ nodes) | Optional Mermaid under Shape. Not a costume. |

Keep: no word caps, no synonym dictionary, no `→` costume, no list-of-5 law, no `**What.**` / `**Why.**` / `**How.**` headings.
