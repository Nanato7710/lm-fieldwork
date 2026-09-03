# Week 4 — Post-training / Evaluation / Paper reading

> 中心問い: LLM論文は何を主張し、その主張をどんな証拠で支えている？

## この週で使うファイル

1. このREADMEで、post-training、evaluation、論文読解の範囲を確認する。
2. [`work/week04/paper_notes.md`](../../work/week04/paper_notes.md)を開き、記録する10項目を確認する。
3. [tasks.md](tasks.md)を開き、Core checklistを上から進める。
4. checklistから[Chat template primer](chat_template_primer.md)と、講師が指定した1本の論文を開く。

`course/`内の教材は直接編集しません。
新しいメモや補助コードを作る場合は、原則として`work/week04/`に置きます。

## 進める順番

1. 「Learning goals」を読み、post-trainingとevaluationの用語を分ける。
2. paper notesを開き、最初の予想と未解決語を書く。
3. [tasks.md](tasks.md)を開き、以降はchecklistを上から進める。
4. [Chat template primer](chat_template_primer.md)を読み、messagesからtoken IDsまでを手作業で追う。
5. 言語処理100本ノックの問94、95を確認演習として読み、chat templateの入力と出力を確認する。
6. 講師指定論文のAbstract、Introduction、figures/tables overviewを2人とも読む。
7. 2人で主要claimと重要なtableを一つずつ決める。
8. Method、Main Results、Ablation、Limitationsの必要箇所へ進む。
9. paper notesを分担した場合も、最後に2人で内容を照合する。
10. 「完了の目安」と照合し、共同発表と未解決語をfinal meetingへ持っていく。

言語処理100本ノックは、chat templateを初めて説明する教材ではなく、primer後の確認問題として使います。

## Learning goals

baseとinstruct/chat、chat template、SFT、preference data、DPO、RLHF/RLの位置付けを区別します。
metric、benchmark、baseline、ablation、contamination、human evaluation、LLM-as-a-Judgeの注意点を使い、claimとevidenceを分けます。

## Source links / exact ranges

- [言語処理100本ノック 2025 第10章](https://nlp100.github.io/2025/ja/ch10.html): 問94「チャットテンプレート」、95「マルチターン」を、primerで見たdata flowの確認に使う。
- 講師がWeek 3終了までに指定する同一論文: Abstract → Introduction → figures/tables overview → Method → Main Results → Ablation → Limitationsの順で読む。

100本ノックの問98、99はOptionalです。
SFTやpreference dataの位置付けを確認した後に読み、導入教材としては使いません。
主要claimとtableは原文を確認し、LLMには指定sectionの翻訳や局所解説を依頼して構いません。

## Core（約3時間）

1. primerのdata flowを手作業で追ってから、問94、95でchat templateとmulti-turn promptの役割を確認する。
2. 2人で同じ論文を読み、`work/week04/paper_notes.md`のProblem、Method、Evidence、What is not establishedを埋める。
3. baselineと最重要ablationを1つずつ選び、claimを本当に支えるか議論する。

## Standard

compute/data budget、contamination、human evaluationまたはLLM-as-a-Judge、統計的不確実性を確認し、uncontrolledな点をnotesに追加します。
2人共同で15〜20分、3〜5枚程度の簡易資料を作ります。
形式は問いません。

## Deep Dive（optional）

問98、99またはDPO/RLHFの原論文へ進み、学習に使う入力、教師信号、出力の関係だけを追います。
導出や実装は不要で、未実施でも修了できます。

## Deliverables

- `work/week04/paper_notes.md`
- 共同発表（3〜5枚を推奨し、見栄えは評価しない）

## Meetingに持ってくるもの

Problem、Method、Evidence、interpretation、next experiment、未解決語、原文の主要表。

## 完了の目安

論文のclaimとevidenceを対応付け、この結果だけでは言えないこと、最小の次実験を説明できれば完了です。

これで本編は完了です。
継続する場合だけ[`extensions/README.md`](../../extensions/README.md)を確認します。
