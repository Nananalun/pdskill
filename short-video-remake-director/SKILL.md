---
name: short-video-remake-director
description: Short-video remake director workflow for competitor/reference videos. Use when the user asks to run or test a video, find a video's "神"/spirit, do 短视频复刻, 对标视频拆解, 元素单元拆解, 单元状态时间线, 说话人归属, 在场/缺席时间线, high-similarity scripts, 编导策略, 拍摄单, or remap a reference video to a product such as 紫砂水培罐 while preserving sensory similarity instead of producing generic scripts.
---

# Short Video Remake Director

## Core Rule

Treat every source video as a new directing problem. Do not reuse the last video's spirit. Find what makes this exact video feel like itself, then remap that feeling to the user's product with the smallest reasonable change.

Sensory similarity comes before theory. The audience feels casting, posture, camera distance, subtitles, BGM, voice style, rhythm, proof staging, texture, and editing before it understands the selling-point logic.

For scripted or semi-scripted videos, unit-state causality comes before story causality. Do not treat units as a static inventory. First track each important unit across time: whether it is present, absent, speaking, silent, moving, refusing, returning, proving, being revealed, or becoming a conversion prop. The story spine must be derived from this state timeline.

## Evidence Workflow

1. Confirm the source video path and product target.
2. Read metadata with `ffprobe`.
3. Run `scripts/prepare_video_evidence.py` to create frames, opening frames, tile images, audio, and waveform.
4. Inspect `overview_tile.jpg` and `opening_tile.jpg` before writing strategy.
5. If TwelveLabs/TWE is available, run it with fields for people, actions, expression, product, scene, proof, screen text, spoken text, BGM, SFX, camera, editing, visual texture, sensory anchors, and mechanism-vs-shell. For acted content, also request speaker attribution, presence/absence, plot beats, character objective, conflict, reversal, joke/payoff, and product-bridge fields. Treat TWE as evidence, not final judgment.
6. Cross-check TWE against keyframes. Manually add missing units, especially opening performance, BGM, spoken style, overall visual style, proof props, subtitle rhythm, conversion shots, speaker attribution, presence/absence, and plot causality.
   - For host-led, role-led, sales-led, or acted videos, treat spoken copy/subtitles as child units of the speaking person, not as standalone ad copy. Use IDs such as `P01.V01` and record the speaker identity, speaker state, bound visual evidence, bound prop/product/text units, rhythm, function, and replacement rule.
7. If the video is scripted, semi-scripted, role-play, skit, or conflict-led, write a unit state timeline before the story spine. Use `references/unit-state-timeline.md`.
8. Then write the story spine from the unit state timeline. Use `references/story-layer.md`.
9. Write source units before the remake script. Do not jump directly to remapping.

If TWE is unavailable, continue from local frames and mark the missing evidence.

## Required Output Order

For a full trial, output artifacts in this order:

1. Source evidence summary: video metadata, local frame evidence, TWE segment count/path if used.
2. Raw/TWE segment summary: compact timeline with purpose, visible evidence, spoken/screen text, and uncertainty.
3. Unit state timeline when the source is scripted or conflict-led: all important units, per-time presence/absence, speaker attribution, actions, states, relations, and post-edit units. It must be possible to reconstruct the video from this table alone.
4. Story spine when the source is scripted or conflict-led: plot premise, character objectives, knowledge gaps, conflict, beat-by-beat cause/effect, reversal, joke/payoff, product bridge, and what can/cannot be changed.
5. Source unit summary review: human-auditable table covering people, product, props, scene/background, problem visuals, proof, subtitles, voice/dialogue, BGM, live sound/SFX, camera, editing, performance style, whole-video style, sensory anchors, omissions.
6. Structured source graph: stable IDs for `units`, `unit_state_timeline`, `story_spine`, `plot_beats`, `character_arcs`, `structure_blocks`, `element_units`, `unit_events`, `unit_relations`, `mechanism_links`, `remake_requirements`, `uncertainties`.
7. Mechanism vs shell: what must be preserved because it creates the source's effect, and what must change because it is category-specific, false, risky, or incompatible.
8. High-similarity remap table: `source_unit_ids`, action `keep|replace|delete|add|borrow-only`, remake units, and reason.
9. Director brief: core mind, opening conflict, unit-state engine, story engine, main conversion shot, proof method, rhythm, visual style, deletion choices, sensory similarity target.
10. Visual script: shot-by-shot, with framing, actor positions, posture, gaze, hand actions, object state, unit state change, product entry, story beat, subtitle timing, voice style, BGM/SFX, live sound, psychological beat.
11. Shooting sheet and risks: props, people, scenes, must-capture shots, compliance risks, likely places where the remake will become generic.

