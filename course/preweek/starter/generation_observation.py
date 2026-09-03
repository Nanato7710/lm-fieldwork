"""Observe temperature and perplexity with fixed toy values."""

from __future__ import annotations

import math

import torch


def main() -> None:
    candidates = ["読む", "書く", "眠る"]
    logits = torch.tensor([2.0, 1.0, 0.0])

    print(f"fixed logits: {dict(zip(candidates, logits.tolist(), strict=True))}")
    for temperature in (0.5, 1.0, 2.0):
        probabilities = torch.softmax(logits / temperature, dim=0)
        rounded = [round(value, 3) for value in probabilities.tolist()]
        print(f"temperature={temperature}: {dict(zip(candidates, rounded, strict=True))}")

    observed_token_probabilities = [0.5, 0.25, 0.5]
    mean_negative_log_probability = -sum(
        math.log(probability) for probability in observed_token_probabilities
    ) / len(observed_token_probabilities)
    perplexity = math.exp(mean_negative_log_probability)
    print(f"observed token probabilities: {observed_token_probabilities}")
    print(f"toy perplexity: {perplexity:.3f}")
    print("These fixed values illustrate the calculation; they are not model measurements.")


if __name__ == "__main__":
    main()
