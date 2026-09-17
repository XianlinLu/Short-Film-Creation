# Entry Scenarios

Choose the path that matches the user's starting material. The core production contract remains the same in every path: independent short shots by default, controlled native continuation only for eligible same-scene action, character and scene references on every shot, separate narration and dialogue, and final soundtrack replacement.

## Scenario A: The user already has a script

1. Preserve the script as the authoritative source unless the user asks for editing.
2. Identify characters, narrators, locations, recurring props, costume states, and missing visual or voice assets.
3. Build and approve independent character, scene, prop, narration-voice, and dialogue-voice assets.
4. Split the script into short atomic shots with one primary action and one primary camera setup.
5. Create the complete canonical manifest.
6. Produce audio first, then choose independent generation or controlled native continuation per shot.
7. Reattach character and scene references in both modes. Use predecessor video only for motion and composition continuity; use tail frames only as a fallback where hard composition continuity matters.
8. Replace every video soundtrack in post with the approved spoken tracks and controlled sound design.

Example:

```text
Use $continuity-first-short-film with my finished script. Preserve the story and dialogue, split it into short atomic shots, create an asset-gap list and canonical manifest, and generate narration and character dialogue separately. Use independent generation by default; use native continuation only for eligible same-scene direct action. In either mode, reconnect locked character, scene, and required prop references. Treat predecessor video as motion/composition reference only and replace all native video audio in the final edit.
```

中文示例：

```text
使用 $continuity-first-short-film 处理我的完整剧本。保留故事和台词，把剧本拆成原子短镜头，建立资产缺口表和完整 Manifest；旁白与角色对白分开生成；默认独立生成，只有同场景直接动作连续且通过门禁时才使用原生视频续写。两种模式都重新连接锁定角色图、场景图和必要道具；上一段视频只负责动作与构图连续；最终替换全部视频原生音轨。
```

## Scenario B: The user already has generated videos

1. Inventory clips, source images, audio, node settings, and shot order.
2. Review each clip separately and in sequence. Keep clips that pass; do not regenerate the whole film.
3. Recover or create locked character and scene references if they do not exist.
4. Mark identity, costume, prop, scene, composition, mouth, and audio failures per shot.
5. Keep approved clips. For a failed or next shot, choose an independent short clip by default; use native continuation only when the approved predecessor and next shot pass the continuation gate.
6. Reattach locked character and scene references in either mode. Use predecessor video for motion/composition only; use approved tail frames only as a fallback for hard composition continuity.
7. Generate clean narration and character dialogue separately, then replace all native video audio in the edit.

Example:

```text
Use $continuity-first-short-film to continue or repair my existing generated clips. Keep every shot that passes. Audit whether true native continuation is available and use it only for eligible same-scene direct action; otherwise rebuild or create the next shot independently. Reattach locked character and scene references in either mode, preserve approved character voices, generate narration and dialogue separately, and produce a final audio-replacement plan.
```

中文示例：

```text
使用 $continuity-first-short-film 续写或修复我已经生成的视频片段。保留所有正确镜头，先核查是否存在真正的原生续写能力；只有同场景直接动作连续时才续写，否则独立生成下一镜或重做失败镜头。两种模式都重新连接锁定角色图和场景图，保持角色声音母带不变；旁白和对白分开生成，最终替换视频原生音轨。
```

## Scenario C: The user has no script or images

1. Develop the creative brief: premise, genre, audience, target length, format, tone, and visual direction.
2. Draft a logline, outline, character list, location list, and screenplay. Ask for approval before production assets.
3. Create and approve character masters, scene masters, recurring props, narration voice, and character voices.
4. Build the atomic-shot manifest.
5. Follow the same audio-first workflow. Use independent shots by default and controlled continuation only after the assets, pilot, and manifest exist.

Do not generate a large batch of videos directly from a loose idea. Establish the script and reusable visual assets first.

Example:

```text
Use $continuity-first-short-film to develop my idea into a complete short film. I do not have a script or reference images yet. Help me define the concept, write and approve the screenplay, design and approve reusable character, scene, and voice references, then split it into atomic shots. Generate independently by default, reserve controlled continuation for eligible same-scene action, keep narration and dialogue separate, and replace native video audio in the final edit.
```

中文示例：

```text
使用 $continuity-first-short-film 从零开发一部短片。我目前没有剧本和参考图片。请先帮助我确定创意、完成并确认剧本，再创建和确认可复用的角色图、场景图与声音资产，之后拆成原子短镜头；默认独立生成，只对符合条件的同场景直接动作使用受控续写；旁白与对白分开生成，最终替换视频原生音轨。
```
