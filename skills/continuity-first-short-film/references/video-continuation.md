# Controlled Video Continuation

Use this reference before extending an approved clip. Independent short-shot generation remains the default. Native continuation is a controlled branch for direct same-scene action continuation, not a replacement for locked character, scene, prop, or voice assets.

## 1. Audit the live capability

Inspect the actual model and node schema. Classify the available operation as one of:

- `NATIVE_CONTINUATION`: the component explicitly extends or continues an input video's timeline;
- `VIDEO_REFERENCE`: the component accepts a video as a visual reference but creates a new clip;
- `NO_VIDEO_CONTINUATION`: neither capability is exposed.

Do not label `VIDEO_REFERENCE` as native continuation. Record the provider's current duration limits, continuation-round limit, whether the output is the appended segment or a full extended clip, accepted image/audio inputs, and any lip-sync or audio-generation behavior. Use the live schema as authority; model family names alone are insufficient.

## 2. Continuation eligibility gate

A shot is `CONTINUATION_READY` only when all conditions pass:

- the predecessor has a real video output and is human-approved and locked;
- both shots share the same scene, time, character identities, costume state, and relevant prop state;
- the next shot is a direct continuation of action, movement, performance, or camera motion;
- the predecessor contains no identity, anatomy, costume, scene, prop, or voice drift that would be carried forward;
- the next shot does not require a deliberate reset to a materially different camera setup or composition;
- a true `NATIVE_CONTINUATION` mode is exposed and accepts all required locked references;
- the continuation round remains within the live provider limit.

Use an independent shot instead for scene or time changes, age or costume changes, a new speaking setup, a major camera reset, identity recovery, or any shot whose predecessor already contains drift.

## 3. Required continuation inputs

Every continuation node must receive:

1. the approved predecessor video as `SOURCE_VIDEO`, scoped to motion, composition, pacing, camera, pose, and spatial continuity only;
2. the locked image reference for every on-screen character in the new shot;
3. the locked scene master;
4. only the locked props and costume-state references needed by the new shot;
5. the exact approved dialogue audio when the tool uses audio for lip-sync conditioning;
6. an explicit next-shot action and camera instruction from the canonical manifest.

Every image, audio, and source-video input above must be inserted as a real native material binding. A typed `@` name or asset alias is invalid. Verify `MATERIAL_BINDING_CHECK = PASS` before generating the continuation.

The continuation instruction must contain one definite action path and one definite camera path. Do not include alternative outcomes, optional gestures, approximate timing, or uncertain language. Resolve those decisions in the manifest before creating the continuation node.

Narration remains a separate audio asset and must not make visible characters speak. A source video never becomes a character master, scene master, voice master, or final-audio source.

If native continuation cannot accept required locked character or scene references, mark the shot `NATIVE_CONTINUATION_UNSAFE` and generate it independently.

## 4. Audio and voice rules

- Character identity comes from locked character images; voice identity comes from a locked voice master or approved shot dialogue.
- Do not rely on the predecessor video's native soundtrack to preserve voice identity.
- Do not ask a continuation model to invent new final dialogue.
- If dialogue lip sync is supported, condition with the approved dry dialogue while still treating the returned soundtrack as preview audio.
- If dialogue conditioning is not supported, generate picture only and complete lip sync or audio replacement with an available downstream component or external editor.
- Always mark continuation audio `TEMP_PREVIEW_AUDIO / NOT_FOR_FINAL_MIX` and replace it with approved narration and dialogue in the final edit.

## 5. Chaining discipline

Never submit an unchecked continuation chain. For each round:

1. generate one continuation;
2. verify that a real video output exists;
3. review identity, costume, props, scene, action boundary, camera, mouth behavior, voice, and audio contamination;
4. lock the approved picture or picture-and-lip-sync result;
5. only then allow it to become the next `SOURCE_VIDEO`.

Record `CONTINUATION_ROUND` and `MAX_CONTINUATION_ROUNDS`. Reset with a fresh independent anchor shot before the live limit, after a scene boundary, or at the first sign of accumulated drift.

## 6. Output handling

Record `EXTENSION_OUTPUT_MODE` as:

- `APPENDED_SEGMENT`: the output contains only the newly generated continuation; or
- `FULL_EXTENDED_VIDEO`: the output contains the source clip plus the new continuation.

Do not duplicate the predecessor during editing. For a full extended output, identify and export only the new segment or replace the earlier assembly deliberately.

## 7. Fallback order

When continuation is unavailable or unsafe:

1. generate the next shot independently with locked character, scene, prop, and approved audio references;
2. use soft continuity through matched camera, lens, eyeline, movement direction, palette, and edit timing;
3. if hard composition continuity is essential, use a real final stable frame from the predecessor as composition-only input;
4. if automatic extraction is unavailable, request one manual tail-frame upload for that dependency.

Never use a similar image, whole video, or regenerated approximation as a fake tail frame.

## 8. Failure recovery

If a continuation drifts, preserve all successful earlier shots and retry only the failed continuation from the last approved source. Reattach the complete locked reference set. If drift repeats, mark `FALLBACK_TO_INDEPENDENT_SHOT` and create a fresh independent shot instead of extending a corrupted result.

If the picture and lip sync pass but the generated soundtrack contains wrong voices, music, ambience, or effects, lock picture separately, keep the native soundtrack out of the final mix, and use the approved audio assets.
