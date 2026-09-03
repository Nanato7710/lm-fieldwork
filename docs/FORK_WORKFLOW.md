# Fork workflow

自分の fork URL と講師から示された upstream URL に置き換えて実行します。

```bash
git clone <student-fork-url>
cd lm-fieldwork
git remote add upstream <upstream-url>
uv sync
uv run python scripts/check_environment.py
```

更新を取り込むとき:

```bash
git fetch upstream
git merge upstream/main
```

学習成果は learner-owned の `work/` に保存します。

```bash
git add work/
git commit -m "week01: attention experiment"
git push
```

`course/`, `docs/`, `src/`, `scripts/` は upstream 所有です。コース開始後、upstream は既存の `work/**` placeholder を原則変更しません。checkpoint、dataset cache、大きな出力は commit しません。
