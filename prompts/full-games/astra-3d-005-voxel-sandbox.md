---
id: astra-3d-005
title: Voxel Sandbox
category: full-games
slug: voxel-sandbox
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.35
top_p: 0.9
seed: 1337
max_output_tokens: 9000
runtime: modern browser
stack: Three.js
difficulty: advanced
verified: draft
tags: [threejs, webgl, voxel, sandbox, greedy-mesh, single-file]
license: CC0-1.0
---

# Voxel Sandbox

> A seeded voxel world you can fly around, dig into, and build in — with greedy-meshed chunks.

## What you get

`index.html`, self-contained: a chunked voxel world generated from a seed, greedy meshing so the
triangle count stays sane, block add/remove by raycast, and a simple hotbar. The hardest of the
full-game recipes, and the one where performance discipline matters most.

## Before you start

- **Runtime:** any modern browser with WebGL2.
- **Dependencies:** none; Three.js via CDN import map.
- **Assets / inputs:** none. Block colours are defined in code.
- **Model access:** plain chat completion; this is the largest output in the list.

## The prompt

```text
You are a senior Three.js engineer. Build a chunked voxel sandbox in ONE self-contained index.html.

Deliverable
- A single `index.html` that runs by double-clicking it. No build step, no server.
- Three.js r170+ via an import map from a CDN. No external assets.

World
- Declare `const SEED = 1337;` and `const CHUNK = 16;`. Generate terrain height and block types from
  a small seeded noise implementation you write yourself (no external library).
- World is 8x8 chunks (128x128 blocks), height 32, with grass/dirt/stone/water block types.
- Rebuild only the chunks that changed when a block is edited. Never rebuild the whole world per frame.

Meshing (performance is the point)
- Implement greedy meshing per chunk so that coplanar faces of the same block type merge into
  quads. Upload each chunk as a single BufferGeometry.
- Use a single texture-free material with per-vertex colours per block type.

Interaction
- First-person controls with pointer lock: WASD, mouse look, Space to fly up, Shift to fly down
  (a creative/fly mode is acceptable and simpler than a walk mode).
- Raycast from the crosshair. Left-click removes the targeted block; right-click places the currently
  selected block on the face you are looking at. Do not allow placing inside the player.
- A hotbar of at least four block types selectable with keys 1-4, with a visible selection indicator.

HUD
- Show the current block type, the chunk count, and an FPS counter.

Engineering
- requestAnimationFrame with a delta-time clock.
- Separate concerns: world data, noise, chunk meshing, block edit, raycast/interaction, HUD, rendering.
- Dispose of old geometry when a chunk is remeshed so memory does not grow.
- Handle resize and devicePixelRatio. No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with brief comments per subsystem.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.35` | Meshing algorithms benefit from a little latitude, but the chunk contract must hold. |
| `seed` | `1337` | API seed; the world seed is the in-prompt `SEED`. |
| `max_output_tokens` | `9000` | The largest recipe. Truncation here produces a half-written file — give it room. |

## Expected output

- `index.html` — one file, roughly 800–1200 lines.
- A greedy-meshing function that merges coplanar faces, plus per-chunk geometry disposal.

## Verify it worked

- [ ] Terrain appears and is walkable/flyable with no missing chunks.
- [ ] The same `SEED` produces the same terrain across reloads; changing it changes the terrain.
- [ ] Left-click removes the targeted block; right-click places one on the face you see.
- [ ] Editing a block remeshes **only** the affected chunk(s) — confirm via the FPS counter staying high.
- [ ] Memory does not climb steadily while digging for a minute (geometry is disposed).
- [ ] Keys 1-4 change the selected block and the HUD reflects it.
- [ ] Framerate is stable while flying across the world.

## Tune it

- **World size** (`8x8` chunks) — the first thing to cut if it is slow.
- **`CHUNK` size** — 16 is a compromise; 32 means fewer meshes but more work per remesh.

## Where it drifts

- **"Greedy meshing" that is actually naive per-face meshing.** The output will still look right but
  will be slow. The FPS check while traversing, and the requirement to describe merging, are the
  guards. If the author is honest, the code shows merged quads.
- **Full-world rebuild on every edit.** The dominant failure. The "rebuild only changed chunks"
  requirement exists precisely because it is what separates a working voxel demo from a slideshow.
- **Geometry leak.** Old chunk geometries not disposed. The memory check catches it.
- **Raycast ignoring placed-block bounds.** Right-click places a block inside the player and they get
  stuck. The "do not place inside the player" constraint is not optional.

## Provenance

- Technique: greedy meshing is a well-known voxel technique (see the classic 0fps write-up); this
  recipe bounds it to a single file and pins the seed.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
