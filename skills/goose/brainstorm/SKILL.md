---
name: brainstorm
description: Relentless Q&A to freeze the what before a plan. Use when sharpening design; no implementation yet. Greenfield branch when empty repo, new product, or user asks greenfield.
metadata:
  area: goose
  inspired_by:
    - mattpocock/skills - grilling, grill-with-docs
    - obra/superpowers - brainstorming
    - compound-engineering - ce-brainstorm
---

# Brainstorm

Turn a fuzzy idea into **shared understanding** (the *what*). Not the implementation plan (*how*) - that is **`planning`**.

Voice for durable prose: **`write-like-goose`** (ASD-STE100).

## Hard gate

Do **not** write production code, scaffold apps, or open pull requests. Do **not** run **`implement`** or **`create-tickets`** until the user confirms shared understanding.

A tiny design is fine. Skipping the freeze is not. "Too simple" is where silent assumptions hurt most. If the user and **`ask`** already treated the change as trivial, confirm in one short breath (purpose, approach, done-when) and exit. Still get an explicit OK.

## When to use

- Idea exists; decisions and shape are still fuzzy.
- Before **`planning`**.

## When not to

- Need facts/libraries first → **`research`**, then return here.
- *How* / task breakdown already agreed → **`planning`**.
- Hard-to-reverse decision already isolated → **`documentation:adr`** (can run mid-brainstorm; see below).

## Branches

| Branch | When |
|--------|------|
| **`product`** (default) | Feature or change in a repo that already has local patterns |
| **`greenfield`** | Empty / near-empty repo, “new product”, “design from scratch”, **or** user asks for greenfield / this branch by name |

Do **not** force **`greenfield`** on a mature repo that already has stack and platform conventions, unless the user asks explicitly.

---

## Branch: product

### Flow

```
orient → grill (1Q at a time) → always 2-3 approaches → design freeze
  → [CONTEXT.md?] → [documentation:adr?] → user OK → planning
  → [optional durable brief if long / multi-session / user asks]
```

### 1. Orient

- Skim the target repo: relevant files, docs, recent commits, existing `CONTEXT.md` / `CONTEXT-MAP.md` (below).
- **Scope check:** multiple independent subsystems? Decompose first; brainstorm **one** slice. Don’t polish details of a platform that should be split.
- Reuse **settled decisions** already made in this thread - don’t re-ask them. Mark them in the freeze.

### 2. Grill

- **One question per message.** Prefer multiple choice when options are real; open-ended when the answer is narrative.
- Walk the decision tree; resolve dependencies one by one.
- On each question: give **your recommended answer** and why, then wait.
- **Facts** → look up (repo, tools). **Decisions** → the human.
- Focus: purpose, constraints, success criteria, non-goals, who it serves.

### 3. Approaches (always)

Always propose **2-3 approaches** with trade-offs before locking the shape - even for “small” work (the set can be short). Lead with your recommendation and why. YAGNI: cut speculative scope from every option.

### 4. Design freeze

Present a compact design. Scale to complexity: a few sentences or short sections. Cover shape, boundaries, data flow, and failure modes worth deciding now. For module shape or seams, use **`codebase-design`** vocabulary (depth, seam, adapter; not "service/API/boundary"). Ask if it looks right. Revise if not.

End with an **Established so far** block (Goose voice): purpose, non-goals, chosen approach, key decisions, open questions (if any).

### 5. Context (`CONTEXT.md`)

Domain terms that crystallize go in **`CONTEXT.md`**. That file **is** the project’s ubiquitous language (glossary of what words mean here) - not ADRs, not implementation notes.

**Format + examples:** [`references/context-format.md`](references/context-format.md) (`CONTEXT.md` and `CONTEXT-MAP.md`).

**Layout (target repo):**

- **Single context (usual):** `CONTEXT.md` at the repo root. Create it when the first term lands if missing.
- **Multiple contexts:** `CONTEXT-MAP.md` at the root points at each context’s `CONTEXT.md` (and how they relate). Update the map when a new context appears; write terms in the right context’s file.
- Repo `AGENTS.md` may override paths - follow it when present.

Update **inline** when a term is resolved (don’t batch until the end). Keep definitions tight: what the term *is*, avoid-list for synonyms - no schemas, endpoints, or framework choices.

Challenge conflicts with the existing language immediately. Sharpen overloaded words (“account” → Customer vs User).

When domain relationships are in play, stress-test them with **concrete scenarios** that force boundaries (partial cancel? two owners? clock skew?). When the user states how something works, **check the code**. If the code contradicts the user, surface it and resolve which is right before you freeze language.

### 6. ADR handoff (sparingly)

Offer **`documentation:adr`** only when all three hold (detail in that skill’s [`adr-format`](../documentation/references/adr-format.md)):

