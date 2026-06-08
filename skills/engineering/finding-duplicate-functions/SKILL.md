---
name: finding-duplicate-functions
description: Use when auditing a codebase for semantic duplication - functions that do the same thing but have different names or implementations. Especially useful for LLM-generated codebases where new functions are often created rather than reusing existing ones.
metadata:
  area: engineering
  upstream:
    repo: obra/superpowers-lab
    path: skills/finding-duplicate-functions
    url: https://github.com/obra/superpowers-lab/tree/main/skills/finding-duplicate-functions
    synced_at: "2026-06-07"
    commit: 51111f74f24058117752d9aa917cb19859f8ec86
    note: Adaptada — categorização e detecção na mesma sessão, sem subagents.
---

# Finding Duplicate-Intent Functions

**Announce at start:** "Estou usando a skill finding-duplicate-functions."

## Overview

LLM-generated codebases accumulate semantic duplicates: functions that serve the same purpose but were implemented independently. Classical copy-paste detectors (jscpd) find syntactic duplicates but miss "same intent, different implementation."

This skill uses extraction + LLM-powered intent clustering.

## When to Use

- Codebase has grown organically with multiple contributors (human or LLM)
- You suspect utility functions have been reimplemented multiple times
- Before major refactoring to identify consolidation opportunities
- After jscpd has been run and syntactic duplicates are already handled

## Quick Reference

| Phase | Tool | Output |
|-------|------|--------|
| 1. Extract | `scripts/extract-functions.sh` | `catalog.json` |
| 2. Categorize | `scripts/categorize-prompt.md` | `categorized.json` |
| 3. Split | `scripts/prepare-category-analysis.sh` | `categories/*.json` |
| 4. Detect | `scripts/find-duplicates-prompt.md` | `duplicates/*.json` |
| 5. Report | `scripts/generate-report.sh` | `report.md` |
| 6. Review | Human | Consolidation plan |

## Process

### Phase 1: Extract Function Catalog

Run from the target project root (not the skills repo):

```bash
./path/to/skills/finding-duplicate-functions/scripts/extract-functions.sh src/ -o catalog.json
```

Or copy the script locally. Options:
- `-o FILE`: Output file (default: stdout)
- `-c N`: Lines of context to capture (default: 15)
- `-t GLOB`: File types (default: `*.ts,*.tsx,*.js,*.jsx`)
- `--include-tests`: Include test files (excluded by default)

Test files (`*.test.*`, `*.spec.*`, `__tests__/**`) are excluded by default.

### Phase 2: Categorize by Domain

Follow the prompt template in `scripts/categorize-prompt.md` **in this session**.

Insert `catalog.json` where indicated. Save output as `categorized.json`.

Do not skip this step — categorization reduces noise in duplicate detection.

### Phase 3: Split into Categories

```bash
./scripts/prepare-category-analysis.sh categorized.json ./categories
```

Only categories with **3+ functions** are worth analyzing in Phase 4.

### Phase 4: Find Duplicates (Per Category)

For each category file in `./categories/`, follow `scripts/find-duplicates-prompt.md` **in this session**.

Analyze thoroughly — semantic duplicates are subtle. Process one category at a time.

Save each output as `./duplicates/{category}.json`.

### Phase 5: Generate Report

```bash
./scripts/generate-report.sh ./duplicates ./duplicates-report.md
```

Produces a prioritized markdown report grouped by confidence level.

### Phase 6: Human Review

Present the report to the user. For HIGH confidence duplicates:
1. Verify the recommended survivor has tests
2. Propose updating callers to use the survivor
3. Delete duplicates only after user approval
4. Run tests (`verification-before-completion`)

Do not auto-delete code without explicit user consent.

## High-Risk Duplicate Zones

| Zone | Common Duplicates |
|------|-------------------|
| `utils/`, `helpers/`, `lib/` | General utilities reimplemented |
| Validation code | Same checks written multiple ways |
| Error formatting | Error-to-string conversions |
| Path manipulation | Joining, resolving, normalizing paths |
| String formatting | Case conversion, truncation, escaping |
| Date formatting | Same formats implemented repeatedly |
| API response shaping | Similar transformations for different endpoints |

## Common Mistakes

**Extracting too much**: Focus on exported functions and public methods.

**Skipping categorization**: Full-catalog duplicate detection produces noise.

**Shallow duplicate analysis**: Compare intent, not just names or signatures.

**Consolidating without tests**: Ensure the survivor has tests covering all use cases before deleting duplicates.

**Auto-deleting without approval**: Report first, consolidate only when the user agrees.
