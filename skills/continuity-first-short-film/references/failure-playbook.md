# Failure Playbook

Use this reference when production cannot safely advance.

## Voice changes between shots

Likely cause: each TTS node generated a fresh voice from text instructions.

Response:

1. Stop full-scene generation.
2. Create one approved dry voice master per character.
3. Verify that downstream audio nodes receive the actual reference audio or supported voice asset, not only a textual ID.
4. Produce two validation lines per voice.
5. Regenerate only affected audio and dependent shots.

## Character identity changes

Likely causes: a combined cast sheet is the only reference, too many irrelevant references are connected, or seeds are being treated as identity controls.

Response: use independent character masters and only the angles and characters needed by the current shot. Keep costume and key prop states explicit. Seeds remain optional reproducibility parameters.

## Video output audio triggers a copyright or sensitive-audio policy error

Treat this as an output-level video-audio failure, not proof that the locked dry voice is invalid.

1. Identify the exact failed node and keep successful nodes untouched.
2. Retry only when allowed by the service and useful; do not loop repeatedly.
3. If supported, create a silent video variant with native audio generation disabled.
4. Preserve the approved dry voice.
5. If no lip-sync or AV-mux component exists, mark the shot for external lip sync or audio replacement.
6. Never change the approved voice or dialogue merely to evade a policy system.

If a normal rerun succeeds, keep the successful original shot and mark any silent recovery branch `UNUSED_RECOVERY_VERSION / DO_NOT_CONNECT / DO_NOT_EXPORT`.

## Native video contains unwanted ambience or effects

Approve picture and lip sync separately from the soundtrack. Mark native audio `TEMP_PREVIEW_AUDIO / NOT_FOR_FINAL_MIX`; mute it in post and use the locked dry dialogue with controlled ambience and effects.

## No automatic frame extraction

For hard continuity, ask the user to export the predecessor clip's last clear stable frame. It should contain no player UI, black frame, fade, subtitles, or watermark. Register it for the next dependent shot only.

If the shot does not truly require pixel-level action continuation, propose downgrading to soft continuity, but require the user to approve that creative tradeoff.

## Manifest is incomplete or summary-only

Do not select the next batch by guessing shot IDs. Preserve existing manifests and build a new complete canonical version from:

1. the approved script or revision;
2. the last complete manifest;
3. later decision notes and QA reports;
4. the locked asset registry;
5. completed-shot status.

Create a delta report. Reconcile shot count, gaps, duplicates, total duration, dialogue, speaker, asset references, and continuity before resuming generation.

## Total duration changes unexpectedly

Compare manifest versions by shot ID and explain every delta. An unexplained difference remains blocked. Do not hide the discrepancy by changing the reported total.

## Asynchronous video jobs have no result yet

Do not submit duplicates. Record the task or node IDs, stop, and query output status later. Tool acceptance is not media completion.

## One shot fails in a batch

Leave successful shots untouched. Report the failed shot's node ID, log ID, exception type, and message. Fix or retry only that shot, then resume from the dependency boundary.

## Tool cannot report audio duration

Do not claim the timing gate passed automatically. Ask the user to listen and inspect the timeline or download the audio for metadata measurement. Record the result as manual timing confirmation.
