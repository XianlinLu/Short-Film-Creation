# AI Short Film Creation

[中文说明](README_zh-CN.md)

This repository contains a reusable skill for planning and producing multi-shot AI short films without losing character identity, voice identity, props, locations, or shot continuity.

It grew out of a practical node-canvas production workflow in which independent short shots are the default, controlled native continuation is used only for eligible same-scene action, every shot reconnects its character and scene references, narration and dialogue are generated separately, and the final edit replaces all native video audio.

## Why this exists

Long-form generative video often fails for structural reasons rather than prompt-writing reasons:

- each TTS node invents a slightly different voice;
- one combined cast sheet makes the video model confuse characters;
- seeds are mistaken for identity controls;
- video-native audio changes between shots or adds unwanted ambience;
- hard-continuity shots are generated without an approved native-continuation source or real predecessor frame;
- a partial manifest replaces the complete production plan;
- successful shots are regenerated when only one node failed.

The skill turns these failure modes into explicit production gates.

## Core method

```text
Script
  -> locked characters, voices, locations, and props
  -> canonical atomic-shot manifest
  -> separate narration and character-dialogue generation
  -> independent short shot OR eligible controlled continuation
  -> character image + scene image reattached in either mode
  -> every image/audio/video reference inserted as a real native @ material binding
  -> predecessor video controls motion/composition only
  -> tail frame used only as a hard-continuity fallback
  -> human visual and continuity approval
  -> mute native video audio
  -> replace with approved narration, dialogue, ambience, SFX, and music
```

The key idea is simple: models generate candidates; humans approve assets; downstream shots consume only approved assets.

## Controlled continuation

Continuation is an optimization for direct same-scene action, not an identity system. The skill first checks the live node to distinguish true timeline extension from ordinary video-reference generation.

| Situation | Mode |
| --- | --- |
| Same scene, time, costume, cast, and directly continuing action | Native continuation may be used after preflight |
| New scene, time, costume, age, speaking setup, or major camera reset | Independent shot |
| Predecessor already contains identity or anatomy drift | Independent shot from locked assets |
| True continuation is unavailable | Independent shot; use matched editing or a real tail frame if hard continuity requires it |

Even during continuation, the next shot reconnects locked character, scene, prop, and approved dialogue assets. The predecessor video controls motion and composition only. Each result is reviewed before it can become the next continuation source.

## Repository structure

```text
skills/continuity-first-short-film/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── workflow.md
    ├── video-continuation.md
    ├── video-prompt-certainty.md
    ├── material-binding.md
    ├── entry-scenarios.md
    ├── production-schema.md
    ├── prompt-templates.md
    └── failure-playbook.md
```

## What the skill helps with

- auditing an existing node canvas for drift risks;
- creating character, voice, scene, and prop asset registries;
- converting a screenplay into atomic shots;
- maintaining a complete canonical shot manifest;
- separating audio readiness from video readiness;
- producing in small scene-local batches;
- generating independently by default and using native continuation only after an eligibility gate;
- reattaching character, scene, and required prop references in either generation mode;
- preserving character voice with locked voice masters or approved shot dialogue instead of predecessor-video audio;
- blocking video prompts that contain uncertain language or unresolved alternatives;
- requiring real native material bindings instead of typed `@ASSET_NAME`, image aliases, or audio aliases;
- using real tail frames only for composition, camera, pose, and spatial continuity;
- keeping narration and character dialogue as separate approved tracks;
- generating copy-ready English and Chinese canvas-agent prompts;
- recovering from incomplete manifests, failed nodes, and output-audio errors;
- preserving clean dialogue for a controlled final mix.

The workflow is tool-aware but not tied to a single video model or canvas product. It inspects the capabilities actually available in the current environment instead of assuming frame extraction, lip sync, or AV muxing exists.

## Installation

Copy or symlink the skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/continuity-first-short-film ~/.codex/skills/
```

Restart or refresh Codex if needed so it can discover the new skill.

## Usage by starting point

### You already have a script

```text
Use $continuity-first-short-film with my finished script. Preserve the story and dialogue, split it into atomic shots, and generate narration and character dialogue separately. Use independent generation by default and native continuation only for eligible same-scene direct action. In either mode, reconnect locked character, scene, and required prop references; preserve approved character voices; and replace native video audio in the final edit.
```

### You already have generated videos

```text
Use $continuity-first-short-film to continue or repair my existing clips. Keep every shot that passes. Audit whether true native continuation is available and use it only for eligible same-scene direct action; otherwise create the next shot independently. Reattach locked character and scene references in either mode, preserve approved character voices, and produce a final audio-replacement plan.
```

### You have no script or reference images

```text
Use $continuity-first-short-film to develop my idea into a complete short film. I do not have a script or reference images yet. Help me define the concept, write and approve the screenplay, design and approve reusable character, scene, and voice references, then split it into atomic shots. Generate independently by default, reserve controlled continuation for eligible same-scene action, keep narration and dialogue separate, and replace native video audio in the final edit.
```

The skill can also be selected automatically when a request clearly concerns multi-shot AI film continuity or gated production.

## Production principles

1. **Independent short shots are the default.**
2. **Native continuation is used only for eligible same-scene direct action.**
3. **Every independent or continued shot reconnects its locked character image and scene image.**
4. **A predecessor video controls motion and composition only, never identity or voice.**
5. **A tail frame is a hard-continuity fallback, not an identity reference.**
6. **Narration and character dialogue are generated as separate approved assets.**
7. **All native video audio is muted and replaced in the final edit.**
8. **Identity comes from locked assets, not names, seeds, tail frames, or predecessor soundtracks.**
9. **Every continuation is human-reviewed before another continuation may start.**
10. **Every video prompt makes one exact choice; vague alternatives are blocked before generation.**
11. **Every referenced image, audio, and source video is an actual native material binding, not typed text.**
12. **Only failed shots are regenerated.**

## Scope

This repository provides the orchestration method, schemas, status vocabulary, and reusable prompt templates. It does not bundle a video model, bypass model policies, or guarantee that a particular canvas exposes frame extraction, lip sync, or final audio muxing.

## Contributing

Improvements are welcome, especially production-tested failure cases, clearer schemas, and tool-neutral prompt patterns. Keep additions focused on decisions that materially improve continuity or production safety.
