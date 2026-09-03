# Pre-Week — LLMを外側から見る

> 中心問い: 文章を入力してから次のtokenが選ばれるまで、外から見て何が起きている？

Coreは個人1.5〜2時間とshort meeting、最大2〜3時間を想定します。
Transformerの内部理解はまだ求めません。

## この週で使うファイル

1. このREADMEで、中心問い、読む順番、完了条件を確認する。
2. [`work/preweek/notes.md`](../../work/preweek/notes.md)を開き、記録する項目を確認する。
3. [tasks.md](tasks.md)を開き、Core checklistを上から進める。
4. checklistから[Tokenization primer](tokenization_primer.md)、[Generation primer](generation_primer.md)、[`starter/`](starter/)を順に開く。

`course/`内のprimerとstarterは、読む・実行するための教材です。
コードを変更したり新しいファイルを作ったりする場合は、原則として`work/preweek/`へコピーしてから行います。

## 進める順番

1. 「Learning goals」を読み、notesのdata flowへ最初の予想を書く（5分）。
2. [tasks.md](tasks.md)を開き、以降はchecklistを上から進める。
3. [Tokenization primer](tokenization_primer.md)とHugging Faceの指定範囲を読む（30〜45分）。
4. tokenizationの予想をnotesへ書き、小さな観察で3通りの分け方を比べる（15〜20分）。
5. 言語処理100本ノックの問49を確認演習として読む（15〜20分）。
6. [Generation primer](generation_primer.md)を読み、予想を書いてから固定したlogitsを観察する（20〜25分）。
7. 言語処理100本ノックの問90、91、93を確認演習として読む（20〜30分）。
8. notesのdata flow、4語の説明、未解決の疑問を完成させる（15〜20分）。
9. 「完了の目安」と照合し、meetingの持参物を揃える。

言語処理100本ノックは、この週の概念を初めて説明する教材ではなく、導入後に理解を確かめる問題集として使います。
外部モデルのdownloadやAPI実行をしなくてもCoreは完了できます。

## Learning goals

- tokenとwordが同一とは限らないと説明する。
- model outputは文章ではなく、まずlogitsだと説明する。
- next-token predictionとautoregressive generationを区別する。
- temperatureはweightsや知識を変えないと説明する。
- perplexityの高低を同じ評価条件の範囲で説明する。

## Source links / exact ranges

- [Hugging Face LLM Course 日本語版「トークナイザー」](https://huggingface.co/learn/llm-course/ja/chapter2/4): はじめに、単語ベース、文字ベース、サブワード、エンコーディング、デコーディングを読む。
- [言語処理100本ノック 2025 第5章](https://nlp100.github.io/2025/ja/ch05.html): 問49「トークン化」を、tokenizerを指定しないとtoken数が一意に決まらないことの確認に使う。
- [同 第10章](https://nlp100.github.io/2025/ja/ch10.html): 問90「次単語予測」、91「続きのテキストの予測」、93「パープレキシティ」を、primerで見たdata flowと用語の確認に使う。

100本ノックの実行例を再現することはCoreの条件ではありません。
問題文と、直前に実行したローカルstarterの出力を読み、入力、処理、出力を自分で対応付けます。

## Core

1. 3通りのtoken数を予想してから、`uv run python course/preweek/starter/tokenization_observation.py`を実行する。
2. 予想と観察結果を比べ、問49への回答とともにnotesへ書く。
3. temperatureを変えたときの確率分布を予想してから、`uv run python course/preweek/starter/generation_observation.py`を実行する。
4. 予想と観察結果を比べ、temperatureで変わったものと変わらなかったものをnotesへ書く。
5. 問90、91、93を読み、`text -> ? -> token IDs -> ? -> logits -> ? -> next token`の`?`を埋める。
6. `work/preweek/notes.md`にtoken、logits、temperature、perplexityを各1〜2文で説明する。
7. まだ分からないことを最低1つ書く。

## Standard

利用可能なローカルモデルや講師のデモがあれば、同じpromptでtemperatureを複数値に変えます。
変更前に予想し、出力の変化と変わらないものを書きます。
モデルのdownloadは必須ではありません。

## Deep Dive（optional）

同じ短文を、利用可能な2種類のpretrained tokenizerで比較します。
token数と先頭20 tokensを記録し、分割が異なる理由を考えます。
未実施でもWeek 1へ進めます。

## Deliverables

- `work/preweek/notes.md`
- StandardまたはDeep Diveを行った場合のみ、`work/preweek/`内の短い観測記録

## Meetingに持ってくるもの

完成させたdata flow、4語の説明、tokenizationで気づいた違い、分からないこと1つ。

## 完了の目安

5つのlearning goalsを自分の言葉で短く話せ、data flowの各矢印を指せれば完了です。

完了後は[Week 1 README](../week01/README.md)へ進みます。
