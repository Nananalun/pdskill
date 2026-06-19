---
name: short-video-remake-auditor
description: Audit a finished short-video remake against a reference-video remake package. Use when the user asks to review, score, diagnose, compare, or audit a completed remake video against outputs from short-video-remake-director, including 神/spirit, unit relationships, pressure fields, visual shock, product selling points, audio/copy, subtitles, editing, and missing or wrong units.
---

# Short Video Remake Auditor

## Core Rule

This skill does not judge whether a video is generally "good." It judges whether the finished remake preserved the reference video's discovered mechanism while truthfully adapting it to the target product.

Score is only the top-level result. The main value is a precise diagnosis: what is wrong, what is insufficient, where it happens in the finished video, which reference unit or script requirement it violates, what user psychology is lost, and whether the fix is recut, reshoot, voiceover, overlay, audio, or compliance rewrite.

Do not audit from the script alone. Re-run evidence on the finished video and compare observed units against the reference analysis, remake map, director brief, and visual script.

## Inputs

Prefer these inputs:

- finished video path.
- reference/source video path if available.
- output directory from `short-video-remake-director`, especially:
  - `07-unit-state-timeline*.md`
  - `08-story-spine*.md`
  - `09-twelvelabs-segment-summary*.md`
  - `10-source-unit-summary-review*.md`
  - `11-source-unit-graph*.yaml`
  - `12-remake-map-and-director-brief*.md`
  - `13-visual-script*.md`

If several versions exist, use the newest approved version unless the user names a specific version. If unsure, inspect file timestamps and version numbers, then state which version is being audited against.

## Evidence Workflow

1. Confirm the finished video path and the reference package path.
2. Read the reference package before judging. Extract:
   - one-sentence source spirit.
   - bottom mechanism or story/proof engine.
   - pressure fields: source pressure field and target product pressure field.
   - visual-shock targets or other user-psychology targets.
   - required unit mappings.
   - required shot/script beats.
   - product main selling point and compliance boundaries.
3. Run finished-video evidence:
   - Use `../short-video-remake-director/scripts/prepare_video_evidence.py` when available to create metadata, frames, opening frames, overview tile, audio, and waveform.
   - Inspect overview and opening tiles before scoring.
   - If TWE/TwelveLabs is available, run structured time-based analysis on the finished video with fields for visual description, spoken text, screen text, people, product, props, scene, proof units, visual shock, user psychology, pressure field, BGM, live sound/SFX, voice delivery, subtitles, camera, editing, post-edit units, omissions, and uncertainty.
   - Treat TWE as evidence, not final judgment; cross-check against frames.
4. Reconstruct the finished video as its own unit-state timeline. Do not merely assume the planned script was executed.
5. Compare the finished unit-state timeline against the reference/remake requirements.
6. Score only after listing evidence-backed issues.

If TWE is unavailable, continue from local frames/audio and mark the evidence gap.

## Finished-Video Reconstruction

Before comparison, write a concise reconstruction of the finished video:

- structure blocks with time ranges.
- important people/product/prop/scene/post-edit/audio/camera units.
- finished unit-state timeline.
- spoken/caption copy child units.
- BGM/live sound/SFX/mix state.
- visual-shock or psychology moments actually present.
- obvious omissions or ambiguous evidence.

The reader should understand what the finished video actually contains without watching it.

## Comparison Layers

Audit from deepest to most visible:

1. **Bottom mechanism / 神**
   - Did the finished video preserve what made the reference work?
   - If the reference relied on visual shock, story reversal, authority, sparse verdicts, social power, live proof pressure, or price pressure, did the finished video create the same user psychology?

2. **Pressure-field correctness**
   - Did scene and prop replacements come from the target product's own proof/story pressure field?
   - Do not reward surface copying if the target product no longer needs that environment.
   - Example: night is a flashlight pressure field, not automatically a sprouting-jar pressure field. For a sprouting jar, the equivalent field may be kitchen counter, failed ordinary containers, same-seed comparison, open-lid full jar, sink drainage, and family-table result.

3. **Unit relationship replacement**
   - Were people, props, scene, product states, subtitles, audio, and camera replaced by function and relationship, not just category name?
   - Can the unit graph still explain what happens and why?

