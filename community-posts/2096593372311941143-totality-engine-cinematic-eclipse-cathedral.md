---
id: astra-post-2096593372311941143
title: "Totality Engine: Cinematic Eclipse Cathedral"
author: "Chris W"
author_url: "https://x.com/Chris_Wozniczek"
original_post: "https://x.com/Chris_Wozniczek/status/2096593372311941143"
posted_on: "2026-09-06"
media_type: image
media_url: "https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/52de12ef7c4dd44ec548962b86297e175683992ebdfdd2665699a18fe86bb9ca.jpg"
live_demo: "https://chris-website-theta.vercel.app/astra-xhigh-totality-engine.html"
source_list: "TripoGrowthLab/awesome-astra-prompts"
source_list_url: "https://github.com/TripoGrowthLab/awesome-astra-prompts"
source_license: MIT
tags: [gpt-6-astra, image, shader, threejs, tripo, unreal]
---

# Totality Engine: Cinematic Eclipse Cathedral

**[Chris W](https://x.com/Chris_Wozniczek)** · 2026-09-06 · [original post ↗](https://x.com/Chris_Wozniczek/status/2096593372311941143)

![preview](https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/52de12ef7c4dd44ec548962b86297e175683992ebdfdd2665699a18fe86bb9ca.jpg)

## Prompt

```text
Create a polished, visually impressive, self-contained single-file HTML/WebGL experience called:

totality-engine.html put it in documents/llm-benchmarks

Do not just describe the idea. Actually generate the complete working HTML file and save it to the current directory.

Build a 32-second looping cinematic short, not a sandbox diorama. The product is the camera performance. Interaction is a bonus after the film has played once.

World:
A drowned gothic cathedral at solar-eclipse totality. Black water covers the nave floor. Filling the crossing is a monumental brass astronomical clock, the Totality Engine: nested orrery rings, glass planets, a black-sun core, and a 40-meter dark-marble pendulum with gold fittings. Wet limestone, verdigris, candle flames, and gold dust. Everything is procedural code. No external models, textures, images, fonts as files, or audio.

Directed film (one clock, named beats, seamless loop):

0.0–4.0s DUST
Extreme close-up. One dust mote turns in a shaft of red-gold light. Almost no context. Slow push.

4.0–10.0s NAVE
Pull back and rise. We are knee-deep in black water in the cathedral crossing. Rib vaults recede into fog. The pendulum enters frame from the left, heavy, slow, and passes close enough to feel its mass. Water rings spread from the camera.

10.0–18.0s ASCENT
Ride the pendulum's upswing. Reveal the orrery in the vault: at least four nested brass rings at different inclinations, three glass planets with distinct atmospheres (one cloudy, one ringed, one storm-banded), and the black-sun core. Candle clusters along the triforium. Gold dust falls upward against gravity.

18.0–24.0s THREAD
Camera threads the orrery. Pass through the glass of the ringed planet (refraction, not a transparency hack), ride its ring plane for a beat, exit toward the black sun. The pendulum's next swing warps the light around it like a weak gravitational lens.

24.0–30.0s TOTALITY
Corona detonates into a ring of white-gold fire that becomes the outermost orrery wheel. One audible-feeling clock tick: every ring snaps into a perfect alignment, then the corona holds. Do not fade to white. Hold the silhouette of the whole machine against the fire-ring.

30.0–32.0s CODA
Ease into a slow continuation that matches frame 0, so the loop is invisible. No smash cut.

After the first full play, enable drag-to-orbit, scroll-wheel zoom, and a "Replay film" control. A Pause button always works. Optional: keys 1–5 jump to beat starts.

Scene craft:
- Strong foreground / midground / background. The pendulum occupies foreground in NAVE. Vaults and fog hold the depth.
- At least two human-scale references (a drowned pew, a fallen spire, a row of candles) so the machine reads as enormous.
- Water is a real material: reflections of the orrery, a faint fresnel, slow displacement, the rings from the pendulum and the camera.
- Glass planets are thick glass, not glowing balls. You should see a distorted cathedral through at least one of them.
- Brass has weight: dark in shadow, only the rims catching corona light.
- Candle flames and gold dust are instanced. Dust is pulled upward only during ASCENT and TOTALITY.
- Rib vaults, flying-buttress silhouettes, and a giant circular rose-window / eclipse aperture in the far wall, aligned with the black sun.
- Limited palette, locked: wet limestone #8a8680, brass #c4a574, verdigris #2f6f66, eclipse crimson #6b1020, corona #ffe9c2, black water #05070c, gold dust #e6c27a. No cyan, no magenta, no neon, no rainbow, no purple-on-black "AI look".
- Typography: one small title "TOTALITY ENGINE" and beat name, filmic, not a dashboard.

Technical requirements:
- Three.js from a stable CDN. All HTML, CSS, and JS in this one file.
- Drive every animation from a single elapsed-time clock with named beat windows. No independent Math.random loops, no Date.now in shaders, no unseeded noise. Seeded RNG only, seed constant 0xA2E1.
- Camera film uses smooth interpolation with ease-in-out on the big moves, a heavier ease on the pendulum (it has mass), and a long-tail settle into TOTALITY. Linear orbit as the primary camera is a fail.
- Custom GLSL (ShaderMaterial or full-screen pass), not stock materials pretending:
1. Water (reflection + fresnel + slow displacement)
2. Black-sun corona (fire / plasma, not a sprite)
3. Pendulum lensing (light bends near the bob during THREAD)
4. Thick glass for at least one planet
- InstancedMesh for dust, candles, and any repeated stone/brass cells. Do not spawn thousands of free Mesh objects.
- Post-processing is allowed but cannot replace lighting. If you use bloom, it is a light touch on the corona and candles only. UnrealBloom over the whole scene is a fail.
- Fog, wet reflections, and the eclipse aperture do the atmosphere. No cheap transparent cones as "god rays" unless they are actually driven by a shader.
- Responsive, full browser window, handle resize, target 60fps on a 2023 laptop. If you have to choose, cut particle count before cutting the camera film.
- Small unobtrusive UI: title, current beat, pause, replay. No FPS counter, no dat.gui, no debug helpers left on.
- No TODO comments, pseudocode, placeholders, missing functions, or "this would be better with X".
- On load, the film starts itself. A still frame behind a start button is a fail.

Quality bar:
This should look like a short film still, not a three.js example. If a screenshot at 26 seconds does not read as "cathedral-sized clock at the moment of eclipse," you are not done. Iterate on composition, materials, and camera before adding more objects.
```

## Provenance

- Original post: https://x.com/Chris_Wozniczek/status/2096593372311941143
- Upstream list: [TripoGrowthLab/awesome-astra-prompts](https://github.com/TripoGrowthLab/awesome-astra-prompts) (MIT)
- Live demo: https://chris-website-theta.vercel.app/astra-xhigh-totality-engine.html

_Prompt text and preview collected from the public community post above; all rights remain with the original author._
