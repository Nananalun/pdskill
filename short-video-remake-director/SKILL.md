---
name: short-video-remake-director
description: Short-video remake director workflow for competitor/reference videos. Use when the user asks to run or test a video, find a video's "神"/spirit, do 短视频复刻, 对标视频拆解, 元素单元拆解, 单元状态时间线, 说话人归属, 在场/缺席时间线, high-similarity scripts, 编导策略, 拍摄单, or remap a reference video to a product such as 膳砂坊紫砂水培育罐 while preserving sensory similarity instead of producing generic scripts.
---

# Short Video Remake Director

## Core Rule

Treat every source video as a new directing problem. Do not reuse the last video's spirit. Find what makes this exact video feel like itself, then remap that feeling to the user's product with the smallest reasonable change.

Sensory similarity comes before theory. The audience feels casting, posture, camera distance, subtitles, BGM, voice style, rhythm, proof staging, texture, and editing before it understands the selling-point logic.

Shot-level spirit comes before selling-point translation. For every important source shot, identify the viewer's mind before the shot, the exact visual/audio/copy units that trigger a change, and the viewer's mind after the shot. A shot that only says "show product", "prove quality", or "highlight selling point" has not been understood.

Human spoken copy comes before polished ad copy. Do not translate product facts directly into clean marketing lines. First identify the source line's function, speaker state, tone, pace, pause, and bound visual unit; then rewrite it as a line a real person in that source format would say.

For scripted or semi-scripted videos, unit-state causality comes before story causality. Do not treat units as a static inventory. First track each important unit across time: whether it is present, absent, speaking, silent, moving, refusing, returning, proving, being revealed, or becoming a conversion prop. The story spine must be derived from this state timeline.

Unit replacement must go one layer deeper than surface similarity. A scene, prop, person, line, sticker, or sound is not portable just because it looks like a sensory anchor. First identify why that unit exists, which other units it depends on, what proof pressure or story pressure it creates for the source product, and what equivalent pressure field the target product needs. Only then decide whether to keep, replace, delete, or borrow its function.
Final user-facing outputs must be Chinese. Use Chinese prose, section titles, table headers, shot descriptions, copy analysis, score summaries, and final chat responses. Stable IDs, file names, paths, provider names such as TWE/TwelveLabs, raw source quotations, code identifiers, and YAML schema keys may stay as-is, but every final reviewable delivery file must have a Chinese version. For full runs, write `中文最终交付.md` as the user-facing final delivery.
Before writing the final user-facing delivery, read `references/chinese-final-delivery-template.md` and follow its structure unless the user explicitly asks for another format. The template is the quality bar for no-context sessions: it must produce one integrated Chinese file that resembles the successful prior deliverable, not a loose pile of separate artifacts.

## Evidence Workflow

1. Confirm the source video path and product target.
2. Read metadata with `ffprobe`.
3. Run `scripts/prepare_video_evidence.py` to create frames, opening frames, tile images, audio, and waveform.
   - Use low-resolution contact sheets for quick overview only. If the source relies on tiny subtitles, hand micro-actions, product edges, skin/texture, stickers, or rough tabletop proof, keep or regenerate higher-resolution reference frames before final judgment.
   - On another computer, if `ffmpeg` or `ffprobe` is missing, install or locate them first instead of downgrading the workflow to text-only analysis.
4. Inspect `overview_tile.jpg` and `opening_tile.jpg` before writing strategy.
5. If TwelveLabs/TWE is available, run it with fields for people, actions, expression, product, scene, proof, screen text, spoken text, copy tone, delivery style, pauses, BGM, SFX, live sound, silence, camera, editing, visual texture, sensory anchors, and mechanism-vs-shell. For acted content, also request speaker attribution, presence/absence, plot beats, character objective, conflict, reversal, joke/payoff, and product-bridge fields. Treat TWE as evidence, not final judgment.
   - Prefer structured field outputs or explicit timecoded rows. Avoid relying on a single freeform summary.
   - If shell/terminal encoding corrupts Chinese prompts or paths, use an ASCII temporary path and an English structured prompt that requests Chinese output. Then cross-check against frames before trusting OCR or ASR.