4. **Visual shock and user psychology**
   - What should the viewer feel at key moments?
   - Did the finished image actually trigger that feeling?
   - For 善砂坊紫砂水培育罐, common visual-shock targets include full-to-the-rim jar, same-seed contrast, one jar poured into a large basin, crisp break, full family-table result, and price/result same-frame.

5. **Structure and rhythm**
   - Are opening, escalation, proof, explanation, price, and CTA in the right order?
   - Are shot lengths, cut density, repeated returns, and proof escalation close enough to the reference?

6. **Visual execution**
   - Is the required action visible?
   - Are key objects framed clearly?
   - Is the result strong enough on screen?
   - Did the camera angle, distance, lighting, and texture preserve the reference's sensory force?

7. **Audio, copy, and subtitles**
   - Did spoken lines inherit source function, tone, pace, emotional temperature, and pause pattern?
   - Did BGM/live sound/SFX carry the same pressure?
   - Are subtitles/stickers present, timed, styled, and placed correctly?

8. **Product selling point**
   - For 善砂坊紫砂水培育罐, the primary mind is health/养生: self-grown water-cultivated vegetables at home, with full-jar result as strongest proof.
   - Structure/process must support the result, not become the main story unless the reference itself is tutorial-led.

9. **Compliance and truth**
   - Flag fake prices, fake reports, fake institutional proof, absolute success claims, medical/disease claims, and unsafe comparisons.

## Scoring

Use a 100-point score, but every lost point must map to evidence and a fix.

| Dimension | Points | What To Audit |
|---|---:|---|
| Bottom mechanism / 神 | 15 | The deepest source effect and user psychology are preserved. |
| Pressure-field adaptation | 12 | Scene/prop replacements belong to the target product's own proof/story pressure field. |
| Unit relationship replacement | 12 | Units are replaced by function, state, and relationship, not surface category. |
| Visual shock / emotional trigger | 15 | Key images create the intended viewer reaction. |
| Structure and rhythm | 12 | Beat order, escalation, proof density, and cut rhythm match the reference mechanism. |
| Audio, copy, and subtitles | 10 | Voice tone, pace, BGM, SFX, subtitles, and copy child-units carry the same function. |
| Product selling point | 12 | Target product's main mind and proof hierarchy are correct. |
| Visual execution clarity | 7 | Camera, lighting, framing, and action clarity make the proof visible. |
| Compliance and truth | 5 | Claims, price, and proof remain truthful and safe. |

Score bands:

- `85-100`: Can publish; only local optimizations remain.
- `70-84`: Direction is right, but key shots/audio/edits need rework.
- `50-69`: Has shape but lacks spirit; needs major recut or targeted reshoots.
- `<50`: Remake failed; return to director stage.

## Required Issue Format

For every meaningful issue, output a row with:

- `issue_id`
- severity: `P0` breaks the remake, `P1` materially weakens conversion/similarity, `P2` polish
- finished video time range
- observed finished-video evidence
- reference requirement or source unit IDs
- what is wrong
- what is insufficient, if it is not fully wrong
- lost user psychology
- score impact
- fix type: `recut`, `reshoot`, `voiceover`, `subtitle/overlay`, `audio`, `color/framing`, `compliance`, or `director-rewrite`
- concrete fix instruction

Do not write vague comments such as "not enough impact" without naming the image, timing, reference requirement, and replacement action.

## Required Output Order

For a full audit, write files to a per-video output directory:

```text
01-finished-video-evidence-summary.v1.md
02-finished-unit-state-timeline.v1.md
03-reference-vs-finished-comparison.v1.md
04-audit-scorecard.v1.md
05-issues-and-fix-plan.v1.md
```

The chat final should be concise: total score, score band, top 3-5 problems, and links to the files.

## Quality Gates

- Do not score before reconstructing the finished video.
- Do not rely on intended script if finished evidence contradicts it.
- Do not reward surface similarity when pressure-field adaptation is wrong.
- Do not say "visual shock is weak" without identifying the exact shot and what should have created the shock.
- Do not collapse audio into "has BGM"; identify BGM role, voice style, SFX/live sound, subtitle rhythm, and missing pressure.
- Do not only list problems; include concrete fix instructions.
- If an issue needs reshoot, say so directly.
- If the reference package is missing, run a partial audit and clearly mark what cannot be compared.

