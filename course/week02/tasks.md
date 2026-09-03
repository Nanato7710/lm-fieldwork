# Week 2 tasks

先に [Week 2 README](README.md) の「進める順番」まで読み、[`work/week02/notes.md`](../../work/week02/notes.md) に Hypothesis を書いてください。
次のコマンドはリポジトリのルートで実行します。

## Core

```bash
uv run python course/week02/starter/tokenizer_comparison.py
uv run python course/week02/starter/train_minilm.py --steps 20 --context-length 64
cp course/week02/starter/train_minilm.py work/week02/experiment.py
```

比較前に次を notes に書きます: Hypothesis / Changed variable / Fixed conditions / What is not controlled / Metrics。1 run ごとに train loss、validation loss、tokens seen、sample を記録します。

## Standard

一変数だけ変えた2 run を行います。同じ step 数でも context length が違えば tokens seen が変わり得るため、実際の値を確認してください。

## Deep Dive

BPE vocab size を変えます。tokenizer、sequence length、model parameter 数の複数が動く場合、それを「一変数」と呼べるか検討してください。
