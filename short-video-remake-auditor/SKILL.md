---
name: short-video-remake-auditor
description: Audit a finished short-video remake against a reference-video remake package. Use when the user asks to review, score, diagnose, compare, or audit a completed remake video against outputs from short-video-remake-director, including 神/spirit, unit relationships, pressure fields, visual shock, product selling points, audio/copy, subtitles, editing, and missing or wrong units.
---

# Short Video Remake Auditor

## Core Rule

This skill does not judge whether a video is generally "good." It judges whether the finished remake preserved the reference video's discovered mechanism while truthfully adapting it to the target product.

Score is only the top-level result. The main value is a precise diagnosis: what is wrong, what is insufficient, where it happens in the finished video, which approved director unit or script requirement it violates, what user psychology is lost, and whether the fix is recut, reshoot, voiceover, overlay, audio, or compliance rewrite.

Do not audit from the script alone. Re-run evidence on the finished video and compare observed units against the reference analysis, remake map, director brief, and visual script.

## Director Script Anchor Rule

The auditor must not become a second director that invents a different remake.

Before judging or fixing, lock the approved director baseline from the reference package. Prefer `中文最终交付.md` as the primary baseline, then `14-visual-script*.md`, `13-remake-map-and-director-brief*.md`, `12-shot-spirit-and-copy-map*.md`, and upstream unit files as supporting evidence. State the exact baseline files and versions in the audit.

All audit findings and fixes must answer: "Did the finished video execute the approved director plan?" Fixes should be the smallest changes needed to bring the finished video back to that plan: recut timing, reshoot a missing unit, restore a sticker, change a line back to the mapped source function, adjust voice/BGM/SFX, or repair a product-fact/compliance issue.

Do not output a brand-new visual script, new story spine, or new selling sequence as the main audit result. If the approved director plan itself is clearly wrong, contradictory, unsafe, or no longer matches the user's latest product strategy, mark that as `director-baseline-defect`, explain the evidence, and recommend returning to `short-video-remake-director`. Keep the auditor output as a defect report and targeted change list, not a replacement script.

When suggesting copy changes, preserve the approved line's source function, speaker/persona, rhythm, bound visual unit, subtitle relation, and user-psychology target. You may provide a revised sentence only as a patch for that exact line, not as a new script system.

For 膳砂坊紫砂水培育罐 audits, load the product library before judging product understanding:

1. First try `D:\Backup\Documents\短视频内容团队\product-library\shanshafang-zisha-hydroponic-jar\product-remake-library.md`.
2. If working in another checkout, also check `product-library/shanshafang-zisha-hydroponic-jar/product-remake-library.md` relative to the current workspace.
3. Treat the live product library as the source of truth for product units, user mind, evidence directions, replacement principles, and expression boundaries.
4. If the live product library is unavailable, use the bundled/director fallback baseline only as a fallback and state that downgrade in the audit report.
5. If the approved director baseline conflicts with the live product library, mark the issue as `director-baseline-defect` instead of silently judging the finished video against stale product facts.

Do not treat product-library evidence directions as fixed required shots. Audit whether the finished video used target-product units to preserve the approved source mechanism and user psychology.

Finished-video TWE/TwelveLabs reconstruction is the default mandatory path. A full audit must rebuild the completed video as its own evidence object before scoring. Skip or downgrade from TWE only when the tool is genuinely unavailable, the upload/analysis fails after a real attempt, or the user explicitly asks for a local-only audit. In that case, mark the audit as partial and write the evidence gap into the outputs.
Final user-facing audit outputs must be Chinese. Use Chinese prose, section titles, table headers, issue descriptions, score explanations, fix instructions, and final chat responses. Stable IDs, filenames, paths, provider names, raw source quotes, and schema keys may stay as-is. For full audits, write `中文审核报告.md` as the user-facing final audit report.
Before writing the final user-facing audit, read `references/chinese-audit-report-template.md` and follow its structure unless the user explicitly asks for another format. The final report must integrate score, evidence, issues, audio/copy audit, unit-state gaps, and exact fixes in one Chinese file.

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
  - `12-shot-spirit-and-copy-map*.md`
  - `13-remake-map-and-director-brief*.md`
  - `14-visual-script*.md`
  - `中文最终交付.md`

If several versions exist, use the newest approved version unless the user names a specific version. If unsure, inspect file timestamps and version numbers, then state which version is being audited against.

## Evidence Workflow

