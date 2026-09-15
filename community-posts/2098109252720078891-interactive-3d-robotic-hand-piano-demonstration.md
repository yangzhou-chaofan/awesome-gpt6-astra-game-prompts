---
id: astra-post-2098109252720078891
title: "Interactive 3D robotic hand piano demonstration"
author: "MSB"
author_url: "https://x.com/KeWai386772"
original_post: "https://x.com/KeWai386772/status/2098109252720078891"
posted_on: "2026-09-10"
media_type: image
media_url: "https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/0da92a87e2cfefd4088b226ccf8d5e8dbd5b9938d4a76f0104f7fbdffd12c3fa.jpg"
live_demo: ""
source_list: "unknown"
source_list_url: "https://github.com/unknown"
source_license: MIT
tags: [gpt-6-astra, unknown]
---

# Interactive 3D robotic hand piano demonstration

**[MSB](https://x.com/KeWai386772)** · 2026-09-10 · [original post ↗](https://x.com/KeWai386772/status/2098109252720078891)

![preview](https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/0da92a87e2cfefd4088b226ccf8d5e8dbd5b9938d4a76f0104f7fbdffd12c3fa.jpg)

## Prompt

```text
Build a complete browser-based demonstration of a detailed five-finger robotic hand playing a miniature piano. The visible finger motion, physical key travel, generated notes, and musical timing must be causally connected. Deliver a visually polished, interactive application within the evaluator's time budget.  1. EXPERIENCE: Use a full-screen 3D scene with a precisely modeled robotic hand, articulated fingers, visible wrist mechanisms, and a 25-key keyboard spanning MIDI notes 60 through 84. Show realistic black-key and white-key geometry, independent key movement, fingertip pads, and refined materials. Include overhead, performer-side, and fingertip close-up cameras. Provide synchronized audio after the user activates playback.  2. COMMON MUSICAL INPUT: Use MIDI note numbers as the source of truth. At 96 BPM, play these events, expressed as (start beat, note, duration in beats): (0,60,0.4), (0.5,64,0.4), (1,67,0.4), (1.5,64,0.4), (2,62,0.4), (2.5,65,0.4), (3,69,0.4), (3.5,65,0.4), (4,60,0.4), (4.5,60,0.4), (5,60,1), (5,64,1), (5,67,1). The last three events form a simultaneous chord. Also support standard MIDI file import using an established parser.  3. HAND CONTROL: Model independently articulated fingers and a movable wrist. Plan reachable finger assignments, approach motions, presses, holds, releases, repeated-note articulation, and chord execution. Fingers must contact the correct keys without intersecting neighboring keys or making implausible jumps. Use inverse kinematics and joint limits. Display planned finger assignments and allow manual inspection of individual motions.  4. SOUND CAUSALITY: Generate note-on events only when the corresponding visible key crosses a documented depression threshold because of finger contact. Generate note-off on release, with hysteresis to prevent chatter. MIDI events are planning targets, not an independent audio playback track. A geometric contact-driven key mechanism is acceptable if explicitly identified; full contact dynamics may be used instead. Keys must not move merely because a MIDI event is scheduled.  5. TIMING: Use a consistent musical clock and timestamp actual key-trigger events against target events. Account for audio scheduling and render timing. Expose tempo, transpose, play, pause, restart, loop, and slow-motion inspection. Pausing or restarting must release active notes appropriately. Slowing playback must preserve synchronization between fingers, keys, and audio.  6. DIAGNOSTICS: Display target notes, planned fingers, actual triggered notes, and onset timing errors on an aligned timeline. Report missed notes, extra notes, wrong pitches, repeated-note failures, and stuck notes. Provide a contact inspection overlay showing which fingertip is depressing each key. Record the evidence needed to distinguish successful planning from approximate hand animation.  7. VERIFICATION: Evaluate melody, repeated notes, and the final chord separately. Aim for no wrong or missing notes, a 95th-percenti
```

## Provenance

- Original post: https://x.com/KeWai386772/status/2098109252720078891
- Upstream list: [unknown](https://github.com/unknown) (MIT)

_Prompt text and preview collected from the public community post; all rights remain with the original author._
