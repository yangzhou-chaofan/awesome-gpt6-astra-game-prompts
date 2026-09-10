---
id: astra-3d-303
title: Navmesh from Level Geometry
category: levels
slug: navmesh-baker
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.3
top_p: 0.9
seed: 4242
max_output_tokens: 7500
runtime: modern browser
stack: Three.js
difficulty: advanced
verified: draft
tags: [threejs, navmesh, pathfinding, a-star, agents, baking, navigation]
license: CC0-1.0
---

# Navmesh from Level Geometry

> Bake a navigation mesh from the level's walkable surfaces, then path agents across it — the missing
> link between a level and AI that can move through it.

## What you get

`index.html`, self-contained: a voxelise-and-merge navmesh baker over arbitrary walkable geometry, a
portal graph, A* over that graph with funnel/simple string-pulling, and ten agents that path from
clicked start to clicked goal.

## Before you start

- **Runtime:** modern browser with WebGL2.
- **Dependencies:** Three.js via CDN import map.
- **Assets / inputs:** a test level of boxes and ramps, built in code.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior gameplay engineer. Build a navmesh baker and pathfinding demo in one self-contained
index.html for Three.js.

Deliverable
- One `index.html`, runs on double-click. Three.js r170+ via import map. No external assets.
- The test level is built in code: a floor, several boxes as obstacles, a ramp and a narrow doorway.

Baking (implement it yourself; no navmesh library)
- Voxelise the walkable surfaces: sample the level with downward raycasts on a grid, keep cells whose
  surface normal is within the walkable slope limit (45 degrees) and which have headroom.
- Recast-style region merging: flood-fill contiguous walkable cells, compute a convex polygon
  approximation per region (or keep a tile grid if you document the choice), and store the result as a
  navmesh of polygons with adjacency.
- Erode the navmesh by the agent radius (default 0.4 units) so agents do not clip corners.
- Build a portal graph between adjacent polygons; each portal is the shared edge.

Pathfinding
- A* over the polygon graph using portal midpoints as an initial path, then apply a funnel (simple
  string-pulling) pass so the resulting path hugs corners instead of zig-zagging through centres.
- Expose `findPath(from, to)` returning an array of world-space waypoints, or null if unreachable.
- Agents: 10 capsules that walk along a computed path with steering and simple avoidance, so two agents
  meeting in the doorway do not deadlock permanently.

Debug visualisation
- Toggleable overlay showing the navmesh polygons, the portal edges, the raw A* path and the smoothed
  path, plus the voxel grid that produced them.
- Click on the floor to set a goal; the nearest agent paths from its position to it.

Engineering
- Baking runs once on level load (and on demand), not per frame.
- Separate: voxelisation, region merging, portal graph, A*, funnel, agent steering, debug overlay.
- No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with comments per stage.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.3` | Geometry and graph code is exact; the algorithm choice is the only latitude. |
| `seed` | `4242` | API seed; the demo level is deterministic. |
| `max_output_tokens` | `7500` | Voxelisation through agents is a large single file. |

## Expected output

- `index.html` — one file, roughly 600–900 lines.
- A baked navmesh with polygons, adjacency portals, A* and a funnel pass.

## Verify it worked

- [ ] The debug overlay shows a navmesh covering the floor and ramp but not the obstacles.
- [ ] The ramp is included; steep sides of boxes are excluded (slope limit works).
- [ ] Clicking a goal produces a path that goes around obstacles, not through them.
- [ ] The smoothed path hugs corners rather than zig-zagging through polygon centres.
- [ ] Erosion keeps agents from clipping into wall corners.
- [ ] An unreachable goal (across a gap) returns null rather than a path through the void.
- [ ] Ten agents move without permanent deadlock at the doorway.
- [ ] Console is clean.

## Tune it

- **Voxel cell size** — accuracy vs. bake time. Halving it quadruples the work.
- **Agent radius** — how much the navmesh erodes; watch the doorway close if set too high.

## Where it drifts

- **Navmesh with no erosion.** Agents clip through corners and catch on doorways. The erosion
  requirement and the "no clipping" check address it.
- **A* that walks polygon centres.** Paths look drunk. The funnel pass requirement is the fix; verify by
  checking that path corners align with geometry corners.
- **Adjacency built from centroid distance instead of shared edges.** Agents path through walls
  diagonally. Portals must be shared *edges*; the obstacle check catches it.
- **Baking every frame.** The overlay updates trigger a rebake and the demo stutters. The bake-once
  requirement prevents this.
- **Ramp dropped by the slope check.** Normal threshold too strict. Verify the ramp is in the navmesh.

## Provenance

- Technique: Recast-style voxelisation → regions → portals, plus A* and a funnel; simplified to a single
  browser file. The approach is well documented publicly.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