6. Cross-check TWE against keyframes. Manually add missing units, especially opening performance, BGM, spoken style, overall visual style, proof props, subtitle rhythm, conversion shots, speaker attribution, presence/absence, and plot causality.
   - For host-led, role-led, sales-led, or acted videos, treat spoken copy/subtitles as child units of the speaking person, not as standalone ad copy. Use IDs such as `P01.V01` and record the speaker identity, speaker state, bound visual evidence, bound prop/product/text units, tone, emotional temperature, delivery style, pace, pause pattern, rhythm, function, audio relation, subtitle relation, and replacement rule.
   - For every important shot, add a shot-spirit row: `viewer_before -> trigger_units -> viewer_after`. Trigger units must name the exact image, sound, text, cut, sticker, line delivery, or actor state that changes the viewer's mind.
7. If the video is scripted, semi-scripted, role-play, skit, or conflict-led, write a unit state timeline before the story spine. Use `references/unit-state-timeline.md`.
8. Then write the story spine from the unit state timeline. Use `references/story-layer.md`.
9. Write source units before the remake script. Do not jump directly to remapping.

If TWE is unavailable, continue from local frames and mark the missing evidence.

## Proven Full-Run Playbook

This playbook is the actual workflow that produced acceptable results in prior tests. It freezes the method, not the creative template. Follow it as an execution recipe, not as optional advice, whenever the user says "跑这个视频", tests a new reference video, or asks for a high-similarity remake.

Every source video is a new directing problem. Do not reuse the last video's spirit, structure, proof rhythm, copy style, scene grammar, or emotional temperature. A nail-clipper proof montage, a car-window role drama, a white-background authority edit, a pillow health-lifestyle montage, and a host-led price offer all require different unit priorities. The examples below illustrate how to preserve mechanisms after discovering them; they are not templates to apply to unrelated videos.

### 0. Lock the task and product baseline

- Confirm the source video path and the target product.
- For 膳砂坊紫砂水培育罐, load the product library before remapping:
  - First try the live product library at `D:\Backup\Documents\短视频内容团队\product-library\shanshafang-zisha-hydroponic-jar\product-remake-library.md`.
  - If working in another checkout, also check the workspace-relative path `product-library/shanshafang-zisha-hydroponic-jar/product-remake-library.md`.
  - Treat that live product library as the source of truth for product units, user mind, evidence directions, replacement principles, and expression boundaries.
  - Read `references/zisha-product-baseline.md` only as a fallback or historical summary when the live product library is unavailable.
  - In every user-facing full run, state `本次产品信息源` and whether the live product library or fallback baseline was used.
- Treat the product priority as:
  1. Health/养生 mind: 家里自己发健康养生水培菜.
  2. Result proof: 满满一罐发得好的水培菜 is a high-priority proof direction when the source mechanism needs result proof or visual shock.
  3. Structure proof: 紫砂、避光盖、压盘、沥水篦、接水托 explain why the result can happen.
- Do not let the script drift into a usage tutorial unless the source itself is tutorial-led. Process is proof, not the lead selling point.
- Do not treat product-library evidence directions as fixed shots. The source video's unit functions decide the scene and frame. Use the product library only to choose truthful same-function replacement units.

### 1. Build evidence before judgment

Run `scripts/prepare_video_evidence.py` and save outputs under a per-video output directory. Minimum evidence:

- `metadata.json`
- `overview_tile.jpg`
- `opening_tile.jpg`
- `frames/`
- `opening_frames/`
- `audio_16k_mono.wav`
- `audio_waveform.png`

For dense visual sources, also create and inspect time-sliced detail tiles. For audio-sensitive sources, run simple audio diagnostics such as silence detection, volume/rms summary, or waveform inspection. Record whether there are long silences, short pauses, loudness shifts, BGM changes, live sound, SFX, or voice texture changes.

