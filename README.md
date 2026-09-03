# LM Fieldwork

**Read. Trace. Test. Explain. / 読む・追う・試す・説明する。**

LM Fieldwork は、Python と PyTorch の基礎がある NLP 初学者向けの短期コースです。
1週間の Pre-Week と4週間の本編を通して、LLM の資料、コード、小実験を自力で追う練習をします。

初めて開いた場合は、この README の「初回セットアップ」から順に進めてください。
学習を再開する場合は、「コースの順番」から現在の週を選んでください。

## 初回セットアップ

### 1. 前提ツールを確認する

初回だけ、GitHubアカウント、Git、uvを準備します。
Python 3.12はuvで導入するため、システムのPythonを入れ替える必要はありません。

```bash
git --version
uv --version
```

Gitが見つからない場合は、[GitHubのGitセットアップ案内](https://docs.github.com/en/get-started/git-basics/set-up-git)に従います。
macOSでHomebrewを利用している場合は、`brew install uv`でuvを導入できます。
それ以外の導入方法は[uv公式のインストール手順](https://docs.astral.sh/uv/getting-started/installation/)で確認します。

### 2. forkをcloneする

まだ clone していない場合は、先に [fork workflow](docs/FORK_WORKFLOW.md) に従います。
すでにこのリポジトリを開いている場合は、次へ進みます。

### 3. 実行環境を確認する

リポジトリのルート（このREADMEがある場所）で、Python 3.12と依存関係を準備してから環境を確認します。

```bash
uv python install 3.12
uv sync
uv run python scripts/check_environment.py
uv run pytest -q
```

`Environment looks ready.` と表示され、test が通れば準備完了です。
MPS や CUDA が利用できない場合でも、`Selected device: cpu` と表示されれば Core と Standard は進められます。

環境確認で止まった場合は、エラーメッセージを省略せず講師か LLM に共有してください。

### 4. Pre-Weekを開始する

次の順番でファイルを開きます。

1. [Pre-Week README](course/preweek/README.md) で中心問い、到達目標、読む資料を確認する。
2. [Pre-Week notes](work/preweek/notes.md) を開き、記録する項目を確認する。
3. [Pre-Week tasks](course/preweek/tasks.md) を上から実行する。
4. Pre-Week notes に自分の説明と疑問を書く。
5. Pre-Week README の「完了の目安」を確認して meeting に進む。

最初から `src/` や `tests/` をすべて読む必要はありません。
各週の README が参照したファイルだけを開きます。

## ファイルの役割

| 場所 | 役割 | 学習者がすること |
|---|---|---|
| `course/<week>/README.md` | その週の入口 | 最初に読む。範囲、資料、完了条件を確認する |
| `course/<week>/tasks.md` | 作業手順 | README の次に開き、コマンドや課題を順に行う |
| `course/<week>/starter/` | 読む、実行するための見本 | 直接改変せず、変更するときは `work/` へコピーする |
| `work/<week>/` | 学習記録と実験 | notes、予測、変更コード、結果を保存して commit する |
| `docs/` | 全週共通の案内 | 必要になったときに参照する |
| `src/lm_fieldwork/` | starter が使う最小実装 | 各週から指定された class や function だけ追う |
| `scripts/` | 環境確認と LLM 用 context 生成 | README にあるコマンドから実行する |
| `tests/` | 実装の最低限の動作確認 | 通常は読む必要はない。挙動を確かめたいときに参照する |

`course/` は読む場所、`work/` は書く場所と覚えると迷いにくくなります。

> [!IMPORTANT]
> 学習中に新しいファイルを作る場合や既存ファイルを編集する場合は、原則として現在の週の `work/<week>/` に収めます。
> `course/` は upstream が管理する教材なので、直接編集せず、実験したい starter を `work/` へコピーしてください。
> `course/` を変更するのは、教材自体の修正を講師から明示的に依頼された場合だけです。

## 毎週の進め方

Pre-Week 以外の週も、次の順番で進めます。

1. その週の `README.md` を「Source links / exact ranges」まで読む。
2. `work/<week>/notes.md` を開き、現時点の答えと分からないことを書く。
3. README に指定された外部資料の範囲だけを読む。
4. 実験がある週は Prediction を書いてから、`tasks.md` の Core を上から行う。
5. starter を変更する場合は `work/<week>/` へコピーしてから編集する。
6. notes に Result と Interpretation を書き、「完了の目安」と照合する。
7. notes、実験コード、分からないことを meeting に持っていく。
8. 時間があれば Standard、さらに余裕がある場合だけ Deep Dive へ進む。

途中で止まった場合も、動かなかったコードと未解決の疑問を残せば meeting に進めます。
Deep Dive は次週へ進む条件ではありません。

詳しい時間配分と記録の書き分けは [学習の進め方](docs/LEARNING_GUIDE.md) にあります。

## コースの順番

| 順番 | 入口 | 主な作業 | 記録先 |
|---|---|---|---|
| 0 | [Pre-Week](course/preweek/README.md) | 短い導入と観察の後、確認演習でtokenから次tokenまでを追う | [`work/preweek/notes.md`](work/preweek/notes.md) |
| 1 | [Week 1](course/week01/README.md) | attention の shape を追い、causal mask を外す | [`work/week01/`](work/week01/) |
| 2 | [Week 2](course/week02/README.md) | tokenizer と Mini LM を動かし、一つの設定変更に伴う条件の変化を整理する | [`work/week02/`](work/week02/) |
| 3 | [Week 3](course/week03/README.md) | 現代 LLM の5部品をコードと論文で対応付ける | [`work/week03/`](work/week03/) |
| 4 | [Week 4](course/week04/README.md) | 2人で同じ論文を読み、claim と evidence を分ける | [`work/week04/`](work/week04/) |

週の途中から再開するときは、該当する `work/<week>/notes.md` を先に開きます。
最後に書いた Result、Interpretation、未解決の疑問を確認してから、同じ週の `tasks.md` に戻ります。

## Core、Standard、Deep Dive の選び方

- **Core**：忙しい週の必須ルートです。
  ミーティング込みで約3時間を想定します。
- **Standard**：通常のルートです。
  Core と合わせて週5〜8時間を想定します。
- **Deep Dive**：興味と時間がある場合だけ行います。
  未実施でも次週へ進みます。

時間が足りない場合は Core の「完了の目安」を優先します。
Standard や Deep Dive を途中まで行うより、Prediction、Result、Interpretation を Core の notes に残します。

## LLM に質問するとき

翻訳、指定 section の説明、tensor shape の確認、デバッグには LLM を利用できます。
重要な主張は元資料でも確認します。

Web 版の ChatGPT や Claude に現在の週と notes を渡す場合は、次を実行します。

```bash
uv run python scripts/make_context.py --week week01 --clipboard
```

`week01` は現在の週に置き換えます。
利用ルールと質問例は [LLM usage policy](docs/LLM_USAGE.md) にあります。

## fork と upstream の更新

`course/`, `docs/`, `src/`, `scripts/` は upstream が管理します。
学習者は `work/` に notes と実験コードを保存します。

更新の取り込みと commit の手順は [fork workflow](docs/FORK_WORKFLOW.md) を参照してください。
