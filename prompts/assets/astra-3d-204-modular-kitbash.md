---
id: astra-3d-204
title: Modular Kit-Bash Set
category: assets
slug: modular-kitbash
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.4
top_p: 0.9
seed: 4242
max_output_tokens: 7000
runtime: Blender 4.x CLI
stack: Blender 4.x
difficulty: intermediate
verified: draft
tags: [blender, modular, kitbash, level-design, gltf, assets]
license: CC0-1.0
---

# Modular Kit-Bash Set

> A grid-snapped modular kit — walls, floors, doors, pillars — where every piece tiles with every
> other and exports as a single GLB.

## What you get

`build_kit.py`: procedurally builds a modular set on a fixed grid (default 4 m), with consistent pivot
points and naming, exports all pieces into one GLB, and validates that every piece sits exactly on the
grid and shares the same material palette. This is what makes procedurally generated levels buildable.

## Before you start

- **Runtime:** Blender 4.x headless.
- **Dependencies:** none beyond Blender.
- **Assets / inputs:** none.
- **Model access:** plain chat completion.

## The prompt

```text
You are a technical artist writing Blender Python. Produce `build_kit.py` that generates a modular
kit-bash set and exports it as a single GLB.

Hard requirements
- Blender 4.x only, runs headless: `blender --background --python build_kit.py`.
- `const`-style parameters at the top: GRID = 4.0 (metres), WALL_HEIGHT = 3.0, WALL_THICKNESS = 0.2,
  MULLIONS = 3, SEED. Everything derives from these.

Pieces (each on the grid, pivot at the piece's grid origin, +Z up before export)
- floor:         a GRID x GRID tile, subtle top-surface variation.
- wall:          a GRID-wide, WALL_HEIGHT-tall panel, thickness WALL_THICKNESS.
- wall_window:   a wall with MULLIONS vertical window sections cut through it.
- wall_door:     a wall with a doorway opening GRID*0.5 wide and WALL_HEIGHT*0.8 tall.
- wall_corner:   an L-shaped corner piece spanning GRID on both arms.
- pillar:        a square column GRID*0.25 across, WALL_HEIGHT tall.
- stairs:        a run of steps rising WALL_HEIGHT over one GRID.
- railing:       a GRID-wide rail with vertical balusters.

Consistency rules (the point of a kit)
- Every piece except pillar, stairs and railing must be exactly GRID wide/deep so edges meet flush.
- Every piece's origin is its bottom-centre-min corner ON the grid: a piece placed at integer grid
  coordinates must tile with its neighbour with zero gap and zero overlap. Verify this in script by
  bounding-box checks and PRINT any piece that is off-grid.
- One shared material palette (floor_stone, wall_plaster, wood, metal) used consistently across
  pieces. No per-piece materials.
- 150-600 triangles per piece.

Export and validation
- Export all pieces as separate objects into `out/kit.glb`, named exactly after the piece
  (floor, wall, wall_window, ...), +Y up, 1 unit = 1 metre.
- Re-import and print, per piece: name, triangle count, bbox dimensions, and a PASS/FAIL for the grid
  check. Fail loudly (non-zero exit) if any piece is off-grid or a name is missing.

Determinism
- Seeded PRNG for surface variation; the same SEED must give an identical GLB.

Structure
- Functions: parameters, make_floor, make_wall, make_wall_variant, make_corner, make_pillar,
  make_stairs, make_railing, assign_materials, export_and_validate, run from `__main__`.

Output
- Output ONLY the full contents of build_kit.py in one code block.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.4` | Piece shapes have latitude; the grid and naming rules do not. |
| `seed` | `4242` | API seed; geometry seed is `SEED`. |
| `max_output_tokens` | `7000` | Eight pieces plus validation. |

## Expected output

- `build_kit.py` — one script, roughly 400–650 lines.
- `out/kit.glb` with eight named objects sharing one material palette.

## Verify it worked

- [ ] Headless run exits 0 and writes `out/kit.glb` with all eight named pieces.
- [ ] The grid check passes for every piece; moving a piece by hand off-grid makes it report FAIL.
- [ ] Dropping two walls side by side produces zero gap and no z-fighting.
- [ ] A wall, a window wall and a door wall are the same outer dimensions.
- [ ] All pieces use only the four shared materials.
- [ ] Re-running with the same `SEED` yields an identical GLB.
- [ ] The kit imports into a game engine and snaps cleanly to integer grid positions.

## Tune it

- **`GRID`** — the whole set scales with it; keep it recorded because levels depend on it.
- **`MULLIONS`** — window density.

## Where it drifts

- **Off-grid pieces.** The dominant failure: a wall built to `WALL_THICKNESS` wider than the grid, so
  every junction has a gap. The explicit bbox grid check and the flush-tiling check are the guard —
  this is why the recipe spends a requirement on it.
- **Pivot points in inconsistent places.** Pieces pivot at their centre for some and their corner for
  others, so placement maths must special-case every piece. The "origin is bottom-centre-min corner"
  rule prevents it.
- **Per-piece materials.** The model creates a new material per piece, defeating the kit. The shared
  palette requirement and the material-count check catch it.
- **Naming drift.** Objects named `Wall.001`. The exact-name requirement is what makes the kit
  scriptable downstream.

## Provenance

- Technique: original; modular level-design conventions, made machine-checkable by the grid
  validation step.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
