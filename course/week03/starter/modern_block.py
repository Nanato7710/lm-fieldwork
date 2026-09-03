"""Pedagogical Llama-like block: readable shapes, not production optimization."""

from __future__ import annotations

import math

import torch
from torch import Tensor, nn


class RMSNorm(nn.Module):
    def __init__(self, width: int, eps: float = 1e-6) -> None:
        super().__init__()
        self.scale = nn.Parameter(torch.ones(width))
        self.eps = eps

    def forward(self, x: Tensor) -> Tensor:
        rms = x.pow(2).mean(dim=-1, keepdim=True).add(self.eps).rsqrt()
        return self.scale * x * rms


def apply_rope(x: Tensor) -> Tensor:
    """Rotate adjacent feature pairs; x has shape (B, heads, T, head_dim)."""
    _, _, time, width = x.shape
    if width % 2:
        raise ValueError("RoPE head dimension must be even")
    positions = torch.arange(time, device=x.device, dtype=x.dtype)
    frequencies = 1.0 / (10000 ** (torch.arange(0, width, 2, device=x.device) / width))
    angles = positions[:, None] * frequencies[None, :]
    cos, sin = angles.cos()[None, None], angles.sin()[None, None]
    even, odd = x[..., 0::2], x[..., 1::2]
    return torch.stack((even * cos - odd * sin, even * sin + odd * cos), dim=-1).flatten(-2)


class GroupedQueryAttention(nn.Module):
    def __init__(self, width: int, query_heads: int = 4, kv_heads: int = 2) -> None:
        super().__init__()
        if query_heads % kv_heads or width % query_heads:
            raise ValueError("query_heads must divide width and be divisible by kv_heads")
        self.query_heads, self.kv_heads = query_heads, kv_heads
        self.head_dim = width // query_heads
        self.q = nn.Linear(width, query_heads * self.head_dim, bias=False)
        self.k = nn.Linear(width, kv_heads * self.head_dim, bias=False)
        self.v = nn.Linear(width, kv_heads * self.head_dim, bias=False)
        self.out = nn.Linear(width, width, bias=False)

    def forward(self, x: Tensor) -> Tensor:
        batch, time, _ = x.shape
        q = self.q(x).view(batch, time, self.query_heads, self.head_dim).transpose(1, 2)
        k = self.k(x).view(batch, time, self.kv_heads, self.head_dim).transpose(1, 2)
        v = self.v(x).view(batch, time, self.kv_heads, self.head_dim).transpose(1, 2)
        q, k = apply_rope(q), apply_rope(k)
        repeat = self.query_heads // self.kv_heads
        k, v = k.repeat_interleave(repeat, dim=1), v.repeat_interleave(repeat, dim=1)
        scores = (q @ k.transpose(-2, -1)) / math.sqrt(self.head_dim)
        mask = torch.triu(torch.ones(time, time, dtype=torch.bool), diagonal=1)
        weights = torch.softmax(scores.masked_fill(mask.to(x.device), float("-inf")), dim=-1)
        attended = (weights @ v).transpose(1, 2).contiguous().view(batch, time, -1)
        return self.out(attended)


class SwiGLU(nn.Module):
    def __init__(self, width: int, hidden: int) -> None:
        super().__init__()
        self.gate, self.value, self.out = nn.Linear(width, hidden), nn.Linear(width, hidden), nn.Linear(hidden, width)

    def forward(self, x: Tensor) -> Tensor:
        return self.out(torch.nn.functional.silu(self.gate(x)) * self.value(x))


class ModernBlock(nn.Module):
    def __init__(self, width: int = 32) -> None:
        super().__init__()
        self.attention_norm = RMSNorm(width)
        self.attention = GroupedQueryAttention(width)
        self.mlp_norm = RMSNorm(width)
        self.mlp = SwiGLU(width, 64)

    def forward(self, x: Tensor) -> Tensor:
        x = x + self.attention(self.attention_norm(x))
        return x + self.mlp(self.mlp_norm(x))


def kv_cache_shape(batch: int, kv_heads: int, cached_tokens: int, head_dim: int) -> tuple[int, ...]:
    """A cache stores past K or V with this conceptual shape."""
    return batch, kv_heads, cached_tokens, head_dim


if __name__ == "__main__":
    x = torch.randn(2, 8, 32)
    y = ModernBlock()(x)
    print("input -> output:", tuple(x.shape), "->", tuple(y.shape))
    for cached in range(1, 4):
        print("conceptual K/V cache shape with cached_tokens", cached, ":", kv_cache_shape(2, 2, cached, 8))