1. Hard to reverse  
2. Surprising without context later  
3. Real trade-off among alternatives  

Don’t write full ADRs inside brainstorm unless the user wants that skill run now. Point and hand off (or invoke `documentation` branch `adr`).

### 7. Durable brief (optional)

Default: keep the freeze in **chat** (`Established so far`).

Write a short markdown brief to the target repo **only if**:

- the session will span multiple chats, or  
- the problem is large enough that chat will lose the thread, or  
- the user asks  

Prefer path from `AGENTS.md`; else `docs/brainstorms/YYYY-MM-DD-<topic>.md`. Brief = the freeze + approaches rejected in one line each - not a full spec dump. Commit only if the user wants it committed.

### 8. Exit gate

User confirms shared understanding → **`planning`**.  
Fact gap blocks a decision → **`research`**, then return.  
Do **not** jump to **`implement`**.

---

## Branch: greenfield

Stops silent platform defaults at **`implement`**. Same grill rules (1Q, recommend, wait). No feature code or scaffold.

### Flow

```
orient → Shape → Product → Platform (per active pack)
  → 2-3 approaches → design freeze (+ tables) → [CONTEXT.md?] → [adr?]
  → user OK → planning
```

### 1. Orient

- Confirm trigger: empty/near-empty repo, new product language, or explicit greenfield ask.
- If the repo already has a clear stack and platform conventions → switch to **`product`** (unless user insisted on greenfield).

### 2. Shape

Load [`references/greenfield-shape.md`](references/greenfield-shape.md).

Lock surfaces (API / Web / Mobile / Desktop), stack per surface, and **active packs** (order for Platform). Desktop has no Goose pack: user stack or **later**.

### 3. Product

Same focus as product-branch grill: purpose, who it serves, constraints, success criteria, non-goals. One question at a time.

### 4. Platform

For each **active pack**, in Shape order:

1. Load that pack’s `references/greenfield-decision-surface.md` if it exists.
2. Follow that file’s order (dotnet: **core → reminders → triggers**). Status **in / out / later**; deepen only **in**. Triggers only when Shape/Product signaled.
3. Never grill pack-owned defaults (see the surface file).
4. Stub pack (no surface yet): note “pack incomplete” and continue; do not invent SOTA.

Today filled: [`../implement/dotnet/references/greenfield-decision-surface.md`](../implement/dotnet/references/greenfield-decision-surface.md).  
`frontend` / `react-native`: add surfaces when those packs fill.

### 5. Approaches + freeze

2-3 approaches for the overall system shape (YAGNI). Then freeze including:

- Surfaces + stacks + active packs  
- Product: purpose, non-goals, success  
- Per pack: concern table (status + decision if **in**)  
- Chosen approach; rejected approaches in one line each  

No empty status cells. User OK required.

CONTEXT / ADR / durable brief: same rules as **`product`**.

### 6. Exit gate

User confirms → **`planning`** (plan must honor **in / out / later**; do not re-open Shape unless the user does).  
Fact gap → **`research`**, then return.  
Do **not** jump to **`implement`**.

---

## Working in existing codebases

- Prefer existing patterns; propose targeted seam fixes only when they serve this goal.
- No unrelated refactors in the design.

## Checklist

### product

- [ ] Oriented on repo + scope OK (or decomposed)
- [ ] Grilled one question at a time with recommendations
- [ ] 2-3 approaches presented; one chosen
- [ ] Design freeze + **Established so far**; user OK
- [ ] `CONTEXT.md` updated if terms landed
- [ ] ADR offered only when criteria matched
- [ ] Durable brief only when the optional triggers fired
- [ ] Next = **planning** (or research detour)

### greenfield

- [ ] Trigger OK (or switched to **product**)
- [ ] Shape: surfaces + stacks + pack order locked
- [ ] Product grilled
- [ ] Platform: core + reminders asked; triggers only if signaled; statuses set
- [ ] 2-3 approaches; freeze tables complete; user OK
- [ ] Next = **planning** (or research detour)

## Guardrails

1. Freeze the **what** only - no feature code or scaffolding this run.
2. One question at a time (with a recommendation); prefer repo answers over asking the human for facts already in tree.
3. `CONTEXT.md` = terms/glossary, not implementation detail. Skip the long interview when a one-breath confirm is enough and the user OK’d that shortcut.
4. **greenfield:** do not skip Shape; do not exit with empty platform statuses; do not grill pack-owned style; do not invent a desktop pack or web/mobile SOTA beyond stubs; do not force greenfield on a mature local convention unless asked.

## Next

**`planning`** - or **`documentation:adr`** if a hard decision is next, or **`research`** if a fact is missing.
