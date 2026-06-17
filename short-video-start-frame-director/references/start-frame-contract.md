# Start Frame Output Contract

Use this contract when producing shot start frames from a visual remake script.

## Source Map

Each shot needs:

- `shot_id`: stable ID such as `G01`.
- `script_time_range`: time range copied from the visual script.
- `source_frame`: local path to the nearest or manually chosen source frame.
- `source_frame_reason`: why this frame is the best reference.
- `source_units_to_preserve`: camera distance, angle, blocking, actor posture, hand action, prop layout, background, light, roughness, and sensory anchor.
- `source_units_to_delete`: category-specific objects or risky elements that must not carry over.
- `remake_units_to_insert`: product, people, props, scene, action state, proof objects, and product facts.
- `overlay_plan`: counters, subtitles, stickers, price, labels, and timing as post-production.
- `uncertainty`: anything not visible, not proven, or not available to the image model.

## Prompt Package

Each shot prompt package should include:

```yaml
shot_id: G01
base_image_goal: ""
source_frame_reference: ""
product_reference_required: true
chinese_prompt: ""
english_prompt: ""
negative_prompt: ""
overlay_plan:
  include_in_generated_image: []
  add_in_post: []
product_fidelity_notes: []
acceptance_criteria: []
rejection_criteria: []
```

## Prompt Writing Rules

- Start with camera/framing and scene realism, not marketing language.
- Include exact actor positions, posture, gaze, hand action, product state, and prop layout.
- State the product material and structure only as visible requirements.
- For video-model start frames, avoid complex text inside the image. Put digital Chinese text in `overlay_plan.add_in_post`.
- Use physical labels only when they are proof objects, such as a date sticker, usage card, or price tag.
- Negative prompts must block source category leakage, product drift, fake text, wrong materials, wrong sprouts state, studio-ad styling, and impossible props.

## Purple-Clay Jar Negative Prompt Seeds

Use or adapt these when generating 紫砂水培罐 frames:

- no glass jar
- no plastic sprouting box
- no flowerpot
- no metal container
- no scattered sprouts
- no wilted sprouts
- no noodle-like sprouts
- no medical certificate
- no lab coat unless the source video uses a lab shell and the product claim supports it
- no fake Chinese text
- no polished studio advertisement if the source is street/UGC

## QC Checklist

For each generated frame, check:

- Source similarity: same camera distance, roughness, scene type, posture rhythm, and prop density.
- Product fidelity: correct jar shape, clay texture, parts, and sprouts state.
- Claim safety: no absolute safety, cure, guaranteed success, fake authority, or attack on competitors.
- Shot purpose: frame clearly supports the shot's role in the approved script.
- Continuity: adjacent start frames feel like the same video world.

If any check fails, regenerate or rewrite the prompt before moving on.
