---
id: astra-3d-402
title: Radial & Context Menu System
category: ui
slug: radial-menu
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.3
top_p: 0.9
seed: 4242
max_output_tokens: 6000
runtime: modern browser
stack: HTML / CSS
difficulty: intermediate
verified: draft
tags: [ui, radial-menu, context-menu, interaction, gamepad, accessibility]
license: CC0-1.0
---

# Radial & Context Menu System

> A hold-to-open radial menu and a right-click context menu that share one action model — with gamepad
> and keyboard support, not just the mouse.

## What you get

`index.html`, self-contained: a Three.js scene with selectable objects, a radial menu that opens on
long-press or a gamepad button and selects by direction, and a context menu on right-click — both built
from a shared list of actions with icons, labels, disabled states and keyboard access.

## Before you start

- **Runtime:** modern browser.
- **Dependencies:** Three.js via CDN import map.
- **Assets / inputs:** none; icons are inline SVG.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior UI engineer. Build a radial + context menu system for a Three.js scene in one
self-contained index.html.

Deliverable
- One `index.html`, runs on double-click. Three.js r170+ via import map.
- A scene with ~8 selectable objects (boxes with labels). Clicking selects; the menus act on the
  selection.

Shared action model
- Define actions as data: { id, label, icon (inline SVG string), enabled(target), run(target) }.
  Build BOTH menus from the same action list; nothing is duplicated per menu.
- Actions include at least: Inspect, Rename, Duplicate, Change Color (opens a submenu of colours),
  Lock/Unlock (toggles), Delete, and one action that is disabled for some objects.

Radial menu
- Opens on long-press (hold left mouse 250 ms) over the canvas, or on gamepad button Y / triangle.
- Appears centred on the press point, with the selection wedge following the direction from centre to
  cursor (or the right stick). A dead zone in the centre cancels.
- Selecting releases the action on release; moving into the dead zone and releasing cancels.
- The selected wedge's label is shown prominently; other wedges show icon + short label.
- Support up to 8 wedges; if more actions exist, open a second ring (document the layout).

Context menu
- Right-click opens a vertical menu at the cursor with the same actions as a list, plus the colour
  submenu as a flyout. Escape or clicking away closes it.

Keyboard and accessibility
- Radial: hold Space to open, arrow keys to choose a wedge, release Space to confirm; Escape cancels.
- Context: a Menu key or Shift+F10 opens it at the selection; arrow keys navigate, Enter activates.
- Both menus are announced via an `aria-live` region ("Radial menu, 6 actions, Panels selected").
- Focus is trapped inside the context menu while open and restored to the previously focused element
  on close. Disabled actions are skipped in keyboard navigation but still shown.

Engineering
- One menu controller, two renderers. Position using CSS transforms; do not rebuild DOM each open.
- No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with comments per menu, the shared
  action model, and the accessibility behaviour.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.3` | Geometry of wedges and focus handling is exact. |
| `seed` | `4242` | API seed. |
| `max_output_tokens` | `6000` | Two menu renderers plus keyboard/gamepad. |

## Expected output

- `index.html` — one file, roughly 450–700 lines.
- A single action list powering both menus, with a second-ring layout for overflow.

## Verify it worked

- [ ] Long-press opens the radial menu at the cursor; the wedge follows the direction.
- [ ] Releasing over a wedge runs that action on the selected object.
- [ ] Releasing in the dead zone, or pressing Escape, cancels with no action.
- [ ] Right-click opens the context menu with the same actions.
- [ ] Actions that should be disabled are visibly disabled and cannot be run by mouse or keyboard.
- [ ] Hold Space + arrow keys + release performs a radial selection without a mouse.
- [ ] Shift+F10 opens the context menu; arrow keys and Enter work.
- [ ] Focus is trapped in the context menu and restored on close.
- [ ] The `aria-live` region announces the opened menu and the selected action.
- [ ] Opening the menus repeatedly does not rebuild the DOM each time (no leak).
- [ ] Console is clean.

## Tune it

- **Long-press threshold (250 ms)** — accidental opens vs. responsiveness.
- **Wedge count / ring layout** — how many actions feel comfortable.

## Where it drifts

- **Duplicated action definitions.** The two menus drift apart when only one is updated. The single
  shared action list requirement is the guard; add a new action and confirm it appears in both.
- **Mouse-only radial.** No keyboard or gamepad path. The explicit keyboard requirements and the
  Space+arrows check address it — many generated menus omit this entirely.
- **No cancel path.** Releasing anywhere always triggers an action; the dead-zone cancel requirement
  prevents mis-fires. Test by releasing dead centre.
- **Disabled actions still run.** `enabled` is styled but not enforced. The check requires running it by
  keyboard too, which exposes styling-only implementations.
- **Focus not restored.** After closing the context menu, focus is lost and keyboard users are stranded.
  The restore requirement is testable and specific.

## Provenance

- Technique: original; radial/context menu patterns with keyboard and gamepad parity added, which is
  the part generated menus usually skip.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
