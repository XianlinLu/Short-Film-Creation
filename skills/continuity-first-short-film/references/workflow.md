# End-to-End Workflow

Use this reference when starting, auditing, or resuming a multi-shot AI short film.

## 1. Audit the current project

Inventory the script, node graph, existing outputs, model settings, and available component types. Detect common drift risks:

- independent voice generations without a reference voice connection;
- one multi-character reference image feeding every video node;
- video-native audio used as the final voice source;
- long clips containing multiple actions or camera changes;
- fixed seeds used as identity controls;
- shots generated in parallel despite hard continuity;
- a manifest that contains only updates rather than the full shot table.

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

Create a few 4–8 second pilots that stress different risks: close-up identity, two-character dialogue, a location change, a prop close-up, and lip sync. Use only locked assets. Resolve systemic problems before producing the episode.

## 5. Build the canonical atomic-shot manifest

Split the script so each shot has one primary action, one primary camera setup, and at most one speaker. Preserve exact dialogue unless the user approves editorial changes.

Calculate duration from natural speech, action, and breathing room. A practical check is:

`audio duration + headroom + tailroom <= video duration`

Use project-specific margins; 0.3 seconds at the head and 0.4 seconds at the tail are a useful default. Do not solve an overlong line by silently speeding up, deleting, or rewriting it.

Keep a complete table in every canonical manifest version. Update statuses inside the table or merge changes into a new complete version; do not replace the table with a summary.

## 6. Preflight the next batch

Start at the first unproduced shot. Select the largest continuous set that:

- remains in one scene;
- respects the configured batch-size limit;
- does not skip an earlier dependency.

For every shot, produce separate `AUDIO_READY` and `VIDEO_READY` decisions. Missing visual props block video, not necessarily audio. A missing speaker, voice master, approved line, or viable duration blocks audio.

## 7. Generate audio first

Use one node per speaking shot and connect the correct locked voice master. Generate clean speech with no music, ambience, sound effects, or reverb. Do not create fake empty audio for silent shots.

After generation, verify output existence and duration. Human review must confirm voice identity, exact text, pronunciation, emotion, and timing before the audio is locked.

## 8. Resolve visual dependencies

Before video generation:

- lock required prop candidates and their useful angles;
- upload real final stable frames for hard-continuity shots when automatic extraction is unavailable;
- keep continuity frames scoped to the next dependent shot rather than treating them as general character or scene references.

## 9. Generate video in dependency order

Connect only the references needed by each shot. Dialogue shots may use the locked dry voice for lip-sync conditioning if the model supports it. Narration shots should not make visible characters speak.

Generate soft-continuity shots together only when they have no hard dependency on an unfinished predecessor. Stop before a hard-continuity shot whose real tail frame is absent.

## 10. Review and lock

Review adjacent shots in sequence, not only in isolation. Check:

- identity, age, face, hair, costume, and body proportions;
- prop geometry, placement, color, and state;
- scene layout, light direction, palette, and weather;
- dialogue accuracy, voice identity, volume, and lip sync;
- closed mouths for non-speakers and narration shots;
- cuts, eyelines, action continuity, and accidental extra people or text.

Rerun only failed shots. Lock approved picture/lip-sync separately from final audio.

## 11. Finish audio externally when needed

If the canvas lacks audio replacement or AV muxing, mark shots `PENDING_EXTERNAL_FINAL_AUDIO_MIX`. In the editor:

1. mute or remove native video audio;
2. place the locked dry dialogue;
3. add controlled ambience;
4. add deliberate sound effects;
5. add music last;
6. normalize loudness across the sequence.

Do not use inconsistent model-generated ambience as the final sound bed merely because the dialogue sounded correct.
