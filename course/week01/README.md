# Week 1 — GPTを分解する

> 中心問い: GPT は過去の token から、どうやって次の token を予測する？

## この週で使うファイル

1. この README：中心問い、読む範囲、成果物を確認する。
2. [`work/week01/notes.md`](../../work/week01/notes.md)：実行前の Prediction と実行後の解釈を書く。
3. [`starter/attention_walkthrough.py`](starter/attention_walkthrough.py)：変更前の attention を実行して shape を追う。
4. [tasks.md](tasks.md)：実行、コピー、変更の順番を確認する。
5. `work/week01/experiment.py`：starter をコピーして causal mask の実験を行う。

## 進める順番

1. 「Learning goals」を読み、週末に説明する項目を確認する。
2. notes を開き、現時点の答えと分からない用語を書く。
3. 動画を指定 timestamp の順に見てから論文の指定箇所を読み、causal mask を外したときの Prediction を書く。
4. [tasks.md](tasks.md) の最初のコマンドで、変更前の shape と attention weights を確認する。
5. starter を `work/week01/experiment.py` へコピーし、`--no-causal-mask`を付けてcausal maskだけを外す。
6. 変更前後を比べ、notes の Result と Interpretation を書く。
7. 「完了の目安」と照合し、shape trace と未解決点を meeting に持っていく。

## Learning goals

causal LM、embedding、positional information、Q/K/V、scaled dot-product attention、causal mask、multi-head、FFN/residual/norm、logits から cross entropy までを、部品の位置と tensor shape に結び付けます。

## Source links / exact ranges

- [Karpathy — Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY): 22:11–38:00（Bigram LM / loss / generation）、42:13–1:19:11（context aggregation → self-attention）、1:19:11–1:37:49（multi-head / FFN / residual / LayerNorm）。timestamp は目安で、Core は特に 1:02:57 前後からの self-attention 実装を追う。
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762): Abstract、Figure 1、§3.2、§3.2.1。全文読破は不要。

英語が難しい場合の質問例:

- 「動画 1:02:57–1:06:00 の処理を B,T,C の shape だけに絞って説明してください」
- 「論文 §3.2.1 の式(1)について、原文が述べることと補足説明を分けてください」
- 「causal mask 前後の score 行列を T=4 の例で示してください。課題の結論は先に言わないでください」

## Core（約3時間）

1. 指定範囲を読み、`course/week01/starter/attention_walkthrough.py --show-shapes`を実行してQ/K/Vからoutputまでのshapeを記録する。
2. starter を `work/week01/experiment.py` へコピーする。
3. `work/week01/experiment.py --show-shapes --no-causal-mask`を実行し、causal maskを外したときの変化を予測と比べる。
4. `work/week01/notes.md` に Prediction / Changed variable / Fixed conditions / Result / Interpretation を残す。

## Standard

`B=2, T=4, C=8, n_heads=2`でも`Q @ K^T`と`weights @ V`のshapeを手で書く。余力があればtiny LMのmask on/offを短く比較するが、低いtraining lossをそのまま改善と呼ばない。

## Deep Dive（optional）

scale `1/sqrt(d_k)` を外した score / softmax の変化を toy data で観測する。matplotlib で attention map を表示してもよい。未実施でも次週へ進めます。

## Deliverables

- `work/week01/notes.md`
- `work/week01/experiment.py`

## Meeting に持ってくるもの

shape trace、mask on/off の予測と観測、結果から言えないこと1つ。

## 完了の目安

Q/K/V から output まで shape を追い、causal mask が未来 token の参照を止める理由を説明できれば完了です。

完了後は [Week 2 README](../week02/README.md) へ進みます。
