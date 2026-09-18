# Lumina Material Binding Gate

Apply this gate to every prompt sent to an independent-video or continuation node. A readable asset name is not evidence that Lumina has attached the media.

## What counts as a real binding

A material is bound inside a video prompt only when the agent uses Lumina's native `@` material picker, or an equivalent structured API operation that creates the same bound mention token inside the prompt and stores the source asset ID and media object. In the UI this commonly appears as a colored bound token. Verify the underlying asset identity; color alone is not proof.

A canvas edge or material chip outside the prompt may also be required by the node schema, but it does not replace the required native `@` mention inside the prompt.

The following do not count:

- typing `@` followed by an asset name as ordinary text;
- writing `图1=...`, `图2=...`, `音频1=...`, or `视频1=...` without a real material object;
- copying a node title into the prompt;
- declaring an asset ID in Markdown;
- assuming a nearby canvas node is automatically available to the video node;
- creating only an input edge while leaving the in-prompt reference as plain text;
- using a prompt alias whose source material is not actually attached.

## Required binding procedure

For each shot:

1. Read the exact required assets from the canonical manifest.
2. Resolve each asset ID to the node that owns the approved media output.
3. In the final video prompt, insert each required asset with Lumina's native `@` selector. Select the exact asset result rather than typing its displayed name.
4. Create any required structured input connection when the node schema requires both a prompt mention and an input edge. The prompt mention remains mandatory.
5. Assign one explicit role to each bound material: character identity, scene identity, prop identity, continuity frame, continuation source video, dialogue audio, or narration audio.
6. Read the completed node back and verify the stored bindings against the manifest.

If the agent cannot create a native material mention or structured binding with the available tools, stop. Report the exact assets requiring manual binding. Do not substitute plain-text `@` names.

## Binding rules by media type

- Character image: bind every on-screen character's exact locked master or required angle.
- Scene image: bind the exact locked scene master.
- Prop image: bind only required locked props and states.
- Tail frame: bind the approved frame for the specified next shot only; scope it to composition continuity.
- Source video: bind only for an eligible native continuation; scope it to motion and composition continuity.
- Dialogue audio: bind the approved shot dialogue used for lip-sync conditioning, not the predecessor video's soundtrack.
- Narration audio: keep it separate unless the node explicitly accepts narration without driving visible mouths.

Do not bind unrelated materials. Excess references can cause identity and scene drift.

## Required validation record

Create this record before video submission:

```text
MATERIAL_BINDING_CHECK: PASS | FAIL
REQUIRED_MATERIALS: <asset ID + media type + role>
ACTUAL_BOUND_MATERIALS: <asset ID + media type + role>
PLAIN_TEXT_PSEUDO_MENTIONS: NONE | <exact text>
MISSING_BINDINGS: NONE | <asset IDs>
UNEXPECTED_BINDINGS: NONE | <asset IDs>
TYPE_MISMATCHES: NONE | <asset ID + expected type + actual type>
```

Set `PASS` only when:

- every required material appears in `ACTUAL_BOUND_MATERIALS`;
- the bound ID matches the required ID exactly;
- the media type and role are correct;
- `PLAIN_TEXT_PSEUDO_MENTIONS`, `MISSING_BINDINGS`, `UNEXPECTED_BINDINGS`, and `TYPE_MISMATCHES` are all `NONE`;
- the final prompt contains native material mentions for every asset it discusses.

Otherwise set `FAIL`, mark `VIDEO_BLOCKED_BY_UNBOUND_MATERIAL`, and do not submit generation.

## Example

Invalid:

```text
图2=SCENE_JEWELRY_SHOP_V1_MASTER。音频1=EP01_SC03_SH033_VOICE_V1。
```

Valid behavior:

1. Invoke Lumina's `@` material selector.
2. Select the actual `SCENE_JEWELRY_SHOP_V1_MASTER` image output.
3. Invoke the selector again and select the actual `EP01_SC03_SH033_VOICE_V1` audio output.
4. Verify both appear as bound materials with the correct IDs and media types.
5. Refer to those bound tokens directly in the final prompt.
