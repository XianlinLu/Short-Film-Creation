# Continuity-First AI Short Film Creation

[中文说明](README.zh-CN.md)

This repository contains a reusable Codex skill for planning and producing multi-shot AI short films without losing character identity, voice identity, props, locations, or shot continuity.

It grew out of a practical node-canvas production workflow in which every short shot is generated independently, every shot reconnects its character and scene references, predecessor frames control composition only, narration and dialogue are generated separately, and the final edit replaces all native video audio.

## Why this exists

Long-form generative video often fails for structural reasons rather than prompt-writing reasons:

- each TTS node invents a slightly different voice;
- one combined cast sheet makes the video model confuse characters;
- seeds are mistaken for identity controls;
- video-native audio changes between shots or adds unwanted ambience;
- hard-continuity shots are generated without a real predecessor frame;
- a partial manifest replaces the complete production plan;
- successful shots are regenerated when only one node failed.

The skill turns these failure modes into explicit production gates.

## Core method

```text
Script
  -> locked characters, voices, locations, and props
  -> canonical atomic-shot manifest
  -> separate narration and character-dialogue generation
  -> independently generated short shots
  -> character image + scene image reattached on every shot
  -> predecessor tail frame used only for composition continuity
  -> human visual and continuity approval
  -> mute native video audio
  -> replace with approved narration, dialogue, ambience, SFX, and music
```

The key idea is simple: models generate candidates; humans approve assets; downstream shots consume only approved assets.

## Repository structure

```text
skills/continuity-first-short-film/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── workflow.md
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
- generating every shot independently with character and scene references reattached;
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
Use $continuity-first-short-film with my finished script. Preserve the story and dialogue, split it into short independent shots, create an asset-gap list and canonical manifest, generate narration and character dialogue separately, and make every video shot reconnect its character and scene references. Use tail frames only for composition continuity and plan to replace all native video audio in the final edit.
```

### You already have generated videos

```text
Use $continuity-first-short-film to repair my existing generated clips. Keep every shot that already passes, identify only the shots with character, scene, composition, lip-sync, or audio drift, and rebuild those shots independently with character and scene references reattached. Use predecessor frames only for composition, generate narration and dialogue separately, and produce a final audio-replacement plan.
```

### You have no script or reference images

```text
Use $continuity-first-short-film to develop my idea into a complete short film. I do not have a script or reference images yet. Help me define the concept, write and approve the screenplay, design and approve reusable character and scene references, then split it into independent short shots with separate narration and dialogue and a final audio-replacement workflow.
```

The skill can also be selected automatically when a request clearly concerns multi-shot AI film continuity or gated production.

## Production principles

1. **Every short shot is generated independently.**
2. **Every shot reconnects its locked character image and scene image.**
3. **A predecessor tail frame controls composition only, never identity.**
4. **Narration and character dialogue are generated as separate assets.**
5. **All native video audio is muted and replaced in the final edit.**
6. **Identity comes from locked assets, not names, seeds, or tail frames.**
7. **One shot has one primary action, camera setup, and character speaker.**
8. **Human review is required before an output becomes locked.**
9. **Only failed shots are regenerated.**

## Scope

This repository provides the orchestration method, schemas, status vocabulary, and reusable prompt templates. It does not bundle a video model, bypass model policies, or guarantee that a particular canvas exposes frame extraction, lip sync, or final audio muxing.

## Contributing

Improvements are welcome, especially production-tested failure cases, clearer schemas, and tool-neutral prompt patterns. Keep additions focused on decisions that materially improve continuity or production safety.
