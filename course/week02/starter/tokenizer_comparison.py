"""Compare two tokenization choices without downloading a model or dataset."""

from __future__ import annotations

from pathlib import Path

from lm_fieldwork.paths import find_repository_root
from lm_fieldwork.tokenization import CharacterTokenizer, train_local_bpe


ROOT = find_repository_root(Path(__file__).resolve())
CORPUS = ROOT / "data/sample/tiny_ja.txt"


def main() -> None:
    text = CORPUS.read_text(encoding="utf-8")
    char = CharacterTokenizer.from_text(text)
    char_ids = char.encode(text)
    bpe = train_local_bpe(CORPUS)
    bpe_result = bpe.encode(text)

    for name, vocab_size, ids, examples in (
        ("character", char.vocab_size, char_ids, list(text[:12])),
        ("local BPE", bpe.get_vocab_size(), bpe_result.ids, bpe_result.tokens[:12]),
    ):
        print(f"\n{name}")
        print(f"vocab size: {vocab_size}")
        print(f"token count: {len(ids)}")
        print(f"average chars/token: {len(text) / len(ids):.2f}")
        print(f"examples: {examples}")


if __name__ == "__main__":
    main()
