---
id: astra-post-2105298964027265295
title: "Create a 3D Minion Character in Blender"
author: "EvoLink.ai"
author_url: "https://x.com/EvoLinkAi"
original_post: "https://x.com/EvoLinkAi/status/2105298964027265295"
posted_on: "2026-09-30"
media_type: image
media_url: "https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/a85713cf367f06be95da5eb7.jpg"
live_demo: ""
source_list: "TripoGrowthLab/awesome-astra-prompts"
source_list_url: "https://github.com/TripoGrowthLab/awesome-astra-prompts"
source_license: MIT
tags: [gpt-6-astra, tripogrowthlab, blender]
---

# Create a 3D Minion Character in Blender

**[EvoLink.ai](https://x.com/EvoLinkAi)** · 2026-09-30 · [original post ↗](https://x.com/EvoLinkAi/status/2105298964027265295)

![preview](https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/a85713cf367f06be95da5eb7.jpg)

## Prompt

```text
Write a complete, executable Python script using Blender's bpy module to create a 3D Minion character, set up a 360-degree turntable camera animation, and render a 5-second 1:1 video.
Animation & Render Specifications:

Frame Rate & Duration: Set frame rate to 30 fps and render frame range from frame 1 to 150 (exactly 5 seconds).
Aspect Ratio: Set render resolution to 1080x1080 pixels (1:1 square ratio).
Camera Turntable Animation:Animate the camera (or an empty controller object parented to the camera) to perform a seamless 360-degree rotation around the Minion over the 150 frames.
Set keyframe interpolation to LINEAR to ensure smooth, constant-speed rotation.

Output Settings: Set output format to FFmpeg video (H.264 / MP4 container).
Technical Requirements & Model Structure:
Base Body:Create a capsule-like mesh for the main body (yellow material, subsurface scattering/roughness ~0.3).
Add sparse, thin strands of black hair on top of the head.

Goggles & EyesBuild dual-lens goggles using extruded cylinders/toruses.
Goggle Frame Material: Metallic (~0.9), Roughness (~0.2) to simulate brushed aluminum/metal.
Add a black elastic strap wrapping around the body.
Generate two eyeball meshes inside the frame (white sclera, brown iris, shiny pupil).

Clothing - Overalls:Model the denim overalls using separate mesh geometry or extruded body segments.
Material: Blue denim color, higher roughness (~0.6).
Include shoulder straps and a front pocket on the chest.

Appendages & DetailsAdd arms and legs with black gloved hands and black shoes.
Use Mirror Modifier (bpy.ops.object.modifier_add(type='MIRROR')) where applicable (e.g., eyes, goggles frame, arms, straps, legs) to ensure symmetry and clean code.

Lighting & Scene:Place a three-point lighting setup (Key, Fill, Rim lights) parented to the camera or placed uniformly so the lighting stays consistent during rotation.
Set render engine to Cycles or EEVEE with a clean studio background.
Ensure all materials are created using Nodes (use_nodes = True).

Return ONLY valid Python code inside a markdown block with no surrounding text or markdown explanations.
```

- Original post: https://x.com/EvoLinkAi/status/2105298964027265295
- Upstream list: [TripoGrowthLab/awesome-astra-prompts](https://github.com/TripoGrowthLab/awesome-astra-prompts)

_Prompt and preview from the public community post; rights remain with the original author._
