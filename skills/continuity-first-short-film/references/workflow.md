# End-to-End Workflow

Use this reference when starting, auditing, or resuming a multi-shot AI short film. Every path uses short atomic shots. Independent generation is the default; native video continuation is allowed only for direct same-scene continuity after it passes the controlled-continuation gate. Every shot receives its locked character and scene references again.

## 1. Audit the current project

Inventory the script, node graph, existing outputs, model settings, and available component types. Detect common drift risks:

- independent voice generations without a reference voice connection;
- one multi-character reference image feeding every video node;
- video-native audio used as the final voice source;
- long clips containing multiple actions or camera changes;
- fixed seeds used as identity controls;
- shots generated in parallel despite hard continuity;
- a manifest that contains only updates rather than the full shot table.
- a tail frame being used as the only character or scene reference;
- narration and character dialogue baked into one uncontrollable video soundtrack.
- a reference-video node being mislabeled as native continuation;
- a continued shot relying on the predecessor video instead of reattaching locked character and scene references;
- unchecked continuation chains that accumulate face, costume, prop, or voice drift.
- video prompts that leave actions, camera moves, composition, timing, or asset states as uncertain alternatives.
- prompt text that names an image, audio, or video asset without creating a real Lumina material binding.

Do not mutate media during an audit unless the user asks for changes.

## 2. Create and lock assets

Create independent assets for recurring entities:

- character master, front, three-quarter, side, full-body, and critical costume or prop states;
- one dry voice master per recurring speaker;
- scene masters for recurring locations;
- prop masters and only the angles needed by upcoming shots.

Use stable IDs. Candidate assets stay `PENDING_MANUAL_REVIEW`; only a human can promote them to `APPROVED / LOCKED / DO_NOT_REGENERATE`.

Do not create every possible asset up front. Lock high-risk recurring assets before the batch that needs them.

## 3. Validate voices before production

For each speaker:

1. Generate a short dry sample.
2. Connect the resulting audio as the real reference input for at least two verification lines, including a neutral and an emotional line.
3. Have the user listen for identity, pronunciation, pacing, age, and emotional stability.
4. Lock the accepted master.

Names written in prompts are not voice references. A declared ID is useful only when it maps to an actual reusable audio output or supported voice asset.

## 4. Make short pilots

Create a few short pilots, commonly 4–8 seconds, that stress different risks: close-up identity, two-character dialogue, a location change, a prop close-up, and lip sync. Generate each pilot independently and reattach its character and scene references. Resolve systemic problems before producing the episode.

## 5. Build the canonical atomic-shot manifest

Split the script so each atomic shot has one primary action, one primary camera setup, and at most one character speaker. Preserve exact dialogue unless the user approves editorial changes.

Calculate duration from natural speech, action, and breathing room. A practical check is:

`audio duration + headroom + tailroom <= video duration`

Use project-specific margins; 0.3 seconds at the head and 0.4 seconds at the tail are a useful default. Do not solve an overlong line by silently speeding up, deleting, or rewriting it.

Keep a complete table in every canonical manifest version. Update statuses inside the table or merge changes into a new complete version; do not replace the table with a summary.

## 6. Preflight the next batch

Start at the first unproduced shot. Select the largest continuous set that:

- remains in one scene;
- respects the configured batch-size limit;
- does not skip an earlier dependency.

For every shot, produce separate `AUDIO_READY` and `VIDEO_READY` decisions. Also record `GENERATION_MODE = INDEPENDENT` or `NATIVE_CONTINUATION`. Missing visual props block video, not necessarily audio. A missing speaker, voice master, approved line, or viable duration blocks audio.

Before marking video ready, convert the manifest row into one deterministic video prompt. Specify one action, one camera setup, one composition, exact timing, exact character and prop states, and explicit mouth behavior. Do not include uncertainty or alternative choices such as `可能`, `或者`, `或许`, `也许`, `大概`, `似乎`, `尽量`, `适当`, `maybe`, `perhaps`, `possibly`, `either`, or `or`. If a creative choice is unresolved, block the shot instead of asking the video model to decide.

