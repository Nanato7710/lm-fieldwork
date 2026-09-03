# Pre-Week Notes

## Data flow

`text -> ? -> token IDs -> ? -> logits -> ? -> next token`

## Tokenization observation

### Prediction

- characters:
- manual word-like proposal:
- local BPE:

### Result

- 3通りのtoken数:
- 予想と違った点:

### 問49から考えたこと

- tokenizerを指定しないとtoken数が一意に決まらない理由:
- token数が増えたときに起こりそうなこと:

## Generation observation

### Prediction

- temperatureを下げたときの最有力候補の確率:
- temperatureを変えたときにlogitsが変わるか:

### Result

- temperatureで変わったもの:
- 変わらなかったもの:
- toy perplexityから分かったこと:

## 用語（各1–2文）

- token:
- logits:
- temperature:
- perplexity:

## まだ分からないこと

-
