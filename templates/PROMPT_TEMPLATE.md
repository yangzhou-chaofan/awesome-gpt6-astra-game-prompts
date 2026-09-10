---
id: astra-3d-000
title: Replace With A Human Name
category: full-games
slug: replace-with-a-human-name
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.3
top_p: 0.9
seed: 4242
max_output_tokens: 6000
runtime: modern browser
stack: Three.js
difficulty: beginner
verified: draft
verified_by: your-github-handle
verified_on: 2026-09-10
tags: [threejs, webgl, replace-me]
license: CC0-1.0
---

# Replace With A Human Name

> One sentence: what does a person get when they run this recipe?

## What you get

Describe the deliverable precisely — file names, format, what it does, and why it is worth using
over writing the prompt yourself. Name the single most important property (self-contained, seeded,
no external assets, ...).

## Before you start

- **Runtime:** exactly what the output needs to run (e.g. any modern browser; Node 20+).
- **Dependencies:** list them, or state "none".
- **Assets / inputs:** starting files, API keys, paid services. Say "none" if none.
- **Model access:** anything needed beyond plain chat completion (tool use, code execution).

## The prompt

Everything between the fences is the exact text to paste. Do not paraphrase it in the recipe.

```text
You are a senior <domain> engineer. Build <precise deliverable> in <exact form>.

Deliverable
- <what to produce, named>
- <where it runs, and how it is launched>

Requirements (must all work)
- <behaviour 1>
- <behaviour 2>
- <controls / interaction>

Constraints
- <runtime, versions, libraries — this is what removes drift>

Output
- Output ONLY <the artifact> in one code block. No explanation before or after.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `model` | `gpt-6-astra` | The only family this list targets. |
| `model_version` | `2026-09-03` | Behavior drifts between releases; this is the one verified. |
| `temperature` | `0.3` | Low, to keep structure stable across runs. |
| `top_p` | `0.9` | — |
| `seed` | `4242` | If the API exposes a seed; otherwise `none` and pin the seed inside the prompt. |
| `max_output_tokens` | `6000` | Enough for the full artifact; raise if it truncates. |

Explain any non-obvious choice, especially anything you had to tune to pass the acceptance checks.

## Expected output

- `<file 1>` — what it is, roughly how big.
- `<file 2>` — ...
- Anything the output must **not** contain (build steps, external downloads, missing assets).

## Verify it worked

A checklist a person or a script can actually run. Each item must be able to fail.

- [ ] <observation 1>
- [ ] <observation 2>
- [ ] No errors in the console / no warnings on load.
- [ ] <performance or determinism check>

## Tune it

The one or two variables worth changing, and what changes when you do. Keep it short.

## Where it drifts

Known failure modes: what the model tends to get wrong on this task, and how the constraints above
avoid it. If you saw a specific failure, describe it. Do not claim the recipe is flawless.

## Provenance

- Technique adapted from: <link or "original">
- Verification run: <date, model version, reviewer handle>, or "not yet reproduced".
