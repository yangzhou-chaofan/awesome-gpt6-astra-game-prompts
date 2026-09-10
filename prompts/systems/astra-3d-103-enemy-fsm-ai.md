---
id: astra-3d-103
title: Enemy AI State Machine
category: systems
slug: enemy-fsm-ai
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.3
top_p: 0.9
seed: 4242
max_output_tokens: 6500
runtime: modern browser
stack: Three.js
difficulty: intermediate
verified: draft
tags: [threejs, ai, fsm, stealth, patrol, guard]
license: CC0-1.0
---

# Enemy AI State Machine

> A readable finite-state guard: patrol, investigate, chase, attack, stunned — with a vision cone and
> a memory of where it last saw you.

## What you get

`index.html`, self-contained: a top-down or third-person scene with one or more guards driven by an
explicit FSM, a visible vision cone, last-known-position memory, and a debug overlay showing the
current state and transitions.

## Before you start

- **Runtime:** modern browser.
- **Dependencies:** Three.js via CDN import map.
- **Assets / inputs:** none; level is boxes.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior game AI engineer. Implement a finite-state-machine enemy AI in one self-contained
index.html for Three.js, with a first-person player to be detected.

Deliverable
- One `index.html`, runs on double-click. Three.js r170+ via import map. No external assets.
- FSM written as explicit states with named enter/update/exit functions — not a switch buried in a
  giant update().

States (all required, with clear transitions)
- PATROL: follow a hard-coded waypoint loop at walking speed.
- INVESTIGATE: move to a suspicion point (last known position or a heard noise), look around, then
  return to patrol after a timeout.
- CHASE: move directly toward the player while the player is visible or recently seen.
- ATTACK: when within attack range, stop and attack on a cooldown; return to CHASE if the player
  leaves range.
- STUNNED: entered when hit by the player's projectile; cannot act for 1.5 s, then returns to CHASE.

Perception
- A vision cone: 90-degree field of view and a 15-unit range, blocked by obstacles. Implement occlusion
  with a raycast against the level colliders. Draw the cone as a translucent mesh that turns red when
  the player is visible.
- Hearing: if the player runs within 8 units, the guard investigates the noise even without line of sight.
- Memory: when sight is lost, the guard keeps the last known position for 4 s before giving up.

Player
- Simple third-person capsule with WASD movement and a click-to-shoot projectile. Being hit stuns the
  guard and has no other effect (this is an AI testbed, not a game).

Debug
- An on-screen overlay lists the current state, the time in state, and the last few transitions.

Engineering
- update(dt) with a delta clock. No global mutable state outside the guard object — one guard factory
  `createGuard(waypoints, scene)` so multiple guards can coexist independently.
- No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with comments naming each state.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.3` | State transitions are logic; keep sampling tight. |
| `seed` | `4242` | API seed. No RNG needed in behavior. |
| `max_output_tokens` | `6500` | Five states plus perception plus a player. |

## Expected output

- `index.html` — one file, roughly 500–750 lines.
- Five clearly named states with enter/update/exit, and a `createGuard` factory that allows two guards
  with independent state.

## Verify it worked

- [ ] A guard patrols its waypoint loop when undisturbed.
- [ ] Walking into the cone turns it red and the guard transitions to CHASE.
- [ ] Breaking line of sight behind an obstacle makes the guard move to the last known position.
- [ ] After 4 s of no sight, the guard returns to patrol.
- [ ] Running near a guard without being seen makes it investigate the noise.
- [ ] Hitting a guard with a projectile shows STUNNED for ~1.5 s, then CHASE.
- [ ] In ATTACK range the guard stops and attacks on a cooldown.
- [ ] Two guards placed in the scene keep independent state (no shared globals).
- [ ] Console is clean.

## Tune it

- **Cone angle and range** — the whole stealth feel.
- **Memory duration (4 s)** — how forgiving the guards are.

## Where it drifts

- **The FSM is a boolean pile.** States collapse into `if (seesPlayer) chase else patrol`, losing
  INVESTIGATE and STUNNED. The explicit named-states requirement is the guard; check the debug overlay
  actually reports all five.
- **Vision cone without occlusion.** The guard sees through walls. The raycast requirement catches it —
  test by standing behind a pillar directly in the cone.
- **Shared mutable state across guards.** A module-level `currentState` variable means all guards move
  in lockstep. The `createGuard` factory requirement and the two-guard check expose it.
- **Occlusion raycast hitting the guard's own mesh.** The guard never sees anything. Verify the cone
  responds at all before debugging further.

## Provenance

- Technique: original; the enter/update/exit FSM is standard, made reproducible here by the explicit
  state list and the factory.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
