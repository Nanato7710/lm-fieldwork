"""Run each attention step on tiny tensors and optionally print shapes."""

from __future__ import annotations

import argparse

import torch

from lm_fieldwork.attention import ToySelfAttention


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--show-shapes", action="store_true")
    parser.add_argument("--no-causal-mask", action="store_true")
    args = parser.parse_args()

    torch.manual_seed(7)
    batch, time, channels, heads = 1, 4, 8, 2
    x = torch.randn(batch, time, channels)
    layer = ToySelfAttention(channels, heads)
    output, weights = layer(x, causal=not args.no_causal_mask)

    if args.show_shapes:
        print(f"input:   {tuple(x.shape)} = (B, T, C)")
        print(f"weights: {tuple(weights.shape)} = (B, H, T, T)")
        print(f"output:  {tuple(output.shape)} = (B, T, C)")
    print("head 0 attention weights:")
    print(weights[0, 0].detach())


if __name__ == "__main__":
    main()
