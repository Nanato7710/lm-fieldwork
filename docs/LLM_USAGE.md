# LLM usage policy

ChatGPT、Claude などは、翻訳、指定 section の言い換え、数式、tensor shape、コード追跡、デバッグ、用語確認、模擬質問に利用してよい。

## 3つのルール

1. 重要な主張は元資料で確認し、LLM 回答を参考文献の代わりにしない。
2. 自分で説明できないものを「理解したこと」に書かない。
3. 分からないことを隠さず、分からない箇所の特定に使う。

良い質問は範囲と目的を絞ります。例: 「Section 3.2 の式(1)について Q, K の shape を具体例で説明し、原文の内容と補足を分けてください」。Web 版へ現在の文脈を渡すには次を使います。

```bash
uv run python scripts/make_context.py --week week01 --clipboard
```
