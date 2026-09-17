# Continuity-First AI Short Film Creation

[中文说明](README.zh-CN.md)

This repository contains a reusable Codex skill for planning and producing multi-shot AI short films without losing character identity, voice identity, props, locations, or shot continuity.

It grew out of a practical node-canvas production workflow in which a screenplay is converted into locked reusable assets, an atomic-shot manifest, small production batches, human approval gates, and an external final audio mix.

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
  -> scene-local batch preflight
  -> dry dialogue generation and human approval
  -> prop and tail-frame resolution
  -> dependency-ordered video generation
  -> human visual and continuity approval
  -> external final dialogue, ambience, SFX, and music mix
```

The key idea is simple: models generate candidates; humans approve assets; downstream shots consume only approved assets.

## Repository structure

```text
skills/continuity-first-short-film/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── workflow.md
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
- enforcing real tail-frame continuity;
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

## Usage

Invoke the skill explicitly:

```text
Use $continuity-first-short-film to audit my AI-video canvas and identify the next safe production batch.
```

```text
Use $continuity-first-short-film to convert this screenplay into a continuity-safe atomic-shot manifest.
```

```text
Use $continuity-first-short-film to diagnose why character voices and appearances drift between shots.
```

The skill can also be selected automatically when a request clearly concerns multi-shot AI film continuity or gated production.

## Production principles

1. **Identity comes from locked assets, not names or seeds.**
2. **One shot has one primary action, camera setup, and speaker.**
3. **Dry dialogue is generated and approved before video.**
4. **Audio and video have separate readiness gates.**
5. **Hard continuity requires a real stable frame.**
6. **Video-native audio is provisional unless explicitly approved.**
7. **Human review is required before an output becomes locked.**
8. **Only failed shots are regenerated.**

## Scope

This repository provides the orchestration method, schemas, status vocabulary, and reusable prompt templates. It does not bundle a video model, bypass model policies, or guarantee that a particular canvas exposes frame extraction, lip sync, or final audio muxing.

## Contributing

Improvements are welcome, especially production-tested failure cases, clearer schemas, and tool-neutral prompt patterns. Keep additions focused on decisions that materially improve continuity or production safety.
