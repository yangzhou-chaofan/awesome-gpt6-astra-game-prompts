---
id: astra-3d-105
title: Third-Person Camera Rig
category: systems
slug: third-person-camera
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.25
top_p: 0.9
seed: 4242
max_output_tokens: 5500
runtime: modern browser
stack: Three.js
difficulty: intermediate
verified: draft
tags: [threejs, camera, third-person, spring-arm, collision]
license: CC0-1.0
---

# Third-Person Camera Rig

> A spring-arm camera that orbits, follows, never clips through walls, and eases rather than snaps.

## What you get

`index.html`, self-contained: a third-person rig with mouse orbit, distance zoom, a smoothed follow
that lags the target naturally, and spring-arm collision so the camera pulls in when a wall is behind
the player.

## Before you start

- **Runtime:** modern browser.
- **Dependencies:** Three.js via CDN import map.
- **Assets / inputs:** none; the test scene is a room with pillars.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior game engineer. Build a third-person camera rig for Three.js in one self-contained
index.html, with a scene that exercises it.

Deliverable
- One `index.html`, runs on double-click. Three.js r170+ via import map. No external assets.
- Expose `createThirdPersonCamera(camera, target, collisionMeshes)` returning `update(dt, input)`.

Requirements
- Orbit: mouse movement (pointer lock) controls yaw and pitch. Clamp pitch to roughly -30..+70 degrees.
- Distance: mouse wheel zooms between 2 and 10 units, smoothly interpolated, not stepped.
- Follow: the rig follows a target point at the player's head height. Position and look-at both use
  exponential smoothing (frame-rate independent: `1 - exp(-k * dt)`), so the camera lags a hard turn
  slightly rather than snapping.
- Spring arm collision: cast from the target toward the desired camera position; if a wall is hit,
  pull the camera in to just before the hit. Never let the camera pass through geometry.
- Target collision: if the camera would end up inside the player mesh, push the near plane / distance
  so the player is not clipped through.
- No jitter when the player moves and the mouse is still. No gimbal flip at the pitch limits.

Test scene
- A room with pillars and a narrow corridor, plus a WASD capsule to move the target, so collision can
  be exercised by backing into a wall or a pillar.

Engineering
- Rotation is applied in a stable order (yaw then pitch) to avoid roll.
- No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with comments for orbit, smoothing,
  and spring-arm collision.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.25` | Smoothing constants and order-of-operations are exact. |
| `seed` | `4242` | API seed; the rig is deterministic. |
| `max_output_tokens` | `5500` | The rig plus a small scene. |

## Expected output

- `index.html` — one file, roughly 300–450 lines.
- Frame-rate-independent smoothing via an exponential term — not a fixed `lerp(0.1)` per frame.

## Verify it worked

- [ ] Mouse orbits the camera; pitch clamps without flipping.
- [ ] Wheel zoom is smooth and bounded between 2 and 10 units.
- [ ] The camera lags a hard turn slightly, then settles — no snap.
- [ ] Backing into a wall pulls the camera in; it never ends up behind the wall.
- [ ] Standing still after moving produces no jitter.
- [ ] The player is never clipped through at close range.
- [ ] Camera behaviour is identical at 60 Hz and 144 Hz.
- [ ] Console is clean.

## Tune it

- **Smoothing constant `k`** — responsive vs. cinematic.
- **Pitch clamp** — how much the player can look up.

## Where it drifts

- **Frame-rate-dependent smoothing.** `position.lerp(target, 0.1)` each frame means the camera behaves
  differently on different monitors. The exponential form and the 60/144 Hz check are the guards.
- **Spring arm only checking the camera's final point.** The camera can clip on the way. Must cast
  along the arm and pull in to the first hit.
- **Gimbal flip.** Rotation applied pitch-then-yaw or with Euler roll. The stable-order requirement and
  the pitch-limit check catch it.
- **Zoom applied instantly.** Stepped wheel zoom feels cheap; the smooth interpolation requirement
  addresses it.

## Provenance

- Technique: original; spring-arm cameras are conventional, made reproducible here by pinning the
  smoothing model and collision test.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