Resolve every required image, audio, and video asset to an actual Lumina material binding. Use the native `@` selector or an equivalent structured binding operation. Typed `@` names and aliases such as `图2=...` or `音频1=...` do not count. Apply [material-binding.md](material-binding.md) and block the shot if the stored bindings cannot be verified.

For proposed continuation shots, audit the actual component and apply [video-continuation.md](video-continuation.md). A video input does not by itself prove continuation support. If the next shot is not eligible or the component cannot accept the required locked references, use `INDEPENDENT`.

## 7. Generate audio first

Generate narration and character dialogue separately. Use one node per narration segment or character-speaking shot and connect the correct locked voice master. When narration and dialogue share the same picture, keep them as separate audio nodes or tracks. Generate clean speech with no music, ambience, sound effects, or reverb. Do not create fake empty audio for silent shots.

After generation, verify output existence and duration. Human review must confirm voice identity, exact text, pronunciation, emotion, and timing before the audio is locked.

## 8. Resolve visual dependencies and choose generation mode

Before video generation:

- lock required prop candidates and their useful angles;
- upload real final stable frames for hard-continuity shots when automatic extraction is unavailable;
- keep continuity frames scoped to the next dependent shot and use them only for composition, camera, pose, and spatial layout;
- require every new shot to reconnect its locked character, scene, and necessary prop references even when a tail frame is present.
- for native continuation, lock the approved predecessor video and scope it to motion, composition, pacing, camera, pose, and spatial continuity only;
- reject continuation for a scene/time/costume/age change, major camera reset, identity recovery, or a predecessor that already contains drift;
- record the continuation round, live provider limit, and whether the output is an appended segment or a full extended video.

## 9. Generate video in dependency order

For `INDEPENDENT` shots, generate a fresh short clip. For `NATIVE_CONTINUATION` shots, extend only the last human-approved predecessor. In both modes, reconnect the locked character image and locked scene image, plus only the props that shot needs. A predecessor video or tail frame may guide motion, composition, camera placement, pose, pacing, and spatial layout, but it must not become the source of character identity, costume, scene identity, prop identity, or voice identity. Submit only prompts whose `PROMPT_CERTAINTY_CHECK` and `MATERIAL_BINDING_CHECK` are both `PASS`.

Dialogue shots may use the locked dry dialogue for lip-sync conditioning if the model supports it. Narration stays on a separate audio asset and should not make visible characters speak.

Generate soft-continuity shots together only when they have no hard dependency on an unfinished predecessor. Generate one continuation round at a time and stop for human review before chaining it. If native continuation is unavailable, fall back to an independent shot; require a real tail frame only when hard composition continuity cannot be achieved otherwise.

## 10. Review and lock

Review adjacent shots in sequence, not only in isolation. Check:

- identity, age, face, hair, costume, and body proportions;
- prop geometry, placement, color, and state;
- scene layout, light direction, palette, and weather;
- dialogue accuracy, voice identity, volume, and lip sync;
- whether continuation has carried forward visual or audio drift;
- whether a full extended output would duplicate its source clip during editing;
- closed mouths for non-speakers and narration shots;
- cuts, eyelines, action continuity, and accidental extra people or text.

Rerun only failed shots. Lock approved picture/lip-sync separately from final audio.

## 11. Finish audio externally when needed

Every video model soundtrack is temporary. If the canvas lacks audio replacement or AV muxing, mark shots `PENDING_EXTERNAL_FINAL_AUDIO_MIX`. In the editor:

1. mute or remove native video audio;
2. place the locked narration track;
3. place the locked character-dialogue tracks;
4. add controlled ambience;
5. add deliberate sound effects;
6. add music last;
7. normalize loudness across the sequence.

Do not retain native video audio in the final delivery merely because the dialogue sounded correct. Replace it with the approved spoken tracks and controlled sound design.
