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

characters:
  - id: CH01
    role:
    objective:
    obstacle:
    power_position:
    knowledge_gap:
    expression_pattern:
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

remake_requirements:
  sensory_similarity_targets: []
  must_keep: []
  must_replace: []
  optional_additions: []
  non_goals: []

uncertainties: []
```

If the source is not story-driven, set `story_spine` to a brief `not_story_driven` note and omit detailed `characters` / `plot_beats`.

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

## Required Style Units

Always create IDs for:

- BGM or music function.
- Voice/spoken style.
- Subtitle rhythm and visual style.
- Whole-video visual texture.
- Editing density.
- Camera pattern.
- Main proof staging.
- Opening performance/directing pattern.
- Conversion-shot texture.

## Required Story Units

For scripted, role-play, conflict-led, or semi-scripted sources, always create IDs for:

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
