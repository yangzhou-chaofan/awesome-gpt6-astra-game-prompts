---
id: astra-3d-203
title: Rigged Character from a Prompt
category: assets
slug: rigged-character
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.4
top_p: 0.9
seed: 4242
max_output_tokens: 7500
runtime: Blender 4.x CLI
stack: Blender 4.x
difficulty: advanced
verified: draft
tags: [blender, rigging, armature, skinning, gltf, character, assets]
license: CC0-1.0
---

# Rigged Character from a Prompt

> A Blender script that builds a low-poly humanoid, rigs it with a named bone hierarchy, skins it, and
> exports an animated GLB with a walk cycle.

## What you get

`build_character.py`: procedurally constructs a stylised humanoid from primitives, creates an armature
with a conventional bone naming scheme, parents the mesh with automatic weights, adds a looping walk
cycle, and exports `out/character.glb` with the animation included. Advanced because skinning is where
procedural generation most often fails.

## Before you start

- **Runtime:** Blender 4.x headless.
- **Dependencies:** none beyond Blender.
- **Assets / inputs:** none.
- **Model access:** plain chat completion (code-execution helpful).

## The prompt

```text
You are a technical artist writing Blender Python. Produce `build_character.py` that builds, rigs,
skins and animates a low-poly humanoid, then exports a game-ready GLB.

Hard requirements
- Blender 4.x API only, runs headless: `blender --background --python build_character.py`.
- Parameters at the top: HEIGHT, HEAD_SCALE, LIMB_THICKNESS, SEED. Derive geometry from them.
- Mesh from primitives, 400-1500 triangles, one flat-colour material per body region
  (skin, cloth, hair, boots) — no textures.

Armature (use these exact bone names)
- root, hips, spine, chest, neck, head,
  shoulder.L/R, upper_arm.L/R, forearm.L/R, hand.L/R,
  thigh.L/R, shin.L/R, foot.L/R.
- Build the armature in edit mode with correct parenting and sensible roll. Mirror the left/right bones.
- Bones must be positioned inside the mesh limbs, not floating beside them.

Skinning
- Parent the mesh to the armature with automatic weights.
- Then POST-PROCESS the weights: for each vertex, ensure the weights are normalised and that no vertex
  has more than 4 bone influences (glTF limit). Report any vertex left with zero total weight and fix
  it by assigning it to the nearest bone.

Animation
- Create a walk cycle on the armature, 24 frames looping at 24 fps: alternating leg swing, opposite arm
  swing, slight hip and chest counter-rotation, and a subtle head bob.
- The first and last keyframes must be identical so the loop is seamless. Set the action name to "Walk".
- Keep it driven by keyframes on bone rotations only — no constraints, no drivers.

Export
- Apply modifiers (except the armature) and transforms. Export to `out/character.glb` with
  +Y up, 1 unit = 1 metre, skinning and animation included.
- Re-import the GLB and print: triangle count, bone count, animation name and frame range, and the
  maximum bone influences per vertex. Fail loudly (non-zero exit) if any vertex exceeds 4 influences
  or if the animation is missing.

Structure
- Functions: parameters, build_mesh, build_armature, skin, animate_walk, export_and_validate, run in a
  `__main__` block. Print a one-line summary at the end.

Output
- Output ONLY the full contents of build_character.py in one code block.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.4` | More latitude than the prop: proportions are a judgement call, the rig is not. |
| `seed` | `4242` | API seed; geometry seed is `SEED`. |
| `max_output_tokens` | `7500` | Mesh + armature + weights + animation + validation is a long script. |

## Expected output

- `build_character.py` — one script, roughly 400–700 lines.
- `out/character.glb` containing a skinned mesh and an animation named `Walk`.

## Verify it worked

- [ ] Headless run exits 0 and writes `out/character.glb`.
- [ ] Re-import reports 400–1500 triangles and the full bone list with the exact names above.
- [ ] No vertex has more than 4 bone influences; none has zero weight.
- [ ] The animation is present, named `Walk`, 0–23 frames.
- [ ] Playing the GLB in a viewer shows a looping walk with no snap at the loop point.
- [ ] The rig deforms the mesh plausibly: no limbs detaching, no candy-wrapper twisting at elbows/knees.
- [ ] Changing `HEIGHT` scales the whole character, rig included.
- [ ] Re-running with the same `SEED` yields an identical file.

## Tune it

- **`LIMB_THICKNESS` and `HEAD_SCALE`** — silhouette.
- **Walk-cycle frame count** — a shorter cycle is faster and reads as more energetic.

## Where it drifts

- **Bones not inside the mesh.** Automatic weights then attach the wrong vertices and the character
  tears. The bone-position requirement and the "deforms plausibly" check address it; inspect the rig
  in the viewer rather than trusting the script.
- **More than 4 influences per vertex.** Blender allows it; glTF does not, and the export silently
  drops weights, producing a broken skin. The explicit 4-influence normalisation and the fail-loud
  check are the most important part of this recipe.
- **Edge-loop animation.** First and last keys differ, so the walk snaps on loop. Verify by playing two
  cycles back to back.
- **Context errors from `bpy.ops` in background mode.** Pose-mode operators need the right active
  object and mode. If the animation is missing, this is usually why — check the re-import report.

## Provenance

- Technique: original; conventional humanoid rig naming and a 24-frame walk, with the glTF influence
  limit handled explicitly — the part most procedural rigs get wrong.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