1. Confirm the finished video path and the reference package path.
2. Read the reference package before judging. Extract:
   - approved director baseline files and versions; prefer `中文最终交付.md` plus the newest approved `14-visual-script*.md`.
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
   - Run TWE/TwelveLabs structured time-based analysis on the finished video by default. Use a low-bitrate proxy if needed, but keep enough resolution for subtitles, stickers, props, and hand actions.
   - Persist the finished-video TWE artifacts under the audit directory, for example `twelvelabs-finished-v1/`, including raw responses, parsed segments, and a concise segment summary. If the provider wraps the real payload inside nested JSON such as `rawResponse.task.result.data`, parse that nested value before deciding the run is empty.
   - The finished-video TWE schema must include: time range, visual description, spoken text, screen text, speaker/persona if visible or audible, people, product, props, scene, proof units, unit relationships, visual shock, user psychology, pressure field, BGM, live sound/SFX, voice delivery, subtitles, camera, editing, post-edit units, omissions, and uncertainty.
   - Build a separate voice/audio unit audit. Do not collapse audio into "has BGM" or "has spoken copy." Extract narrator persona, perceived timbre, emotional temperature, delivery style, sentence length, pause pattern, attack points, repetition, BGM role, action SFX, sticker/transition sounds, and voice-picture alignment. If you cannot directly hear or reliably model timbre, mark it as an evidence gap instead of inventing it.
   - Treat TWE as evidence, not final judgment; cross-check against frames.
4. Reconstruct the finished video as its own unit-state timeline. Do not merely assume the planned script was executed.
5. Compare the finished unit-state timeline against the approved director baseline first, then use source/reference requirements to explain why each deviation matters.
6. Score only after listing evidence-backed issues.

If TWE is unavailable or fails, do not silently continue as if the audit is complete. Record:

- attempted provider/tool and failure reason.
- what evidence remains: frames, local audio, waveform, OCR/ASR if available.
- which dimensions have reduced confidence, especially audio/voice, subtitles, stickers, and fast unit-state changes.
- whether the score is a partial-audit score.

## Finished-Video Reconstruction

Before comparison, write a concise reconstruction of the finished video:

- structure blocks with time ranges.
- TWE/TwelveLabs finished segment summary, unless explicitly unavailable.
- important people/product/prop/scene/post-edit/audio/camera units.
- finished unit-state timeline.
- spoken/caption copy child units.
- BGM/live sound/SFX/mix state.
- voice child units: speaker identity/persona, timbre, tone, pace, stress, pause, sentence density, and whether each line behaves like accusation, proof, verdict, value, price pressure, or CTA.
- visual-shock or psychology moments actually present.
- obvious omissions or ambiguous evidence.

The reader should understand what the finished video actually contains without watching it.

## Voice And Audio Unit Audit

Audio is a first-class remake unit. For short-video remakes, spoken delivery can carry as much spirit as the image.

Always audit these sub-units:

- **Speaker/persona unit**: gender/age impression if evident, role, authority level, intimacy, and whether the speaker feels like a livestream seller, evaluator, housewife, expert, friend, or narrator.
- **Timbre and texture unit**: bright/dry/warm/thin/thick/hoarse/soft/sharp/calm/urgent if directly supported by listening or reliable tool evidence. If not supportable, say the timbre cannot be verified.
- **Delivery-temperature unit**: calm, cold, irritated, teasing, urgent, excited, authoritative, restrained, or instructional.
- **Rhythm unit**: words or characters per second when transcript timing is available; short burst vs long explanation; where pauses or breath spaces should happen.
- **Sentence-function unit**: each spoken line should be labeled as pain accusation, rejection, proof, result verdict, objection answer, value build, price pressure, or CTA.
- **Audio-picture sync unit**: whether the strongest words land exactly on the strongest visual action, sticker pop, product reveal, failure reveal, result reveal, price reveal, or CTA.
- **BGM unit**: melody/tempo/energy curve, whether it builds authority, anxiety, comedy, shock, warmth, or purchase pressure.
- **SFX/live-sound unit**: open-lid sound, water pour, click, slap, crunch, sticker pop, transition whoosh, room tone, and whether these make the proof feel real.

Flag these failure modes:

- The copy is right but the voice sounds like a clean explainer instead of the reference's seller/persona.
- The transcript says the right selling point but lines are too long, too even, or too tutorial-like.
- BGM exists but does not create the same authority, urgency, comedy, shock, or live-commerce pressure.
- Key visuals happen without vocal stress, pause, SFX, or subtitle emphasis.
- The reference relies on sparse verdicts, but the remake fills every second with explanation.
- The reference relies on fast live-sale pressure, but the remake voice is smooth and educational.

