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

Create one node per shot named <SHOT_ID>_VOICE_V1. Connect the actual locked voice master. Use the exact approved line; do not add names, stage directions, or explanations. Output clean speech only: no music, ambience, effects, or reverb.

Silent shots remain NO_DIALOGUE and receive no fake empty audio. Record output existence and duration, then mark each result GENERATED / MANUAL_AUDIO_QA_PENDING. Do not generate video or approve audio. Stop for human listening.
```

## 3. Lock approved audio and generate video

```text
The user has approved the batch's formal audio. Mark those nodes APPROVED / LOCKED / DO_NOT_REGENERATE.

Recheck video gates. Generate only the executable shots in dependency order. For each shot, connect only its actual character references, scene master, required locked props, approved voice, and explicitly required real continuity frame.

Only the speaker may move their mouth; narration keeps visible characters' mouths closed. Do not add text, subtitles, watermarks, extra people, or extra dialogue. Treat native video audio as TEMP_PREVIEW_AUDIO / NOT_FOR_FINAL_MIX; preserve the locked dry voice for the final mix.

Stop before any hard-continuity shot whose real predecessor frame is absent. Mark outputs GENERATED / MANUAL_QA_PENDING and stop for human review.
```

## 4. Lock a human-approved batch

```text
The user has reviewed <SHOT_RANGE> in sequence and approves identity, props, scene, action, dialogue, voice, mouth behavior, and continuity.

Mark dialogue shots APPROVED_PICTURE_AND_LIPSYNC / LOCKED / DO_NOT_REGENERATE and narration or silent shots APPROVED_PICTURE / LOCKED / DO_NOT_REGENERATE. Keep native video audio TEMP_PREVIEW_AUDIO / NOT_FOR_FINAL_MIX. Record MUTE_NATIVE_VIDEO_AUDIO_AND_USE_LOCKED_DIALOGUE and PENDING_EXTERNAL_FINAL_AUDIO_MIX.

Update the canonical manifest, registry, and batch QA record. Do not create the next batch in this run.
```

## 5. Register a real tail frame

```text
Verify that <TAILFRAME_ID> is a real image extracted from <SOURCE_VIDEO_ID>, without player UI, black frames, transition blur, subtitles, or watermarks.

Register it APPROVED_CONTINUITY_FRAME / LOCKED / FOR_<NEXT_SHOT>_ONLY / DO_NOT_REGENERATE. It is not a character master, scene master, or general reference. Connect it only to the hard-continuity shot that explicitly depends on it.
```

## 中文简版：批次预检

```text
读取权威 Manifest 与锁定资产登记表。从 <首个未生产镜头> 开始，选择最多 <批次数量> 个同场景连续镜头，不跨场景、不跳过依赖。

创建 <预检节点>，逐镜头记录：台词、说话角色、声音母带、出场角色、场景、道具、动作、机位、口型规则、连续性、尾帧依赖，以及 AUDIO_READY/AUDIO_BLOCKED 和 VIDEO_READY/VIDEO_BLOCKED。

缺少视觉资产只阻塞视频，不阻塞有效音频。本轮不生成媒体，写完并验证预检后停止。
```

## 中文简版：正式音频

```text
只为 AUDIO_READY 的对白或旁白镜头生成正式干声。每镜头一个 <SHOT_ID>_VOICE_V1 节点，并真实连接对应锁定声音母带。台词逐字使用权威 Manifest；不添加角色名、说明或额外对白；无音乐、环境音、音效和混响。

无语言镜头保持 NO_DIALOGUE，不创建空音频。生成后标记 GENERATED / MANUAL_AUDIO_QA_PENDING，等待人工试听；不得生成视频或自动批准音频。
```

## 中文简版：正式视频

```text
用户已确认本批正式音频。锁定音频后重新检查视频门禁，只按依赖顺序生成当前可执行镜头。每镜头仅连接实际出场角色、场景、必要锁定道具、正式音频和明确要求的真实尾帧。

只有说话角色动嘴；旁白镜头人物闭口。禁止字幕、文字、水印、额外人物和额外对白。视频原生音轨只作预览，最终使用锁定干声。缺少真实尾帧时停止，不得伪造。生成后标记 GENERATED / MANUAL_QA_PENDING，等待人工验收。
```
