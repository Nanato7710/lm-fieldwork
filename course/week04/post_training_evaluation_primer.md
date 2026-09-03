# Post-training and evaluation primer

このページでは、論文を読む前にpost-trainingとevaluationの用語を配置します。
各手法の導出や実装は扱いません。

## Base modelからchat modelまで

pre-trainingでは、大量のtoken列から次のtokenを予測することで**base model**を作ります。
base modelは文章の続きを生成できますが、利用者の指示へ望ましい形式で答えるように調整済みとは限りません。

**SFT**（Supervised Fine-Tuning）では、promptと望ましいresponseの組を使ってweightsを更新します。
SFT後のモデルは、指示に従う応答形式を学んだ**instruct model**の候補になります。

複数のresponseを比較したデータを**preference data**と呼びます。
preference dataの使い方には、chosen/rejectedの組を使って明示的なreward modelなしで学ぶDPOと、reward modelを介して方策を更新するRLHF/RLなどがあります。
DPOとRLHF/RLは別の経路であり、すべてのモデルが両方を順番に行うわけではありません。

```text
text corpus
  ↓ next-token pre-training
base model
  ↓ promptと望ましいresponseによるSFT
instruct model
  ├─ chosen/rejectedの組を使うDPO
  └─ preference dataからreward modelを作り、RLHF/RLで更新
```

chat templateは、messagesをモデルが学習時に見た形式へ直す入力処理です。
chat templateの適用だけではweightsは変わりません。

## 論文の評価を読むための用語

- **metric**：結果を数値にする計算規則。
- **benchmark**：複数の手法を共通条件で比べるための課題やデータの集合。
- **baseline**：提案手法と比較する基準。
- **ablation**：構成要素を除くか変えて、その要素と結果の関係を調べる比較。
- **contamination**：評価問題や近い内容が学習データへ含まれ、未知データへの能力だけを測れなくなる状態。
- **human evaluation**：人が基準に沿って出力を評価する方法。
- **LLM-as-a-Judge**：別のLLMに出力を評価させる方法。
- **statistical uncertainty**：標本、乱数、評価者などが変わると結果も動くという不確実性。

一つのmetricやbenchmarkで高い値を得ても、利用場面全体の品質を保証したことにはなりません。
human evaluationとLLM-as-a-Judgeにも、評価基準、順序、好み、再現性を確認する必要があります。

## Paper notesへ書くこと

まず、SFT、DPO、RLHF/RL、chat templateについて、使うデータ、weightsを更新するか、目的を表にします。
その後、指定論文の主要claimに対して、metric、benchmark、baseline、ablation、contamination対策、評価者、不確実性の記載場所を確認します。
論文に記載がない項目は推測で埋めず、「記載を確認できない」と残します。
