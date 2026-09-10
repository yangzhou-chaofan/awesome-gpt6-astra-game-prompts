---
id: astra-3d-004
title: Top-Down Arena Shooter
category: full-games
slug: topdown-arena-shooter
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.3
top_p: 0.9
seed: 4242
max_output_tokens: 7500
runtime: modern browser
stack: Three.js
difficulty: intermediate
verified: draft
tags: [threejs, webgl, shooter, arena, twin-stick, single-file]
license: CC0-1.0
---

# Top-Down Arena Shooter

> A twin-stick arena shooter with waves, pooled bullets, and enemy AI that closes in from all sides.

## What you get

`index.html`, self-contained: an orthographic top-down camera, WASD movement plus mouse aiming,
pooled projectiles, three enemy behaviours (chaser, charger, shooter), escalating waves, health,
score, and win/lose overlays.

## Before you start

- **Runtime:** any modern browser.
- **Dependencies:** none; Three.js via CDN import map.
- **Assets / inputs:** none; primitives only.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior Three.js engineer. Build a complete top-down twin-stick arena shooter in ONE index.html.

Deliverable
- A single `index.html` that runs by double-clicking it. No build step, no server.
- Three.js r170+ via an import map from a CDN. Primitives only, no external assets.
- Use an orthographic camera looking down at a fixed angle, so movement reads clearly.

Player
- WASD to move; the mouse aims and left-click fires. The player is a capsule/cylinder with a barrel
  that points at the cursor.
- Health (100) with regeneration after 5 seconds without taking damage. Invulnerability frames of
  0.5s after a hit, shown by blinking.
- Movement is clamped to the arena bounds (a bounded square with visible walls).

Projectiles
- Implement an object pool for bullets: pre-allocate N bullets, reuse them, never allocate in the loop.
- Player bullets damage enemies; enemy bullets damage the player. Bullets die on the arena wall.

Enemies
- Three types, spawned from the arena edges:
  1. Chaser — walks straight at the player.
  2. Charger — periodically dashes at high speed in a straight line.
  3. Shooter — keeps distance and fires slow projectiles.
- Enemies have health, contact/attack damage, and are killed by bullets. Kills grant score.

Waves and UI
- Waves spawn increasing counts and mix types. A short gap between waves.
- HUD: health bar, score, wave number, and enemies remaining.
- Game over overlay on death; victory overlay after the defined final wave. Both restart cleanly.

Determinism
- Declare `const SEED = 4242;` and use a small seeded PRNG you implement yourself for spawn positions
  and any variation. Wave *composition* is hard-coded, not random.

Engineering
- requestAnimationFrame with a delta-time clock; all speeds and rates per second.
- Separate concerns: input, player, enemies, bullets/pool, waves, collisions, UI, rendering.
- Simple circle-vs-circle collision. No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with brief comments per subsystem.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.3` | The pool and AI behaviours are easy to get subtly wrong; keep it tight. |
| `seed` | `4242` | API seed plus in-prompt `SEED`. |
| `max_output_tokens` | `7500` | Fits the pool plus three enemy behaviours. |

## Expected output

- `index.html` — one file, roughly 550–850 lines.
- An explicit, reusable bullet pool — not a `bullets.push()`/`splice()` per shot.

## Verify it worked

- [ ] The player moves with WASD and the barrel tracks the mouse.
- [ ] Firing continuously for a minute does not grow memory (pool is reused).
- [ ] Each of the three enemy types visibly behaves differently.
- [ ] Bullets stop at the arena walls; the player cannot leave the arena.
- [ ] Health regenerates after a lull and blinks during i-frames.
- [ ] Waves escalate and the victory overlay appears after the final wave.
- [ ] Restart fully resets health, score, wave, and all enemy/bullet state.
- [ ] Console is clean; frame rate steady with 20+ enemies alive.

## Tune it

- **Fire rate and player speed** — the feel dials.
- **Enemy mix per wave** — the difficulty curve.

## Where it drifts

- **The "pool" is a facade.** Many outputs name a pool but allocate per frame. The memory check in the
  acceptance list is what exposes it — watch the browser's memory timeline while firing.
- **Enemies stack into one blob.** No separation steering, so all chasers occupy the same point. If it
  matters to you, add a light repulsion term; the recipe accepts either but should be read with eyes
  open.
- **Delta-time applied twice.** Speed doubles on high-refresh monitors. Verify on a 144 Hz display or
  by capping refresh in devtools.

## Provenance

- Technique: original; twin-stick decomposition with an explicit pool requirement.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
