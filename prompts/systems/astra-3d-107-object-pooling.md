---
id: astra-3d-107
title: Object Pooling & Culling
category: systems
slug: object-pooling
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.25
top_p: 0.9
seed: 4242
max_output_tokens: 6000
runtime: modern browser
stack: Three.js
difficulty: advanced
verified: draft
tags: [threejs, performance, pooling, instancing, culling, memory]
license: CC0-1.0
---

# Object Pooling & Culling

> Sustained 10,000 moving objects without a single allocation in the frame loop.

## What you get

`index.html`, self-contained: a stress scene of 10,000 projectiles driven by an explicit pool and
instanced meshes, with frustum culling and an on-screen allocation counter proving the loop is
allocation-free.

## Before you start

- **Runtime:** modern browser with WebGL2.
- **Dependencies:** Three.js via CDN import map.
- **Assets / inputs:** none.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior performance engineer. Build a stress test in one self-contained index.html for
Three.js that simulates 10,000 projectiles with zero allocation in the frame loop.

Deliverable
- One `index.html`, runs on double-click. Three.js r170+ via import map. No external assets.

Pools
- An explicit pool of 10,000 projectiles backed by fixed-size typed arrays (Float32Array for position,
  velocity, age, alive flag). Do NOT allocate objects, arrays, or closures inside update().
- Spawning reuses dead slots in a free list; when the pool is exhausted, the oldest projectile is
  recycled. Document the policy in a comment.

Rendering
- Use a single THREE.InstancedMesh with capacity 10,000 and setMatrixAt per live projectile. Set
  instanceMatrix.needsUpdate once per frame. No per-object Mesh, no per-frame geometry creation.

Culling and LOD (where it matters)
- Skip updating and rendering projectiles outside the camera frustum where that is cheaper than
  updating them; document the trade-off. Beyond a distance threshold, freeze projectiles and render
  them as a single merged batch.
- Group projectiles into spatial buckets (a coarse grid) so collision checks against a handful of
  targets are O(n) and not O(n*m).

Instrumentation (the acceptance surface)
- An overlay showing: live count, freed count, current frame time (ms), a rolling 60-frame average, and
  an "allocations this frame" counter that must stay at 0 during steady state.
- A `performance.measureUserAgentSpecificMemory` or `performance.memory` reading where available.

Controls
- Start spawn at 10,000/s; buttons to add/remove 1,000 projectiles per second; a button to toggle the
  debug overlay.

Engineering
- requestAnimationFrame with a delta clock. Projectile motion is integrated with the delta.
- No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with comments for the pool, the
  instanced rendering, and the culling policy.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.25` | Tight-array code and instancing have little room for variation. |
| `seed` | `4242` | API seed. |
| `max_output_tokens` | `6000` | The pool, instancing, buckets and overlay. |

## Expected output

- `index.html` — one file, roughly 400–600 lines.
- Fixed-size typed arrays and a single `InstancedMesh` with capacity 10,000.

## Verify it worked

- [ ] 10,000 projectiles run and visibly move.
- [ ] The "allocations this frame" counter stays at 0 in steady state.
- [ ] Memory does not grow over a minute of running.
- [ ] Frame time stays reasonable (target under ~8 ms on the test machine) and is displayed.
- [ ] Recycling the oldest projectile is visible on the overlay when the pool saturates.
- [ ] Toggling the overlay does not itself allocate noticeably.
- [ ] No per-object `Mesh` exists in the scene graph for projectiles.
- [ ] Console is clean.

## Tune it

- **Pool capacity** — 10,000 vs. 50,000 changes which limit you hit first.
- **Spatial bucket size** — trades collision cost against bucket overhead.

## Where it drifts

- **A "pool" that still allocates.** `new THREE.Vector3()` inside the loop, or closures per spawn,
  defeats the whole recipe. The allocations-per-frame counter is the only honest check — read it.
- **InstancedMesh matrices updated per-object.** Setting `needsUpdate` inside the loop uploads the
  buffer thousands of times. The requirement to set it once per frame is the guard.
- **`performance.memory` assumed present.** It is Chromium-only; the recipe allows a fallback rather
  than crashing on Firefox.
- **Culling that costs more than it saves.** Computing frustum checks for 10,000 tiny objects can be
  slower than drawing them. The documented trade-off requirement keeps the author honest.

## Provenance

- Technique: original; instancing and pooling are conventional, turned into a measurable recipe by the
  allocation counter and the explicit pool policy.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
