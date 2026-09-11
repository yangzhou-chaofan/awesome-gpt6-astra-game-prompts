# P4 · Computer-Use Player 🤖

> **难度 ★★★** · 不让模型做游戏，让它"长手"亲自玩 —— Computer Use 看屏幕、动键鼠通关。这是 GPT-6 Astra 发布期的头条玩法（案例：只看屏幕通关《火红》、语音通关《杀戮尖塔 2》、自己玩游戏自己录屏剪辑）。

## 玩法是什么

给模型屏幕访问权 + 一条目标，它截图→决策→操作→再截图循环。你的工作不是写 prompt 玩法，而是**搭好可观测的执行环境**（模拟器/窗口/录屏），并设定边界（能做什么、绝不能做什么）。

## 前置（比 prompt 更重要）

- 运行环境：模拟器（游戏）、独立浏览器 profile（网页）、或虚拟机（桌面软件）
- 观测：录屏从头开（案例里"自玩自录"是标配）
- 断路器：设置每 N 分钟截图存档，防止死循环烧 token

## Prompt 模板

```text
You are playing <GAME> on the emulator window in front of you. You see screenshots;
you act with mouse and keyboard.

Goal: <GOAL, e.g. "reach the first gym badge">

Rules of engagement
- Act on what you see. If the screen is ambiguous, take one exploratory action,
  then re-observe before committing.
- Menu text is ground truth; do not invent mechanics you have not seen.
- Save state when the game offers it.
- Hard limits: do not open system settings, do not delete saves, do not enter
  payment/online flows. Stop and report if stuck >15 minutes on one screen.

Report: when done (or stuck), write PLAYTHROUGH.md — timeline of key decisions,
what worked, what you'd do differently.
```

## 变量

| 变量 | 说明 |
|---|---|
| `<GAME>` | 目标游戏/软件 |
| `<GOAL>` | 可判定终点的目标（"通关 1 关" > "玩得好"） |

## 翻车点

- **目标不可判定**："玩得好"无法验收，"拿第一个徽章"可以。
- **死循环烧钱**：必须有 stuck-检测与硬限额。
- **权限蔓延**：硬性禁区写进 prompt（系统设置/付费/线上），别靠事后补救。
- **版权内容直播**：自玩自录的剪辑注意游戏画面版权，发布前看平台规则。
