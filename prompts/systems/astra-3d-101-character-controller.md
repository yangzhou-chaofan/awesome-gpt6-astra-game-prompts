---
id: astra-3d-101
title: Character Controller
category: systems
slug: character-controller
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.25
top_p: 0.9
seed: 4242
max_output_tokens: 6000
runtime: modern browser
stack: Three.js
difficulty: intermediate
verified: draft
tags: [threejs, controller, movement, kinematics, coyote-time]
license: CC0-1.0
---

# Character Controller

> A kinematic capsule controller with coyote time, jump buffering and slope handling — the movement
> layer every 3D game needs, and the one most models write badly.

## What you get

A drop-in `createCharacterController(camera, world)` module in one HTML file with a live test scene:
a capsule you drive in third person across flat ground, slopes, steps and a gap.

## Before you start

- **Runtime:** modern browser.
- **Dependencies:** Three.js via CDN import map.
- **Assets / inputs:** none — the test scene is boxes.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior game engineer. Write a reusable kinematic character controller for Three.js, as a
single self-contained index.html that demonstrates it.

Deliverable
- One `index.html`, runs on double-click. Three.js r170+ via import map. No external assets.
- Expose `createCharacterController(camera, world)` returning an object with `update(dt, input)` and
  the player mesh.

Controller requirements (all must hold)
- Capsule collider approximated by a sphere cast / multi-ray down the capsule.
- Ground detection with a slope limit: walkable up to 45 degrees, sliding down steeper surfaces.
- Gravity with a terminal velocity. Grounded state is stable — no flicker between grounded and airborne.
- Coyote time: the player can still jump for 0.12 s after leaving the ground.
- Jump buffering: a jump pressed up to 0.15 s before landing fires on landing.
- Variable jump height: releasing the jump key early cuts upward velocity.
- Step-up: the player climbs ledges up to 0.4 units without jumping.
- Acceleration and friction for horizontal movement, with a configurable max speed. No instant
  direction snaps.
- Moving platforms: the controller inherits the platform's velocity while standing on it.

Input abstraction
- Take an input object `{ moveX, moveZ, jumpHeld, jumpPressed }` — the controller must not read the
  keyboard itself, so it can be driven by AI later.

Test scene
- Build a scene with a ramp, a staircase, a 45-degree and a 60-degree slope, a small gap, and one
  moving platform, so every requirement above is visible.

Engineering
- update(dt) is called once per frame with a delta clock. Keep the controller free of rendering code.
- No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with comments naming each rule above.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.25` | Movement maths is exact; the lowest setting here is deliberate. |
| `seed` | `4242` | API seed; the controller is deterministic. |
| `max_output_tokens` | `6000` | Fits the controller plus the test scene. |

## Expected output

- `index.html` — one file, roughly 350–550 lines.
- The controller reads only the `input` object — no `addEventListener` inside it.

## Verify it worked

- [ ] Grounded state is stable while walking on flat ground (no flicker).
- [ ] The 45-degree slope is walkable; the 60-degree slope causes sliding.
- [ ] Walking off the ramp allows a jump for a moment afterwards (coyote time).
- [ ] Jumping just before landing still jumps (jump buffering).
- [ ] Tapping jump gives a shorter hop than holding it.
- [ ] The player steps up a 0.4-unit ledge without jumping.
- [ ] The player inherits the moving platform's velocity when standing on it.
- [ ] The controller contains no keyboard listeners; input arrives via the object.
- [ ] Console is clean.

## Tune it

- **Slope limit (45°)** and **coyote/ buffer windows** — the feel dials most players notice.
- **Max speed and acceleration** — heavy vs. snappy.

## Where it drifts

- **Coyote time and jump buffering conflated into one timer.** They are separate windows around the
  same event; merging them makes one of the two checks fail. Test each independently.
- **Grounded flicker.** A single downward ray misses on slopes; the model needs a small sphere cast or
  multiple rays. The "stable grounded state" check catches the flicker.
- **Instant direction changes.** Accel/friction omitted because they are fiddly. Watch a 180° turn —
  a snap means friction was skipped.
- **Keyboard read inside the controller.** Makes it untestable and un-drivable by AI. The input-object
  requirement is the guard.

## Provenance

- Technique: original; the coyote/buffer pattern is standard platformer practice.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