Prefer writing these to files when the run is substantial. Use concise final chat summaries with file links.

Visual script picture descriptions should stay lightweight but complete. Use one clear sentence for the frame/action column, not a heavy start/middle/end breakdown, but include any key spatial move, absence/return, foreground/background, product/prop entry, and post-edit sticker that changes the shot. Example: "车内前挡风 POV 看见男主把电动车从车前退到侧窗，女伴仍在后座冷脸，车门框压住下沿，头顶黄黑 `？！` 贴纸跟随移动。"

When the user next asks for 每个镜头的开始帧, start frames, storyboard keyframes, or image-generation prompts from the approved visual script, hand off to `short-video-start-frame-director` instead of expanding this skill.

## Source Unit Rules

Use stable IDs and include both object units and style units. Do not bury style in prose. A unit is not only an object; it is a stateful entity over time.

Spoken copy is usually a sub-unit, not a free writing layer. For each important speaker, split voiceover/dialogue/subtitles into child units such as `P01.V01`. A copy child unit must state whose line it is, what state the speaker is in, what visible unit it is attached to, which post-edit text or sound reinforces it, what function it serves, and how it should be replaced. Do not convert the user's selling point directly into a polished ad sentence if the source speaker would not say it that way.

Minimum categories:

- People/casting: role, age/identity signal, clothing, status, power position, expression, gaze, posture, gesture sequence.
- Product: appearance, state, entry timing, hand interaction, repeated memory shots.
- Props: tools, containers, documents, stickers, screens, food, body parts, proof objects.
- Scene/background: authority background, kitchen, lab, street, bedroom, white background, clutter, premium environment.
- Problem visuals: failure texture, fear image, before state, unpleasant close-up, contradiction.
- Proof: reports, papers, certificates, lab, maps, comparisons, user feedback, before/after, social proof.
- Text/graphics: subtitles, title bars, lower thirds, red X, explosion words, highlighter, maps, diagrams, stickers, price.
- Audio: BGM mood/tempo/function, voice style, live sound, SFX, transition sounds, silence.
- Camera/editing: frame size, angle, movement, picture-in-picture, montage, cut density, repeated return pattern.
- Whole-video style: news, medical, UGC, white authority, role drama, street interview, premium lab, rough realness.
- Sensory anchors: the few units that make the source feel like itself.

For scripted or semi-scripted videos, add a unit-state layer, a story layer, and a performance layer. The unit-state layer captures each important unit's timeline state and relationships. The story layer captures plot premise, character objectives, obstacles, trigger, escalation, reversal, payoff, product bridge, and conversion logic. The performance layer captures who judges whom, who has power, what insecurity/desire is triggered, what micro-action reverses power, and how the product enables that reversal.

## Finding The "神"

Classify the source's primary spirit before remapping. Common examples:

- Story-driven commerce spirit: the plot is the carrier. Preserve the character objective, conflict, misunderstanding, reveal, reversal, and conversion bridge before changing product facts.
- Role-drama spirit: casting, social power, gaze, micro-expressions, blocking, insult/desire/reversal.
- Medicalized fear spirit: extreme problem, authority diagnosis, hidden cause visualization, product as targeted solution, proof stack, user sensory result.
- News/science spirit: anchor desk, yellow title bars, research pages, maps, data, lab, certificates, product technology, UGC collage.
- White-background authority spirit: pure background, sparse short phrases, BGM melody, precise object choreography, subtitle-as-verdict rhythm.
- UGC proof spirit: rough selfie, real room, user language, live sound, repeated result demonstrations.

Preserve the source shell by default. Change a shell only when it conflicts with product facts, audience, compliance, or shooting feasibility. If deleting a shell, replace its sensory function with an equivalent unit.

## Product Remap Rules

The product is not the only replacement unit. Remake-side people, props, scenes, proof, text, stickers, sounds, BGM, camera, edit rhythm, and performance may all need adding, deleting, or replacing.

For each source feature, decide:

- `mechanism_to_preserve`: why the source works.
- `shell_to_keep`: a visible/audible form that can remain.
- `shell_to_replace`: a form that must change.
- `replacement_sensory_function`: how the new unit recreates the same feeling.

