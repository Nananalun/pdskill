# Audit Output Contract

Use this reference when the audit needs stricter output formatting.


## Chinese Final Audit Report

All final user-facing audit output files must be Chinese. Use Chinese section names, table headers, issue descriptions, score explanations, fix instructions, and uncertainty notes.

Required final user-facing file:

```text
中文审核报告.md
```

`中文审核报告.md` is the primary file the user should read. It must follow `references/chinese-audit-report-template.md` and include, in Chinese:

- Audit conclusion and total score.
- Main mechanism/spirit preservation judgment.
- Scorecard summary.
- Top issues and exact fixes.
- Voice/audio audit summary.
- Visual/unit-state gaps.
- Evidence limits and uncertainty.

Internal artifact filenames, stable IDs, provider names such as TWE/TwelveLabs, paths, raw source quotes, and schema keys may remain non-Chinese. If an English word is not required for those purposes, rewrite it in Chinese before finalizing.

If `中文审核报告.md` does not follow the template sections, lacks an issue table with exact fixes, or omits the voice/audio audit, the audit is incomplete.
## Evidence Summary

Must include:

- finished video metadata.
- evidence files generated.
- TWE status and segment count. Finished-video TWE/TwelveLabs is mandatory for a full audit unless explicitly unavailable or the user requests local-only.
- TWE artifact directory, raw response path, parsed segment path, and evidence downgrade notes if TWE failed.
- reference package version audited against.
- approved director baseline audited against, especially `中文最终交付.md` and the newest approved `14-visual-script*.md`.
- missing evidence and uncertainty.

## Comparison Table

Each row should include:

- approved director shot/line/unit requirement.
- reference unit or requirement.
- intended function.
- target pressure field.
- finished video evidence.
- match level: `match`, `partial`, `miss`, `wrong`, `not_applicable`.
- reason.
- smallest fix needed to return the finished video to the approved director baseline.

Do not use the comparison table to create a new remake script. If the approved director baseline is itself wrong, mark the row as `director-baseline-defect`, explain why, and recommend returning to `short-video-remake-director`.

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
- approved director shot/line/unit requirement.
- source/reference requirement.
- observed problem.
- why it matters.
- lost user psychology.
- fix type. Use `director-baseline-defect` only when the approved director baseline itself is wrong; otherwise use recut, reshoot, voiceover, subtitle/overlay, audio, color/framing, or compliance.
- exact fix instruction.

The issue plan must also include:

- A voice/audio unit audit section inside `05-issues-and-fix-plan.v1.md`, not a separate sixth file unless requested.
- A director-baseline alignment section: each issue should be a deviation from the approved script/shot/unit, not a newly invented script direction.
- Shot-spirit failures: missing or weak `viewer_before -> trigger_units -> viewer_after` for important shots.
- Human-copy failures: lines that sound written, educational, explanatory, repetitive, brand-first, or disconnected from visible action.
- Unit-state clarity failures: vague visual rows where people, product, props, scene, post-edit, audio, or user psychology cannot be reconstructed.
