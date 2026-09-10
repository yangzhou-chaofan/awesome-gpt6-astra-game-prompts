---
id: astra-3d-106
title: Save / Load System
category: systems
slug: save-load-system
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.25
top_p: 0.9
seed: 4242
max_output_tokens: 5500
runtime: modern browser
stack: Three.js
difficulty: beginner
verified: draft
tags: [threejs, persistence, save, local-storage, versioning]
license: CC0-1.0
---

# Save / Load System

> Versioned, validated persistence with migrations — so a save from yesterday still loads after you
> change the game today.

## What you get

`index.html`, self-contained: a small player state (position, health, inventory, unlocks), a versioned
save format, a migration chain, three save slots, autosave on a timer, and a corrupt-save recovery path.

## Before you start

- **Runtime:** modern browser with localStorage.
- **Dependencies:** Three.js via CDN import map.
- **Assets / inputs:** none.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior engineer. Build a versioned save/load system for a small Three.js game in one
self-contained index.html.

Deliverable
- One `index.html`, runs on double-click. Three.js r170+ via import map. No external assets.
- A minimal game state to persist: player position (x,y,z), health, an inventory array of
  { id, count }, a set of unlocked flags, and a total playtime in seconds. A simple third-person
  capsule with WASD stands in for the game.

Save format
- `{ version: 3, savedAt: <ISO string>, state: {...} }` stored under keys `save.slot.0`, `save.slot.1`,
  `save.slot.2` in localStorage. Three slots.
- All writes go through `save(slot)`. All reads through `load(slot)`.

Durability (the point of this recipe)
- `load()` validates the parsed object: version present and numeric, state shape correct, numbers
  finite. On any failure it must NOT throw and must NOT overwrite the bad data — it returns a typed
  error and leaves the payload intact so it can be inspected.
- Migrations: implement a `MIGRATIONS` map from an older version to the next (e.g. 1→2 adds
  `unlocked`, 2→3 renames `hp` to `health`). `load()` runs the chain until the payload is current.
- Seed a deliberately old v1 payload from a dev button so migrations can be seen working.
- Schema drift: if an unknown field appears, preserve it through save/load round-trips rather than
  dropping it.

UI
- A panel with three slots showing savedAt and playtime, with Save / Load / Delete per slot, an
  autosave toggle (every 30 s), and a status line reporting errors and migrations performed.

Engineering
- State serialisation is separate from the game loop.
- No console errors or warnings on load; corrupt payloads are reported, not thrown.

Output
- Output ONLY the full contents of index.html in one code block, with comments for the format, the
  validation, and the migration chain.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.25` | Format and migration rules are exact; low temperature keeps them consistent. |
| `seed` | `4242` | API seed. |
| `max_output_tokens` | `5500` | Comfortable for the system and its UI. |

## Expected output

- `index.html` — one file, roughly 350–550 lines.
- A `MIGRATIONS` map and a validation routine that returns errors instead of throwing.

## Verify it worked

- [ ] Saving and reloading the page restores position, health, inventory and playtime.
- [ ] Loading a deliberately corrupted slot reports an error and leaves the raw payload intact.
- [ ] Seeding a v1 payload and loading it runs both migrations and lands on version 3.
- [ ] An unknown field added by hand survives a save/load round-trip.
- [ ] Autosave writes every 30 s while enabled and stops when disabled.
- [ ] Delete removes only the chosen slot.
- [ ] No uncaught exceptions appear in the console for any of the above.

## Tune it

- **Slot count** and **autosave interval** — the only knobs; keep them constants at the top.

## Where it drifts

- **`JSON.parse` not wrapped.** A corrupt payload throws and kills the game loop. The "returns a typed
  error, does not throw" requirement is the guard.
- **Validation that overwrites bad data.** Load fails, the game writes a fresh save over the evidence.
  The "leave the payload intact" requirement prevents it.
- **Migrations that mutate in place and are not idempotent.** Running the chain twice corrupts state.
  Test by loading an old payload twice.
- **Dropping unknown fields.** Round-trip silently loses data added by a newer build. The preservation
  check catches it.

## Provenance

- Technique: original; standard durable-persistence practice applied to a browser game.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
