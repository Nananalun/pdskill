# Structured Unit Schema

Use this schema when the user needs units to serve later product recomposition, automation, or review.

## Minimal YAML Shape

```yaml
source_video:
  path:
  duration_sec:
  observed_genre:
  spirit_summary:

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

If these are missing, the unit graph is too thin.
