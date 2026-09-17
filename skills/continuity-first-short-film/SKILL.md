---
name: continuity-first-short-film
description: Plan, audit, and run continuity-safe AI short-film production from a script or an existing node canvas. Use when character identity, voice, props, locations, shot continuity, batch generation, or human approval gates must remain consistent across many generated shots.
---

# Continuity-First Short Film

Build the production around locked assets and explicit gates. Treat model outputs as candidates until a human approves them; never let downstream nodes infer identity or continuity from prose alone.

## Route the task

- For a new project or a full production plan, read [references/workflow.md](references/workflow.md).
- When creating or repairing manifests, registries, IDs, or statuses, read [references/production-schema.md](references/production-schema.md).
- When the user needs copy-ready instructions for a canvas agent, read [references/prompt-templates.md](references/prompt-templates.md).
- When a run fails, a manifest is incomplete, a tail frame is unavailable, or native audio is blocked, read [references/failure-playbook.md](references/failure-playbook.md).

Read only the references needed for the current stage.

## Establish the source of truth

Before generating media, identify:

1. The authoritative script or approved revision.
2. The canonical shot manifest.
3. The locked asset registry.
4. The latest completed and human-approved shot.
5. The next unproduced shot and its scene boundary.

Do not infer missing rows from a summary-only manifest. Recover or create a complete canonical manifest first. Preserve older manifests and create a new version when repairing material data loss.

## Preserve these invariants

- Give every character, voice, location, prop, shot, and continuity frame a stable asset ID.
- Use independent character masters and angle references. Do not use a multi-character composition sheet as the only identity reference.
- A seed may aid reproduction but never substitutes for a character or prop reference.
- Generate one speaker per audio node and one primary action with one primary camera setup per video shot.
- Keep spoken audio separate by character and shot. The approved dry voice is the final dialogue source.
- Treat model-generated video audio as preview audio unless the user explicitly approves it for the final mix.
- For narration, keep visible characters' mouths closed unless the script explicitly makes them speak.
- Use only the characters and props actually present in the shot.
- Do not cross scene boundaries merely to fill a batch.
- Use a real final stable frame for hard continuity. Never substitute an entire video, a similar image, or a newly generated approximation.
- Do not mark subjective quality as approved without explicit human review.
- Do not regenerate locked assets or successful shots to fix an unrelated failure.

## Separate the gates

Track audio readiness and video readiness independently.

An absent visual prop or continuity frame may block video without blocking an otherwise valid dry voice. Generate audio only when speaker, text, voice master, and timing are sound. Generate video only when every required visual asset and hard-continuity dependency is present.

When a batch contains a blocker, continue only with an unbroken prefix or with independently safe audio work. Do not skip a blocked shot if later shots depend on it.

## Work in small batches

Prefer scene-local batches of up to roughly six atomic shots unless the user chooses another batch size. For each batch:

1. Preflight against the canonical manifest and asset registry.
2. Generate and verify dry voices.
3. Wait for human audio approval.
4. Resolve missing props and tail frames.
5. Generate the currently executable videos.
6. Wait for human visual, identity, voice, and lip-sync approval.
7. Lock approved outputs and record post-production audio requirements.

If the canvas runs video jobs asynchronously, submit the intended scope, stop, then query results in a later turn. Do not silently submit duplicates.

## Adapt to actual tool capabilities

Inspect the live model schema and available components rather than assuming support for frame extraction, lip sync, audio replacement, or AV muxing. If a component is unavailable, record an explicit external post-production requirement instead of pretending the canvas completed it.

When video generation needs audio for lip sync, the generated soundtrack can still be temporary. Preserve the locked dry voice and plan to mute native video audio and replace it during final editing.

## Communicate the next safe action

Report:

- what is locked;
- what remains pending human review;
- the exact next shot range;
- separate audio and video blockers;
- required user actions such as listening, uploading a tail frame, or approving a prop;
- the stopping condition for the next run.

Provide copy-ready agent instructions when useful, but keep them scoped to one production stage. Avoid prompts that combine asset approval, unrestricted batch generation, and final delivery in one uncontrolled run.
