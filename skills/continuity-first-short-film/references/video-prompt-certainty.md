# Video Prompt Certainty Gate

Apply this gate to the exact final text sent to every independent-video or continuation node. Do not apply it to capability audits, QA reports, failure explanations, or planning discussions.

## PASS requirements

A video prompt passes only when it specifies:

- one primary subject action;
- one camera setup and one camera path;
- one composition and subject placement;
- exact clip duration and action timing;
- exact character identity, costume, emotion, pose, and mouth behavior;
- exact scene, lighting, weather, and time state;
- exact required prop identity, placement, and state;
- direct prohibitions written as separate statements.

The video model must not choose among alternatives or infer an unresolved creative decision.

## Automatic lexical FAIL

Fail the prompt when it contains any ambiguity marker, including:

```text
可能
或
或者
或许
也许
大概
大约
约为
差不多
似乎
尽量
适当
酌情
任选
任意
某种
类似
左右
等等
maybe
perhaps
possibly
possible
might
could
probably
likely
roughly
approximately
somewhat
optionally
optional
either
or
as appropriate
if desired
try to
etc.
and so on
```

Do not retain these terms inside negative instructions. Rewrite each prohibition as its own direct sentence.

## Structural FAIL

Fail even when no listed term appears if the prompt contains:

- two actions presented as alternatives;
- two camera moves without a fixed order and timing;
- a range where one exact value is required;
- an unspecified direction, speed, framing, emotion, prop state, or mouth state;
- placeholders, slash-separated choices, parenthetical choices, or instructions that tell the model to decide;
- conflicting positive and negative instructions.

## Required validation record

Write this record before creating the video node:

```text
PROMPT_CERTAINTY_CHECK: PASS | FAIL
AMBIGUOUS_TERMS: NONE | <exact terms>
UNRESOLVED_CHOICES: NONE | <exact choices>
FINAL_VIDEO_PROMPT: <exact prompt that will be submitted>
```

Set `PASS` only when both `AMBIGUOUS_TERMS` and `UNRESOLVED_CHOICES` are `NONE`. A failed prompt must be rewritten and checked again. Do not generate a video while the result is `FAIL`.

## Rewrite example

Reject:

```text
她可能转身，或者看向窗外，镜头或许缓慢推进。
```

Use:

```text
她向右转身，看向窗外。镜头沿直线缓慢推进，持续 5 秒。
```
