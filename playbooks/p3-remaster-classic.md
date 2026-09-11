# P3 · Remaster Classic 🕹️

> **难度 ★★** · 复刻老游戏。怀旧自带辨识度，且"原版是什么样"给了模型明确的对齐目标 —— 这是它最容易出活的玩法之一（案例：Mosswing/Flappy、LEGO Racers、Contra、Sonic、文明、模拟城市）。

## 玩法是什么

以"大家记忆中的 X"为锚，要求**保留核心记忆点、重做其余一切**。版权上避开原素材（美术/音乐/角色名），只借玩法记忆。

## Prompt 模板

```text
Remaster the classic "<GAME>" — the one where <ONE_LINE_MEMORY_OF_MECHANIC>.
As a 3D game playable in a browser. One index.html, opens and plays instantly,
no external assets (CDN allowed).

Keep the core exactly as everyone remembers it:
- <MEMORY_POINT_1, e.g. one-tap control>
- <MEMORY_POINT_2, e.g. gaps scroll toward you>
- <MEMORY_POINT_3, e.g. one hit and you're done>

Everything else is yours to decide: art direction, world, camera, juice,
how far to take the visuals. Design an original style — do NOT copy the
original's art, names, or music.

I won't answer clarifying questions. I'm judging a complete, elegant,
great-feeling piece — not a feature list. Small and finished beats big and rough.
```

## 变量

| 变量 | 说明 |
|---|---|
| `<GAME>` | 大众记忆锚点（越国民越好） |
| `<ONE_LINE_MEMORY>` | 一句话说清原版机制，给模型对齐目标 |
| `<MEMORY_POINT_1..3>` | "不可动"的核心记忆点 2-3 条 |

## 翻车点

- **复刻跑偏成"重制"**：模型把玩法改得面目全非 —— 记忆点必须逐条列出并说 "keep exactly"。
- **版权踩线**：明确 "do NOT copy art/names/music"，要求原创皮。
- **情怀滤镜遮 bug**：验收只对"记忆点是否成立"，别被整体氛围带跑。
