# Canvas-Agent Prompt Templates

Use these as building blocks. Replace placeholders with actual IDs read from the project. Keep one stage per prompt.

## 1. Batch preflight

```text
Read the canonical manifest and locked asset registry.

Start at <FIRST_UNPRODUCED_SHOT>. Select up to <BATCH_SIZE> consecutive shots without crossing a scene boundary or skipping a dependency.

Create <BATCH_PRECHECK_NODE>. For each shot record exact dialogue, speaker, voice master, on-screen characters, scene, props, action, camera, mouth rule, continuity type, tail-frame dependency, AUDIO_READY/AUDIO_BLOCKED, VIDEO_READY/VIDEO_BLOCKED, and the exact blocker.

Missing visual assets block video but do not block valid audio. Do not generate media in this run. Stop after writing and verifying the preflight.
```

## 2. Formal dry voices

```text
Use <BATCH_PRECHECK_NODE>. Generate audio only for AUDIO_READY speaking or narration shots.

Create separate narration and character-dialogue nodes. Use <SHOT_ID>_NARRATION_V1 for narration and <SHOT_ID>_DIALOGUE_<CHARACTER>_V1 for character speech. Connect the actual locked narrator or character voice master. If both occur over one shot, keep both nodes. Use the exact approved text; do not add names, stage directions, or explanations. Output clean speech only: no music, ambience, effects, or reverb.

Silent shots remain NO_DIALOGUE and receive no fake empty audio. Record output existence and duration, then mark each result GENERATED / MANUAL_AUDIO_QA_PENDING. Do not generate video or approve audio. Stop for human listening.
```

## 3. Lock approved audio and generate video

```text
The user has approved the batch's formal audio. Mark those nodes APPROVED / LOCKED / DO_NOT_REGENERATE.

Recheck video gates. Generate each executable shot as an independent short clip in dependency order. On every shot, reconnect its actual locked character image and locked scene image, then add only the required locked props and approved dialogue audio. A predecessor tail frame may also be connected, but only to control composition, camera, pose, and spatial layout; it never replaces character, costume, scene, or prop references.

Only the character speaker may move their mouth; narration stays separate and keeps visible characters' mouths closed. Do not add text, subtitles, watermarks, extra people, or extra dialogue. Treat native video audio as TEMP_PREVIEW_AUDIO / NOT_FOR_FINAL_MIX and always replace it with approved narration and dialogue in the final mix.

Stop before any hard-continuity shot whose real predecessor frame is absent. Mark outputs GENERATED / MANUAL_QA_PENDING and stop for human review.
```

## 4. Lock a human-approved batch

```text
The user has reviewed <SHOT_RANGE> in sequence and approves identity, props, scene, action, dialogue, voice, mouth behavior, and continuity.

Mark dialogue shots APPROVED_PICTURE_AND_LIPSYNC / LOCKED / DO_NOT_REGENERATE and narration or silent shots APPROVED_PICTURE / LOCKED / DO_NOT_REGENERATE. Keep native video audio TEMP_PREVIEW_AUDIO / NOT_FOR_FINAL_MIX. Record MUTE_NATIVE_VIDEO_AUDIO_AND_REPLACE_WITH_APPROVED_TRACKS and PENDING_EXTERNAL_FINAL_AUDIO_MIX.

Update the canonical manifest, registry, and batch QA record. Do not create the next batch in this run.
```

## 5. Register a real tail frame

```text
Verify that <TAILFRAME_ID> is a real image extracted from <SOURCE_VIDEO_ID>, without player UI, black frames, transition blur, subtitles, or watermarks.

Register it APPROVED_COMPOSITION_FRAME / LOCKED / FOR_<NEXT_SHOT>_ONLY / DO_NOT_REGENERATE. It is not a character master, scene master, prop master, or identity reference. Connect it only to the dependent shot and still reconnect that shot's locked character, scene, and prop references.
```

## 中文简版：批次预检

```text
读取权威 Manifest 与锁定资产登记表。从 <首个未生产镜头> 开始，选择最多 <批次数量> 个同场景连续镜头，不跨场景、不跳过依赖。

创建 <预检节点>，逐镜头记录：台词、说话角色、声音母带、出场角色、场景、道具、动作、机位、口型规则、连续性、尾帧依赖，以及 AUDIO_READY/AUDIO_BLOCKED 和 VIDEO_READY/VIDEO_BLOCKED。

缺少视觉资产只阻塞视频，不阻塞有效音频。本轮不生成媒体，写完并验证预检后停止。
```

## 中文简版：正式音频

```text
旁白与角色对白分开生成。旁白使用 <SHOT_ID>_NARRATION_V1，角色对白使用 <SHOT_ID>_DIALOGUE_<角色>_V1，并分别连接对应锁定声音母带。同一画面同时存在旁白和对白时仍保留两个独立音频节点。文本逐字使用权威 Manifest；不添加角色名、说明或额外对白；无音乐、环境音、音效和混响。

无语言镜头保持 NO_DIALOGUE，不创建空音频。生成后标记 GENERATED / MANUAL_AUDIO_QA_PENDING，等待人工试听；不得生成视频或自动批准音频。
```

## 中文简版：正式视频

```text
用户已确认本批正式音频。锁定音频后重新检查视频门禁，把每个镜头作为独立短视频生成。每一镜都必须重新连接实际出场角色图和锁定场景图，再连接必要道具与角色对白音频。上一镜尾帧只能控制构图、机位、姿态和空间关系，不能替代角色图、场景图或道具图。

只有说话角色动嘴；旁白保持独立，旁白画面人物闭口。禁止字幕、文字、水印、额外人物和额外对白。视频原生音轨只作预览，最终必须静音并替换为已确认的旁白和对白轨。缺少真实尾帧时停止，不得伪造。生成后标记 GENERATED / MANUAL_QA_PENDING，等待人工验收。
```
