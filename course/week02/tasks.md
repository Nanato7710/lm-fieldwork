# Week 2 tasks

先に [Week 2 README](README.md) の「進める順番」まで読み、[`work/week02/notes.md`](../../work/week02/notes.md) に Hypothesis を書いてください。
次のコマンドはリポジトリのルートで実行します。

## Core

```bash
uv run python course/week02/starter/tokenizer_comparison.py
cp course/week02/starter/train_minilm.py work/week02/experiment.py
uv run python work/week02/experiment.py --steps 20 --context-length 32
uv run python work/week02/experiment.py --steps 20 --context-length 128
```

実行前にHypothesis、Changed setting、Fixed CLI arguments、What is not controlled、Metricsをnotesへ書きます。
実行後は各runのtrain loss、validation loss、tokens seen、sampleを記録します。
同じstep数でもcontext lengthが違えば、tokens seen、position embeddingのparameter数、共通parameterの初期値、sample位置が変わり得ます。
実際の値と未統制条件を比較に含め、loss差をcontext lengthだけの効果とは解釈しません。
starterは元テキストを分けてから各範囲を反復するため、trainとvalidationの由来も記録します。

## Standard

Coreと同じ2条件を`--steps 100`で再実行し、短いrunだけで見えた傾向が保たれるか確認します。
100 stepsへの延長では解消しない未統制条件も書きます。

## Deep Dive

BPE vocab size を変えます。tokenizer、sequence length、model parameter 数の複数が動く場合、それを「一変数」と呼べるか検討してください。
