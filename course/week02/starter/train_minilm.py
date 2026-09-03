"""Train the educational MiniGPT briefly on the repository's sample corpus."""

from __future__ import annotations

import argparse
from pathlib import Path

import torch

from lm_fieldwork.device import select_device
from lm_fieldwork.minigpt import MiniGPT, MiniGPTConfig
from lm_fieldwork.tokenization import CharacterTokenizer
from lm_fieldwork.training import train_steps


ROOT = Path(__file__).resolve().parents[3]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, default=100)
    parser.add_argument("--context-length", type=int, default=64)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--device", choices=("cpu", "mps", "cuda"))
    args = parser.parse_args()

    torch.manual_seed(42)
    text = (ROOT / "data/sample/tiny_ja.txt").read_text(encoding="utf-8") * 8
    tokenizer = CharacterTokenizer.from_text(text)
    ids = torch.tensor(tokenizer.encode(text), dtype=torch.long)
    split = int(0.9 * len(ids))
    train_data, validation_data = ids[:split], ids[split:]
    config = MiniGPTConfig(vocab_size=tokenizer.vocab_size, context_length=args.context_length)
    device = select_device(args.device)
    model = MiniGPT(config).to(device)
    print(f"device={device} parameters={model.parameter_count():,}")
    result = train_steps(
        model,
        train_data,
        validation_data,
        steps=args.steps,
        batch_size=args.batch_size,
    )
    print(f"train loss: {result.train_losses[0]:.4f} -> {result.train_losses[-1]:.4f}")
    print(f"validation loss: {result.validation_loss:.4f}")
    print(f"tokens seen: {result.tokens_seen:,}")
    prompt = torch.tensor([[tokenizer.encode("言葉")[0]]], device=device)
    generated = model.generate(prompt, max_new_tokens=60, temperature=0.9)[0].tolist()
    print("sample:", tokenizer.decode(generated))


if __name__ == "__main__":
    main()
