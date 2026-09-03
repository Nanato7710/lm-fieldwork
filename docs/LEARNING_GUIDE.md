# 学習の進め方

[root README](../README.md) はコース全体の案内板です。
この文書では、1週間の中で「いつ、どのファイルを開き、何を記録するか」を説明します。

## 週を始める前の確認

リポジトリのルートで次を実行します。
初回セットアップ後は、依存関係が更新されたときか、環境に問題があるときだけで構いません。

```bash
uv sync
uv run python scripts/check_environment.py
```

次に、現在の週の README を開きます。
たとえば Week 1 なら [`course/week01/README.md`](../course/week01/README.md) です。

各週の README と `tasks.md` には別の役割があります。

- **README**：中心問い、到達目標、読む資料の範囲、成果物、完了条件を確認する。
- **tasks.md**：コマンド、コピー先、変更箇所などの実作業を確認する。
- **work/**：考えたこと、変更したコード、実行結果を書く。

README を確認する前に `tasks.md` のコマンドだけを実行すると、何を観察する実験なのか分からなくなります。

## Core の標準ルート

Core は次の7段階に分けて進めます。
時間は目安であり、理解できた段階で次へ移って構いません。

### 1. 中心問いと到達目標を読む（10分）

その週の README を冒頭から「Learning goals」まで読みます。
この時点では答えを調べ切らず、何を説明できれば完了かを確認します。

### 2. notes に開始時点の理解を書く（10分）

`work/<week>/notes.md` を開きます。
現時点の答えと分からない用語を書き、Prediction の欄があることを確認します。
Prediction は資料を読んだ後、starter を実行する前に書きます。

### 3. 指定範囲だけ読む（40〜70分）

README の「Source links / exact ranges」にある順番で資料を読みます。
全文読破はせず、指定された section、figure、timestamp で止めます。

読みながら notes に次を残します。

- 説明できそうな用語
- 重要だと思った図、式、コードのうち1つ
- 元資料の該当箇所
- まだ分からないこと

英語で止まった場合は、[LLM usage policy](LLM_USAGE.md) の質問例を使って局所的に確認します。

実験がある週は、読み終えた時点の予想を Prediction に書きます。
Prediction は正解を当てるための欄ではなく、結果を見た後の説明と実行前の考えを区別するための欄です。

### 4. starter をそのまま実行する（20〜40分）

`tasks.md` に書かれた最初のコマンドを変更せず実行します。
まず正常な出力を保存し、何を入力して何が出たかを確認します。

エラーが出た場合は、次の4点を記録します。

- 実行したコマンド
- エラーメッセージ
- エラーになったファイルと行
- 期待していた結果

### 5. `work/` で一箇所だけ変える（30〜60分）

変更実験がある週は、starter を `work/<week>/` へコピーします。
`course/` 内の starter は比較元として残します。

変更前に notes の次の欄を埋めます。

- Prediction
- Changed variable
- Fixed conditions
- What is not controlled

一度に複数箇所を変えると、結果の原因を切り分けられません。
`tasks.md` が指定した箇所から始めます。

### 6. 結果と解釈を書く（20〜30分）

出力、loss、shape、生成例など、実際に観測した内容を Result に書きます。
Interpretation では次の二つを分けます。

- この条件と観測から言えること
- この実験だけでは言えないこと

小規模な1 run は一般的な性能差を証明しません。
機種、seed、data、実行時間など、揃えていない条件も残します。

### 7. 完了条件を確認して meeting に進む（10分）

README の「完了の目安」と「Meeting に持ってくるもの」を読み直します。
不足があれば notes に未解決として書き、動かなかったコードもそのまま持参します。

すべてを理解してから meeting に進む必要はありません。
どこまで追えたかと、どこで止まったかを説明できれば診断できます。

## Standard と Deep Dive へ進むタイミング

Core の成果物と未解決点を整理してから Standard へ進みます。
通常の学習時間は Core と Standard を合わせて週5〜8時間です。

Deep Dive は Standard の後に時間が残った場合だけ選びます。
Deep Dive の未実施や未完了は次週への持ち越しにしません。

## Week 1 の具体例

Week 1 は次の順番になります。

1. [Week 1 README](../course/week01/README.md) の中心問いと goals を読む。
2. [`work/week01/notes.md`](../work/week01/notes.md) を開き、分からない用語を書く。
3. 動画と論文の指定範囲を読み、Prediction を書く。
4. [Week 1 tasks](../course/week01/tasks.md) の1つ目のコマンドで shape と mask を確認する。
5. starter を `work/week01/experiment.py` へコピーする。
6. causal mask だけを変更して再実行する。
7. Result と Interpretation を書き、meeting の持参物を確認する。

他の週も同じ順番です。
変わるのは読む資料、starter、記録する観測だけです。

## 途中から再開する方法

学習を中断した後は、次の順番で再開します。

1. `work/<week>/notes.md` の最後に書いた Result と未解決点を読む。
2. `course/<week>/tasks.md` で完了した項目を確認する。
3. 実験コードがある場合は、実行コマンドと Changed variable を確認する。
4. 次の未完了項目を一つだけ進める。

再開時に外部資料を最初から読み直す必要はありません。
notes に元資料の section や timestamp を残しておくと、その箇所から戻れます。

## LLM に現在地を渡す方法

Web 版の LLM に質問する場合は、現在週の README、tasks、notes を自動でまとめられます。

```bash
uv run python scripts/make_context.py --week week02 --clipboard
```

自分の実験コードも渡す場合は `--include` を追加します。

```bash
uv run python scripts/make_context.py \
  --week week02 \
  --include work/week02/experiment.py \
  --clipboard
```

生成された Markdown の末尾に、現在の疑問を一つ書いて質問します。