Avoid turning a high-similarity remake into a generic tutorial. If the source is news-like, the remake should still feel like a news segment. If the source is drama-like, the remake should still feel acted and socially charged. If the source is a proof montage, the remake should still feel dense and evidence-led.

When the source is story-driven, map story roles before mapping product units:

- protagonist/seller role -> remake protagonist/seller role.
- judge/skeptic role -> remake judge/skeptic role.
- conflict object -> remake conflict object.
- product bridge -> truthful remake product bridge.
- reversal/payoff -> remake reversal/payoff with the same timing and power shift.

Before mapping story roles, map unit states. If a character leaves, returns alone, becomes silent, becomes absent, moves behind the car, starts speaking offscreen, or appears only as a post-edit sticker, that state change is often the real story mechanism.

Before writing remake copy, map copy child units. Preserve the original line's function and relationship graph before replacing words. Example: a measurement host's "我们征集了100个家庭常用的锅 / 就为了看看你们家用的那口" is not a generic hook; it is `sample source + test purpose` bound to sample visuals. Replace it with an equivalent action-based line such as "我们找了几种家里常见的发豆芽方法 / 就为了看看，想吃点养生豆芽，到底哪种发得稳", not with a detached selling-point line.

## Purple-Clay Sprouting Jar Baseline

When the target product is the 紫砂水培罐, read `references/zisha-product-baseline.md`.

Default selling priority for this product:

1. Health/养生 mind: self-sprouted at home, visible process, natural clay feel, more reassuring for family meals.
2. Result proof: pressure plate, light blocking, drainage, and clay structure help sprouts grow cleaner-looking, stronger, straighter, and crisper.

Do not lead with "easy tool" unless the user asks. Lead with health/养生 and use structure as proof.

## Quality Gates

- The source unit summary must appear before the remake script.
- For story-driven sources, the unit state timeline must appear before the story spine. If the timeline is missing or vague, stop and fix it before writing the story spine.
- The unit state timeline must include presence/absence, speaker attribution, state changes, relationship changes, and post-edit units. If looking only at the timeline does not reveal what happened in the video, the analysis is not ready.
- For story-driven sources, the story spine must be derived from the unit state timeline and appear before the source unit summary. If the story spine contradicts the state timeline, fix the timeline or spine before writing the remake.
- The story spine must name each main character's objective, obstacle, power position, knowledge gap, turning point, and payoff. "Short drama" or "conflict" alone is not enough.
- Every causal claim must point to a visible state change, spoken line, subtitle, edit, or post-edit unit. Do not infer causality only from the product's desired selling logic.
- The remake script must preserve the source story engine unless there is a clear compliance or product-truth reason to change it. If the engine changes, explain the replacement engine.
- In visual scripts, the picture/frame column must be concise but not lossy: one sentence should say what the camera sees and any critical movement or missing unit. If a key movement such as "vehicle moves from front windshield to side window" is omitted, revise the shot.
- The opening must be analyzed at higher resolution than the rest of the video.
- BGM, voice style, subtitles, overall visual style, and edit rhythm must have unit IDs.
- In host-led, acted, or sales-led sources, important spoken copy must be represented as speaker child units (`Pxx.Vxx`). If remake lines read like independent marketing copy rather than the source speaker's state-bound speech, revise before finalizing.
- The remake must explain why it still feels like the source.
- Avoid fake authority. Do not invent papers, certificates, patent claims, medical claims, product guarantees, or data.
- Avoid absolute claims such as guaranteed success, 100%, safe, cures, lowers blood sugar, or disease benefits.
- If a claim needs proof and no proof is available, replace the proof unit with a truthful equivalent such as real structure close-up, real comparison, family observation record, or explicit uncertainty.

## Resources

- `scripts/prepare_video_evidence.py`: extract metadata, keyframes, opening frames, tile images, mono audio, and waveform.
- `references/unit-state-timeline.md`: required unit status and relationship timeline rules for scripted, role-play, and conflict-led videos.
- `references/story-layer.md`: required story extraction and remap rules for scripted, role-play, and conflict-led videos.
- `references/unit-schema.md`: structured fields for the source graph.
- `references/output-contract.md`: required artifact shapes and file naming.
- `references/zisha-product-baseline.md`: purple-clay sprouting jar selling points and compliance boundaries.
