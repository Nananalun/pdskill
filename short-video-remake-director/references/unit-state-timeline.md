# Unit State Timeline Rules

Use this reference for scripted, role-play, skit, conflict-led, acted, prank-like, or semi-scripted commerce videos.

## Core Rule

Do not start from plot. Start from units and their state changes over time. A good unit state timeline should let a reader reconstruct what happened without reading the story spine.

## What Counts As A Unit

Units include:

- People and roles.
- Products and product states.
- Props and scene frames.
- Background objects that affect meaning.
- On-screen subtitles, stickers, price cards, counters, product labels, and other post-edit units.
- BGM, live sound, SFX, silence, voice texture, and audio mix.
- Camera/editing units such as POV, window frame, insert shot, hard cut, split screen, zoom, montage.

## Required Timeline Fields

For each important time row:

- `time`
- `frame_state`: camera view and composition.
- `unit_states`: per-unit present/absent/offscreen, position, posture, expression, action, product state, whether it speaks, and any voice/audio state attached to it.
- `spoken_lines`: exact or approximate spoken/subtitle lines with speaker attribution, tone, delivery style, pace, pause pattern, audio relation, subtitle relation, and certainty.
- `relationship_change`: who blocks whom, who persuades whom, who leaves/returns, who gains or loses power.
- `post_edit_units`: subtitles, stickers, labels, price, BGM/SFX/silence/mix changes.
- `event`: what happened because of the state changes.
- `evidence`: frame/time, subtitle, audio, or TWE reference.

## State Changes To Look For

Always check for:

- A character leaving, returning, appearing alone, or becoming absent.
- A character speaking while offscreen.
- A subtitle that belongs to a different actor than the visible face.
- A prop or product appearing only after a state change.
- A post-edit sticker or price card changing the meaning of the scene.
- A camera cut that moves attention from one character to another.
- A BGM/SFX pause that marks a joke, reveal, or conversion push.
- A voice tone or delivery shift that changes power, authority, intimacy, threat, comedy, or sales pressure.
- A BGM, SFX, live-sound, silence, or mix change that carries the emotional beat more than the picture does.

## Speaker Attribution

Do not trust OCR/TWE alone for speaker identity. Assign each important line using:

1. Visible mouth movement.
2. Character position and timing.
3. Subtitle placement and color if meaningful.
4. Reaction shot.
5. Prior/following line logic.

If uncertain, write `uncertain` and explain the alternatives. Do not build causality on uncertain speaker attribution.

Speaker attribution is not enough. For each important line, also assign the likely speaking style from evidence: calm/cold/warm/urgent/flat/teasing/authoritative, short-phrase or flowing, fast or slow, loud or low, and where the line pauses. If delivery cannot be inferred, mark delivery as `uncertain` and do not let the remake default to generic enthusiasm.

## Quality Gate

Stop before story spine if:

- Main characters' presence/absence is unclear.
- Important spoken lines lack speaker attribution.
- Important spoken lines lack tone, delivery style, pause/audio relation, or explicit uncertainty.
- BGM/SFX/live-sound/silence changes that shape the beat are missing.
- The timeline skips a visible leave/return/reveal/insert/price-card change.
- The event chain cannot be reconstructed from the unit states alone.
- The inferred story contradicts a visible unit state.
