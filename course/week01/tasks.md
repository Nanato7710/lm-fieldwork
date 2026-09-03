# Week 1 tasks

先に [Week 1 README](README.md) の「進める順番」まで読み、[`work/week01/notes.md`](../../work/week01/notes.md) に Prediction を書いてください。
次のコマンドはリポジトリのルートで実行します。

## Core

```bash
uv run python course/week01/starter/attention_walkthrough.py --show-shapes
cp course/week01/starter/attention_walkthrough.py work/week01/experiment.py
uv run python work/week01/experiment.py --show-shapes --no-causal-mask
```

最後のコマンドは、コピー側の`--no-causal-mask`オプションでcausal maskだけを外します。
先にnotesを書き、同じseed、input、projectionを固定してください。
Q/K/V、scores、weights、headごとの出力、結合後のoutputまでのshapeと、未来位置のweightを変更前後で比べます。

## Standard

`B=2, T=4, C=8, n_heads=2` で各 tensor shape を紙か notes に書き、head ごとの `d_k` を示してください。

## Deep Dive

scale だけを一変数として外します。softmax の尖り方を比較しますが、1回の random input から一般的性能を結論しません。