Do not write strategy from memory, from the user’s complaint, or from a single overview tile. Inspect frames first. If TWE disagrees with frames, the frames win unless the issue is audio-only.

### 2. Run TWE as structured evidence, not as final judgment

When TWE/TwelveLabs is available, prefer structured shot-level or time-based metadata fields over a freeform summary. Ask for dense segment fields like:

- `visual_description`
- `spoken_text`
- `speaker_attribution`
- `copy_tone_delivery`
- `screen_text`
- `people_casting_performance` or `people_hands`
- `character_objective`
- `plot_beat`
- `presence_absence`
- `actions_body_posture`
- `facial_expression`
- `product`
- `product_state`
- `scene_background`
- `props`
- `problem_visuals`
- `proof_units`
- `music`
- `sound_sfx_live`
- `audio_mix_timing`
- `rhythm`
- `camera`
- `editing`
- `post_edit_units`
- `sensory_anchors`
- `mechanism_vs_shell`
- `uncertainty`

Use 2-5 second segments when possible. Save:

- request body
- asset/task or provider ids if applicable
- final raw response
- parsed segment JSON
- human-readable `09-twelvelabs-segment-summary.v1.md`

If TWE returns too few segments, garbled OCR/ASR, or a generic summary, do not accept it. Use it only as a rough clue and manually reconstruct from local keyframes. If terminal encoding corrupts Chinese prompt/path handling, use an ASCII temporary path and an English structured prompt that requests timecoded output; then cross-check against local frames.

### 3. Source reconstruction comes before product remap

Before writing any remake script, produce a source-only reconstruction. The reader should be able to understand what happened in the original without seeing the video.

Required source reconstruction:

- Whole-video spirit in one sentence.
- Structure blocks with time range, purpose, visible evidence, audio/copy evidence, and why each block exists.
- Unit state timeline with stable IDs.
- Source unit summary review.
- Structured source graph.
- Mechanism-vs-shell judgment.

For non-story proof videos, the "story" is still a proof engine. Capture the sequence of proof pressure, not only objects. For example, in a nail-clipper source this may be pain close-up -> ordinary tool failure -> dedicated tool structure -> repeated proof benches -> material/accessory proof -> pain callback -> CTA. In another source, the engine may instead be role conflict, quiet authority, lifestyle aspiration, family testimony, price shock, sensory comfort, white-background rhythm, or BGM-led pacing. Discover the engine from evidence each time.

### 4. Unit-state timeline is not a static inventory

Write units as stateful entities over time. Include at least:

- People/hands/casting: real foot, hand model, white glove, host, family member, offscreen speaker.
- Product/tool states: absent, introduced, failed, compared, opened, used, cleaned, packaged, converted into price prop.
- Problem visuals: what physically looks wrong or uncomfortable.
- Proof props: reports, skeletons, ordinary containers, water, paper towel, sprouting result, packaging, date cards.
- Scene/background states: brown tabletop, white test table, black grid desk, kitchen, bed, factory, live room.
- Post-edit units: title bars, yellow bars, corner stickers, subtitles, arrows, red circles, dotted lines, warning signs, price cards.
- Audio units: BGM, voice, SFX, live sound, silence, mix density.
- Camera/editing units: macro, top-down, handheld, fixed phone close-up, fast cut, repeated return.

Track each important unit's presence/absence, position, action, state change, relation to other units, and function. If looking only at this timeline cannot reconstruct the video, the analysis is not detailed enough.

### 5. Copy and audio are child units, not decorative text

Every important spoken/subtitle line must be attached to the unit that carries it. Record:

- parent speaker or narrator
- speaker state
- bound visual units
- bound post-edit units
- tone
- emotional temperature
- pace
- pause pattern
- volume or pressure
- BGM/SFX relation
- subtitle relation
- function
- replacement rule

When remapping copy, preserve the line's source function before changing words. Do not convert a source-style short judgment or proof line into generic polished ad copy.

Audio units are equal to visual units. Record the role of BGM, live sound, SFX, silence, voice texture, and audio mix. If the source feels calm, sparse, and authoritative, do not remake it as excited shouting. If the source feels urgent, dense, and live-commerce-like, the remake must carry that pressure through delivery and subtitle rhythm.

