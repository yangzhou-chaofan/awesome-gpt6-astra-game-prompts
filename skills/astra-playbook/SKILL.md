---
name: gpt6-astra-playbook
description: Turn a one-line idea into a runnable GPT-6 Astra creation. Use when someone wants a game, 3D scene, website, video, app or computer-use task built with GPT-6 Astra and needs the prompt actually assembled — not just a list of examples. Routes the idea to the right output form, fills the eight-block prompt frame, and attaches acceptance checks so the result can be judged.
---

# GPT-6 Astra Playbook

A prompt list tells you what worked for someone else. This playbook turns *your* idea into a prompt
that produces something you can run, watch, or click.

## When to use it

- "Build me a game / scene / website / video with Astra."
- "I have this idea — what's the prompt?"
- You found something in the [catalog](../../CATALOG.md) and want your own version.

If the task is to *find* existing work, stop and read [`CATALOG.md`](../../CATALOG.md) instead.

## The method

1. **Name the deliverable in one file.** Decide the single artifact that comes out: one
   `index.html`, one `.blend`, one repo, one MP4. Ambiguous output is the main cause of drift.
2. **Route the form.** Use the table below to pick the stack and the acceptance checks for that form.
3. **Fill the eight blocks.** A prompt is not a wish; it is a spec with eight named parts (below).
4. **Pin the degrees of freedom.** Runtime, version, palette, dimensions, seed. Every unpinned choice
   is a chance the model invents something you did not want.
5. **Attach acceptance.** State the checks that decide pass/fail *before* you run it, then run it.

## Route the form

| Idea | Deliverable | Stack | Acceptance checks |
| --- | --- | --- | --- |
| A game | single-file `index.html` | Three.js r170+ (import map) | runs on double-click; no console errors; controls respond; win/lose and restart work |
| A scene / model | `.blend` + glTF/GLB export | Blender 4.x | opens clean; named parts; exports without missing textures |
| A website | `index.html` + assets | HTML/CSS, no build step | opens offline; responsive at 375px and 1440px; no broken assets |
| A video | shot script + source project | Remotion / Blender / HyperFrames | every shot has duration + motion; renders end-to-end; audio in sync |
| An app / tool | one runnable file or small repo | JS/TS + one entry point | installs with one command; the core action works once; errors are visible |
| A computer-use task | a short action plan + verification | Astra computer use | each step is observable; a screenshot proves the end state |

## The eight blocks

Write the prompt as these eight labeled blocks. Keep the labels — they stop the model from silently
dropping a requirement.

```text
You are a senior <domain> engineer. Build <precise deliverable> as <exact form>.

1. Deliverable
   - <what to produce, named> · <where it runs> · <how it is launched>

2. Requirements (all must work)
   - <the 4-8 concrete behaviours a user would test>

3. Constraints (pin the degrees of freedom)
   - <runtime + version> · <geometry/material palette> · <no external assets / no build step>

4. Look
   - <camera, lighting, palette, reference in words and numbers>

5. Interaction
   - <input map: keys, pointer, or "none"> · <what the user may change at runtime>

6. Determinism
   - <seed the prompt itself must use for any procedural output>

7. Acceptance
   - <the observable, fail-able checks from the table above>

8. Failure modes to avoid
   - <the specific ways this task usually goes wrong — say them out loud>
```

## Worked example

Idea: *"a tiny game where I surf a wave and dodge rocks"* → one `index.html`, Three.js.

- **1 Deliverable:** `index.html`, runs on double-click, no build step.
- **2 Requirements:** board auto-advances; left/right carve; speed ramps; hitting a rock ends the run;
  score = distance; best persists; R restarts.
- **3 Constraints:** Three.js r170 via import map; primitives only; no textures, no external files.
- **4 Look:** follow camera with smoothing; low-poly; sunrise palette (list hex codes); fog for depth.
- **5 Interaction:** ←/→ or A/D to carve; space to hop; nothing else.
- **6 Determinism:** drive rock spawn and wave geometry from a seeded PRNG, seed `4242`.
- **7 Acceptance:** no console errors; carving changes the line; collision ends the run; restart resets.
- **8 Failure modes:** external model loads, missing import map, unseeded procedural spawns, missing
  restart. Name each as forbidden.

## After the run

- **Verify against block 7, not against vibes.** A different color is fine; a broken restart is not.
- If it fails, fix the **block** that was under-specified rather than adding more adjectives.
- If you produced something good, consider contributing it: a demo goes in the
  [catalog](../../catalog/entries/) with its source; a prompt that reliably reproduces goes under
  [`prompts/`](../../prompts) with the full [reproducibility contract](../../docs/REPRODUCIBILITY.md).

## Anti-patterns

- "Make it look nice" — unbounded. Say the palette, the camera, the reference.
- "Make a 3D game" — the drift engine. Say one file, one runtime, one loop.
- Ten requirements for a first pass — start with the core loop, add later.
- No acceptance line — you cannot tell success from a pretty screenshot.
