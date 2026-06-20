# Structured Unit Schema

Use this schema when the user needs units to serve later product recomposition, automation, or review.

## Minimal YAML Shape

```yaml
source_video:
  path:
  duration_sec:
  observed_genre:
  spirit_summary:

story_spine:
  premise:
  story_engine:
  product_bridge:
  payoff:

units:
  - id: U01
    label:
    type:
    core_function:
    sensory_anchor:
    remake_action:

unit_state_timeline:
  - time: "0-3s"
    states:
      U01:
      U02:
    spoken_lines:
      - speaker:
        text:
        certainty:
    relationship_change:
    event:
    evidence:

characters:
  - id: CH01
    role:
    objective:
    obstacle:
    power_position:
    knowledge_gap:
    expression_pattern:
    child_units:
      voiceover_copy:
        - id:
          time:
          text:
          speaker_state:
          tone:
          emotional_temperature:
          delivery_style:
          pace:
          volume:
          pause_pattern:
          bound_units: []
          bound_post_edit_units: []
          audio_relation:
          subtitle_relation:
          rhythm:
          function:
          remake_delivery_rule:
          replacement_rule:
    remake_role:

plot_beats:
  - id: PB01
    time: "0-3s"
    beat_type:
    cause:
    action:
    reaction:
    information_revealed:
    power_shift:
    product_bridge:
    source_units: []
    remake_rule:

structure_blocks:
  - id: B01
    time: "0-3s"
    function:
    objective:
    source_units: []
    psychology: []
    evidence:

element_units:
  people: []
  products: []
  props: []
  scenes: []
  problem_visuals: []
  proof_units: []
  text_graphics: []
  audio_units: []
  camera_editing: []
  performance_style: []
  whole_style: []

unit_events:
  - id: EV01
    time:
    units: []
    action:
    sensory_effect:

unit_relations:
  - from:
    to:
    relation:

mechanism_links:
  - id: M01
    mechanism:
    source_units: []
    effect:
    remake_rule:

shot_spirit_matrix:
  - id: SSM01
    source_time:
    source_shot_or_block:
    viewer_before:
    trigger_visual_units: []
    trigger_audio_units: []
    trigger_copy_units: []
    viewer_after:
    psychology_type:
    remake_requirement:
    evidence:

human_copy_map:
  - id: HCM01
    source_copy_unit:
    source_line_function:
    source_delivery:
    bound_visual_units: []
    bound_audio_units: []
    literal_target_product_fact:
    final_spoken_line:
    why_it_sounds_human:
    ai_copy_risk:

remake_requirements:
  sensory_similarity_targets: []
  must_keep: []
  must_replace: []
  optional_additions: []
  non_goals: []

uncertainties: []
```

If the source is not story-driven, set `story_spine` to a brief `not_story_driven` note and omit detailed `characters` / `plot_beats`.


## Chinese User-Facing Values

When this schema feeds a final delivery file, write all user-facing values in Chinese. Stable schema keys, IDs, provider names, paths, and raw quoted source text may remain as-is, but labels, functions, psychology descriptions, replacement rules, uncertainty notes, and final spoken lines should be Chinese.
## Unit Fields

For every important unit, capture:

- `id`: stable short ID.
- `category`: people/product/prop/scene/proof/text/audio/camera/editing/style.
- `label`: human-readable label.
- `role`: function in persuasion or sensory similarity.
- `attributes`: visible/audible facts.
- `actions`: time-bound actions.
- `state`: static/dynamic, before/after, clean/dirty, full/empty, open/closed.
- `time_range`: where it appears.
- `certainty`: high/medium/low.
- `sensory_anchor`: true/false.
- `remake_action`: keep/replace/delete/add/borrow-only.
- `replacement_function`: when replaced, what sensory function the new unit must preserve.

## Copy Child Unit Fields

For host-led, role-led, sales-led, acted, or dialogue-heavy sources, model important spoken copy and subtitle copy as child units of the speaker/person unit:

- `id`: stable child ID such as `P01.V01`.
- `parent_unit`: speaker/person ID.
- `time_range`: when the line appears.
- `text`: source line or subtitle.
- `speaker_state`: what state the speaker is in, such as investigating, refusing, discovering, proving, joking, closing.
- `tone`: calm, cold, warm, excited, teasing, annoyed, authoritative, anxious, urgent, intimate, flat, or uncertain.
- `emotional_temperature`: low/medium/high pressure, restrained/explosive, friendly/hostile, detached/involved.
- `delivery_style`: how the line is performed, such as short verdict, clipped phrases, flowing explanation, sales push, deadpan, whisper, shout, tease, complaint, expert explanation.
- `pace`: slow/medium/fast and whether the line accelerates or slows down.
- `volume`: low/normal/loud and whether it changes.
- `pause_pattern`: where the speaker pauses, breathes, repeats, or lets BGM/SFX fill the gap.
- `bound_units`: visual units the line depends on, such as sample array, prop, product close-up, proof table, user feedback.
- `bound_post_edit_units`: subtitles, red words, big numbers, arrows, stickers, charts, SFX.
- `audio_relation`: BGM/SFX/live-sound/silence units that reinforce or contrast with the line.
- `subtitle_relation`: whether subtitles mirror the line, compress it, exaggerate it, turn it into a verdict, or add new information.
- `rhythm`: phrase length, delivery style, pause, repetition, verdict style.
- `function`: sample source, test purpose, conflict, discovery, proof explanation, mechanism explanation, reveal, close.
- `remake_delivery_rule`: what speaking style, pressure, pace, pause, and audio relation must survive in the remake.
- `replacement_rule`: what function and relationships must be preserved when remapping to the user's product.

