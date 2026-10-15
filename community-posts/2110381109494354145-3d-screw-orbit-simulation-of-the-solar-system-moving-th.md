---
id: astra-post-2110381109494354145
title: "3D Screw-Orbit Simulation of the Solar System Moving Through the Milky Way"
author: "AI TANUKI（AIたぬき）"
author_url: "https://x.com/ecsamuraigold"
original_post: "https://x.com/ecsamuraigold/status/2110381109494354145"
posted_on: "2026-10-14"
media_type: image
media_url: "https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/078138c80c08d2337a617711.jpg"
live_demo: ""
source_list: "TripoGrowthLab/awesome-astra-prompts"
source_list_url: "https://github.com/TripoGrowthLab/awesome-astra-prompts"
source_license: MIT
tags: [gpt-6-astra, tripogrowthlab]
---

# 3D Screw-Orbit Simulation of the Solar System Moving Through the Milky Way

**[AI TANUKI（AIたぬき）](https://x.com/ecsamuraigold)** · 2026-10-14 · [original post ↗](https://x.com/ecsamuraigold/status/2110381109494354145)

![preview](https://raw.githubusercontent.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/main/assets/previews/078138c80c08d2337a617711.jpg)

## Prompt

```text
Create a 3D animation of the Sun traveling through the Milky Way at approximately 220 km/s, with the eight planets orbiting around it in a screw (helical) pattern through 3D space as they follow the Sun. Build it as a single HTML file (HTML5 Canvas or Three.js) that can be previewed in Artifacts.

[Visualization and physics model requirements]
1. The Sun's movement and the tilt of the ecliptic plane (important)
   - The Sun continuously moves forward along its direction-of-travel vector through the Milky Way, represented by an axis with a gold arrow.
   - The planets' orbital plane (the ecliptic) moves forward with the Sun while maintaining a single plane tilted approximately 60° relative to the Sun's direction of travel. The planets must not lag behind the Sun and trail it in a cone; instead, they should advance while orbiting on the same tilted plane as the Sun, creating corkscrew-like helical trajectories through 3D space.
   - At the Sun's current position, display a semitransparent guide ring for the approximately 60°-tilted ecliptic plane, including each planet's circular orbit, along with crosshairs.

2. The eight planets and 3D helical trajectories (screw orbits)
   - Render the eight planets: Mercury, Venus, Earth (+ Moon), Mars, Jupiter, Saturn (+ rings), Uranus, and Neptune.
   - Set the orbital timing according to Kepler's laws: inner planets should have shorter orbital periods and tighter-pitch helices, while outer planets should have slower, wider-pitch helices.
   - Leave vivid 3D helical trails in space by connecting each planet's past positions with a ribbon or line that fades toward the tail.
   - Display Japanese labels next to each body: 太陽, 水星, 金星, 地球, 火星, 木星, 土星, 天王星, 海王星.
   - Place a moving star field and cylindrical depth guide rings in the background to convey motion through galactic space.

3. Screen layout and UI panels (dark theme, 16:9 composition)
   - Left-to-center area (main 3D view):
     - In the upper left, display the title 「銀河系を進む太陽系：3Dスクリュー（らせん）軌道シミュレーション」 and the subtitle 「秒速約220kmで進む太陽を、約60°傾いた黄道面上で公転する惑星が追いかけ、3D空間にらせん軌跡を描きます」.
     - In the lower left, display an explanatory badge: 「ポイント：惑星は太陽の後ろに遅れて引っ張られるのではなく、進行方向に対し約60°傾いた同一平面（黄道面）を保ったまま太陽と一緒に進むため、3次元空間全体で見るとコルク抜き（スクリュー）のようならせん軌道を描きます。」
   - Right area (HUD information panel):
     - Top: Add a submonitor frame titled 「横から見たスクリュー波形（側面投影）」 and render, in real time, sine-wave-like patterns showing each planet moving above and below the Sun's direction-of-travel axis (the horizontal line).
     - Middle: Display real-time counters for 「太陽の銀河系公転速度: 約 220 km/s」 and 「銀河空間の移動距離（百万km単位・地球換算年数）」.
     - Bottom: For each of the eight planets, display a colored dot, its name in Japanese and English, its actual average orbital speed (Mercury 47.4 km/s to Neptune 5.4 km/s), its cumulative orbit count (〇〇周), and a progress bar for the current orbit.

4. Interactive controls
   - Allow the user to freely rotate the 3D camera angle by dragging the mouse and zoom with the scroll wheel. The camera should continuously follow the advancing Sun.
   - Provide play/pause, simulation-speed slider, and camera-view reset controls.
```

- Original post: https://x.com/ecsamuraigold/status/2110381109494354145
- Upstream list: [TripoGrowthLab/awesome-astra-prompts](https://github.com/TripoGrowthLab/awesome-astra-prompts)

_Prompt and preview from the public community post; rights remain with the original author._
