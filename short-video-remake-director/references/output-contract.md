# Output Contract

Use these artifact names when writing files for a full run.

```text
07-unit-state-timeline.v1.md
08-story-spine.v1.md
09-twelvelabs-segment-summary.v1.md
10-source-unit-summary-review.v1.md
11-source-unit-graph.v1.yaml
12-shot-spirit-and-copy-map.v1.md
13-remake-map-and-director-brief.v1.md
14-visual-script.v1.md
中文最终交付.md
```

For iterative fixes, increment the version instead of overwriting:

```text
14-visual-script.v2.md
```


## Chinese Final Delivery

All final user-facing output files must be Chinese. Use Chinese section names, table headers, explanations, shot descriptions, copy comments, and final recommendations.

Required final user-facing file:

```text
中文最终交付.md
```

`中文最终交付.md` is the primary file the user should read. It must include, in Chinese:

- Source-video spirit judgment.
- Important unit summary and unit relationships.
- Shot-level spirit and human-copy map.
- Remake strategy for the target product.
- Visual script with Chinese column names and Chinese shot descriptions.
- Execution notes, compliance notes, and known uncertainties.

Internal artifact filenames, stable IDs such as `P01.V01`, provider names such as TWE/TwelveLabs, paths, raw source quotes, and YAML schema keys may remain non-Chinese. If an English word is not required for an ID, provider name, filename, path, raw quote, or schema key, rewrite it in Chinese before finalizing.
## Source Unit Summary Review

Must include:

- Evidence sources and missing evidence.
- One-sentence spirit judgment.
- Unit state timeline summary when the source is scripted or conflict-led.
- Story spine summary when the source is scripted or conflict-led.
- Timeline structure blocks.
- Unit summary table.
- Copy delivery table: important spoken/subtitle lines with speaker, tone, emotional temperature, delivery style, pace, pause, BGM/SFX/subtitle relation, and uncertainty.
- Audio unit table: BGM, live sound, SFX, silence, voice texture, and audio mix with time range, mood, intensity, function, bound visual/copy units, and replacement rule.
- Mechanism-to-preserve table.
- Shell-to-change table.
- Omissions/uncertainties.

## Unit State Timeline

Required before story spine for scripted, role-play, conflict-led, or semi-scripted sources.

Must include:

- Unit list: people, products, props, scene frames, post-edit text/stickers, BGM, live sound, camera/editing units.
- Per-time state table: each important unit's presence/absence, position, speaker status, action, expression, product state, and relation to other units.
- Speaker attribution table: every important spoken/subtitle line mapped to a likely speaker, with uncertainty.
- Speaker child-unit table for host-led, acted, sales-led, or dialogue-heavy videos: each important spoken/subtitle line should have an ID such as `P01.V01`, parent speaker, speaker state, tone, emotional temperature, delivery style, pace, volume, pause pattern, bound visual units, bound post-edit units, BGM/SFX relation, subtitle relation, rhythm, function, remake delivery rule, and replacement rule.
- Audio-state table: BGM, live sound, SFX, silence, voice texture, and mix changes that alter emotion, rhythm, authority, comedy timing, or conversion pressure.
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
- Relationship-depth mapping for major scene, prop, proof, audio, and copy units: source relationships, source pressure field, target pressure field, replacement logic, and whether the surface shell is kept or changed.
- Copy child-unit mapping before final script lines. Preserve the line's function, bound units, tone, delivery style, emotional temperature, pause, and audio/subtitle relation before changing the words.
- Audio-unit mapping before final script lines. Preserve BGM/SFX/live-sound/silence functions that create the source's pressure, authority, joke timing, proof rhythm, or conversion push.
- Compliance/fact boundary.
- Deletion and addition choices.

## Shot Spirit And Human Copy Map

Must include one row per important source shot or source block:

- Source time and source shot/block.
- Viewer-before: the belief, worry, desire, doubt, or emotion before the shot.
- Trigger visual units: exact visible unit states and state changes.
- Trigger audio units: BGM, SFX, live sound, silence, voice texture, pace, pause, emphasis.
- Trigger copy units: source spoken/subtitle IDs and source line function.
- Viewer-after: the intended new belief, feeling, or urge.
- Psychology type: disgust, fear, relief, authority trust, "that is me", envy, value shock, proof satisfaction, social pressure, purchase urgency, joke payoff, or another specific psychology.
- Target-product remake requirement: the feeling/function to preserve, not just the object to show.
- Literal product fact: the plain factual target-product claim.
- Spoken seller/person line: the final human line that preserves source function and sounds sayable.
- AI-copy risk: what would make the line sound mechanical, educational, or generic.

If this map is missing, do not continue to the visual script.

## Visual Script

Each shot must specify:

- Time range.
- Which source shot/structure it aligns to.
- Which unit state change it carries.
- Which story beat it carries.
- Frame and background.
- Why this scene/background belongs to the target product's own proof or story pressure field, when it replaces a strong source scene shell.
- People positions, posture, gaze, expression, gesture.
- Product/prop state and hand actions.
- Subtitle and spoken text.
- Spoken delivery style: tone, emotional temperature, pace, pause, and volume when relevant.
- BGM/live sound/SFX/silence and their relation to the spoken line.
- Subtitle rhythm and whether it mirrors, compresses, exaggerates, or adds to the spoken line.
- Intended psychological beat.
- Viewer-before -> trigger-units -> viewer-after spirit diagnosis.
- Human-copy check: source line function, literal product fact, final spoken line, and why it sounds like a real person in this format.
- Unit-state clarity check: people, product, prop, scene, post-edit, audio, and user psychology states are specific enough to reconstruct the screen.

The picture/frame field should be one clear sentence, not a heavy multi-part breakdown, but it must not omit key units. Include critical spatial movement, who is present or absent, foreground/background frame, product/prop entry, and post-edit text/stickers when they affect the shot. Example: "车内前挡风 POV 看见男主把电动车从车前退到侧窗，女伴仍在后座冷脸，车门框压住下沿，头顶黄黑 `？！` 贴纸跟随移动。"

Avoid conceptual shots such as "show health" or "prove quality." Say what the camera sees.

For host-led, acted, or sales-led videos, each important spoken line should align to a source copy child unit (`Pxx.Vxx`) or a clearly added remake-only unit. If the line can stand alone as generic ad copy, it is probably not source-faithful enough.

If the words are visible but the tone cannot be inferred, mark the delivery as uncertain and state what evidence is missing. Do not replace an uncertain source delivery with generic enthusiasm.

Reject vague picture/action rows such as "展示产品", "展示效果", "进行对比", or "突出卖点" unless the row also names the exact visible units, their states, their positions, their actions, and the post-edit/audio units that create the user psychology.
