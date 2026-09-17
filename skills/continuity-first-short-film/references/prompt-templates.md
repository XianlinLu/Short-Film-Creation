# Canvas-Agent Prompt Templates

Use these as building blocks. Replace placeholders with actual IDs read from the project. Keep one stage per prompt.

## 1. Batch preflight

```text
Read the canonical manifest and locked asset registry.

Start at <FIRST_UNPRODUCED_SHOT>. Select up to <BATCH_SIZE> consecutive shots without crossing a scene boundary or skipping a dependency.

Create <BATCH_PRECHECK_NODE>. For each shot record exact dialogue, speaker, voice master, on-screen characters, scene, props, action, camera, mouth rule, continuity type, proposed generation mode, continuation eligibility, source-video or tail-frame dependency, AUDIO_READY/AUDIO_BLOCKED, VIDEO_READY/VIDEO_BLOCKED, and the exact blocker.

Write the final VIDEO_PROMPT for every shot as a deterministic instruction with one action, one camera path, one composition, exact timing, exact asset states, and explicit mouth behavior. Reject any prompt containing uncertain or alternative language, including 可能、或者、或许、也许、大概、似乎、尽量、适当、maybe、perhaps、possibly、either、or. If any creative choice is unresolved, mark VIDEO_BLOCKED_BY_AMBIGUOUS_PROMPT. Set PROMPT_CERTAINTY_CHECK = PASS only after rewriting the prompt into one exact executable choice.

Missing visual assets block video but do not block valid audio. Do not generate media in this run. Stop after writing and verifying the preflight.
```

## 2. Formal dry voices

```text
Use <BATCH_PRECHECK_NODE>. Generate audio only for AUDIO_READY speaking or narration shots.

Create separate narration and character-dialogue nodes. Use <SHOT_ID>_NARRATION_V1 for narration and <SHOT_ID>_DIALOGUE_<CHARACTER>_V1 for character speech. Connect the actual locked narrator or character voice master. If both occur over one shot, keep both nodes. Use the exact approved text; do not add names, stage directions, or explanations. Output clean speech only: no music, ambience, effects, or reverb.

Silent shots remain NO_DIALOGUE and receive no fake empty audio. Record output existence and duration, then mark each result GENERATED / MANUAL_AUDIO_QA_PENDING. Do not generate video or approve audio. Stop for human listening.
```

## 3. Lock approved audio and generate independent video

```text
The user has approved the batch's formal audio. Mark those nodes APPROVED / LOCKED / DO_NOT_REGENERATE.

Recheck video gates. Generate each executable shot as an independent short clip in dependency order. On every shot, reconnect its actual locked character image and locked scene image, then add only the required locked props and approved dialogue audio. A predecessor tail frame may also be connected, but only to control composition, camera, pose, and spatial layout; it never replaces character, costume, scene, or prop references.

Before creating each video node, verify PROMPT_CERTAINTY_CHECK = PASS. The prompt must contain one exact action, camera path, composition, duration, character state, prop state, and mouth rule. Do not submit prompts containing alternatives, approximation, optional behavior, or uncertainty. Do not let the video model choose.

Only the character speaker may move their mouth; narration stays separate and keeps visible characters' mouths closed. Do not add text, subtitles, watermarks, extra people, or extra dialogue. Treat native video audio as TEMP_PREVIEW_AUDIO / NOT_FOR_FINAL_MIX and always replace it with approved narration and dialogue in the final mix.

Stop before any hard-continuity shot whose real predecessor frame is absent. Mark outputs GENERATED / MANUAL_QA_PENDING and stop for human review.
```

## 4. Audit native continuation capability

