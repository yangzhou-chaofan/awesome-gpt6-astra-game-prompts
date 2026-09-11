<div align="center">

# 🕹️ Awesome GPT-6 Astra · Game Prompts

### 一条 prompt，一个能玩的 3D 游戏

**26 条可复现配方 · 103 个真实案例（101 带图预览）· 6 个玩法 Playbook**

[🚀 五分钟上手](#-五分钟上手) · [🏆 精选推荐](#-精选推荐) · [🖼️ 案例画廊](#️-案例画廊) · [🧪 配方库](#-可复现配方-26-条) · [📖 Playbooks](#-玩法-playbooks) · [🌐 网页版](site/index.html)

[![validate](https://github.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/actions/workflows/validate.yml/badge.svg)](https://github.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/actions/workflows/validate.yml)
[![license: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![model: gpt-6-astra](https://img.shields.io/badge/model-gpt--6--astra-6f42c1.svg)](https://platform.openai.com/docs/models)

</div>

---

> **GPT-6 Astra**（OpenAI · 2026-09-03）让"一句话做出能玩的 3D 游戏"成为现实。
> 这个仓库把社区一周内跑出来的玩法收成三层，各司其职：
>
> **🖼️ 案例层** — 看到别人做出了什么（带图、带原帖、带 prompt 原文）
> **🧪 配方层** — 想自己复现时的精确参数与验收清单
> **📖 方法层** — 拿着自己的点子，怎么组合出下一个作品

---

## 🚀 五分钟上手

**想看效果** → 往下滑到 [案例画廊](#️-案例画廊)，点任意图片直达 X 原帖
**想抄 prompt** → 每张图下方"📜 prompt 与出处"里有作者公开的原文
**想自己做一个** → 跑一遍 [astra-3d-001 无尽跑酷](prompts/full-games/astra-3d-001-endless-runner.md)（整个清单的冒烟测试）
**有自己点子** → 翻 [玩法 Playbooks](#-玩法-playbooks)，六种套路挑一个套

---

## 🏆 精选推荐

*不是"效果好"而是"值得学"—— 每条给出值得学的理由。*

| | 案例 | 值得学什么 |
|---|---|---|
| ⭐ | [**Browser Flight Simulator with a Complete Flight Loop**](community-posts/2096236137266512181-browser-flight-simulator-with-a-complete-flight-loop.md) | 教科书级验收链：START → ACCELERATE → … → PLAY AGAIN，还要求模型『自己跑一遍、修到能玩』 |
| ⭐ | [**Windhaven Coastal Fantasy Adventure Game**](community-posts/2096629506047955327-windhaven-coastal-fantasy-adventure-game.md) | 长叙事范本：风格→世界→镜头→负面约束（no UI / no text / no logos）一段扛住全案 |
| ⭐ | [**Three.js dark-fantasy action RPG**](community-posts/2096637091627364531-three-js-dark-fantasy-action-rpg.md) | 氛围与系统平衡最好：哥特废墟、溪流瀑布的意象如何变成可执行需求 |
| ⭐ | [**Rebuilding Lego 1999 Racers**](community-posts/2096438110095585753-rebuilding-lego-1999-racers.md) | 复刻范本：原版记忆点给模型对齐目标，怀旧辨识度 × 现代手感 |
| ⭐ | [**Mini World 3D exploration game**](community-posts/2096641728497275011-mini-world-3d-exploration-game.md) | 为真人设计（4 岁孩子）：视角/缩放/难度约束写出手感与上手性 |
| ⭐ | [**只看屏幕通关《火红》**](showcase/entries/只看屏幕通关火红.md) | Computer Use 边界：零游戏 API，18h12m 纯看屏幕操作 |
| ⭐ | [**做完游戏自己玩自己录**](showcase/entries/我让-gpt-6-astra-做了个游戏然后让它自己玩自己录屏再剪一段开发实录.md) | 做→自玩→自录→自剪，全自动内容管线 |

---

## 🖼️ 案例画廊

*全部为社区真实产出。点图直达 X 原帖，"prompt 与出处"里是作者公开的原文。🌟 = 在线可玩。*

<table>
<tr><td align="center" width="33%"><a href="https://x.com/adxtyahq/status/2096236137266512181"><img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/bbb03f5650350e6b4a323f0dd76f98d1abb0cbe94896f2dbe24d68c4bfbf8ce8.jpg" width="100%" alt="✈️ 完整飞行模拟循环"/></a><br/><b>✈️ 完整飞行模拟循环</b> · 起飞→飞行→降落→评分一条龙<br/><a href="community-posts/2096236137266512181-browser-flight-simulator-with-a-complete-flight-loop.md">📜 prompt 与出处</a></td><td align="center" width="33%"><a href="https://x.com/HiltonMisia/status/2096637091627364531"><img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/ad164224745a34f4bcd14af8ec14fe0d7a6cf7203a80ea7544106dd1b76dc8f7.jpg" width="100%" alt="⚔️ 暗黑 ARPG"/></a><br/><b>⚔️ 暗黑 ARPG</b> · 单 prompt 出完整动作 RPG<br/><a href="community-posts/2096637091627364531-three-js-dark-fantasy-action-rpg.md">📜 prompt 与出处</a></td><td align="center" width="33%"><a href="https://x.com/tripoai/status/2096629506047955327"><img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/e3304eeb4bf4186f9a57768af5e1962741c3dce44ed5aace2aef04585d0e69ca.jpg" width="100%" alt="🏝️ Windhaven 冒险"/></a><br/><b>🏝️ Windhaven 冒险</b> · 长叙事 prompt 范本<br/><a href="community-posts/2096629506047955327-windhaven-coastal-fantasy-adventure-game.md">📜 prompt 与出处</a></td></tr>
<tr><td align="center" width="33%"><a href="https://x.com/EngMoElgaraihy/status/2096438110095585753"><img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/e14b00869191181ad52fe51c4e0a57d3ad72c405802c16cb36147a9b5d613143.jpg" width="100%" alt="🏎️ LEGO Racers 复刻"/></a><br/><b>🏎️ LEGO Racers 复刻</b> · 怀旧游戏现代化<br/><a href="community-posts/2096438110095585753-rebuilding-lego-1999-racers.md">📜 prompt 与出处</a></td><td align="center" width="33%"><a href="https://x.com/majidmanzarpour/status/2096251574918013135"><img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/8f55d646820e4f1f0b98d00cdc85125c79f19093abe73bc0cecdfbf2e2365e50.webp" width="100%" alt="🦖 Kaiju 城市大战"/></a><br/><b>🦖 Kaiju 城市大战</b> · 实时对战 · 在线可玩 🌟<br/><a href="community-posts/2096251574918013135-kaiju-city-battle.md">📜 prompt 与出处</a></td><td align="center" width="33%"><a href="https://x.com/zeuuss_01/status/2096337879173591171"><img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/b357895cffa990ebc6d5404e59b1f2371a45536a5cabca80b976c590192d8338.webp" width="100%" alt="🦀 螃蟹动作游戏"/></a><br/><b>🦀 螃蟹动作游戏</b> · 物理驱动 · 在线可玩 🌟<br/><a href="community-posts/2096337879173591171-a-crab-game-with-action-driven-mechanics.md">📜 prompt 与出处</a></td></tr>
</table>

**[→ 游戏专区全部 21 条](#-游戏专区-带缩略图) · [→ 3D / 视频 / 网页分类](#-更多分类)**

---

## 🎮 游戏专区 (带缩略图)

| 预览 | 案例 | 作者 | 试玩 |
|---|---|---|---|
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/b357895cffa990ebc6d5404e59b1f2371a45536a5cabca80b976c590192d8338.webp" width="150"/> | [A crab game with action-driven mechanics](community-posts/2096337879173591171-a-crab-game-with-action-driven-mechanics.md) 🌟 | [@zeuuss_01](https://x.com/zeuuss_01) | [▶ play](https://beach-crab-game.netlify.app/) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/8f55d646820e4f1f0b98d00cdc85125c79f19093abe73bc0cecdfbf2e2365e50.webp" width="150"/> | [Kaiju city battle](community-posts/2096251574918013135-kaiju-city-battle.md) 🌟 | [@majidmanzarpour](https://x.com/majidmanzarpour) | [▶ play](https://stormcolossus.netlify.app/) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/bbb03f5650350e6b4a323f0dd76f98d1abb0cbe94896f2dbe24d68c4bfbf8ce8.jpg" width="150"/> | [Browser Flight Simulator with a Complete Flight Loop](community-posts/2096236137266512181-browser-flight-simulator-with-a-complete-flight-loop.md) | [@adxtyahq](https://x.com/adxtyahq) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/2b020e0fc8275195843fe93dfea7923e440940671c21060866aa6fd429e471e9.webp" width="150"/> | [Browser city game with a supplied character](community-posts/2096398839830008292-browser-city-game-with-a-supplied-character.md) | [@djrio_vr](https://x.com/djrio_vr) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/b00b0f3011c9f77412b6212bff0efb0fc453cefca3af7186267fabb90c0536f0.webp" width="150"/> | [Complete Three.js puzzle level](community-posts/2096505740643246231-complete-three-js-puzzle-level.md) | [@TvWoo](https://x.com/TvWoo) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/9188a5a53301b71d404af1d10d6baf4e44585869cc933918118ae2180cf3c1ab.jpg" width="150"/> | [Interactive Robot Pet on a Workbench](community-posts/2097004192627933279-interactive-robot-pet-on-a-workbench.md) | [@zeuuss_01](https://x.com/zeuuss_01) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/177462bb87e3089acbf23e2e6f58e75e4fa5cb7291601fdce6da2a3fb5f2b6af.webp" width="150"/> | [Komorebi river kayaking](community-posts/2096244208533455049-komorebi-river-kayaking.md) | [@ItsmeAjayKV](https://x.com/ItsmeAjayKV) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/2b65a179759aadacaa8dcf78ecfd45f3e7dcd04b4d1f535bc553c3d9f7505f2d.jpg" width="150"/> | [LEGO Minifig Game Asset with Blender MCP](community-posts/2096766465730847059-lego-minifig-game-asset-with-blender-mcp.md) | [@_simonsmith](https://x.com/_simonsmith) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/30b921728503d9086c9f52adbcc90a3fa3dc568cb7e85903172fc1c5295cb279.jpg" width="150"/> | [Mini World 3D exploration game](community-posts/2096641728497275011-mini-world-3d-exploration-game.md) | [@weijianzhang_](https://x.com/weijianzhang_) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/eceebf1bdd5561e25fada5daec055473bd5506cf272760a5a08a8b4ad111988c.webp" width="150"/> | [Mobile-playable Unity rally game](community-posts/2096556692842348826-mobile-playable-unity-rally-game.md) | [@kevinkern](https://x.com/kevinkern) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/756d0d4859c6a3bec065b9594d7fed7544101b6f6b6fb1e331bbfee059e84738.jpg" width="150"/> | [Photorealistic Editable Dragon Reconstruction in Blender](community-posts/2096335588727349434-photorealistic-editable-dragon-reconstruction-in-blender.md) | [@doomdave](https://x.com/doomdave) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/a50398d5761279d4c67fa425f175dd71bdd68472435b1df9f4c8e703c7edb035.jpg" width="150"/> | [Playroom: Retro 3D Browser Arcade](community-posts/2097339176094195899-playroom-retro-3d-browser-arcade.md) | [@tripoai](https://x.com/tripoai) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/66b6fe9a782625a1d13bf79872857593fecf604421e40eb8cfd67c212ad0b695.webp" width="150"/> | [Railway network simulation game](community-posts/2096362653480562751-railway-network-simulation-game.md) | [@tomkrcha](https://x.com/tomkrcha) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/e14b00869191181ad52fe51c4e0a57d3ad72c405802c16cb36147a9b5d613143.jpg" width="150"/> | [Rebuilding Lego 1999 Racers](community-posts/2096438110095585753-rebuilding-lego-1999-racers.md) | [@EngMoElgaraihy](https://x.com/EngMoElgaraihy) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/36b98467e6157525383fbc35526f9c07f2cadf9f16b1559da917bb3cc5fc4eca.jpg" width="150"/> | [Recreate League of Legends as a Web Game](community-posts/2097336230078013598-recreate-league-of-legends-as-a-web-game.md) | [@liyue_ai](https://x.com/liyue_ai) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/36b98467e6157525383fbc35526f9c07f2cadf9f16b1559da917bb3cc5fc4eca.jpg" width="150"/> | [Recreate a Mini 3D Game Inspired by League of Legends](community-posts/2097320830602809682-recreate-a-mini-3d-game-inspired-by-league-of-legends.md) | [@LufzzLiz](https://x.com/LufzzLiz) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/0ba729978213ae4955dbc48dc1842a22c3ccfe72d686a037cf599fba60a214dd.webp" width="150"/> | [The Quiet Crossing exploration quest](community-posts/2096574297703637111-the-quiet-crossing-exploration-quest.md) | [@Motion_Viz](https://x.com/Motion_Viz) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/ad164224745a34f4bcd14af8ec14fe0d7a6cf7203a80ea7544106dd1b76dc8f7.jpg" width="150"/> | [Three.js dark-fantasy action RPG](community-posts/2096637091627364531-three-js-dark-fantasy-action-rpg.md) | [@HiltonMisia](https://x.com/HiltonMisia) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/9467608cd8acae08c8272517d7c6605284f8073c38eefd78221597d07dfe93db.webp" width="150"/> | [Trading-card battle game loop](community-posts/2096555856204644550-trading-card-battle-game-loop.md) | [@FaryaBlender3D](https://x.com/FaryaBlender3D) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/e3304eeb4bf4186f9a57768af5e1962741c3dce44ed5aace2aef04585d0e69ca.jpg" width="150"/> | [Windhaven Coastal Fantasy Adventure Game](community-posts/2096629506047955327-windhaven-coastal-fantasy-adventure-game.md) | [@tripoai](https://x.com/tripoai) | — |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/67349df6f55e75c5acee30371c715c3ec04b9ae5c26c628e71d3afb3aae6c9e0.webp" width="150"/> | [Wright Flyer through a Japanese forest](community-posts/2096467585785286808-wright-flyer-through-a-japanese-forest.md) | [@thebuggeddev](https://x.com/thebuggeddev) | — |

---

## 🧱 更多分类

<details>
<summary><b>🧱 3D 世界 · 🎬 视频 · 🕸️ 网页（点击展开）</b></summary>

### 🧱 3D 世界与建模

| 预览 | 案例 | 作者 |
|---|---|---|
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/ea082ba0b96ce2048a717565f743d1448c4bef031ad0585dcdb75aced928fad8.jpg" width="130"/> | [3D render of an X picture](community-posts/2096338836854804782-3d-render-of-an-x-picture.md) | [@MattJamesBoyle](https://x.com/MattJamesBoyle) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/3e060bfb3bf3973f0efb048cacbdc625fe879b8bca0cb46c2bb8fd367eb75268.jpg" width="130"/> | [A 12-Second Forest Road in Blender](community-posts/2096986557244723371-a-12-second-forest-road-in-blender.md) | [@Jomolos](https://x.com/Jomolos) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/3dac0cf4428bc4a32bd1418c62a971bc75be632f3e10e918ba9b45800f364ba2.webp" width="130"/> | [A house modeled from scratch in Blender](community-posts/2096576154337734865-a-house-modeled-from-scratch-in-blender.md) | [@mizkun](https://x.com/mizkun) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/76eeeaa8710b4767fb99c09689e3a0b87ba770495f026e34ea34cb2b5f1f76fc.webp" width="130"/> | [Apartment sketch to rendered interiors](community-posts/2096566686266597754-apartment-sketch-to-rendered-interiors.md) | [@WorldEverett](https://x.com/WorldEverett) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/3388e9e5e8f519fb22f67c35c98f5038335da857c0a1b8883c406c6e14c36c4a.webp" width="130"/> | [Assemble and animate generated 3D assets](community-posts/2096481425050743048-assemble-and-animate-generated-3d-assets.md) | [@Stefan_3D_AI](https://x.com/Stefan_3D_AI) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/721eed98f68b8ad4264b4fbd922b185c7e6501834c9aa828a0b3b369fba5ff28.jpg" width="130"/> | [Backrooms-inspired Blender VHS scene](community-posts/2097534290112188602-backrooms-inspired-blender-vhs-scene.md) | [@chrisfirst](https://x.com/chrisfirst) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/d13ca069743cb65e0501484737d96a1fbde81927026e9b8837b149ece9b0693d.webp" width="130"/> | [Blender models with Unity VFX](community-posts/2096560142871658589-blender-models-with-unity-vfx.md) | [@CST_negi](https://x.com/CST_negi) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/b6d2405bd8f8e5cd9543cde67c0c3719a2e7b5ac38c080cca7336d0f7c1ec1d1.jpg" width="130"/> | [Building a Comedy Scene of a Robotic Arm Chasing a Cat with GPT-6 Astra and Blender](community-posts/2097675660873605422-building-a-comedy-scene-of-a-robotic-arm-chasing-a-cat-with.md) | [@TanLuAI](https://x.com/TanLuAI) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/1712c53120622f0ba430f5985562bd6eb307621c1a4466ef9d2cf26c99b81716.jpg" width="130"/> | [Character Concept to Rigged 3D Model and Cartoon](community-posts/2096342420543660277-character-concept-to-rigged-3d-model-and-cartoon.md) | [@higgsfield_ai](https://x.com/higgsfield_ai) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/0203a375c4a0f77f1fae00d9c8c9173739b940debd87bf4144d4f375ccc8c12e.jpg" width="130"/> | [Create and render a black hole in Blender](community-posts/2096391653669953761-create-and-render-a-black-hole-in-blender.md) | [@JohnKlerAI](https://x.com/JohnKlerAI) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/a8ee5a495643a02333b8f904a4d46c26f8211b6ba6ecb40ba3b2521387e81571.jpg" width="130"/> | [Edit a Blender scene for knurled posts and PCB fit](community-posts/2096990373813858591-edit-a-blender-scene-for-knurled-posts-and-pcb-fit.md) | [@rboyd](https://x.com/rboyd) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/aed224d4a25ce9c0d436ebd4d2bfb7fadb211bdf624364e3f7905a0dbec1546f.jpg" width="130"/> | [Folding Carton Animation from a Dieline](community-posts/2096612394281603144-folding-carton-animation-from-a-dieline.md) | [@Salmaaboukarr](https://x.com/Salmaaboukarr) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/bffeb201cd39ed86178dd22e30bda1ea70e4ff92902307d88ba66700e21dcd32.jpg" width="130"/> | [Hogwarts 3D scene](community-posts/2096907617117540478-hogwarts-3d-scene.md) | [@HiltonMisia](https://x.com/HiltonMisia) |
| <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/8528f6aaa8b6070a8c1e3732f0791feac42ed1ba7d0c23cc85c7c9e0212600a1.png" width="130"/> | [Improve a 3D Model’s Facial Features in Blender Using a Reference Image](community-posts/2097313247116341424-improve-a-3d-models-facial-features-in-blender-using-a-refer.md) | [@carlos_olivera](https://x.com/carlos_olivera) |

### 🎬 视频

| 案例 | 作者 | 预览 |
|---|---|---|
| [Witch's First Flight — 15s Generated Shot Script](community-posts/2095873015007592679-witch-s-first-flight-15s-generated-shot-script.md) | — | <img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/HEAD/media/witch-first-flight.webp" width="130"/> |
| [AdCar TV — In-Repo One-Shot Launch Video](community-posts/2096258259459964963-adcar-tv-in-repo-one-shot-launch-video.md) | — | <img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/HEAD/media/adcar-tv.webp" width="130"/> |
| [T Cells — One Sentence, Five Minutes](community-posts/2095659170661904804-t-cells-one-sentence-five-minutes.md) | — | <img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/HEAD/media/t-cells.webp" width="130"/> |
| [High-Speed Parkour Motion Previz](community-posts/2096096560690209130-high-speed-parkour-motion-previz.md) | — | <img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/HEAD/media/parkour-previz.webp" width="130"/> |

### 🕸️ 网页与交互

| 案例 | 作者 | 预览 |
|---|---|---|
| [Endless Miniature Street in Three.js WebGPU](community-posts/2096956214680965501-endless-miniature-street-in-three-js-webgpu.md) | [@creativedash](https://x.com/creativedash) | <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/c2aa4cd5daf5e1bc8f71051db13c08e7f52359b5a5aaf7b813b72d474117897e.jpg" width="130"/> |
| [Create an Interactive Soft-Body Slime with Three.js and WebGPU](community-posts/2096793432987464010-create-an-interactive-soft-body-slime-with-three-js-and-webg.md) | [@Delroy715](https://x.com/Delroy715) | <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/080a768b7958082811553a4d1a4c865caeee6e542e68fe0ba9e32ed478233342.jpg" width="130"/> |
| [Interactive jelly lemon tree](community-posts/2097065330728128920-interactive-jelly-lemon-tree.md) | [@vib3coded](https://x.com/vib3coded) | <img src="https://raw.githubusercontent.com/TripoGrowthLab/awesome-astra-prompts/HEAD/assets/previews/19fa5b36caaf4663987e99892e3cb3babcc452cbe50e1ef2f6108a859d3eba36.jpg" width="130"/> |

> 其余分类（工程 / Agent / 研究 / 官方指南）见 **[CATALOG.md](CATALOG.md)**。

</details>

---

## 🧪 可复现配方 · 26 条

*案例证明"做得出"，配方保证你"复现得了"。每条钉死四件事：*

| 契约 | 内容 |
|---|---|
| **模型** | `gpt-6-astra` · 版本钉死到日期（2026-09-03） |
| **参数** | temperature / top_p / seed / max_output_tokens 全部记录 |
| **输入** | 运行时、依赖、起始文件、素材 —— 缺一样都列出来 |
| **验收** | 预期产物 + 能失败的检查清单 + "Where it drifts" 翻车点 |

<details>
<summary><b>📋 全部 26 条配方（自动生成的完整索引）</b></summary>

<!-- BEGIN INDEX -->
> **26** prompts · 5 categories · targeting `gpt-6-astra` (2026-09-03).

The initial batch ships as **📝 draft** — format-complete and reviewed, but not yet independently reproduced. Run one and record it to promote it to 🧪 community.

### 🎮 Full games — one prompt, a playable game

| ID | Prompt | Stack | Difficulty | Verified |
| --- | --- | --- | --- | --- |
| `astra-3d-001` | [Endless Runner](prompts/full-games/astra-3d-001-endless-runner.md) | Three.js | beginner | 📝 draft |
| `astra-3d-002` | [First-Person Explorer](prompts/full-games/astra-3d-002-first-person-explorer.md) | Three.js | intermediate | 📝 draft |
| `astra-3d-003` | [Tower Defense](prompts/full-games/astra-3d-003-tower-defense.md) | Three.js | intermediate | 📝 draft |
| `astra-3d-004` | [Top-Down Arena Shooter](prompts/full-games/astra-3d-004-topdown-arena-shooter.md) | Three.js | intermediate | 📝 draft |
| `astra-3d-005` | [Voxel Sandbox](prompts/full-games/astra-3d-005-voxel-sandbox.md) | Three.js | advanced | 📝 draft |
| `astra-3d-006` | [Physics Marble Platformer](prompts/full-games/astra-3d-006-marble-platformer.md) | Three.js + Rapier | advanced | 📝 draft |

### ⚙️ Systems — drop-in gameplay machinery

| ID | Prompt | Stack | Difficulty | Verified |
| --- | --- | --- | --- | --- |
| `astra-3d-101` | [Character Controller](prompts/systems/astra-3d-101-character-controller.md) | Three.js | intermediate | 📝 draft |
| `astra-3d-102` | [Seeded Procedural Terrain](prompts/systems/astra-3d-102-procedural-terrain.md) | Three.js | intermediate | 📝 draft |
| `astra-3d-103` | [Enemy AI State Machine](prompts/systems/astra-3d-103-enemy-fsm-ai.md) | Three.js | intermediate | 📝 draft |
| `astra-3d-104` | [Inventory & Pickups](prompts/systems/astra-3d-104-inventory-and-pickups.md) | Three.js | beginner | 📝 draft |
| `astra-3d-105` | [Third-Person Camera Rig](prompts/systems/astra-3d-105-third-person-camera.md) | Three.js | intermediate | 📝 draft |
| `astra-3d-106` | [Save / Load System](prompts/systems/astra-3d-106-save-load-system.md) | Three.js | beginner | 📝 draft |
| `astra-3d-107` | [Object Pooling & Culling](prompts/systems/astra-3d-107-object-pooling.md) | Three.js | advanced | 📝 draft |
| `astra-3d-108` | [Deterministic Replay Harness](prompts/systems/astra-3d-108-deterministic-replay.md) | Three.js | advanced | 📝 draft |

### 🧱 Assets — geometry, rigs and textures as code

| ID | Prompt | Stack | Difficulty | Verified |
| --- | --- | --- | --- | --- |
| `astra-3d-201` | [Text → Low-Poly Prop (GLB)](prompts/assets/astra-3d-201-text-to-3d-prop.md) | Blender 4.x | intermediate | 📝 draft |
| `astra-3d-202` | [Procedural PBR Texture Set](prompts/assets/astra-3d-202-pbr-texture-set.md) | Canvas / WebGL | intermediate | 📝 draft |
| `astra-3d-203` | [Rigged Character from a Prompt](prompts/assets/astra-3d-203-rigged-character.md) | Blender 4.x | advanced | 📝 draft |
| `astra-3d-204` | [Modular Kit-Bash Set](prompts/assets/astra-3d-204-modular-kitbash.md) | Blender 4.x | intermediate | 📝 draft |
| `astra-3d-205` | [Texture Atlas Packer](prompts/assets/astra-3d-205-texture-atlas.md) | Node / Sharp | beginner | 📝 draft |

### 🗺️ Levels & worlds

| ID | Prompt | Stack | Difficulty | Verified |
| --- | --- | --- | --- | --- |
| `astra-3d-301` | [Seeded Procedural Dungeon](prompts/levels/astra-3d-301-procedural-dungeon.md) | Three.js | intermediate | 📝 draft |
| `astra-3d-302` | [Procedural City Block](prompts/levels/astra-3d-302-procedural-city.md) | Three.js | advanced | 📝 draft |
| `astra-3d-303` | [Navmesh from Level Geometry](prompts/levels/astra-3d-303-navmesh-baker.md) | Three.js | advanced | 📝 draft |
| `astra-3d-304` | [Wave / Spawn Director](prompts/levels/astra-3d-304-spawn-director.md) | Three.js | intermediate | 📝 draft |

### 🖥️ UI & HUD

| ID | Prompt | Stack | Difficulty | Verified |
| --- | --- | --- | --- | --- |
| `astra-3d-401` | [HUD, Menus & Pause Screen](prompts/ui/astra-3d-401-hud-and-menus.md) | HTML / CSS | beginner | 📝 draft |
| `astra-3d-402` | [Radial & Context Menu System](prompts/ui/astra-3d-402-radial-menu.md) | HTML / CSS | intermediate | 📝 draft |
| `astra-3d-403` | [Settings & Accessibility Panel](prompts/ui/astra-3d-403-settings-panel.md) | HTML / CSS | beginner | 📝 draft |
<!-- END INDEX -->

</details>

> 配方与案例的关系：案例层（community-posts / showcase）**不承诺可复现**，只承诺"真实发生"；
> 配方层（prompts/）**承诺可复现**，四条契约缺一不收。两层在条目内互相引用。

---

## 📖 玩法 Playbooks

*配方是"这个 prompt 长什么样"，playbook 是"我想做 X 该怎么组合"。*

| | Playbook | 一句话 | 难度 |
|---|---|---|---|
| 🎈 | **[One-Shot Arcade](playbooks/p1-one-shot-arcade.md)** | 一个 prompt 出一把流小游戏（含 [Mosswing 实战例证](https://mosswing-quiet-flight.jack-514.chatgpt.site/)） | ★ |
| 🏗️ | **[Spec-First Big Build](playbooks/p2-spec-first-big-build.md)** | 先写 SPEC.md 再照规格施工大项目 | ★★ |
| 🕹️ | **[Remaster Classic](playbooks/p3-remaster-classic.md)** | 复刻老游戏：怀旧辨识度 × 现代手感 | ★★ |
| 🤖 | **[Computer-Use Player](playbooks/p4-computer-use-player.md)** | 让模型"长手"亲自玩游戏 | ★★★ |
| 🧪 | **[Playable World Diorama](playbooks/p5-playable-world-diorama.md)** | 把任意地点变成可探索 3D 微缩世界 | ★★ |
| 🎨 | **[Co-Creative Design Partner](playbooks/p6-co-creative-design.md)** | 先让模型当策划再当工人 | ★ |

**配套技能**：[`skills/astra-playbook`](skills/astra-playbook/SKILL.md) — 把一句话点子路由到正确形态、填满八段式 prompt 框架、附验收清单。

---

## 🌐 网页版 & 生态目录

- **[site/index.html](site/index.html)** — 可浏览的网页版（catalog 数据驱动）
- **[CATALOG.md](CATALOG.md)** — 28 条生态条目：游戏 / 3D / 网页 / 视频 / 应用 / Agent / 工程 / 研究，⭐ featured / ✦ notable / · community 三级推荐
- **[showcase/](showcase/README.md)** — 103 条 X 案例库完整数据层（[data.json](showcase/data.json)，网页与 repo 共建）

---

## 🤝 参与贡献

| 方式 | 价值 | 入口 |
|---|---|---|
| 🖼️ 提交社区案例 | 发现新玩法 | PR 到 `community-posts/`，见 [CONTRIBUTING](CONTRIBUTING.md) |
| 🧪 复现配方 | 把 📝 draft 升级为 🧪 community（**当前最缺的贡献**） | 跑通任一 recipe 并记录 |
| ⭐ 新增配方 | 扩充可复现契约库 | [模板](templates/PROMPT_TEMPLATE.md) + [契约文档](docs/REPRODUCIBILITY.md) |

---

<div align="center">

案例快照 **2026-09-11** · X 原帖为唯一 record source，awesome lists 仅作聚合渠道 · 所有权利归原作作者 · 非官方社区项目，与 OpenAI 无关

[CC0-1.0](LICENSE)

</div>