### 6. Identify spirit through sensory anchors

Name the few units that make the source feel like itself. These are hard to delete:

- camera distance and roughness
- background type
- performer casting, posture, gaze, hand behavior
- subtitle shape and density
- BGM mood and pressure
- voice delivery
- proof staging
- repeated visual returns
- conversion-shot layout
- stickers/overlays when they define the source style

If deleting a sensory anchor, state the incompatibility and replace its function with an equivalent sensory unit. Do not delete it silently.

### 6.5 Build a shot-level spirit matrix

Before remapping, create a shot-level spirit matrix for the source's important shots or time blocks. This is not optional when the user has complained about "有型没神", generic remakes, AI-like copy, or vague visuals.

Each row must include:

- `source_time`
- `source_shot_or_block`
- `viewer_before`: what the viewer likely believes, worries about, wants, doubts, or feels before the shot.
- `trigger_visual_units`: exact visible units and state changes that affect the viewer.
- `trigger_audio_units`: BGM, SFX, live sound, silence, voice texture, pace, pause, or emphasis.
- `trigger_copy_units`: source spoken/subtitle line IDs and line function.
- `viewer_after`: the new belief, feeling, or urge the shot creates.
- `psychology_type`: disgust, fear, relief, authority trust, "that is me", envy, value shock, proof satisfaction, social pressure, purchase urgency, joke payoff, or another specific psychology.
- `remake_requirement`: what the target-product shot must make the viewer feel, not just what it must show.

If you cannot write this matrix, do not continue to the visual script. A one-sentence whole-video spirit is not enough.

### 7. Remap by relationship depth, not surface shape

Before making the remake-side inventory, run a relationship-depth check for the source's most important units. This is mandatory for scene/background units, proof props, comparison objects, spoken hooks, and any sensory anchor that looks tempting to copy.

For each important source unit, write:

- `surface_unit`: what is visible or audible.
- `source_relationships`: which people, product states, props, text, camera, audio, and edits it is bound to.
- `source_pressure_field`: the condition that makes this unit necessary. For example, a flashlight video needs darkness because darkness makes brightness testable; a sprouting jar needs kitchen failure/result conditions because those make health, freshness, drainage, and full-jar success testable.
- `source_function`: problem creation, proof, contrast, authority, scale, emotion, joke, price pressure, CTA, or rhythm.
- `target_pressure_field`: the target product's own environment where the same function can be truthfully proven.
- `replacement_logic`: keep only if the target product has the same pressure field; otherwise replace the unit while preserving its function and sensory force.

Scene units are especially relational. Do not directly copy night, bedroom, street, lab, car, white background, kitchen, or live-room shells until you can explain why the source product needed that environment. If the environment exists only to make the source product's function visible, replace it with the target product's own proof environment. Preserve the deeper mechanism, not the borrowed scene shell.

Examples:

- Night in a flashlight test is not automatically a "night aesthetic"; it is the pressure field that makes brightness, distance, and beam spread visible. For a purple-clay sprouting jar, the equivalent field is kitchen counter, sink, ordinary failed sprouting containers, same-seed comparison, open-lid full jar, drainage, and family table result.
- A white authority background may be a proof-pressure field for precise object choreography and sparse verdicts. Keep the clean background only if the target product can also prove itself through controlled object choreography; otherwise replace it with a truthful proof setting that carries the same authority.
- A car-window role drama scene may be a power-position field, not just a car shell. Replace the location only after preserving who controls attention, who is blocked, who returns, who is absent, and what state change creates the reversal.

If the remake keeps a surface unit whose pressure field no longer fits the target product, revise before writing the script. That is usually fake similarity: it preserves shape while losing the source's real mechanism.

### 8. Remap every category, not only the product

Build the remake-side unit inventory before scripting:

- target product/product states
- people/hands available
- scenes/backgrounds
- ordinary/failure comparison objects
- proof props
- result shots
- subtitles/stickers/overlay rules
- BGM/SFX/live sound
- camera/editing style
- compliance boundaries

