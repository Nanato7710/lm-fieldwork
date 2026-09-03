# Fork workflow

## 1. GitHub上にforkを作る

1. upstreamの[`Nanato7710/lm-fieldwork`](https://github.com/Nanato7710/lm-fieldwork)を開く。
2. 右上の「Fork」を押す。
3. Ownerが自分のGitHubアカウントになっていることを確認する。
4. repository nameを`lm-fieldwork`のままにして「Create fork」を押す。

詳しい画面説明は[GitHub公式のfork手順](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo)にあります。

## 2. 自分のforkをcloneする

作成したforkで「Code」、「HTTPS」の順に開き、`https://github.com/<自分のユーザー名>/lm-fieldwork.git`というURLをコピーします。
`<student-fork-url>`をコピーしたURLへ置き換えて実行します。

```bash
git clone <student-fork-url>
cd lm-fieldwork
git remote add upstream https://github.com/Nanato7710/lm-fieldwork.git
git remote -v
uv python install 3.12
uv sync
uv run python scripts/check_environment.py
```

`origin`が自分のfork、`upstream`が`Nanato7710/lm-fieldwork`を指していれば準備完了です。

## 3. upstreamの更新を取り込む

```bash
git fetch upstream
git merge upstream/main
```

## 4. 学習記録を保存する

学習成果は learner-owned の `work/` に保存します。

```bash
git add work/
git commit -m "week01: attention experiment"
git push
```

`course/`, `docs/`, `src/`, `scripts/` は upstream 所有です。コース開始後、upstream は既存の `work/**` placeholder を原則変更しません。checkpoint、dataset cache、大きな出力は commit しません。