## Comparison Layers

Audit from deepest to most visible:

1. **Bottom mechanism / 神**
   - Did the finished video preserve what made the reference work?
   - If the reference relied on visual shock, story reversal, authority, sparse verdicts, social power, live proof pressure, or price pressure, did the finished video create the same user psychology?
   - For every major shot, identify the viewer-mind change: what the viewer believes or feels before the shot, what exact visual/audio/copy trigger changes it, and what belief or urge the viewer should have after the shot.
   - Do not accept a generic "this shows the selling point" explanation. Name the psychological hook, such as disgust, fear of waste, relief, authority trust, "that is me", envy, value shock, proof satisfaction, or purchase urgency.

2. **Pressure-field correctness**
   - Did scene and prop replacements come from the target product's own proof/story pressure field?
   - Do not reward surface copying if the target product no longer needs that environment.
   - Example: night is a flashlight pressure field, not automatically a sprouting-jar pressure field. For a sprouting jar, the equivalent field may be kitchen counter, failed ordinary containers, same-seed comparison, open-lid full jar, sink drainage, and family-table result.

3. **Unit relationship replacement**
   - Were people, props, scene, product states, subtitles, audio, and camera replaced by function and relationship, not just category name?
   - Can the unit graph still explain what happens and why?
   - A unit is not complete unless it has: identity, visible state, time range, action or stillness, owner/actor if any, relationship to other units, and reason for existing in the shot.
   - If only reading the unit table cannot reconstruct what happened on screen, the unit decomposition is too coarse.

4. **Visual shock and user psychology**
   - What should the viewer feel at key moments?
   - Did the finished image actually trigger that feeling?
   - For 膳砂坊紫砂水培育罐, candidate visual-shock directions include full-to-the-rim jar, same-seed contrast, one jar poured into a large basin, crisp break, full family-table result, and price/result same-frame. These are not fixed requirements; use them only when the approved director baseline or source mechanism requires visual shock/result proof.

5. **Structure and rhythm**
   - Are opening, escalation, proof, explanation, price, and CTA in the right order?
   - Are shot lengths, cut density, repeated returns, and proof escalation close enough to the reference?
   - For each shot, check whether visual action, spoken line, subtitle/sticker, BGM/SFX, and cut point fire at the same user-psychology target. If they point at different targets, the shot has shape but no spirit.

6. **Visual execution**
   - Is the required action visible?
   - Are key objects framed clearly?
   - Is the result strong enough on screen?
   - Did the camera angle, distance, lighting, and texture preserve the reference's sensory force?

7. **Audio, copy, and subtitles**
   - Did spoken lines inherit source function, tone, pace, emotional temperature, and pause pattern?
   - Did BGM/live sound/SFX carry the same pressure?
   - Are subtitles/stickers present, timed, styled, and placed correctly?
   - Did timbre, persona, sentence density, pause, stress, and audio-picture sync recreate the source's listening experience?
   - Flag AI-like copy: explanatory clauses, abstract nouns, repeated sentence templates, "because/therefore" logic, brand-first introductions, and lines that sound written instead of spoken.
   - A replacement line must keep the source line's function and human delivery, not just the product fact. Prefer spoken verdicts tied to visible action: "水别闷根", "压住才粗", "看这一罐", "别再用盒子泡了".

8. **Product selling point**
   - For 膳砂坊紫砂水培育罐, the primary mind is health/养生: self-grown water-cultivated vegetables at home. Full-jar result is a strong proof direction, not a fixed shot requirement when the source mechanism calls for another truthful same-function proof.
   - Structure/process must support the result, not become the main story unless the reference itself is tutorial-led.

9. **Compliance and truth**
   - Flag fake prices, fake reports, fake institutional proof, absolute success claims, medical/disease claims, and unsafe comparisons.

## Shot Spirit Gate

For each important shot, write or verify a one-line spirit diagnosis with this shape:

```text
viewer before -> trigger units -> viewer after
```

Examples:

- "viewer is worried home sprouts rot -> sticky rotten roots plus disgust close-up plus urgent question -> viewer admits their old method is unsafe/unreliable"
- "viewer doubts the jar is different -> pressure plate moves down plus water drains away plus short verdict '水别闷根' -> viewer sees structure as proof, not decoration"
- "viewer wants result proof -> lid opens on full-to-rim sprouts plus pause plus '看这一罐' -> viewer feels quantity/value shock"

