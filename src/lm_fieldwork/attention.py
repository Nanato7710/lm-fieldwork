"""Attention functions kept explicit so tensor shapes are easy to trace."""

from __future__ import annotations

import math

import torch
from torch import Tensor, nn


def scaled_dot_product_attention(
    q: Tensor, k: Tensor, v: Tensor, *, causal: bool = True
) -> tuple[Tensor, Tensor]:
    """Return attention output and weights for tensors shaped (B, H, T, D)."""
    scores = q @ k.transpose(-2, -1)
    scores = scores / math.sqrt(q.size(-1))
    if causal:
        time = q.size(-2)
        mask = torch.triu(
            torch.ones(time, time, dtype=torch.bool, device=q.device), diagonal=1
        )
        scores = scores.masked_fill(mask, float("-inf"))
    weights = torch.softmax(scores, dim=-1)
    return weights @ v, weights


class ToySelfAttention(nn.Module):
    """A minimal multi-head self-attention layer, without output dropout."""

    def __init__(self, d_model: int, n_heads: int) -> None:
        super().__init__()
        if d_model % n_heads != 0:
            raise ValueError("d_model must be divisible by n_heads")
        self.n_heads = n_heads
        self.head_dim = d_model // n_heads
        self.qkv = nn.Linear(d_model, 3 * d_model, bias=False)
        self.out = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x: Tensor, *, causal: bool = True) -> tuple[Tensor, Tensor]:
        batch, time, channels = x.shape
        q, k, v = self.qkv(x).chunk(3, dim=-1)

        def split_heads(tensor: Tensor) -> Tensor:
            return tensor.view(batch, time, self.n_heads, self.head_dim).transpose(1, 2)

        attended, weights = scaled_dot_product_attention(
            split_heads(q), split_heads(k), split_heads(v), causal=causal
        )
        merged = attended.transpose(1, 2).contiguous().view(batch, time, channels)
        return self.out(merged), weights
