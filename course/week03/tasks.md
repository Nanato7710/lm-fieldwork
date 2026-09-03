# Week 3 tasks

先に [Week 3 README](README.md) の「進める順番」を読み、Track A/B を決めてください。
次のコマンドはリポジトリのルートで実行します。

## Core

```bash
uv run python course/week03/starter/modern_block.py
```

`Embedding → [Norm → Attention → residual] → [Norm → MLP → residual] → LM head` の各部品をコード行へ対応付け、RoPE と GQA が Attention 内のどこへ入るか書きます。Track A/B の担当は固定名ではなく2人で選びます。

## Standard

担当外 track の説明を聞いた後、自分の言葉で対応表を更新します。KV cache が training loss を改善する技術かどうかも分類します。

## Deep Dive

MoE / MQA / prefill vs decode の1つ。次週の prerequisite ではありません。
