# Week 4 tasks

先に[Week 4 README](README.md)の「進める順番」を読み、講師から指定された論文を確認してください。
記録と新規ファイルは、原則として[`work/week04/`](../../work/week04/)に置きます。

## Core

- [ ] [Post-training and evaluation primer](post_training_evaluation_primer.md)を読む
- [ ] SFT、DPO、RLHF/RL、chat templateを、使うデータ、weights更新の有無、目的で分類する
- [ ] 8つの評価用語について、指定論文内で確認する場所をnotesへ用意する
- [ ] [Chat template primer](chat_template_primer.md)を読む
- [ ] 2回のuser入力を含むmessagesへtoy templateを適用し、直列化後の文字列を予想する
- [ ] `uv run python course/week04/starter/chat_template_observation.py`を実行し、予想と出力を比べる
- [ ] [言語処理100本ノックの問94、95](https://nlp100.github.io/2025/ja/ch10.html)を確認演習として読み、primerの流れと対応付ける
- [ ] 2人で同じ論文をREADMEの順に読む
- [ ] paper notesの10項目に、該当section、figure、tableを添える
- [ ] 主要claim、baseline、最重要ablationを対応付ける
- [ ] 15〜20分、3〜5枚程度の共同発表を準備する

最初から論文全文を精読する必要はありません。

## Standard

別のclaimを一つ選び、compute/data budget、contamination、評価者、統計的不確実性まで確認します。

## Deep Dive

問98、99またはDPO/RLHFの原論文で、学習に使う入力、教師信号、出力を追います。
PPO/DPOの実装は不要です。
