# Generation primer

このページは、言語処理100本ノックの問90、91、93を読む前の10〜15分の足場です。
Transformer内部の計算ではなく、token IDsを受け取った後の入出力だけを追います。

## 次のtokenを一つ予測する

モデルは入力されたtoken列に対して、次に来る各候補の **logit** を出します。
logitは正規化前の点数なので、そのままでは確率ではありません。
softmaxを通すと、候補全体で合計1になる確率分布へ変わります。

```text
token IDs
  ↓ model
logits
  ↓ temperatureを反映してsoftmax
probabilities
  ↓ 一つ選ぶ
next token
```

## 一つずつ繰り返して文章にする

一回の予測で得られるのは、基本的に次のtoken一つです。
選んだtokenを入力列の末尾へ足し、もう一度予測する処理を繰り返すと文章になります。
この繰り返しをautoregressive generationと呼びます。

temperatureは、同じlogitsから作る確率分布の尖り方を変えます。
temperatureを変えても、モデルのweightsや学習済み知識そのものは変わりません。

perplexityは、正解として観測したtoken列をモデルがどれくらい予測しやすかったかを見る値です。
同じ評価条件なら、低い方がその列へ高い確率を割り当てたと解釈できます。
ただし、異なるtokenizerや異なるデータで得た値を単純に比較したり、会話品質全体と同一視したりはできません。

## 読み終えたら

次の問いへの予想を書いてから、`starter/generation_observation.py` を実行します。

1. temperatureを低くすると、最有力候補の確率はどうなるか。
2. temperatureを変えると、logits自体は変わるか。
3. 一つの正解tokenへ低い確率しか与えない状態が続くと、perplexityはどうなるか。