Then map source units with `keep`, `replace`, `delete`, `add`, or `borrow-only`. Each row should cite source unit IDs and explain the reason. Also include the source unit's relationships, source pressure field, target pressure field, and replacement logic for scene/background, proof-prop, comparison, audio, and copy units. For 膳砂坊, possible replacements include the examples below, but only use the ones that fit the current source's discovered mechanism:

- body/tool pain shells can become failed home sprouting visuals only when the source relies on problem close-ups.
- product/tool structure shells can become purple-clay jar structure only when the source relies on mechanism proof.
- instant proof shells can become open-lid full jar, hand grabs dense sprouts, drainage works, or tray water poured away only when the source uses action proof.
- accessory/value shells can become five-piece set, cleaning, packaging, family table, or finished dish only when the source sells through completeness/value.
- live-commerce pressure can become real price `149` and truthful live-room/CTA only when the source's ending is conversion-pressure-led.
- If the source's core is casting, relationship, quiet authority, BGM melody, white background, sparse short phrases, or role power, preserve those sensory functions first and choose different remake-side units.

### 9. Director brief before visual script

Before the shot table, write a director brief:

- core mind
- opening conflict
- unit-state engine
- proof engine or story engine
- source pressure field and target pressure field
- main conversion-shot group
- proof method
- visual style
- audio style
- what to delete
- what to preserve for sensory similarity
- what would make the remake become generic

If this brief cannot clearly explain why the remake still feels like the source, do not write the script yet.

### 10. Visual script must be shootable and source-faithful

For each shot, include:

- shot id and time range
- source alignment
- one clear picture/action sentence that says what the camera sees
- people/hands state
- product/prop state
- spoken text/subtitle
- delivery style
- BGM/SFX/live sound/overlay state
- psychological beat
- viewer-before -> trigger-units -> viewer-after spirit diagnosis
- human-copy check: source line function, literal product fact, final spoken line, and why it sounds like a person in this format
- unit-state clarity: people/product/prop/scene/post-edit/audio states must be clear enough to reconstruct the screen

The picture/action sentence should be concise but not lossy. It must include key spatial movement, foreground/background, product/prop entry, absence/return, and post-edit unit if it changes meaning.

Do not write conceptual frames such as "show health", "prove quality", or "display structure". Say what the camera sees: "普通塑料盒里水积在底部，稀疏豆芽贴着盒底，手晃盒子让浑水反光."

Reject AI-like copy during visual script review. Red flags include abstract nouns, long causal explanations, repeated sentence patterns, brand-first introductions before pain is felt, and lines that would not be spoken by the source format's speaker. Rewrite by moving from literal product fact to spoken seller/person line. Example: product fact "the drainage structure reduces root soaking" becomes "水别闷根"; product fact "pressure plate helps sprouts grow thicker" becomes "压住才粗"; result claim "full jar result proves value" becomes "看这一罐."

### 11. Review against failure modes

Before finalizing, explicitly check:

- Did the main selling point stay health/养生 for 膳砂坊?
- When the source mechanism needs result proof or visual shock, did the remake keep a strong product-library-consistent result proof instead of drifting into tool display?
- Did process/structure stay proof instead of becoming the main story?
- Does the script preserve the source's camera/background/subtitle/audio/proof rhythm?
- Did scene and prop replacements come from the target product's own proof/story pressure field instead of directly copying the source shell?
- Did copy inherit source tone and function, or become generic ad copy?
- Are BGM, voice style, SFX, live sound, and pauses represented?
- Are post-edit units represented as units, not vague "字幕"?
- Are product claims within the baseline and compliance boundaries?
- Would the user recognize which source video this remake came from?

If any answer fails, revise before final response.

## Required Output Order

For a full trial, output artifacts in this order:

