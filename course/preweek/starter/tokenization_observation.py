"""Observe three possible tokenizations without downloading a model."""

from __future__ import annotations

from pathlib import Path

from lm_fieldwork.tokenization import CharacterTokenizer, train_local_bpe


ROOT = Path(__file__).resolve().parents[3]
CORPUS = ROOT / "data/sample/tiny_ja.txt"
TEXT = "学生は短い文章を読み、次に来る文字を予想してからコードを動かした。"


def show(name: str, tokens: list[str], ids: list[int] | None = None) -> None:
    print(f"\n{name}")
    print(f"token count: {len(tokens)}")
    print(f"tokens: {tokens}")
    if ids is not None:
        print(f"token IDs: {ids}")


def main() -> None:
    character = CharacterTokenizer.from_text(TEXT)
    character_ids = character.encode(TEXT)
    character_tokens = [character.chars[token_id] for token_id in character_ids]

    # This is one learner-like proposal, not a unique linguistic answer.
    manual_tokens = [
        "学生",
        "は",
        "短い",
        "文章",
        "を",
        "読み",
        "、",
        "次",
        "に",
        "来る",
        "文字",
        "を",
        "予想して",
        "から",
        "コード",
        "を",
        "動かした",
        "。",
    ]

    local_bpe = train_local_bpe(CORPUS)
    bpe_result = local_bpe.encode(TEXT)

    print(f"text: {TEXT}")
    show("characters", character_tokens, character_ids)
    show("manual word-like proposal", manual_tokens)
    show("local BPE", bpe_result.tokens, bpe_result.ids)
    print("\nThe local BPE was trained only on data/sample/tiny_ja.txt.")
    print("Its split is an observation from this vocabulary, not a universal answer.")


if __name__ == "__main__":
    main()