```text
Do not generate media in this run. Inspect the live video model and node schema for <MODEL_OR_NODE>.

Determine whether it exposes true native timeline extension/continuation, ordinary video-reference generation, or no continuation. A video input port alone is not proof of native continuation. Record supported source-video inputs, required image/audio inputs, duration limit, maximum continuation rounds, whether locked character and scene images can be reattached, whether approved audio can condition lip sync, native-audio behavior, and whether output is APPENDED_SEGMENT or FULL_EXTENDED_VIDEO.

Create <CONTINUATION_CAPABILITY_REPORT>. Conclude NATIVE_CONTINUATION_AVAILABLE, VIDEO_REFERENCE_ONLY, or NO_VIDEO_CONTINUATION. Do not create or modify video, audio, image, or locked assets. Stop after verifying the report.
```

## 5. Generate one controlled continuation

```text
Generate only <NEXT_SHOT_ID>. Do not create later shots in this run.

First verify that <SOURCE_VIDEO_ID> has a real human-approved locked video output and that the next shot remains in the same scene, time, costume state, character set, and direct action/camera continuity. Verify that the live node exposes true native continuation and that the continuation round is within its current limit. If any check fails, create a preflight record with CONTINUATION_BLOCKED or FALLBACK_TO_INDEPENDENT_SHOT and stop without generating media.

If all checks pass, create <NEXT_SHOT_ID>_CONTINUATION_V1. Connect <SOURCE_VIDEO_ID> only as motion, composition, pacing, camera, pose, and spatial-continuity input. Reconnect the locked image for every on-screen character, the locked scene master, and only the required locked prop/costume references. Never use the source video as character, scene, prop, or voice identity.

Verify PROMPT_CERTAINTY_CHECK = PASS. The continuation prompt must state one exact next action, one exact camera path, one composition, and exact timing. It must not contain possible outcomes, alternative actions, optional gestures, approximate duration, or ambiguous terms.

For character dialogue, connect the exact approved dry dialogue <DIALOGUE_AUDIO_ID> only if the continuation node supports audio lip-sync conditioning. For narration, do not feed narration into visible mouths; keep <NARRATION_AUDIO_ID> separate. Do not invent or regenerate dialogue. Preserve one primary action and one primary camera movement.

Record CONTINUATION_ROUND, MAX_CONTINUATION_ROUNDS, and EXTENSION_OUTPUT_MODE. Treat all returned native audio as TEMP_PREVIEW_AUDIO / NOT_FOR_FINAL_MIX and record MUTE_NATIVE_VIDEO_AUDIO_AND_REPLACE_WITH_APPROVED_TRACKS. Mark the result GENERATED / MANUAL_QA_PENDING and stop for human review. Do not automatically chain another continuation.
```

## 6. Lock a human-approved batch

```text
The user has reviewed <SHOT_RANGE> in sequence and approves identity, props, scene, action, dialogue, voice, mouth behavior, and continuity.

Mark dialogue shots APPROVED_PICTURE_AND_LIPSYNC / LOCKED / DO_NOT_REGENERATE and narration or silent shots APPROVED_PICTURE / LOCKED / DO_NOT_REGENERATE. Keep native video audio TEMP_PREVIEW_AUDIO / NOT_FOR_FINAL_MIX. Record MUTE_NATIVE_VIDEO_AUDIO_AND_REPLACE_WITH_APPROVED_TRACKS and PENDING_EXTERNAL_FINAL_AUDIO_MIX.

Update the canonical manifest, registry, and batch QA record. Do not create the next batch in this run.
```

## 7. Register a real tail frame

```text
Verify that <TAILFRAME_ID> is a real image extracted from <SOURCE_VIDEO_ID>, without player UI, black frames, transition blur, subtitles, or watermarks.

Register it APPROVED_COMPOSITION_FRAME / LOCKED / FOR_<NEXT_SHOT>_ONLY / DO_NOT_REGENERATE. It is not a character master, scene master, prop master, or identity reference. Connect it only to the dependent shot and still reconnect that shot's locked character, scene, and prop references.
```

## 中文简版：批次预检

