# Week 3 — Modern LLM architecture

> 中心問い: なぜ最近の LLM は GPT-2 の構成をそのまま使わず、部品を変更している？

## この週で使うファイル

1. この README：5要素の範囲、Track A/B、読む論文を確認する。
2. [`work/week03/notes.md`](../../work/week03/notes.md)：architecture mapping と担当 track の説明を書く。
3. [`starter/modern_block.py`](starter/modern_block.py)：Llama-like block を実行し、class と tensor shape を追う。
4. [tasks.md](tasks.md)：対応表の作り方と担当外 track の扱いを確認する。

## 進める順番

1. 「Learning goals」と Scope を読み、Core が5要素だけであることを確認する。
2. 2人で Track A または Track B の担当を決める。
3. modern block を変更せず実行し、notes の5行へ class/function を対応付ける。
4. 担当 track の原論文だけを指定範囲まで読む。
5. notes に「位置、置換対象、狙い、training/inference の分類」を書く。
6. 5分の相互説明を行い、担当外 track の行を更新する。
7. 「完了の目安」と照合し、対応表と質問1つを meeting に持っていく。

## Learning goals

RoPE / RMSNorm / SwiGLU / GQA / KV cache について、block のどこにあるか、何を置き換えるか、狙い、training 構造か inference optimization かを分類します。FlashAttention は know-only、MoE は Deep Dive です。

## Source links / exact ranges

原論文は全文読破不要です。

- [RoFormer](https://arxiv.org/abs/2104.09864): Abstract、§3.2.2。
- [RMSNorm](https://arxiv.org/abs/1910.07467): Abstract、§3 “RMSNorm”。
- [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202): Abstract、§2 の GLU variants。
- [GQA](https://arxiv.org/abs/2305.13245): Abstract、Figure 1、§2。
- [FlashAttention](https://arxiv.org/abs/2205.14135): Abstract、Figure 1のみ。近似ではなく exact attention を IO-aware に計算する高速・省メモリ化として読む。

## Core（約3時間）

1. `modern_block.py` を実行し、diagram の各箱を class/function に対応させる。
2. Track A（RoPE + RMSNorm）または Track B（SwiGLU + GQA/KV cache）を選び、担当資料を読む。
3. 相手に5分で説明する準備をする。meeting 後は全 Core 用語を位置と狙いのレベルで共有する。

## Standard

担当外trackもcodeと原論文の指定範囲を追い、対応表を完成させる。
starterが表示するのは、`cached_tokens`を1ずつ増やしたときのK/V cacheの概念的なshapeです。
K/V tensorの保存、追記、再利用を実装したcache動作の検証ではありません。

## Deep Dive（optional）

MoE、MQA、prefill vs decode のどれかを調べる。Optional experiment として LayerNorm ↔ RMSNorm または GELU MLP ↔ SwiGLU を比較してよいが、小規模 run から一般的優劣を断定しない。未実施でも次週へ進めます。

## Deliverables

- `work/week03/notes.md` の architecture 対応表と担当 track の説明
- Optional experiment をした場合のみコード

## Meeting に持ってくるもの

5分説明、対応表、担当外で聞きたい質問1つ。

## 完了の目安

5要素すべてを「位置・置換対象・狙い」で短く分類でき、FlashAttention を近似手法と誤認しなければ完了です。

完了後は [Week 4 README](../week04/README.md) へ進みます。
