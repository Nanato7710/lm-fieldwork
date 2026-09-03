# Week 1 tasks

先に [Week 1 README](README.md) の「進める順番」まで読み、[`work/week01/notes.md`](../../work/week01/notes.md) に Prediction を書いてください。
次のコマンドはリポジトリのルートで実行します。

## Core

```bash
uv run python course/week01/starter/attention_walkthrough.py --show-shapes
cp course/week01/starter/attention_walkthrough.py work/week01/experiment.py
```

コピー側で `causal=True` を `False` に変えます。先に notes を書き、同じ seed/input/projection を固定してください。観測は「未来情報が見えるか」と shape に絞ります。

## Standard

`B=2, T=4, C=8, n_heads=2` で各 tensor shape を紙か notes に書き、head ごとの `d_k` を示してください。

## Deep Dive

scale だけを一変数として外します。softmax の尖り方を比較しますが、1回の random input から一般的性能を結論しません。
