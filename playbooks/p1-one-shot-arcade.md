# P1 · One-Shot Arcade 🎈

> **难度 ★** · 一个 prompt，一个能玩的 HTML。是所有玩法里投入产出比最高的，也是验证模型版本能力的标准烟雾测试。

## 玩法是什么

给一段紧凑但完整的 brief，让模型一次性输出**单个自包含 HTML 文件**。双击即玩，无构建、无服务器、无外部资产。
来自 @ayi1337 的 Mosswing、@tripoai 收录的飞行模拟、@ElIngeRRC 的一句 GTA 等案例的共同骨架。

## 什么时候用

- 想快速验证一个点子好不好玩（5 分钟出一个能摸的版本）
- 想测试新模型版本的"一次到位"能力
- 内容创作：录屏/发帖，单文件天然适合传播

## Prompt 模板（可粘贴）

```text
You are a senior game engineer. Build a complete, playable <GENRE> game in ONE self-contained
HTML file.

Deliverable
- One file, `index.html`. Opens by double-click. No build step, no server, no external assets
  (CDN allowed only for <LIB>).

Gameplay (all must work)
- <CORE_LOOP：3 条以内核心机制，每条一行>
- One clear lose condition and one clear restart path (press R).
- Score + persisted best (localStorage).

Feel (judge me on this)
- <FEEL：手感目标，例如 "snappy: input responds within 1 frame; hit-stop 60ms on death">
- I am judging a complete, elegant, great-feeling piece of work — not a feature list.
  Small and finished beats big and rough.

Output
- Output ONLY the full HTML in one code block. No prose before or after.
```

## 变量

| 变量 | 说明 | 例子 |
|---|---|---|
| `<GENRE>` | 玩法类型，越窄越好 | "lane-based endless runner" / "one-button flap" / "top-down arena shooter" |
| `<LIB>` | 唯一允许的 CDN 库 | `three`（3D）/ 无（2D 用 Canvas 就够） |
| `<CORE_LOOP>` | 核心 1-3 条机制 | "tap to rise, gravity pulls down, gaps scroll" |
| `<FEEL>` | 手感硬指标 | "coyote time 80ms", "screen shake on hit" |

## 翻车点（来自案例的常见 drift）

- **模型加"功能清单"堆料**：加 `<FEEL>` 段的 "not a feature list" 一句，明确评判标准。
- **CDN import map 漏写**：`file://` 打开直接黑屏 —— 要求 "runs by double-clicking" 能兜住。
- **delta-time 丢失**：不同刷新率速度不同，写明 "framerate-independent"。
- **不给 restart**：写死 "press R restarts"，别指望模型自觉。
