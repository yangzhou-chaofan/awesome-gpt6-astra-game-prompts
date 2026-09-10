---
id: astra-3d-001
title: Endless Runner
category: full-games
slug: endless-runner
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
tags: [threejs, webgl, arcade, endless-runner, single-file]
license: CC0-1.0
---

# Endless Runner

> One prompt produces a single self-contained HTML file that plays a complete lane-based endless
> runner — no build step, no server, no assets.

## What you get

`index.html`, self-contained. Double-click it and the game runs: three lanes, procedural obstacles,
jump and slide, distance score with a persisted best, speed ramp, restart. It is the canonical
"does this recipe reproduce?" smoke test for the whole list, because every part of it is observable.

## Before you start

- **Runtime:** any modern browser (Chrome/Firefox/Safari/Edge, 2023+).
- **Dependencies:** none. Three.js is loaded from an ES-module CDN inside the file.
- **Assets / inputs:** none — primitives only.
- **Model access:** plain chat completion. No tools required.

## The prompt

```text
You are a senior Three.js engineer. Build a complete, self-contained endless runner game in ONE HTML file.

Deliverable
- A single file `index.html` that runs by double-clicking it. No build step, no npm, no local server.
- Load Three.js r170 or newer from an ES module CDN using an import map.

Gameplay (all of this must work)
- Lane-based runner: 3 lanes, automatic forward motion.
- Controls: ArrowLeft/ArrowRight or A/D to change lane; Space or ArrowUp to jump; ArrowDown to slide.
- Obstacles spawn procedurally ahead and move toward the player. Colliding with any obstacle ends the run.
- Score increases with distance travelled. Best score persists in localStorage.
- Speed ramps up gradually with distance.
- Pressing R restarts. A "Game Over" overlay shows the final score and the best score.

Presentation
- Third-person follow camera with slight smoothing.
- Low-poly aesthetic using only primitive geometry (Box, Cylinder) and MeshStandardMaterial.
  No external models, no textures.
- A ground made of repeating segments so the sense of motion is visible.
- Directional light plus hemisphere light, soft shadows, and fog for depth.

Engineering
- Use requestAnimationFrame with a delta-time clock so speed is framerate-independent.
- Keep concerns separated: input, spawning, collision (AABB), scoring, rendering.
- Use a fixed logical timestep for movement and collision.
- Handle window resize and devicePixelRatio.
- No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block. No explanation before or after.
- Add brief comments naming each subsystem.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.3` | Low: this task is structural, not creative, and low temperature keeps the subsystem layout stable. |
| `top_p` | `0.9` | — |
| `seed` | `4242` | Used where the API exposes a seed; the game needs no RNG of its own. |
| `max_output_tokens` | `6000` | Comfortably fits one HTML file; raise to `8000` if it truncates. |

## Expected output

- `index.html` — one file, roughly 300–500 lines, including the import map and the game code.
- It must **not** contain: a package.json, a build instruction, a fetch of a local asset, or a
  reference to an image/model file.

## Verify it worked

- [ ] Opening the file in a browser starts the game with no click-through or error screen.
- [ ] The console shows zero errors and zero warnings on load.
- [ ] A/D and Arrow keys change lanes; the change is visible within one frame.
- [ ] Space and ArrowUp jump; ArrowDown slides.
- [ ] Hitting an obstacle shows the Game Over overlay with the current and best score.
- [ ] Pressing R restarts and resets the score to zero.
- [ ] Reloading the page still shows the best score from the previous run.
- [ ] Framerate stays smooth on integrated graphics (no visible stutter over 30 seconds).

## Tune it

- **`SPEED` and `SPEED_RAMP`** near the top of the script. Raising the ramp shortens a run; it is the
  single dial that changes difficulty most.
- **Lane count.** Changing `3` to `4` is a good test of whether the movement code generalised or was
  hard-coded.

## Where it drifts

- **Slides become a crouch that does not clear anything.** The model often forgets the collider height
  change. The requirement that sliding must let the player pass under obstacles (implied by pairing it
  with jump) is the check that catches it — add an explicit low obstacle in your test run.
- **Frame-dependent speed.** If the delta clock is dropped, the game runs at different speeds per
  machine. The "framerate-independent" requirement prevents this; verify by throttling the CPU.
- **CDN import map omitted.** The model sometimes writes `import * as THREE from 'three'` without the
  import map, which fails on a bare `file://` open. The "runs by double-clicking" requirement pins it.

## Provenance

- Technique: original, drawing on the open Three.js examples' single-file pattern.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
