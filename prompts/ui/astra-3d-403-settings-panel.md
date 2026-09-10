---
id: astra-3d-403
title: Settings & Accessibility Panel
category: ui
slug: settings-panel
model: gpt-6-astra
model_version: "2026-09-03"
temperature: 0.3
top_p: 0.9
seed: 4242
max_output_tokens: 6500
runtime: modern browser
stack: HTML / CSS
difficulty: beginner
verified: draft
tags: [ui, settings, accessibility, persistence, remapping, html, css]
license: CC0-1.0
---

# Settings & Accessibility Panel

> A real settings screen: graphics, audio, controls remapping, and accessibility options — persisted,
> applied live, and resettable.

## What you get

`index.html`, self-contained: a settings panel with graphics, audio, gameplay and accessibility
sections; live preview of changes; key rebinding with conflict detection; persistence to localStorage;
and apply/cancel/reset behaviour that does not lie about what is active.

## Before you start

- **Runtime:** modern browser.
- **Dependencies:** Three.js via CDN import map (for the preview scene).
- **Assets / inputs:** none.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior UI engineer. Build a complete settings and accessibility panel for a Three.js game in
one self-contained index.html, with a small preview scene that reflects the settings.

Deliverable
- One `index.html`, runs on double-click. Three.js r170+ via import map.
- The panel is HTML/CSS overlaid on the canvas, opened with Escape or a Settings button.

Sections and controls
- GRAPHICS: resolution scale (50-100%), shadows on/off, antialiasing on/off, FOV slider, quality preset
  (Low/Medium/High) that sets the others. Show the current renderer draw calls and frame time.
- AUDIO: master, music and effects volume sliders with live percentage, and a mute toggle.
- GAMEPLAY: mouse sensitivity, invert-Y, and a "hold to sprint" toggle.
- ACCESSIBILITY: UI scale (100-200%), high-contrast UI toggle, colour-blind palette
  (off / protanopia / deuteranopia / tritanopia), reduced motion, screen-shake intensity, subtitle
  size, and a "toggle instead of hold" option for any hold action.

Key rebinding (the fiddly part)
- Every gameplay action is rebindable by clicking its key and pressing a new one.
- CONFLICT DETECTION: if the new key is already bound to another action, do not silently overwrite.
  Show both actions and ask to swap or cancel.
- Support a secondary binding per action. A "Reset to defaults" restores the table.
- The active bindings must be used by the actual input system, not just displayed.

Apply / Cancel / Reset semantics
- Edits live in a draft copy. Apply commits and applies them live. Cancel discards the draft and
  reverts the preview. Reset restores defaults for the current section only.
- Persist committed settings to localStorage and load them on start. If persisted settings are invalid
  or from an older schema, fall back to defaults and say so.

Live preview
- Changing resolution scale, shadows, FOV, colour-blind palette, UI scale or contrast updates the
  preview scene immediately, before Apply, so the player can see the effect. Cancel reverts.

Engineering
- Settings are a plain object with a schema (type, range, default) that drives both the UI and the
  validation. Adding a setting is one schema entry, not a new hand-written control.
- Separate: schema, state/draft, persistence, UI rendering, application to the renderer.
- No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with comments for the schema, the
  draft/apply model, conflict detection, and persistence.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.3` | Schema-driven UI and rebinding logic are exact. |
| `seed` | `4242` | API seed. |
| `max_output_tokens` | `6500` | Five sections plus rebinding and persistence. |

## Expected output

- `index.html` — one file, roughly 500–750 lines.
- A settings schema driving the UI, a draft/apply model, and key-conflict detection.

## Verify it worked

- [ ] Opening the panel shows all four sections with the persisted or default values.
- [ ] Changing resolution scale, shadows, FOV, UI scale and colour-blind palette updates the preview
      immediately, before Apply.
- [ ] Cancel reverts the preview to the committed settings.
- [ ] Apply persists to localStorage; reloading restores the applied values.
- [ ] Rebinding an action to an already-used key shows a conflict with a swap/cancel choice.
- [ ] The rebound key actually controls the game (bindings feed the input system).
- [ ] "Reset to defaults" affects only the current section.
- [ ] Invalid or old-schema persisted settings fall back to defaults with a visible notice.
- [ ] Adding a setting means adding one schema entry and the UI renders it.
- [ ] Console is clean.

## Tune it

- **Ranges** (FOV, sensitivity, UI scale) — the sensible bounds.
- **Quality presets** — which settings each preset touches.

## Where it drifts

- **Displayed bindings that the input system ignores.** The panel is cosmetic. The "bindings feed the
  input system" check catches it; rebind an action and use it.
- **Silent key conflicts.** Overwriting another action's binding with no warning. The conflict-detection
  requirement is explicit and testable.
- **Cancel that lies.** The preview was already committed, so Cancel cannot revert. The draft/apply
  model requirement prevents it; test by changing something then cancelling and reloading.
- **Persistence that crashes on old data.** Missing validation, so a schema change bricks settings.
  The fallback requirement addresses it; hand-edit localStorage to test.
- **Hand-written controls.** Each new setting needs bespoke code and one is missed. The schema-driven
  requirement is the structural fix.

## Provenance

- Technique: original; schema-driven settings with a draft/apply model and real conflict detection,
  which is the part most generated settings screens leave out.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
