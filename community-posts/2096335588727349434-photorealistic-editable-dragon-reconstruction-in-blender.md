---
id: astra-post-2096335588727349434
title: "Photorealistic Editable Dragon Reconstruction in Blender"
author: "Sarang Borude"
author_url: "https://x.com/doomdave"
original_post: "https://x.com/doomdave/status/2096335588727349434"
posted_on: "2026-09-05"
media_type: image
media_url: "https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/756d0d4859c6a3bec065b9594d7fed7544101b6f6b6fb1e331bbfee059e84738.jpg"
live_demo: ""
source_list: "TripoGrowthLab/awesome-astra-prompts"
source_list_url: "https://github.com/TripoGrowthLab/awesome-astra-prompts"
source_license: MIT
tags: [blender, game, gpt-6-astra, image, mcp, tripo]
---

# Photorealistic Editable Dragon Reconstruction in Blender

**[Sarang Borude](https://x.com/doomdave)** · 2026-09-05 · [original post ↗](https://x.com/doomdave/status/2096335588727349434)

![preview](https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/756d0d4859c6a3bec065b9594d7fed7544101b6f6b6fb1e331bbfee059e84738.jpg)

## Prompt

```text
Create a photorealistic, fully editable 3D reconstruction of the dragon shown in the attached reference sheet inside Blender.

Use every supplied view—including the side, front, top, back, head angles, head closeup, eye closeup, scale detail and wing detail—to reconstruct one coherent and anatomically believable dragon.

Match the reference as closely as possible, especially:

- Overall body proportions and silhouette
- Long muscular neck and tapering tail
- Four legs and two large bat-like wings
- Head and jaw shape
- Horn number, shape and placement
- Dorsal spikes along the neck, back and tail
- Dark charcoal and earthy-brown scale patterns
- Layered armor-like scales
- Golden-amber eyes with vertical pupils
- Claws, teeth and wing membranes
- Ancient, realistic and threatening appearance

The reference panels may contain small inconsistencies. Reconcile them into a physically coherent, symmetrical base creature while preserving the dragon’s visual identity. Use the side view for overall proportions, the front view for width and stance, the top and back views for wings and tail, and the closeups for the head, eyes, scales and wing materials.

Build the dragon from scratch as actual editable Blender geometry. Do not download or import an existing dragon model. Do not use billboards, 2D projections, depth-map illusions or generated video in place of geometry.

Use modular Blender Python (`bpy`) scripts and Blender’s executable in background/headless mode as the primary construction method. Keep the scripts reproducible and preserve successful versions of the `.blend` file. Use computer use to open and inspect the Blender scene whenever visual inspection is helpful. Do not install or rely on a Blender MCP server.

MODELING APPROACH

Begin with an anatomical blockout before adding detail. Establish:

- Skull, jaw and eye sockets
- Neck, chest, rib cage and pelvis
- Four anatomically convincing legs
- Separated toes and curved claws
- Wing shoulders integrated into the torso
- Articulated wing arms and finger bones
- Properly connected wing membranes
- Long tail continuing naturally from the pelvis
- Primary horns and dorsal spines

Avoid extra limbs, duplicated horns, disconnected membranes, broken joints, floating scales, intersections, paper-thin forms, accidental asymmetry and toy-like proportions.

After validating the blockout, add secondary and tertiary details:

- Layered chest and neck plates
- Directional scales that follow the anatomy
- Brow ridges and eyelids
- Real nostril openings
- Mouth interior, gums and individual teeth
- Horn ridges, chips and worn tips
- Leg armor and knuckle plates
- Wing tendons, folds, veins and restrained scars
- Dorsal spikes continuing down the tail
- Subtle natural asymmetry

Use geometry for anything affecting the silhouette, including horns, claws, teeth, major scales, dorsal spines, wing fingers and important membrane folds. Use normal maps, bump or restrained displacement only for micro-detail.

MATERIALS

Create physically based, photorealistic materials.

The scales should be predominantly charcoal-black with subtle graphite and earthy-brown variation. Add restrained color, roughness and micro-normal variation. Raised scales, recessed skin and armored plates should reflect light differently. Avoid uniform plastic shine and indiscriminate procedural noise.

The wing membranes should look like weathered reptilian leather. They should appear thinner between the supporting bones and thicker near joints and leading edges. Include subtle veins, folds, tension, scars, translucency and color variation without making them resemble cloth, rubber or paper.

Create keratin-like horns and claws with dark bases, lighter worn tips, lengthwise ridges and subtle damage.

The eyes should have:

- Golden-amber irises
- Vertical black pupils
- Detailed iris structures
- Dark limbal regions
- Proper three-dimensional eyeballs
- Realistic eyelids
- Wet corneal highlights
- Subtle moisture along the eyelid edges

Do not make the eyes emissive or artificially glowing.

LIGHTING AND ENVIRONMENT

Create a restrained cinematic environment similar to the reference:

- Dark rocky pedestal or mountain outcrop
- Distant atmospheric mountains
- Dramatic overcast sky
- Cool ambient illumination
- Subtle warmer directional light revealing the face and scales
- Light atmospheric mist
- No distracting structures or additional creatures

Pose the dragon in a stable, commanding stance:

- Head raised and alert
- Neck slightly curved
- Wings fully or nearly fully displayed
- Weight distributed credibly across all four feet
- Tail resting or curving naturally behind it
- Mouth closed or slightly parted
- Eyes directed toward or just past the camera

VISUAL VERIFICATION

Create matched validation cameras for:

- Side view
- Front view
- Top view
- Back view
- Left and right head profiles
- Three-quarter hero view
- Head closeup
- Eye closeup
- Scale closeup
- Wing closeup

Perform at least three critic-and-correction loops.

During each loop:

1. Render every validation camera.
2. Compare each render with the corresponding reference panel.
3. Evaluate silhouette, anatomy, proportions, head identity, horns, wings, legs, feet, tail, scale flow, materials, symmetry, intersections, shading and normals.
4. Produce a ranked list of discrepancies.
5. Correct the most visually important problems.
6. Rerender the same cameras.
7. Preserve before-and-after comparisons.

Do not claim completion merely because the objects were created. Completion requires inspecting the actual renders and correcting visible problems.

10-SECOND CAMERA FLYAROUND

Create a cinematic camera flyaround of the completed dragon with these requirements:

- Exactly 10 seconds
- 1920 × 1080 resolution
- 30 frames per second
- Exactly 300 frames
- Smooth continuous camera movement
- No cuts
- Approximately one complete 360-degree orbit
- Start from a strong front three-quarter composition
- Travel around the side, back and opposite side
- End in a composition that connects smoothly with the opening frame
- Add a restrained elevation change to reveal the back and wing construction
- Keep the complete dragon inside the frame
- Keep the head and torso as the main visual focus
- Use smooth Bézier interpolation
- Avoid sudden acceleration and camera roll
- Avoid clipping through the wings, tail, terrain or body
- Use a natural perspective lens without strong wide-angle distortion
- Keep depth of field subtle enough that the dragon remains readable
- Use restrained motion blur

Before the final render, generate a fast, low-sample 1080p preview of the entire animation. Inspect the complete preview and correct bad framing, camera collisions, awkward silhouettes, obstructed views, abrupt motion, shading defects and visible geometry intersections.

FINAL RENDER

After completing the critic loops and approving the animation preview:

- Render the final animation at 1920 × 1080.
- Use Cycles with GPU acceleration when available.
- Render at 30 fps for exactly 300 frames.
- Use adaptive sampling and denoising.
- Render to individual image frames first so an interrupted render can be resumed.
- Use 16-bit PNG or OpenEXR for the master frames.
- Assemble the rendered frames into a high-quality H.264 MP4.
- Do not use AI frame interpolation.
- Retain the individual frames after assembling the video.

DELIVERABLES

Provide:

1. Final editable `.blend` file
2. All reproducible `bpy` scripts
3. README with rebuild and rendering instructions
4. Reference-analysis and assumptions report
5. Matched-view reference comparisons
6. Before-and-after critic-loop comparisons
7. High-quality still renders of the complete dragon and important details
8. Complete 300-frame image sequence
9. Final 10-second 1080p H.264 video
10. Geometry and material validation report
11. A manifest identifying any permitted external environment resources and their licenses

SUCCESS CRITERIA

Success means:

- The result is recognizably the same dragon as the reference.
- Its anatomy remains coherent from every angle.
- The head, horns, amber eyes, wings, dorsal spines and dark layered scales closely match the reference.
- The dragon is fully three-dimensional and editable.
- Major and medium details are modeled rather than faked.
- Materials respond naturally as the camera moves.
- There are no obvious intersections, floating scales, duplicated anatomy or broken normals.
- It resembles a photographed physical creature rather than a toy, sculpture, generic procedural model or ordinary game asset.
- The camera movement is smooth, cinematic and exactly 10 seconds long.

Work autonomously through these stages. Begin with reference analysis and the anatomical blockout. If you encounter a major ambiguity that cannot be resolved from the reference, make the most anatomically plausible choice, document the assumption and continue.
```

## Provenance

- Original post: https://x.com/doomdave/status/2096335588727349434
- Upstream list: [TripoGrowthLab/awesome-astra-prompts](https://github.com/TripoGrowthLab/awesome-astra-prompts) (MIT)

_Prompt text and preview collected from the public community post above; all rights remain with the original author._