1. Source evidence summary: video metadata, local frame evidence, TWE segment count/path if used.
2. Raw/TWE segment summary: compact timeline with purpose, visible evidence, spoken/screen text, and uncertainty.
3. Unit state timeline when the source is scripted or conflict-led: all important units, per-time presence/absence, speaker attribution, actions, states, relations, and post-edit units. It must be possible to reconstruct the video from this table alone.
4. Story spine when the source is scripted or conflict-led: plot premise, character objectives, knowledge gaps, conflict, beat-by-beat cause/effect, reversal, joke/payoff, product bridge, and what can/cannot be changed.
5. Source unit summary review: human-auditable table covering people, product, props, scene/background, problem visuals, proof, subtitles, voice/dialogue, BGM, live sound/SFX, camera, editing, performance style, whole-video style, sensory anchors, omissions.
6. Structured source graph: stable IDs for `units`, `unit_state_timeline`, `story_spine`, `plot_beats`, `character_arcs`, `structure_blocks`, `element_units`, `unit_events`, `unit_relations`, `mechanism_links`, `remake_requirements`, `uncertainties`.
7. Mechanism vs shell plus relationship-depth check: what must be preserved because it creates the source's effect; what must change because it is category-specific, false, risky, incompatible, or outside the target product's proof/story pressure field; and how each major scene/prop/copy/audio unit relates to other units.
8. Shot-level spirit and human-copy map: `source_time`, viewer-before, trigger visual/audio/copy units, viewer-after, psychology type, source line function, literal target fact, final spoken rewrite, and remake requirement.
9. High-similarity remap table: `source_unit_ids`, action `keep|replace|delete|add|borrow-only`, source relationships, source pressure field, target pressure field, remake units, and reason.
10. Director brief: core mind, opening conflict, unit-state engine, story engine, main conversion shot, proof method, rhythm, visual style, deletion choices, sensory similarity target.
11. Visual script: shot-by-shot, with framing, actor positions, posture, gaze, hand actions, object state, unit state change, product entry, story beat, subtitle timing, voice style, BGM/SFX, live sound, psychological beat, and shot-level spirit diagnosis.
12. Shooting sheet and risks: props, people, scenes, must-capture shots, compliance risks, likely places where the remake will become generic.

Prefer writing these to files when the run is substantial. Use concise final chat summaries with file links.
After writing the structured artifacts, write `中文最终交付.md` using `references/chinese-final-delivery-template.md`. This is the file the user should read first. It must summarize the source spirit, important units, unit relationships, remap strategy, human copy map, and visual script in Chinese. It must use the integrated Chinese sections and visual-script table shape from the template. Run a simple Latin-letter scan or manual review and remove non-essential English from prose and table headers. English may remain only for stable IDs, filenames, paths, provider names, raw source text, code identifiers, and YAML keys.

Visual script picture descriptions should stay lightweight but complete. Use one clear sentence for the frame/action column, not a heavy start/middle/end breakdown, but include any key spatial move, absence/return, foreground/background, product/prop entry, and post-edit sticker that changes the shot. Example: "车内前挡风 POV 看见男主把电动车从车前退到侧窗，女伴仍在后座冷脸，车门框压住下沿，头顶黄黑 `？！` 贴纸跟随移动。"

When the user next asks for 每个镜头的开始帧, start frames, storyboard keyframes, image-generation prompts, or video-model first frames from the approved visual script, stop using this skill as the executor and hand off to `short-video-start-frame-director`. The remake script is only Stage A. Stage B must produce source maps, prompt packages, base images, overlay plans, generated frames when possible, and QC.

## Source Unit Rules

Use stable IDs and include both object units and style units. Do not bury style in prose. A unit is not only an object; it is a stateful entity over time.

Spoken copy is usually a sub-unit, not a free writing layer. For each important speaker, split voiceover/dialogue/subtitles into child units such as `P01.V01`. A copy child unit must state whose line it is, what state the speaker is in, what visible unit it is attached to, which post-edit text or sound reinforces it, what function it serves, and how it should be replaced. Do not convert the user's selling point directly into a polished ad sentence if the source speaker would not say it that way.

