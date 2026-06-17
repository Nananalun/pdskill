---
name: short-video-remake-director
description: Short-video remake director workflow for competitor/reference videos. Use when the user asks to run or test a video, find a video's "神"/spirit, do 短视频复刻, 对标视频拆解, 元素单元拆解, 高相似脚本, 编导策略, 拍摄单, or remap a reference video to a product such as 紫砂水培罐 while preserving sensory similarity instead of producing generic scripts.
---

# Short Video Remake Director

## Core Rule

Treat every source video as a new directing problem. Do not reuse the last video's spirit. Find what makes this exact video feel like itself, then remap that feeling to the user's product with the smallest reasonable change.

Sensory similarity comes before theory. The audience feels casting, posture, camera distance, subtitles, BGM, voice style, rhythm, proof staging, texture, and editing before it understands the selling-point logic.

## Evidence Workflow

1. Confirm the source video path and product target.
2. Read metadata with `ffprobe`.
3. Run `scripts/prepare_video_evidence.py` to create frames, opening frames, tile images, audio, and waveform.
4. Inspect `overview_tile.jpg` and `opening_tile.jpg` before writing strategy.
5. If TwelveLabs/TWE is available, run it with fields for people, actions, expression, product, scene, proof, screen text, spoken text, BGM, SFX, camera, editing, visual texture, sensory anchors, and mechanism-vs-shell. Treat it as evidence, not final judgment.
6. Cross-check TWE against keyframes. Manually add missing units, especially opening performance, BGM, spoken style, overall visual style, proof props, subtitle rhythm, and conversion shots.
7. Write source units first. Do not jump directly to a remake script.

If TWE is unavailable, continue from local frames and mark the missing evidence.

## Required Output Order

For a full trial, output artifacts in this order:

1. Source evidence summary: video metadata, local frame evidence, TWE segment count/path if used.
2. Raw/TWE segment summary: compact timeline with purpose, visible evidence, spoken/screen text, and uncertainty.
3. Source unit summary review: human-auditable table covering people, product, props, scene/background, problem visuals, proof, subtitles, voice/dialogue, BGM, live sound/SFX, camera, editing, performance style, whole-video style, sensory anchors, omissions.
4. Structured source graph: stable IDs for `structure_blocks`, `element_units`, `unit_events`, `unit_relations`, `mechanism_links`, `remake_requirements`, `uncertainties`.
5. Mechanism vs shell: what must be preserved because it creates the source's effect, and what must change because it is category-specific, false, risky, or incompatible.
6. High-similarity remap table: `source_unit_ids`, action `keep|replace|delete|add|borrow-only`, remake units, and reason.
7. Director brief: core mind, opening conflict, main conversion shot, proof method, rhythm, visual style, deletion choices, sensory similarity target.
8. Visual script: shot-by-shot, with framing, actor positions, posture, gaze, hand actions, object state, product entry, subtitle timing, voice style, BGM/SFX, live sound, psychological beat.
9. Shooting sheet and risks: props, people, scenes, must-capture shots, compliance risks, likely places where the remake will become generic.

Prefer writing these to files when the run is substantial. Use concise final chat summaries with file links.

When the user next asks for 每个镜头的开始帧, start frames, storyboard keyframes, or image-generation prompts from the approved visual script, hand off to `short-video-start-frame-director` instead of expanding this skill.

## Source Unit Rules

Use stable IDs and include both object units and style units. Do not bury style in prose.

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

For scripted or semi-scripted videos, add a performance layer: who judges whom, who has power, what insecurity/desire is triggered, what micro-action reverses power, and how the product enables that reversal.

## Finding The "神"

Classify the source's primary spirit before remapping. Common examples:

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

## Purple-Clay Sprouting Jar Baseline

When the target product is the 紫砂水培罐, read `references/zisha-product-baseline.md`.

Default selling priority for this product:

1. Health/养生 mind: self-sprouted at home, visible process, natural clay feel, more reassuring for family meals.
2. Result proof: pressure plate, light blocking, drainage, and clay structure help sprouts grow cleaner-looking, stronger, straighter, and crisper.

Do not lead with "easy tool" unless the user asks. Lead with health/养生 and use structure as proof.

## Quality Gates

- The source unit summary must appear before the remake script.
- The opening must be analyzed at higher resolution than the rest of the video.
- BGM, voice style, subtitles, overall visual style, and edit rhythm must have unit IDs.
- The remake must explain why it still feels like the source.
- Avoid fake authority. Do not invent papers, certificates, patent claims, medical claims, product guarantees, or data.
- Avoid absolute claims such as guaranteed success, 100%, safe, cures, lowers blood sugar, or disease benefits.
- If a claim needs proof and no proof is available, replace the proof unit with a truthful equivalent such as real structure close-up, real comparison, family observation record, or explicit uncertainty.

## Resources

- `scripts/prepare_video_evidence.py`: extract metadata, keyframes, opening frames, tile images, mono audio, and waveform.
- `references/unit-schema.md`: structured fields for the source graph.
- `references/output-contract.md`: required artifact shapes and file naming.
- `references/zisha-product-baseline.md`: purple-clay sprouting jar selling points and compliance boundaries.
