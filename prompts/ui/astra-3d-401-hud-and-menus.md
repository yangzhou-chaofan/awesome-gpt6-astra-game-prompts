---
id: astra-3d-401
title: HUD, Menus & Pause Screen
category: ui
slug: hud-and-menus
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
tags: [ui, hud, menus, pause, accessibility, html, css]
license: CC0-1.0
---

# HUD, Menus & Pause Screen

> The full game-shell UI: live HUD, title screen, pause menu, game-over screen, and the state machine
> that keeps them from fighting each other.

## What you get

`index.html`, self-contained: an accessible HTML/CSS overlay layer over a Three.js scene, with a HUD
(health, ammo, score, minimap placeholder), a title screen, a pause screen that actually pauses the
simulation, a game-over screen, and keyboard/gamepad navigation across all of them.

## Before you start

- **Runtime:** modern browser.
- **Dependencies:** Three.js via CDN import map (for the placeholder scene).
- **Assets / inputs:** none; icons are inline SVG.
- **Model access:** plain chat completion.

## The prompt

```text
You are a senior UI engineer. Build the complete UI shell for a Three.js game in one self-contained
index.html.

Deliverable
- One `index.html`, runs on double-click. Three.js r170+ via import map for a placeholder scene.
- All UI is HTML/CSS overlaid on the canvas, not 3D. Icons are inline SVG.

Screens and states
- Define one UI state machine: BOOT -> TITLE -> PLAYING <-> PAUSED -> GAME_OVER -> TITLE.
  Only one screen is visible at a time; transitions are explicit functions.
- TITLE: game title, Play, Settings, Quit. 
- PLAYING: the HUD only. Escape pauses.
- PAUSED: Resume, Restart, Settings, Quit to title. The simulation must actually pause (the game loop
  stops updating, though it may keep rendering a frozen frame).
- GAME_OVER: final score, best score, Retry, Quit to title.

HUD
- Health as a segmented bar, ammo as a counter, score as a number, and a small minimap placeholder.
- Values update from a single `setHud(state)` call, not by the render loop touching DOM directly.
- Damage feedback: a brief red vignette flash and a health-bar pulse. Score changes animate upward.
- The HUD must not capture pointer events over the game canvas (use `pointer-events: none` except on
  actual controls).

Accessibility (required, not optional)
- Full keyboard navigation: Tab/Shift-Tab to move, Enter/Space to activate, Escape to go back.
- A visible focus ring on every focusable element; never remove the outline.
- `aria-live="polite"` on the score and health so screen readers announce changes.
- Respect `prefers-reduced-motion`: disable the flash and the score animation.
- Buttons are real <button> elements, not clickable divs.

Engineering
- One UI module with `show(screen)`, `setHud(state)`, and a callback registry for button actions; the
  game code listens to callbacks and never queries the DOM for state.
- No console errors or warnings on load.

Output
- Output ONLY the full contents of index.html in one code block, with comments per screen and for the
  accessibility requirements.
```

## Settings

| Field | Value | Why |
| --- | --- | --- |
| `temperature` | `0.3` | State machine and accessibility attributes are exact. |
| `seed` | `4242` | API seed. |
| `max_output_tokens` | `6500` | All screens plus HUD plus a11y. |

## Expected output

- `index.html` — one file, roughly 450–700 lines.
- A UI state machine, `setHud`, and real `<button>` elements with an untouched focus outline.

## Verify it worked

- [ ] BOOT goes to TITLE; Play enters PLAYING and shows the HUD.
- [ ] Escape pauses; the simulation visibly freezes (nothing on screen continues to move).
- [ ] Resume continues exactly where it left off; Restart resets; Quit returns to TITLE.
- [ ] GAME_OVER shows final and best scores and Retry works.
- [ ] The HUD updates via `setHud`; no console errors from DOM access in the loop.
- [ ] Tab cycles focus through every control, with a visible focus ring.
- [ ] Screen readers announce score and health changes (`aria-live` present and working).
- [ ] With `prefers-reduced-motion` enabled, the flash and score animation are absent.
- [ ] Clicking through the HUD does not block camera/mouse control in-game.
- [ ] Console is clean.

## Tune it

- **HUD corner placement** and **color palette** — the visible identity.
- **Animation duration** — snappy vs. soft; keep it reducible.

## Where it drifts

- **"Pause" that only hides the UI.** The render loop keeps simulating, so the player dies while paused.
  The "simulation must actually pause" requirement and the freeze check are the guard.
- **`div` soup instead of buttons.** Keyboard and screen-reader support is then absent. The real-button
  requirement and the Tab check catch it.
- **`outline: none`.** The classic accessibility regression. The focus-ring requirement is explicit for
  this reason.
- **HUD capturing mouse events.** The game becomes unplayable behind the overlay. The `pointer-events`
  requirement addresses it; test by trying to look around.
- **Two screens visible at once.** State machine not exclusive. The "one screen at a time" requirement
  prevents it.

## Provenance

- Technique: original; conventional game-shell UI with accessibility taken seriously, which most
  generated UI omits.
- Verification run: not yet reproduced on `gpt-6-astra` 2026-09-03.