A spoken line is incomplete if it only records "what it means." It must also record how it is said: calm or heated, cold or friendly, flat or teasing, authoritative or casual, short-phrase verdict or flowing explanation, fast or slow, loud or low, where it pauses, and whether BGM/SFX/subtitles carry the pressure. The remake line must inherit the source line's speaking function and emotional temperature before changing the words.

Audio units are equal to visual units. BGM, live sound, SFX, silence, voice texture, and the audio mix must have IDs when they affect the source's spirit. Track their time range, mood, tempo, intensity, state changes, and what visual/copy units they bind to. If the source relies on calm BGM plus sparse short phrases, do not remake it into excited sales talk. If the source relies on urgent pressure, the remake copy must keep that pressure through delivery, not only through meaning.

Minimum categories:

- People/casting: role, age/identity signal, clothing, status, power position, expression, gaze, posture, gesture sequence.
- Product: appearance, state, entry timing, hand interaction, repeated memory shots.
- Props: tools, containers, documents, stickers, screens, food, body parts, proof objects.
- Scene/background: authority background, kitchen, lab, street, bedroom, white background, clutter, premium environment.
- Problem visuals: failure texture, fear image, before state, unpleasant close-up, contradiction.
- Proof: reports, papers, certificates, lab, maps, comparisons, user feedback, before/after, social proof.
- Text/graphics: subtitles, title bars, lower thirds, red X, explosion words, highlighter, maps, diagrams, stickers, price.
- Audio: BGM mood/tempo/function, voice style, tone, emotional temperature, pace, volume, pause pattern, live sound, SFX, transition sounds, silence, audio mix.
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

Preserve the source shell only after the relationship-depth check says the shell still belongs to the target product's proof or story pressure field. Change a shell when it conflicts with product facts, audience, compliance, shooting feasibility, or the target product's own proof logic. If deleting a shell, replace its sensory function with an equivalent unit.

## Product Remap Rules

The product is not the only replacement unit. Remake-side people, props, scenes, proof, text, stickers, sounds, BGM, camera, edit rhythm, and performance may all need adding, deleting, or replacing.

For each source feature, decide:

- `mechanism_to_preserve`: why the source works.
- `unit_relationships`: which other units give this feature meaning.
- `source_pressure_field`: why this feature was necessary for the source product or story.
- `target_pressure_field`: where the target product can truthfully create the same proof/story pressure.
- `shell_to_keep`: a visible/audible form that can remain.
- `shell_to_replace`: a form that must change.
- `replacement_sensory_function`: how the new unit recreates the same feeling.

Avoid turning a high-similarity remake into a generic tutorial. If the source is news-like, the remake should still feel like a news segment. If the source is drama-like, the remake should still feel acted and socially charged. If the source is a proof montage, the remake should still feel dense and evidence-led.

Do not replace by category name alone. "Night" does not map to night, "lab" does not map to lab, "car" does not map to car, and "white background" does not map to white background until their unit relationships are understood. Replace the reason the unit exists, then choose the target product's most truthful scene, prop, sound, and action to carry that reason.

When the source is story-driven, map story roles before mapping product units:

- protagonist/seller role -> remake protagonist/seller role.
- judge/skeptic role -> remake judge/skeptic role.
- conflict object -> remake conflict object.
- product bridge -> truthful remake product bridge.
- reversal/payoff -> remake reversal/payoff with the same timing and power shift.

Before mapping story roles, map unit states. If a character leaves, returns alone, becomes silent, becomes absent, moves behind the car, starts speaking offscreen, or appears only as a post-edit sticker, that state change is often the real story mechanism.

Before writing remake copy, map copy child units. Preserve the original line's function, relationship graph, delivery style, and emotional temperature before replacing words. Example: a measurement host's "我们征集了100个家庭常用的锅 / 就为了看看你们家用的那口" is not a generic hook; it is `sample source + test purpose` bound to sample visuals, said with a specific pace and proof-seeking posture. Replace it with an equivalent action-based line such as "我们找了几种家里常见的水培菜培育方式 / 就为了看看，想在家吃点养生水培菜，到底哪种发得稳", not with a detached selling-point line.

