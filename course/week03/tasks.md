# Week 3 tasks

先に [Week 3 README](README.md) の「進める順番」を読み、Track A/B を決めてください。
次のコマンドはリポジトリのルートで実行します。

## Core

```bash
uv run python course/week03/starter/modern_block.py
```

`Embedding → [Norm → Attention → residual] → [Norm → MLP → residual] → LM head` の各部品をコード行へ対応付け、RoPE と GQA が Attention 内のどこへ入るか書きます。Track A/B の担当は固定名ではなく2人で選びます。

担当trackを5分で説明し、相手の説明を聞いた後に担当外trackの行を自分の言葉で更新します。
最後に5要素すべてを「位置、置換対象、狙い」で分類します。

## Standard

担当外trackのコードと原論文も自分で指定範囲まで読みます。
KV cacheがtraining lossを改善する技術かどうかも分類します。

## Deep Dive

MoE / MQA / prefill vs decode の1つ。次週の prerequisite ではありません。
