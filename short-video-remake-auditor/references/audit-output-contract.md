# Audit Output Contract

Use this reference when the audit needs stricter output formatting.


## Chinese Final Audit Report

All final user-facing audit output files must be Chinese. Use Chinese section names, table headers, issue descriptions, score explanations, fix instructions, and uncertainty notes.

Required final user-facing file:

```text
中文审核报告.md
```

`中文审核报告.md` is the primary file the user should read. It must include, in Chinese:

- Audit conclusion and total score.
- Main mechanism/spirit preservation judgment.
- Scorecard summary.
- Top issues and exact fixes.
- Voice/audio audit summary.
- Visual/unit-state gaps.
- Evidence limits and uncertainty.

Internal artifact filenames, stable IDs, provider names such as TWE/TwelveLabs, paths, raw source quotes, and schema keys may remain non-Chinese. If an English word is not required for those purposes, rewrite it in Chinese before finalizing.
## Evidence Summary

Must include:

- finished video metadata.
- evidence files generated.
- TWE status and segment count. Finished-video TWE/TwelveLabs is mandatory for a full audit unless explicitly unavailable or the user requests local-only.
- TWE artifact directory, raw response path, parsed segment path, and evidence downgrade notes if TWE failed.
- reference package version audited against.
- missing evidence and uncertainty.

## Comparison Table

Each row should include:

- reference unit or requirement.
- intended function.
- target pressure field.
- finished video evidence.
- match level: `match`, `partial`, `miss`, `wrong`, `not_applicable`.
- reason.
- fix.

## Scorecard

Each dimension must include:

- points possible.
- points earned.
- evidence.
- main deduction.
- fix priority.

## Issue Plan

Each issue must include:

- severity.
- finished time range.
- source/reference requirement.
- observed problem.
- why it matters.
- lost user psychology.
- fix type.
- exact fix instruction.

The issue plan must also include:

- A voice/audio unit audit section inside `05-issues-and-fix-plan.v1.md`, not a separate sixth file unless requested.
- Shot-spirit failures: missing or weak `viewer_before -> trigger_units -> viewer_after` for important shots.
- Human-copy failures: lines that sound written, educational, explanatory, repetitive, brand-first, or disconnected from visible action.
- Unit-state clarity failures: vague visual rows where people, product, props, scene, post-edit, audio, or user psychology cannot be reconstructed.