## Purple-Clay Sprouting Jar Baseline

When the target product is the 膳砂坊紫砂水培育罐, read the live product library first:

1. `D:\Backup\Documents\短视频内容团队\product-library\shanshafang-zisha-hydroponic-jar\product-remake-library.md`
2. `product-library/shanshafang-zisha-hydroponic-jar/product-remake-library.md` relative to the current workspace, if present.

Use it as the source of truth for product understanding. It overrides the bundled baseline when they differ. If neither live path exists, read `references/zisha-product-baseline.md` as fallback and clearly mark the product source as fallback in the outputs.

The product library is not a fixed shot template. It provides product units, user psychology, evidence directions, replacement principles, and compliance boundaries. Always remap from the source video's unit function first, then choose a target-product unit that carries the same proof/story/sensory role.

Default selling priority for this product:

1. Health/养生 mind: self-grown water-cultivated vegetables at home, natural purple-clay feel, more reassuring for family meals.
2. Result display: a full jar of well-grown water-cultivated vegetables is a high-priority proof direction when the source mechanism needs result proof or visual shock; bean sprouts are one common result, not the whole category.
3. Proof support: usage steps, pressure plate, light blocking, drainage, and clay structure are evidence for the result, not the main selling point.

Do not lead with "easy tool" or a usage tutorial unless the user asks. Lead with health/养生 and full-jar result display, then use structure and process as proof.

## Quality Gates

- The source unit summary must appear before the remake script.
- For story-driven sources, the unit state timeline must appear before the story spine. If the timeline is missing or vague, stop and fix it before writing the story spine.
- The unit state timeline must include presence/absence, speaker attribution, state changes, relationship changes, and post-edit units. If looking only at the timeline does not reveal what happened in the video, the analysis is not ready.
- For story-driven sources, the story spine must be derived from the unit state timeline and appear before the source unit summary. If the story spine contradicts the state timeline, fix the timeline or spine before writing the remake.
- The story spine must name each main character's objective, obstacle, power position, knowledge gap, turning point, and payoff. "Short drama" or "conflict" alone is not enough.
- Every causal claim must point to a visible state change, spoken line, subtitle, edit, or post-edit unit. Do not infer causality only from the product's desired selling logic.
- Every important source shot must have a viewer-before -> trigger-units -> viewer-after spirit diagnosis. If this is missing, the remake will likely have shape without spirit.
- Final remake copy must pass the human-copy gate: it must preserve the source line's function and sound like a real person in that video format, not a product manual or AI summary.
- Every important visual-script row must be reconstructable from text. If people, product, prop, scene, post-edit, audio, and user psychology states are vague, revise the row.
- The remake script must preserve the source story engine unless there is a clear compliance or product-truth reason to change it. If the engine changes, explain the replacement engine.
- In visual scripts, the picture/frame column must be concise but not lossy: one sentence should say what the camera sees and any critical movement or missing unit. If a key movement such as "vehicle moves from front windshield to side window" is omitted, revise the shot.
- The opening must be analyzed at higher resolution than the rest of the video.
- BGM, voice style, subtitles, overall visual style, and edit rhythm must have unit IDs.
- In host-led, acted, or sales-led sources, important spoken copy must be represented as speaker child units (`Pxx.Vxx`). If remake lines read like independent marketing copy rather than the source speaker's state-bound speech, revise before finalizing.
- If a source line's tone, delivery style, pace, pause, emotional temperature, BGM relation, or subtitle relation is missing, the copy unit is not ready for remapping. If the tone cannot be inferred from evidence, mark it as uncertain instead of filling in generic enthusiasm.
- The visual script must carry audio with the shot: spoken text plus delivery style, BGM state, live sound/SFX, silence if meaningful, and subtitle rhythm. A script that preserves pictures but loses speaking style or music pressure is not source-faithful.
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
- `references/chinese-final-delivery-template.md`: required integrated Chinese final delivery template and self-check list.
- `references/zisha-product-baseline.md`: purple-clay sprouting jar selling points and compliance boundaries.
