---
id: astra-3d-104
title: Inventory & Pickups
category: systems
slug: inventory-and-pickups
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.25
top_p: 0.9
seed: 4242
max_output_tokens: 6000
runtime: modern browser
stack: Three.js
difficulty: beginner
verified: draft
tags: [threejs, inventory, pickups, hud, items, grid]
license: CC0-1.0
---

# Inventory & Pickups

> A grid inventory with stacking, drag-to-rearrange, and world pickups that fly to the player.

## What you get

`index.html`, self-contained: a hotbar and a 5x4 grid inventory rendered as HTML over the 3D view,
stacking items with a max stack size, drag-and-drop rearrangement, and pickups scattered in the world
that tween toward the player on approach.

## Before you start

- **Runtime:** modern browser.
- **Dependencies:** Three.js via CDN import map.
- **Assets / inputs:** none; item icons are drawn with emoji or CSS.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior game engineer. Build a grid inventory and pickup system in one self-contained
index.html for Three.js.

Deliverable
- One `index.html`, runs on double-click. Three.js r170+ via import map. No external assets.
- Inventory is DOM/HTML overlaid on the canvas (not a 3D UI), styled with plain CSS.

Data model
- An `Item` type: { id, name, icon, maxStack }. Define at least 4 item types (e.g. coin, apple, key, gem)
  with maxStack 64, 16, 1 and 8 respectively.
- An `Inventory` of 20 slots (5 columns x 4 rows) plus a 5-slot hotbar. Each slot either holds
  { item, count } or is empty.
- `addItem(item, count)` must: fill existing stacks of the same item first, then occupy empty slots,
  and return the amount that did NOT fit (the overflow). It must never exceed maxStack.

Interaction
- Render the inventory as a grid; each slot shows the icon and the stack count. The hotbar is always
  visible; pressing I toggles the full grid.
- Drag and drop: pick a stack up with the mouse, drop it on an empty slot to move it, on a stack of
  the same item to merge (respecting maxStack, leaving overflow in the source), or on a different item
  to swap. A held stack follows the cursor.
- Number keys 1-5 select the active hotbar slot; the selection is highlighted.

World pickups
- Scatter 20 item pickups in the world. When the player (a simple WASD capsule) comes within 3 units,
  the pickup tweens toward the player, is added via addItem, and is removed when collected.
- If addItem returns overflow, drop the overflow back into the world at the player's feet and show a
  brief "Inventory full" toast.

Engineering
- Separate the inventory logic (pure, testable, no DOM) from its rendering.
- requestAnimationFrame for the 3D scene; DOM updates only when state changes, not every frame.
- No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with comments naming the data model,
  the add logic, drag/drop, and pickups.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.25` | The stacking/overflow rules are exact and easy to get wrong. |
| `seed` | `4242` | API seed; pickup placement may use it. |
| `max_output_tokens` | `6000` | Comfortable for the system plus the scene. |

## Expected output

- `index.html` — one file, roughly 400–600 lines.
- Inventory logic in functions that do not touch the DOM, with rendering bound to state changes.

## Verify it worked

- [ ] Collecting items fills partial stacks before using empty slots.
- [ ] A stack never exceeds its `maxStack`.
- [ ] Overflow is returned by `addItem`, dropped into the world, and a toast is shown.
- [ ] Dragging a stack onto a same-item stack merges and leaves the remainder where it came from.
- [ ] Dragging onto a different item swaps the two.
- [ ] Pressing I toggles the grid; 1-5 change the active hotbar slot.
- [ ] Pickups tween to the player and disappear on collection.
- [ ] The DOM is not rewritten every frame (no flicker, no layout thrash).
- [ ] Console is clean.

## Tune it

- **Slot count and `maxStack` values** — the inventory's feel.
- **Pickup radius (3 units)** — how greedy collection feels.

## Where it drifts

- **Overflow silently discarded.** The most common bug: `addItem` drops what does not fit. The
  "returns overflow" and toast checks make it visible.
- **Stack merge that ignores maxStack.** Produces stacks of 70. Check by collecting one more than
  maxStack at a time.
- **Rendering every frame.** The inventory DOM is rebuilt in the render loop, so dragging stutters.
  The state-change-only requirement is the guard.
- **Pickup radius measured on the wrong axis.** Uses 2D distance and collects through the floor, or
  uses the wrong object's position. Test by walking past at varying heights.

## Provenance

- Technique: original; grid-inventory merge rules are common knowledge, distilled into exact behaviour.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
