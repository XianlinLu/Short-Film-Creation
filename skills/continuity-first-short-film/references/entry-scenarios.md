# Entry Scenarios

Choose the path that matches the user's starting material. The core production contract remains the same in every path: independent short shots, character and scene references on every shot, tail frames for composition only, separate narration and dialogue, and final soundtrack replacement.

## Scenario A: The user already has a script

1. Preserve the script as the authoritative source unless the user asks for editing.
2. Identify characters, narrators, locations, recurring props, costume states, and missing visual or voice assets.
3. Build and approve independent character, scene, prop, narration-voice, and dialogue-voice assets.
4. Split the script into short atomic shots with one primary action and one primary camera setup.
5. Create the complete canonical manifest.
6. Produce audio first, then independently generate each shot with its character and scene references reattached.
7. Use tail frames only where composition continuity matters.
8. Replace every video soundtrack in post with the approved spoken tracks and controlled sound design.

Example:

```text
Use $continuity-first-short-film with my finished script. Preserve the story and dialogue, split it into short independent shots, create an asset-gap list and canonical manifest, generate narration and character dialogue separately, and make every video shot reconnect its character and scene references. Use tail frames only for composition continuity and plan to replace all native video audio in the final edit.
```

中文示例：

```text
使用 $continuity-first-short-film 处理我的完整剧本。保留故事和台词，把剧本拆成独立短镜头，建立资产缺口表和完整 Manifest；旁白与角色对白分开生成；每个视频镜头重新连接角色图和场景图；尾帧只控制构图连续；最终剪辑替换全部视频原生音轨。
```

## Scenario B: The user already has generated videos

1. Inventory clips, source images, audio, node settings, and shot order.
2. Review each clip separately and in sequence. Keep clips that pass; do not regenerate the whole film.
3. Recover or create locked character and scene references if they do not exist.
4. Mark identity, costume, prop, scene, composition, mouth, and audio failures per shot.
5. Regenerate only failed shots as independent short clips. Reattach character and scene references on each replacement shot.
6. Use approved predecessor tail frames only to reproduce composition and spatial layout.
7. Generate clean narration and character dialogue separately, then replace all native video audio in the edit.

Example:

```text
Use $continuity-first-short-film to repair my existing generated clips. Keep every shot that already passes, identify only the shots with character, scene, composition, lip-sync, or audio drift, and rebuild those shots independently with character and scene references reattached. Use predecessor frames only for composition, generate narration and dialogue separately, and produce a final audio-replacement plan.
```

中文示例：

```text
使用 $continuity-first-short-film 修复我已经生成的视频片段。保留所有正确镜头，只找出角色、场景、构图、口型或声音漂移的镜头；重做时每镜重新连接角色图和场景图，上一镜尾帧只负责构图；旁白和角色对白分开生成，并制定最终替换视频音轨的方案。
```

## Scenario C: The user has no script or images

1. Develop the creative brief: premise, genre, audience, target length, format, tone, and visual direction.
2. Draft a logline, outline, character list, location list, and screenplay. Ask for approval before production assets.
3. Create and approve character masters, scene masters, recurring props, narration voice, and character voices.
4. Build the atomic-shot manifest.
5. Follow the same audio-first, independent-shot workflow.

Do not generate a large batch of videos directly from a loose idea. Establish the script and reusable visual assets first.

Example:

```text
Use $continuity-first-short-film to develop my idea into a complete short film. I do not have a script or reference images yet. Help me define the concept, write and approve the screenplay, design and approve reusable character and scene references, then split it into independent short shots with separate narration and dialogue and a final audio-replacement workflow.
```

中文示例：

```text
使用 $continuity-first-short-film 从零开发一部短片。我目前没有剧本和参考图片。请先帮助我确定创意、完成并确认剧本，再创建和确认可复用的角色图、场景图与声音资产，之后拆成独立短镜头；旁白与对白分开生成，最终替换视频原生音轨。
```
