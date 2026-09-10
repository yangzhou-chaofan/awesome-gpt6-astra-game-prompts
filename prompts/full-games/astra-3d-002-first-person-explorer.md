---
id: astra-3d-002
title: First-Person Explorer
category: full-games
slug: first-person-explorer
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.35
top_p: 0.9
seed: 4242
max_output_tokens: 7000
runtime: modern browser
stack: Three.js
difficulty: intermediate
verified: draft
tags: [threejs, webgl, first-person, terrain, collectibles, single-file]
license: CC0-1.0
---

# First-Person Explorer

> A seeded low-poly landscape you walk through in first person, collecting twelve glowing orbs
> against a timer.

## What you get

`index.html`, self-contained: pointer-lock controls, gravity and ground collision on a seeded
heightmap, twelve deterministically placed collectibles, a pickup counter, and a completion overlay
with elapsed time. The terrain is generated from a `SEED` constant you can change.

## Before you start

- **Runtime:** any modern browser.
- **Dependencies:** none; Three.js via CDN import map.
- **Assets / inputs:** none. The terrain is code, not a heightmap image.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior Three.js engineer. Build a first-person explorer demo in ONE self-contained index.html.

Deliverable
- A single `index.html` that runs by double-clicking it. No build step, no server.
- Three.js r170+ via an import map from a CDN.

World (must be deterministic)
- Declare `const SEED = 4242;` near the top. All terrain and all collectible positions derive from it.
- Generate a heightmap terrain procedurally with a small noise function you implement yourself
  (value noise or simplex; no external library). Resolution around 128x128, world size 100x100 units.
- Colour the terrain by height with vertex colours (low = dark green, high = grey rock).
- Place exactly 12 collectibles at positions derived from the same SEED. Each is a small glowing
  sphere with a gentle bobbing animation and a point light.

Controls and physics
- Pointer-lock first-person camera. Click the start overlay to lock the pointer.
- WASD to move, mouse to look, Shift to sprint, Space to jump.
- Gravity, ground collision against the heightmap, and a head-height eye offset. The player must not
  fall through terrain or float above it.
- Walking to within 2 units of a collectible picks it up: it disappears, a counter increments,
  and a soft flash plays.

HUD and completion
- A fixed HUD showing "Orbs: n / 12" and an elapsed timer.
- When the counter reaches 12, show a completion overlay with the final time and a restart button.

Engineering
- requestAnimationFrame with a delta-time clock; framerate-independent movement.
- Separate input, terrain, player physics, interaction, and rendering into clearly named functions.
- Handle resize and devicePixelRatio.
- No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with brief comments per subsystem.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.35` | Slightly above the runner: terrain generation benefits from a little variation, but structure must hold. |
| `seed` | `4242` | API seed where available; the *world* seed lives in the prompt as `SEED`. |
| `max_output_tokens` | `7000` | The terrain and noise code make this file longer than the runner. |

## Expected output

- `index.html` — one file, roughly 400–650 lines.
- No external images, no `.glb`, no noise library — the noise implementation is inline.

## Verify it worked

- [ ] The start overlay appears; clicking it locks the pointer and hides the overlay.
- [ ] WASD moves relative to look direction; the player stays on the surface on slopes.
- [ ] Jumping works and the player lands back on the terrain, not through it.
- [ ] Exactly 12 orbs exist and all are reachable by walking.
- [ ] Walking near an orb removes it and increments the counter.
- [ ] Collecting all 12 shows the completion overlay with a plausible elapsed time.
- [ ] Changing `SEED` and reloading produces a different terrain and different orb positions.
- [ ] Console is clean.

## Tune it

- **`SEED`** — the whole world. Keep it recorded when you share a screenshot.
- **Terrain resolution** (128 → 256) — sharper hills, more triangles; the first thing to hit
  performance on integrated graphics.

## Where it drifts

- **The player falls through the terrain.** Sampling the heightmap at the wrong scale is the classic
  failure. The "must not fall through" requirement plus a slopes check catches it; test on a steep
  hill, not just flat ground.
- **Orbs placed by unseeded `Math.random()`.** Then the world is not reproducible and the SEED
  requirement is a lie. The check "changing SEED changes orb positions" is what exposes it — if
  positions do not change, the seed was ignored.
- **Pointer lock started without a user gesture.** Browsers refuse it. The "click to start overlay"
  requirement is not cosmetic; it is required for the demo to work at all.
- **Noise copied from an external library by reference.** The "implement it yourself, no external
  library" constraint keeps the file self-contained; verify there is no `<script src>` to a noise lib.

## Provenance

- Technique: original; heightmap + collectible pattern is standard tutorial territory, tightened here
  for determinism.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