Do not write remake copy until these child units are mapped. A correct replacement preserves function and relationship first, then changes words.

If the text can be read but the delivery cannot be inferred, mark tone/delivery fields as `uncertain` and name the missing evidence. Do not overwrite uncertainty with generic enthusiasm.

## Audio Unit Fields

Create audio units whenever sound affects the source's spirit or pacing:

- `id`: stable ID such as `A01`.
- `type`: BGM, live_sound, SFX, silence, voice_texture, audio_mix.
- `time_range`: where the audio unit appears or changes.
- `mood`: tense, playful, calm, premium, authoritative, comic, urgent, sentimental, neutral, or uncertain.
- `tempo`: slow/medium/fast or approximate BPM if known.
- `intensity`: low/medium/high, including rises, drops, stingers, or silence breaks.
- `function`: hook pressure, authority, comedy timing, proof rhythm, transition, conversion push, realism, contrast.
- `state_changes`: time-coded changes such as BGM enters, beat drops, SFX hits, volume ducks under voice, silence before reveal.
- `bound_visual_units`: visual units the sound supports.
- `bound_copy_units`: copy child units the sound supports.
- `replacement_rule`: how the remake should preserve the same sound function without copying category-specific claims.

## Unit State Fields

For each timeline row, capture:

- `time`: exact or approximate time range.
- `states`: per-unit state. Include present/absent/offscreen, position, action, expression, product state, and whether the unit is speaking.
- `spoken_lines`: line-level speaker attribution with certainty.
- `relationship_change`: how unit relationships changed in this row.
- `event`: what happened as a consequence of state changes.
- `evidence`: frame, subtitle, audio, or post-edit evidence.

The timeline is not a summary. It is the source of truth used to derive story beats.

## Required Style Units

Always create IDs for:

- BGM or music function.
- BGM state changes and music-to-cut rhythm.
- Voice/spoken style, including tone, emotional temperature, pace, volume, and pause pattern.
- Audio mix or loudness pattern when it shapes the viewing experience.
- Silence when it marks a joke, reveal, authority beat, or conversion pressure.
- Subtitle rhythm and visual style.
- Whole-video visual texture.
- Editing density.
- Camera pattern.
- Main proof staging.
- Opening performance/directing pattern.
- Conversion-shot texture.

## Required Story Units

For scripted, role-play, conflict-led, or semi-scripted sources, always create IDs for:

- Stateful units including people, products, props, scene frames, text/stickers, BGM, live sound, and camera/editing.
- Presence/absence changes.
- Speaker attribution changes.
- Relationship changes.
- Plot premise.
- Main character objective.
- Skeptic/judge objective.
- Opening trigger.
- Conflict object.
- Knowledge gap or misunderstanding.
- Escalation beat.
- Product-entry bridge.
- Reversal or reveal.
- Conversion beat.
- Payoff/joke.

If required story units or style units are missing, the source graph is not ready for remapping.

## Required Shot-Spirit Units

For every important shot or block, capture:

- `viewer_before`: viewer belief, worry, desire, doubt, or emotion before the shot.
- `trigger_visual_units`: exact visual units and state changes that create the effect.
- `trigger_audio_units`: BGM/SFX/live sound/silence/voice delivery units that create the effect.
- `trigger_copy_units`: spoken or subtitle child units and their functions.
- `viewer_after`: viewer belief, feeling, or purchase urge after the shot.
- `psychology_type`: disgust, fear, relief, authority trust, "that is me", envy, value shock, proof satisfaction, social pressure, purchase urgency, joke payoff, or another specific psychology.
- `remake_requirement`: what the target-product remake must make the viewer feel or believe.

If these fields are missing, do not rely on a one-sentence spirit summary.

## Human Copy Map Fields

Before final remake lines, capture:

- `source_copy_unit`: source spoken/subtitle child unit ID.
- `source_line_function`: accusation, rejection, proof, result verdict, objection answer, value pressure, price pressure, CTA, joke, reversal, authority claim, or another exact function.
- `literal_target_product_fact`: plain product fact before rewriting.
- `final_spoken_line`: the line that should be spoken in the remake.
- `why_it_sounds_human`: why this line fits the source speaker/persona and delivery style.
- `ai_copy_risk`: what would make this line sound written, educational, abstract, repetitive, or generic.

Do not accept the final spoken line if it only paraphrases the selling point.
