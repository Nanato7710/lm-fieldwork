# Classical NLP reverse-reference map

現代 LLM の疑問から必要な背景へ戻るための短い地図です。本編の前提となる長い歴史学習ではありません。

| 今の疑問 | 戻って見る概念 | 接続 |
|---|---|---|
| token をどう数値化する？ | BoW / TF-IDF | 語彙ごとの sparse な固定長表現。順序を直接持たない |
| embedding は何を表す？ | Word2Vec | 学習された dense な分散表現という入口 |
| Attention は何を変えた？ | RNN | token を順に処理する系列モデルと長距離依存の難しさ |
| Q/K/V はどこから来た？ | Seq2Seq + Attention | encoder の情報を重み付きで参照する発想 |
| Transformer の違いは？ | Self-Attention | recurrence を主役にせず token 間を直接関連付ける |

必要になった行だけ調べ、現代のコード・論文へ戻ってください。
