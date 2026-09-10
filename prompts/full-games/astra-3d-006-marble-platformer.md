---
id: astra-3d-006
title: Physics Marble Platformer
category: full-games
slug: marble-platformer
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.3
top_p: 0.9
seed: 4242
max_output_tokens: 8000
runtime: modern browser
stack: Three.js + Rapier
difficulty: advanced
verified: draft
tags: [threejs, rapier, physics, platformer, rolling, single-file]
license: CC0-1.0
---

# Physics Marble Platformer

> A rolling-ball platformer driven by a real physics engine, with a fixed timestep so it behaves the
> same everywhere.

## What you get

`index.html`, self-contained: Rapier (WASM) loaded from a CDN, a ball the player tips with the arrow
keys or WASD, a course of ramps, moving platforms and a goal, checkpoints, and a fixed-timestep loop.

## Before you start

- **Runtime:** modern browser with WebGL2 and WASM.
- **Dependencies:** Three.js and `@dimforge/rapier3d-compat` via CDN import map.
- **Assets / inputs:** none; the course is built from boxes.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior Three.js engineer. Build a rolling-marble platformer in ONE self-contained index.html
using Rapier for physics.

Deliverable
- A single `index.html` that runs by double-clicking it. No build step, no server.
- Load Three.js r170+ and `@dimforge/rapier3d-compat` from a CDN via an import map, and await
  `RAPIER.init()` before starting.

Physics
- A dynamic ball (sphere) with realistic friction and restitution. The player applies torque/force to
  roll it, plus a small air control. WASD or arrow keys control it relative to the camera.
- Fixed physics timestep of 1/60 s, decoupled from the render loop, with an accumulator and
  interpolation of the ball's visual position. The simulation must behave identically regardless of
  display refresh rate.
- Static colliders for the course; a moving platform driven by a kinematic body with a known path.

Course
- Hard-code a course of at least: a starting ramp, a narrow bridge, two gaps, one moving platform,
  and a raised goal pad. Build it from box colliders with matching Three.js meshes.
- Three checkpoints along the course. Falling below y = -10 respawns the ball at the last checkpoint.

Goal and UI
- Reaching the goal pad shows a completion overlay with elapsed time and a restart button.
- HUD: timer, checkpoint indicator, and a restart key hint.

Engineering
- requestAnimationFrame for rendering; physics stepped at the fixed rate above.
- Separate concerns: physics world, course construction, player control, checkpoints, UI, rendering.
- Handle resize and devicePixelRatio. No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with brief comments per subsystem.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.3` | Physics code has many exact-sign requirements; keep sampling tight. |
| `seed` | `4242` | API seed. The course is deterministic by construction; no RNG needed. |
| `max_output_tokens` | `8000` | Physics setup plus course plus loop. |

## Expected output

- `index.html` — one file, roughly 600–950 lines.
- An accumulator-based fixed-timestep loop, clearly visible in the main loop code.

## Verify it worked

- [ ] The ball appears and rolls when keys are pressed; it falls under gravity.
- [ ] Ramps deflect it; it does not clip through the bridge or the moving platform.
- [ ] The moving platform carries the ball when it is resting on it.
- [ ] Falling off respawns the ball at the last checkpoint reached.
- [ ] The completion overlay appears on the goal pad with a plausible time.
- [ ] Behavior is the same on a 60 Hz and a 144 Hz display (the fixed-step requirement).
- [ ] Console is clean; no WASM load errors.

## Tune it

- **Ball mass and friction** — roll feel. Too much restitution and it bounces forever.
- **Fixed timestep** — 1/60 is standard; lowering it changes stability and is worth understanding.

## Where it drifts

- **`RAPIER.init()` not awaited.** The most common failure: the world is built against an uninitialised
  WASM module and nothing moves. The explicit await requirement is the guard.
- **Variable timestep.** If `world.step()` is called with the frame delta, the simulation becomes
  machine-dependent — tunnels through thin colliders on slow frames. The accumulator requirement
  prevents this; verify by throttling the CPU in devtools and seeing if the ball tunnels.
- **Meshes and colliders drifting apart.** The visual course and the physics course are built twice and
  can disagree. Verify by pressing a debug key that renders collider outlines, or by testing each gap.
- **Kinematic platform without velocity.** Moving platforms that teleport their body do not carry the
  ball. The "known path" requirement implies a kinematic body with a set velocity, which does.

## Provenance

- Technique: original; Rapier's own examples establish the compat build and fixed-step pattern.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