```text
读取权威 Manifest 与锁定资产登记表。从 <首个未生产镜头> 开始，选择最多 <批次数量> 个同场景连续镜头，不跨场景、不跳过依赖。

创建 <预检节点>，逐镜头记录：台词、说话角色、声音母带、出场角色、场景、道具、动作、机位、口型规则、连续性、尾帧依赖，以及 AUDIO_READY/AUDIO_BLOCKED 和 VIDEO_READY/VIDEO_BLOCKED。

同时为每一镜写出最终 VIDEO_PROMPT。提示词必须只有一个明确动作、一个明确机位运动、一个明确构图、精确时长、确定的角色与道具状态，以及明确口型规则。禁止出现“可能、或者、或许、也许、大概、似乎、尽量、适当”等模糊词，禁止让模型在多个方案中自行选择。存在未决选择时标记 VIDEO_BLOCKED_BY_AMBIGUOUS_PROMPT；全部改成唯一确定指令后才标记 PROMPT_CERTAINTY_CHECK = PASS。

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

创建视频节点前必须确认 PROMPT_CERTAINTY_CHECK = PASS。视频提示词只能描述一个确定动作、一个确定机位运动、一个确定构图、精确时长、确定角色状态、确定道具状态和明确口型。禁止“可能、或者、或许、也许、大概、似乎、尽量、适当”等措辞；禁止提供备选方案；禁止让视频模型自行决定。

只有说话角色动嘴；旁白保持独立，旁白画面人物闭口。禁止字幕、文字、水印、额外人物和额外对白。视频原生音轨只作预览，最终必须静音并替换为已确认的旁白和对白轨。缺少真实尾帧时停止，不得伪造。生成后标记 GENERATED / MANUAL_QA_PENDING，等待人工验收。
```

## 中文简版：续写能力核查

```text
本轮不生成媒体。读取 <模型或节点> 的实时参数与端口，判断它提供的是：真正的原生时间线续写、普通视频参考生成，还是完全不支持续写。仅有 video 输入端口不能证明支持原生续写。

创建 <续写能力报告>，记录：源视频要求、是否能同时重新连接角色图和场景图、是否能输入锁定对白做口型、单次时长、最大续写轮数、原生音频行为，以及输出是“仅新增片段”还是“包含源视频的完整延长视频”。结论只能是 NATIVE_CONTINUATION_AVAILABLE、VIDEO_REFERENCE_ONLY 或 NO_VIDEO_CONTINUATION。写完并验证报告后停止，不修改锁定资产。
```

## 中文简版：单镜头受控续写

```text
本轮只生成 <下一镜头 ID>，不得继续创建后续镜头。

先验证 <源视频 ID> 有真实、已人工确认并锁定的视频输出；下一镜必须保持同一场景、时间、服装、角色集合，并直接延续动作或机位。实时节点必须提供真正的原生续写，且当前续写轮次未超过限制。任一条件不满足时，只记录 CONTINUATION_BLOCKED 或 FALLBACK_TO_INDEPENDENT_SHOT，然后停止，不生成媒体。

通过后创建 <下一镜头 ID>_CONTINUATION_V1。把 <源视频 ID> 仅作为动作、构图、节奏、机位、姿态和空间连续参考；同时重新连接本镜实际出场角色的锁定角色图、锁定场景图，以及必要的锁定道具和服装状态图。源视频不能替代任何身份资产或声音母带。

创建节点前必须确认 PROMPT_CERTAINTY_CHECK = PASS。续写提示词必须明确下一步唯一动作、唯一机位运动、确定构图与精确时长；禁止可能结果、替代动作、可选表演和近似时间；禁止任何模糊词。

角色说话镜头只有在续写节点支持音频驱动口型时，才连接已经确认的干声 <对白音频 ID>；旁白 <旁白音频 ID> 保持独立，不驱动画面人物开口。不得重新生成或改写对白。

记录 CONTINUATION_ROUND、MAX_CONTINUATION_ROUNDS 和 EXTENSION_OUTPUT_MODE。生成视频的原生音轨一律标记 TEMP_PREVIEW_AUDIO / NOT_FOR_FINAL_MIX，并记录最终静音后替换为锁定对白与旁白。结果标记 GENERATED / MANUAL_QA_PENDING，等待人工验收；不得自动串联下一次续写。
```