If a shot lacks this diagnosis, it cannot be treated as a finished remake shot. If many shots lack it, the whole remake cannot score above 79 no matter how complete the surface script looks.

## Human Copy Gate

Audit copy as spoken behavior, not written explanation.

Reject lines that:

- explain the product before the viewer has felt the problem.
- sound like a manual, class, brochure, or AI summary.
- use long causal chains when the reference uses short verdicts.
- repeat the same syntax across many shots.
- state a selling point without attaching it to a visible action.

Require lines to:

- preserve the source function: accusation, rejection, proof, result verdict, objection answer, value pressure, price pressure, or CTA.
- be sayable in one breath.
- land on a visible action or post-edit emphasis.
- include human judgment words when appropriate: "别折腾了", "看这一罐", "这才踏实", "真别泡着看运气".
- let the image prove the technical reason, instead of explaining everything in the voiceover.

Before accepting final copy, produce one "literal product fact" version, then rewrite it into a "spoken seller line." Keep the spoken version unless compliance requires restraint.

## Unit-State Clarity Gate

Every visual-script shot and every audit reconstruction must make the screen reconstructable from text.

For each shot, require:

- people: who appears, pose, expression, hand action, gaze, and relation to product.
- product: exact component, position, state, and state change.
- props: failed tool/container/material, state, and why it matters.
- scene: background elements that affect trust, pressure, or reference similarity.
- post-edit: stickers, subtitles, keywords, arrows, disclaimers, badges, and whether they persist or change.
- audio: voice line, voice function, BGM state, SFX/live sound, and whether it syncs with the action.
- user psychology: the intended feeling or belief created by the combined units.

Ban vague visual descriptions such as "展示产品", "展示效果", "进行对比", or "突出卖点" unless followed by exact visible units and state changes.

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
- approved director shot/line/unit requirement
- reference requirement or source unit IDs
- what is wrong
- what is insufficient, if it is not fully wrong
- lost user psychology
- score impact
- fix type: `recut`, `reshoot`, `voiceover`, `subtitle/overlay`, `audio`, `color/framing`, `compliance`, or `director-baseline-defect`
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
中文审核报告.md
```

Put the voice/audio unit audit inside `05-issues-and-fix-plan.v1.md`, after the main issue table. Do not create a separate sixth file unless the user explicitly asks for a standalone audio report.

Put a director-baseline alignment section inside `03-reference-vs-finished-comparison.v1.md` and `中文审核报告.md`: list the exact approved director shots/lines/units, what the finished video did, and the smallest correction needed. This section must not become a new visual script.

`01-finished-video-evidence-summary.v1.md` must state whether finished-video TWE was run, where its artifacts were saved, and whether any evidence downgrade occurred.

The chat final should be concise and Chinese: total score, score band, top 3-5 problems, and links to the files. Link `中文审核报告.md` first when it exists. Build `中文审核报告.md` from `references/chinese-audit-report-template.md`.

## Quality Gates

- Do not score before reconstructing the finished video.
- Do not score a full audit before running finished-video TWE/TwelveLabs or explicitly documenting why it could not be run.
- Do not rely on intended script if finished evidence contradicts it.
- Do not create a different remake script while auditing. Audit against the approved `中文最终交付.md`/`14-visual-script` baseline and give targeted patches only.
- Do not rewrite the selling order, shot order, or story logic unless the issue is explicitly marked `director-baseline-defect` and sent back to the director stage.
- Do not reward surface similarity when pressure-field adaptation is wrong.
- Do not accept a shot without a viewer-before -> trigger-units -> viewer-after spirit diagnosis when the shot is important to the remake.
- Do not accept AI-like copy merely because the selling point is factually correct; flag copy that sounds written, educational, or mechanically explanatory.
- Do not accept vague visual descriptions unless people, product, props, post-edit, audio, and user psychology states are reconstructable from the text.
- Do not say "visual shock is weak" without identifying the exact shot and what should have created the shock.
- Do not collapse audio into "has BGM"; identify BGM role, voice style, SFX/live sound, subtitle rhythm, and missing pressure.
- Do not only list problems; include concrete fix instructions.
- If an issue needs reshoot, say so directly.
- If the reference package is missing, run a partial audit and clearly mark what cannot be compared.
