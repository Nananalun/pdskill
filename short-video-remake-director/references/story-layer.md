# Story Layer Rules

Use this reference for scripted, role-play, skit, conflict-led, acted, prank-like, or semi-scripted commerce videos.

## Core Rule

Do not reduce a story-driven source to "role drama" or "conflict." The remake must preserve the plot engine: who wants what, why it is blocked, what changes, who gains or loses power, and how the product enters without breaking the scene.

Story spine must be derived from a unit state timeline, not directly from a loose summary or TWE plot label. If a causal beat is not supported by a unit state change, spoken line, subtitle, edit, or post-edit unit, mark it uncertain instead of treating it as story fact.

## Required Story Extraction

Before writing product units or a remake script, first create a unit state timeline, then create a story spine:

1. `premise`: one sentence describing the scene situation.
2. `characters`: each main character's visible identity, objective, obstacle, knowledge gap, power position, expression/action pattern, and story function.
3. `trigger`: the event that starts the story.
4. `conflict_object`: what the characters appear to be fighting about before the product enters.
5. `product_bridge`: the exact line, action, misunderstanding, reveal, or prop that allows the product to enter the story.
6. `escalation`: why the seller can keep talking instead of being ignored.
7. `reversal`: who changes the meaning of the scene and how.
8. `payoff`: final joke, reveal, conversion, social proof, or price push.
9. `cause_effect_chain`: each beat must happen because of the previous beat, not because the script needs a selling point.
10. `story_nonnegotiables`: story beats that cannot be deleted without losing the source's identity.

## Story Beat Fields

Use stable `PBxx` IDs:

- `time`
- `beat_type`: trigger, accusation, defense, misunderstanding, product_bridge, proof, objection, reversal, price_push, payoff.
- `actor`
- `objective`
- `obstacle`
- `action`
- `reaction`
- `information_revealed`
- `power_shift`
- `product_bridge`
- `sensory_evidence`
- `remake_rule`

## Character Fields

Use stable `CHxx` IDs:

- `role`: seller, skeptic, judge, target, witness, helper, authority, buyer.
- `objective`: what they visibly want in the scene.
- `obstacle`: who or what blocks them.
- `power_position`: high, low, shifting, hidden, comic.
- `knowledge_gap`: what they know that others do not, or what the viewer does not yet know.
- `expression_pattern`: repeated face/gaze/posture.
- `action_pattern`: repeated movements.
- `story_function`: why this character exists beyond product explanation.
- `remake_boundary`: what can change and what must stay.

## Remap Rules

Map story before product:

1. Preserve the same story engine by default.
2. Replace product facts inside the existing story bridge, not by opening a new tutorial.
3. Keep the skeptic/judge role if the source uses one. Do not turn them into a second salesperson.
4. Keep the product-entry timing. If the source product enters at 30s, do not introduce the remake product at 2s unless the source does.
5. Keep the reversal/payoff timing and power shift.
6. If a source proof is unsafe, fake, or category-specific, replace its proof function while keeping its story position.
7. If the target product cannot plausibly fit the source story, state the conflict and design the smallest story adjustment.

## Quality Failures

Stop and revise if any of these happen:

- The story spine cannot be reconstructed from the unit state timeline.
- A causal statement says a character changed intent, but the timeline shows no visible state change, line, absence/return, or edit proving it.
- A speaker is assigned by OCR/TWE without frame or subtitle support.
- The remake has the source's props but not its cause-effect chain.
- Characters say selling points without a scene reason.
- The skeptic becomes a product explainer.
- The product appears earlier or later without a story reason.
- The final conversion shot no longer resolves or exploits the story conflict.
- The script could be used for any product after changing nouns.
