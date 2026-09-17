---
id: astra-post-2094182215894831283
title: "Ultra-High-Speed Sprint Control MP4"
author: "Kashiko_AIart"
author_url: "https://x.com/Kashiko_AIart"
original_post: "https://x.com/Kashiko_AIart/status/2094182215894831283"
posted_on: "2026-09"
media_type: image
media_url: "None"
live_demo: ""
source_list: "unknown"
source_list_url: "https://github.com/unknown"
source_license: MIT
tags: [gpt-6-astra, unknown]
---

# Ultra-High-Speed Sprint Control MP4

**[Kashiko_AIart](https://x.com/Kashiko_AIart)** · [original post ↗](https://x.com/Kashiko_AIart/status/2094182215894831283)

## Prompt

```text
Remotionで超高速疾走モーションコンテを作ってください。フレーム単位で実際に動く3Dドローン追従型のcontrol MP4を出力。
固定された一つの3Dワールドとして構築し、床グリッド、左右の壁線、一定間隔のゲート、空間中の光跡を配置する。背景をループさせるのではなく、十分に長い一本道を実際に前進させる。
キャラクターは疾走するキャラクターをやや斜め後ろから追従する。
人物とグリッドは必ず同じ3D座標系とカメラ投影を使用してください。2D素材を拡大縮小するだけの疑似カメラにはしないでください。

【人物proxy】
全員、次の2要素だけで表現する。
1. 円形の頭
2. 傾きや回転が可能な一本の縦長胴体

【疾走速度】
見かけだけの速度表現ではなく、root座標を毎フレーム実際に前進させる。

【敵と接触frame】
敵は接触frameを決定してコース上へ固定配置する。
キャラクターは流れるような体術で3体を進行軸の外へ弾き、そのまま走り抜ける。
カメラは接触の前後だけ、短いイージングで別アングルへ移行し、接触後は必ず後方追従へ戻す。

【クリーンcontrol画面】
映像内には人物proxy、空間、接触アクセントだけを表示する。
```

## Provenance

- Original post: https://x.com/Kashiko_AIart/status/2094182215894831283
- Upstream list: [unknown](https://github.com/unknown) (MIT)

_Prompt text and preview collected from the public community post; all rights remain with the original author._
