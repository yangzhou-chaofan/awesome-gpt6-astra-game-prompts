---
id: astra-post-2110073220946592038
title: "3D Flappy Bird-style tropical game"
author: "Ivana"
author_url: "https://x.com/ivanainai"
original_post: "https://x.com/ivanainai/status/2110073220946592038"
posted_on: "2026-10-13"
media_type: image
media_url: "https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/d5b6aa6a3f84f58b3f4770c2.jpg"
live_demo: ""
source_list: "TripoGrowthLab/awesome-astra-prompts"
source_list_url: "https://github.com/TripoGrowthLab/awesome-astra-prompts"
source_license: MIT
tags: [gpt-6-astra, tripogrowthlab, game, threejs]
---

# 3D Flappy Bird-style tropical game

**[Ivana](https://x.com/ivanainai)** · 2026-10-13 · [original post ↗](https://x.com/ivanainai/status/2110073220946592038)

![preview](https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/d5b6aa6a3f84f58b3f4770c2.jpg)

## Prompt

```text
Build a fully playable 3D Flappy Bird-style game in ONE complete, copy-pasteable HTML file using Three.js/WebGL.

Create an original, colorful bird and environment. The game should look beautiful in a screenshot and feel responsive when played.

Return the entire HTML inside ONE fenced html code block. The code must begin with <!DOCTYPE html> and end with </html>. Include all CSS and JavaScript. Do not provide explanations, fragments or additional files.

VISUAL DIRECTION

Create a bright, richly colored tropical coastal world with a turquoise sea, warm sunlight, soft white clouds, distant islands and subtle atmospheric depth.

Keep the foreground crisp and saturated. Use a carefully composed background with gentle parallax, leaving the bird and obstacles easy to see.

The hero is a charming golden-yellow 3D bird with an orange beak, expressive eyes, small animated wings and individually shaped tail feathers. Make it feel like a carefully designed game character.

Animate wingbeats, subtle body movement and a smooth change in body angle when rising or falling.

The obstacles are glossy emerald-green pipes with substantial rounded rims, visible thickness, convincing shadows and beautiful highlights. They must read clearly as solid objects with a navigable gap.

Use tasteful lighting, smooth geometry, soft shadows and restrained reflections. Preserve strong contrast between the yellow bird, green pipes and blue environment.

The opening screen must immediately show the finished world, the bird and several pipes. Keep the interface small and clean.

GAMEPLAY

Use a side-view gameplay plane with real 3D geometry and depth. Keep a fixed camera so the openings and collisions remain easy to judge.

Clicking, tapping or pressing Space makes the bird flap upward. Gravity pulls it downward between flaps.

Pipes move toward the bird at constant speed. Each pair has a gap at a different height. Award exactly one point when the bird successfully passes a pair.

Colliding with a pipe, the ground or the upper gameplay boundary ends the run. Show a short, clear impact response and a Game Over panel with the final score and a working Restart button.

Restart must reset the bird, pipes, score, obstacle sequence and simulation state without reloading the page.

Use these identical gameplay parameters:

Bird position: x = -4.5.
Bird collision radius: 0.35 world units.
Vertical gameplay boundaries: y = -5.4 and +5.4.
Gravity: 18 world units per second squared, downward.
Each flap sets upward velocity to 6.8 world units per second.
Pipe movement speed: 3 world units per second.
Pipe width: 1.2 world units.
Vertical gap size: 3.4 world units.
Horizontal distance between pipe pairs: 5.5 world units.
Gap centers vary between y = -2 and +2.

Use a fixed simulation timestep and collision checks corresponding to the visible bird body and pipe geometry.

Generate obstacle heights deterministically with a dedicated seeded random generator, starting at seed 42. Restart must reproduce the same obstacle sequence. Decorative randomness must not affect this sequence.

AUTOMATIC DEMO

Provide three small controls: Play, Auto Demo and Restart.

Auto Demo must play the actual game automatically. Its controller may only issue the same flap action available to a human player.

It must use the same gravity, obstacles, collision detection and scoring as manual play. It must not reposition the bird directly, disable collisions or make it invincible.

Aim for a smooth, watchable 
```

- Original post: https://x.com/ivanainai/status/2110073220946592038
- Upstream list: [TripoGrowthLab/awesome-astra-prompts](https://github.com/TripoGrowthLab/awesome-astra-prompts)

_Prompt and preview from the public community post; rights remain with the original author._
