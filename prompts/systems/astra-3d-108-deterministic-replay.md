---
id: astra-3d-108
title: Deterministic Replay Harness
category: systems
slug: deterministic-replay
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.25
top_p: 0.9
seed: 4242
max_output_tokens: 6500
runtime: modern browser
stack: Three.js
difficulty: advanced
verified: draft
tags: [threejs, determinism, replay, fixed-timestep, testing, lockstep]
license: CC0-1.0
---

# Deterministic Replay Harness

> Record an input sequence, replay it, and get a bit-identical simulation — the foundation for
> regression-testing a game.

## What you get

`index.html`, self-contained: a tiny deterministic game, a fixed-timestep simulation with integer
physics, an input recorder, a replay player, and a hash of the world state each tick so divergence is
detectable at the exact frame it happens.

## Before you start

- **Runtime:** modern browser.
- **Dependencies:** Three.js via CDN import map.
- **Assets / inputs:** none.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior simulation engineer. Build a deterministic replay harness in one self-contained
index.html with Three.js.

Deliverable
- One `index.html`, runs on double-click. Three.js r170+ via import map. No external assets.

Deterministic simulation
- A fixed timestep of exactly 1/60 s. Rendering interpolates between the two most recent states and
  never feeds back into the simulation.
- Simulation state uses integer or fixed-point maths only (positions in thousandths of a unit, integer
  velocities). NO floating-point accumulation in game logic, NO Math.random(), NO Date.now() inside the
  sim. Any randomness comes from a seeded integer PRNG stored in the state.
- The simulation is a pure function: `step(state, inputs) -> state`. No other global mutable state.

The game
- Keep it minimal but non-trivial: a player square on a bounded field, plus 20 bouncing square "balls"
  with ball-vs-ball and ball-vs-wall collisions, all in integer maths. Enough that divergence would
  actually occur if determinism were broken.

Recording and replay
- Record the input bitmask per tick. A "Record" button starts a run; a "Replay" button re-runs the
  stored inputs from the initial state.
- At the end of each tick, compute a hash of the full simulation state (e.g. FNV-1a over the state
  array) and store it. During replay, compare the hash each tick.
- If a hash mismatch occurs, stop and display the exact tick number and the two hashes. This is the
  point of the recipe.

Instrumentation
- Overlay showing: current tick, recorded tick count, live hash, and a PASS/FAIL for the last replay.

Engineering
- requestAnimationFrame drives rendering; the sim advances by accumulated real time in fixed ticks.
- No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with comments for the fixed step, the
  integer maths, the PRNG, hashing, and the replay comparison.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.25` | Determinism is binary; any creativity here is a bug. |
| `seed` | `4242` | API seed; the *simulation* seed is stored in state and recorded. |
| `max_output_tokens` | `6500` | Sim + recorder + hashing + overlay. |

## Expected output

- `index.html` — one file, roughly 450–700 lines.
- A `step(state, inputs)` pure function, integer state arrays, an FNV-1a hash, and a per-tick hash log.

## Verify it worked

- [ ] Recording a run and replaying it produces identical hashes for every tick (PASS).
- [ ] Replaying the same recording twice gives the same result.
- [ ] Deliberately introducing floating point or `Math.random()` into the sim makes replay FAIL and
      reports the first diverging tick — proving the harness can actually detect divergence.
- [ ] The simulation runs at the same rate regardless of display refresh rate.
- [ ] No `Math.random()`, `Date.now()`, or float accumulation appears in the simulation code.
- [ ] Console is clean.

## Tune it

- **Number of balls** — more collisions means more chances for divergence; 20 is a good stress level.
- **Fixed timestep** — keep 1/60 unless you have a reason; changing it changes the recorded format.

## Where it drifts

- **Floating point creeps back in.** The model writes `position += velocity * dt` with floats. Replay
  then diverges on some machines and the harness fails to detect it if the hash is computed from
  rounded values. The integer-maths requirement and the deliberate-break check are the guards.
- **Hash computed from rendering state, not simulation state.** Then it never detects anything. The
  requirement to hash the full simulation state addresses this.
- **Input recorded per frame instead of per tick.** At high refresh rates more inputs than ticks are
  recorded and replay desynchronises. Record per tick.
- **The harness cannot fail.** If no deliberate break can produce a mismatch, the comparison is
  broken. The third acceptance check exists to prove the detector works.

## Provenance

- Technique: original; lockstep determinism and state hashing are standard in networked and
  speedrunning-adjacent engineering.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
