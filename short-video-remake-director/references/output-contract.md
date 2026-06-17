# Output Contract

Use these artifact names when writing files for a full run.

```text
07-unit-state-timeline.v1.md
08-story-spine.v1.md
09-twelvelabs-segment-summary.v1.md
10-source-unit-summary-review.v1.md
11-source-unit-graph.v1.yaml
12-remake-map-and-director-brief.v1.md
13-visual-script.v1.md
```

For iterative fixes, increment the version instead of overwriting:

```text
13-visual-script.v2.md
```

## Source Unit Summary Review

Must include:

- Evidence sources and missing evidence.
- One-sentence spirit judgment.
- Unit state timeline summary when the source is scripted or conflict-led.
- Story spine summary when the source is scripted or conflict-led.
- Timeline structure blocks.
- Unit summary table.
- Mechanism-to-preserve table.
- Shell-to-change table.
- Omissions/uncertainties.

## Unit State Timeline

Required before story spine for scripted, role-play, conflict-led, or semi-scripted sources.

Must include:

- Unit list: people, products, props, scene frames, post-edit text/stickers, BGM, live sound, camera/editing units.
- Per-time state table: each important unit's presence/absence, position, speaker status, action, expression, product state, and relation to other units.
- Speaker attribution table: every important spoken/subtitle line mapped to a likely speaker, with uncertainty.
- Speaker child-unit table for host-led, acted, sales-led, or dialogue-heavy videos: each important spoken/subtitle line should have an ID such as `P01.V01`, parent speaker, speaker state, bound visual units, bound post-edit units, rhythm, function, and replacement rule.
- Relationship changes: who blocks whom, who leaves, who returns, who becomes absent, who gains/loses power, which post-edit unit changes the meaning.
- Event chain derived only from state changes.
- Contradiction check: any apparent conflict between TWE/OCR, subtitles, frame evidence, and inferred story.
- Reconstruction check: a reader should understand what happened by reading this timeline alone.

## Story Spine

Required for scripted, role-play, conflict-led, or semi-scripted sources.

Must include:

- Plot premise in one sentence.
- Character table: role, objective, obstacle, power position, knowledge gap, expression/action pattern.
- Beat table: trigger, escalation, product bridge, proof stretch, reversal, conversion, payoff.
- Cause-effect chain: why each beat happens because of the previous beat.
- Evidence references back to unit state timeline rows.
- Story units that must be preserved, story shells that may change, and shells that must change for product truth/compliance.
- What the remake would lose if the story is simplified.

## Remake Map

Must include:

- Product selling priority.
- High-similarity strategy.
- Unit state mapping before story role mapping.
- Story role mapping before product unit mapping.
- Source-to-remake unit mapping.
- Copy child-unit mapping before final script lines. Preserve the line's function and bound units before changing the words.
- Compliance/fact boundary.
- Deletion and addition choices.

## Visual Script

Each shot must specify:

- Time range.
- Which source shot/structure it aligns to.
- Which unit state change it carries.
- Which story beat it carries.
- Frame and background.
- People positions, posture, gaze, expression, gesture.
- Product/prop state and hand actions.
- Subtitle and spoken text.
- BGM/live sound/SFX.
- Intended psychological beat.

The picture/frame field should be one clear sentence, not a heavy multi-part breakdown, but it must not omit key units. Include critical spatial movement, who is present or absent, foreground/background frame, product/prop entry, and post-edit text/stickers when they affect the shot. Example: "车内前挡风 POV 看见男主把电动车从车前退到侧窗，女伴仍在后座冷脸，车门框压住下沿，头顶黄黑 `？！` 贴纸跟随移动。"

Avoid conceptual shots such as "show health" or "prove quality." Say what the camera sees.

For host-led, acted, or sales-led videos, each important spoken line should align to a source copy child unit (`Pxx.Vxx`) or a clearly added remake-only unit. If the line can stand alone as generic ad copy, it is probably not source-faithful enough.
