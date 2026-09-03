# Pre-Week tasks

先に[Pre-Week README](README.md)の「進める順番」まで読んでください。
記録と変更は、原則として[`work/preweek/`](../../work/preweek/)で行います。

## Core checklist

- [ ] notesのdata flowへ、現時点の予想を書く
- [ ] [Tokenization primer](tokenization_primer.md)を読む
- [ ] [Hugging Faceのトークナイザー解説](https://huggingface.co/learn/llm-course/ja/chapter2/4)の指定した6節を読む
- [ ] 3通りのtoken数と分け方をnotesへ予想として書く
- [ ] `uv run python course/preweek/starter/tokenization_observation.py`を実行する
- [ ] 3通りのtoken数と、予想と違った点をnotesへ記録する
- [ ] [言語処理100本ノックの問49](https://nlp100.github.io/2025/ja/ch05.html)を確認演習として読み、分割の違いについて2点を書く
- [ ] [Generation primer](generation_primer.md)を読む
- [ ] temperatureを下げたときの最有力候補の確率と、logitsが変わるかをnotesへ予想として書く
- [ ] `uv run python course/preweek/starter/generation_observation.py`を実行する
- [ ] temperatureで変わったものと変わらなかったものをnotesへ記録する
- [ ] [言語処理100本ノックの問90、91、93](https://nlp100.github.io/2025/ja/ch10.html)を確認演習として読む
- [ ] data flowの空欄と4語の説明を完成させる
- [ ] 未解決の疑問を書く

答えを探すときは、まずどの矢印が分からないかを絞り、LLMにはその局所だけを質問してください。

## Standard / Deep Dive

Standardはtemperature比較です。
Deep Diveは2種類のpretrained tokenizerの比較です。
どちらもCoreの完了条件ではありません。
