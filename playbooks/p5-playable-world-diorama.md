# P5 · Playable World Diorama 🧪

> **难度 ★★** · 把一个地点/物件/记忆做成可旋转、可走进的 3D 微缩世界。发布期刷屏玩法（案例：Seoul 微缩、Cluj-Napoca 体素广场、雨夜便利店、海风之屿）。

## 玩法是什么

"地点 + 情绪 + 交互下限"三要素。约束给得少，模型的风格自由度反而带来惊喜 —— 与 P1 的"硬约束"相反，这个玩法靠**氛围词**取胜。

## Prompt 模板

```text
Build an interactive 3D diorama of <PLACE> in one self-contained HTML file
(Three.js from CDN allowed).

Mood: <3-5 MOOD WORDS，例如 "rain-washed neon, quiet 2am, distant thunder">
Life: <2-3 ambient motions, e.g. "steam from a noodle stall; a train passing every 40s;
     flickering sign">

Interaction (minimum, all must work)
- Orbit / zoom / pan with mouse and touch.
- <ONE DELIGHT, e.g. "click any window to light it up">

Constraint: primitives and procedural textures only; no external assets.
Capture the feeling of the place — geometry accuracy matters less than mood.
```

## 变量

| 变量 | 说明 |
|---|---|
| `<PLACE>` | 具体到"可有一百个记忆细节"的地点（"雨夜便利店门口" > "一家便利店"） |
| `<MOOD>` | 情绪词组，3-5 个 |
| `<LIFE>` | 环境动效清单 —— 这是"活感"的来源 |
| `<ONE_DELIGHT>` | 一个彩蛋交互，让人愿意截图转发 |

## 翻车点

- **地点太大**：整座城市 → 泛泛而谈。缩到一个街角。
- **只给地名不给情绪**：出"建模正确但死气沉沉"的场景。情绪词是主料不是装饰。
- **交互过多**：多个半成品交互不如一个打磨好的。
