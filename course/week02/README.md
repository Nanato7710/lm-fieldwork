# Week 2 — Tokenizer / Data / Pre-training

> 中心問い: 同じ Transformer でも、何をどう学習させるかで結果が変わるのはなぜ？

## この週で使うファイル

1. この README：読む範囲、比較実験、完了条件を確認する。
2. [`work/week02/notes.md`](../../work/week02/notes.md)：Hypothesis、条件、結果、解釈を書く。
3. [`starter/tokenizer_comparison.py`](starter/tokenizer_comparison.py)：character tokenizer と local BPE を比較する。
4. [`starter/train_minilm.py`](starter/train_minilm.py)：Mini LM を短時間学習する。
5. [tasks.md](tasks.md)：実行コマンドと実験コードのコピー先を確認する。
6. `work/week02/experiment.py`：一つの設定を変えたとき、連動して変わる条件を整理する。

## 進める順番

1. 「Learning goals」を読み、tokenizer、data、training の三つに項目を分ける。
2. notes を開き、現時点の答えと分からない用語を書く。
3. Hugging Face LLM Course の tokenizer 範囲を読み、tokenizer comparison を実行する。
4. causal LMの指定範囲を読み、context lengthを32から128へ変えたときに直接変わる値と、連動して変わる条件のHypothesisを書く。
5. [tasks.md](tasks.md) に従って starter を `work/week02/experiment.py` へコピーする。
6. context length以外のCLI引数を固定して2 runを行い、固定できていない初期値、sample位置、tokens seenもnotesに記録する。
7. 「完了の目安」と照合し、比較表と未統制条件を meeting に持っていく。

## Learning goals

character / word / subword、BPE、vocabulary sizeとsequence length、embedding/LM head parameters、next-token pre-training、context length、batch、training tokens、train/validation loss、packing、data quality、duplicate、contamination、比較で変わる条件の切り分けを説明します。

## Source links / exact ranges

- [HF LLM Course Chapter 6](https://huggingface.co/learn/llm-course/chapter6/1): Introduction、Byte-Pair Encoding tokenization、Building a tokenizer block by block。各ページの冒頭説明と最初の具体例に限定し、全文読破不要。
- [Training a causal LM from scratch](https://huggingface.co/learn/llm-course/chapter7/6): “Preparing the dataset” と “Initializing a new model” から training loop までの見出し・図・主要コード。大規模 dataset の download/実行はしない。

## Core（約3時間）

1. `tokenizer_comparison.py` で original Japanese corpus の char tokenizer とローカル BPE を比較する。
2. `train_minilm.py`を`work/week02/experiment.py`へコピーする。
3. context lengthを32と128にして、同じseed、width、layers、steps、batch size、dataで2 run比較する。
4. context lengthに伴ってtokens seen、position embeddingのparameter数、共通parameterの初期値、sample位置も変わり得ることを結果へ記録する。
5. trainとvalidationが元テキストの別範囲から作られていることを確認し、`work/week02/notes.md`に未統制条件を書く。

この2 runは、CLIで変更する設定をcontext lengthだけに絞った観察です。
context lengthの因果効果だけを分離した比較ではありません。

## Standard

Coreと同じcontext length比較を100 stepsへ延長し、20 stepsの結果と傾向が同じか確認する。
runを長くしても、初期値、sample位置、tokens seenなどの違いは解消しないことを記録する。
wall-clockは機種依存の参考値として扱う。

## Deep Dive（optional）

vocab size を変え、token count と embedding / LM head parameter 数が同時に変わるため単純な優劣比較にならない点を整理する。未実施でも次週へ進めます。

## Deliverables

- `work/week02/notes.md`
- `work/week02/experiment.py`（starter のコピーまたは自作の短い比較）

## Meeting に持ってくるもの

tokenizer 比較表、2 run の条件表、loss/tokens seen、generation sample、言えること/言えないこと。

## 完了の目安

pre-trainingをnext-token objectiveの反復として説明し、比較で直接変更した設定、連動して変わった条件、固定できていない条件を指せれば完了です。

完了後は [Week 3 README](../week03/README.md) へ進みます。
