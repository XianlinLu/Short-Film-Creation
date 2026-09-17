# Production Schema

Use this reference when creating or repairing registries, manifests, preflight reports, and statuses.

## Stable IDs

Recommended patterns:

```text
CHAR_<NAME>_V1_MASTER
CHAR_<NAME>_V1_<ANGLE>
VOICE_<NAME>_V1_MASTER_LOCKED
SCENE_<LOCATION>_V1_MASTER
PROP_<OBJECT>_V1_MASTER_LOCKED
EP01_SC02_SH014_VOICE_V1
EP01_SC02_SH014_VIDEO_V1
EP01_SC02_SH013_TAILFRAME_V1_LOCKED
```

Use exact project names. Never silently correct a name by replacing it with a homophone or a different character.

## Locked asset registry

Record at least:

| Field | Purpose |
| --- | --- |
| `ASSET_ID` | Stable canonical identifier |
| `TYPE` | Character, voice, scene, prop, continuity frame, audio, or video |
| `SOURCE_NODE` | Actual node that owns the media output |
| `STATUS` | Candidate, approved, locked, unused, or blocked |
| `FIXED_TRAITS` | Details that may not drift |
| `SCOPE` | Global, scene, shot, or next-shot-only |
| `NOTES` | Human decisions and post-production requirements |

## Canonical shot manifest

Every canonical version must contain the complete shot table, not only changes. Recommended fields:

| Field | Meaning |
| --- | --- |
| `SHOT_ID` | Unique ordered ID |
| `SCENE_ID` | Scene grouping |
| `DURATION` | Planned video duration |
| `SHOT_TYPE` | Dialogue, narration, or no dialogue |
| `DIALOGUE` | Exact approved text |
| `SPEAKER` | At most one speaker |
| `DIALOGUE_VOICE_MASTER` | Locked character-dialogue source |
| `NARRATION_TEXT` | Exact narration text, kept separate from dialogue |
| `NARRATION_VOICE_MASTER` | Locked narrator source |
| `CHARACTER_REFS` | Only actual on-screen characters |
| `SCENE_REF` | Locked location master |
| `PROP_REFS` | Required locked props |
| `ACTION` | One primary action |
| `CAMERA` | One primary camera setup |
| `MOUTH_RULE` | Speaker only, all closed, or not applicable |
| `CONTINUITY` | `HARD_CONTINUITY` or `SOFT_CONTINUITY` |
| `PREDECESSOR` | Required prior shot |
| `TAILFRAME_REQUIRED` | Boolean and exact composition-frame asset ID |
| `TAILFRAME_SCOPE` | Composition, camera, pose, and layout only |
| `IDENTITY_REFS_REATTACHED` | Character and scene references explicitly connected on this shot |
| `AUDIO_STATUS` | Readiness and approval state |
| `VIDEO_STATUS` | Readiness and approval state |
| `POST_AUDIO_ACTION` | Always mute native audio and replace it with approved narration/dialogue |
| `BLOCKER` | Exact unresolved dependency |

After repairs, compare old and new manifests by shot ID. Reconcile changes in shot count, total duration, dialogue, speaker, scene, asset references, and continuity. Unexplained deltas remain blocked.

## Status vocabulary

Use explicit compound statuses rather than a vague `done`:

```text
PENDING_MANUAL_REVIEW
APPROVED / LOCKED / DO_NOT_REGENERATE
AUDIO_READY
AUDIO_BLOCKED
VIDEO_READY
VIDEO_BLOCKED
GENERATED / MANUAL_AUDIO_QA_PENDING
GENERATED / MANUAL_QA_PENDING
APPROVED_PICTURE
APPROVED_PICTURE_AND_LIPSYNC
TEMP_PREVIEW_AUDIO / NOT_FOR_FINAL_MIX
MUTE_NATIVE_VIDEO_AUDIO_AND_REPLACE_WITH_APPROVED_TRACKS
PENDING_EXTERNAL_FINAL_AUDIO_MIX
UNUSED_RECOVERY_VERSION / DO_NOT_CONNECT / DO_NOT_EXPORT
BLOCKED_BY_PROP
BLOCKED_BY_TAILFRAME
BLOCKED_BY_DURATION
BLOCKED_BY_MANIFEST_DATA_MISSING
```

## Batch preflight

The report should include:

- exact shot range and scene boundary;
- per-shot audio and video readiness;
- separate narration and character-dialogue readiness;
- missing assets and real-tail-frame dependencies;
- actual generated node names and outputs;
- the next required human decision;
- a clear stopping condition.

An absent formal audio output is `TO_GENERATE`, not inherently a blocker. A missing visual asset may block video while leaving audio ready.

Every video row must name its character reference and scene reference even when a tail frame is attached. A tail frame with no reattached identity references is a preflight failure.

## Approval semantics

Only mark media approved after explicit user confirmation. Tool success proves that an output exists; it does not prove identity, acting, continuity, pronunciation, or artistic quality.
