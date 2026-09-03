"""Offline tokenizers for comparing character and subword representations."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from tokenizers import Tokenizer, models, pre_tokenizers, trainers


@dataclass
class CharacterTokenizer:
    chars: list[str]

    @classmethod
    def from_text(cls, text: str) -> "CharacterTokenizer":
        return cls(sorted(set(text)))

    def __post_init__(self) -> None:
        self.char_to_id = {char: index for index, char in enumerate(self.chars)}

    @property
    def vocab_size(self) -> int:
        return len(self.chars)

    def encode(self, text: str) -> list[int]:
        return [self.char_to_id[char] for char in text]

    def decode(self, ids: list[int]) -> str:
        return "".join(self.chars[index] for index in ids)


def train_local_bpe(corpus_path: Path, vocab_size: int = 160) -> Tokenizer:
    """Train a small, readable BPE tokenizer using only a local text file."""
    tokenizer = Tokenizer(models.BPE(unk_token="<unk>"))
    tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()
    trainer = trainers.BpeTrainer(vocab_size=vocab_size, special_tokens=["<unk>"])
    tokenizer.train([str(corpus_path)], trainer)
    return tokenizer
