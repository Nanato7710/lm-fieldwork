"""Small training helpers; deliberately not a general trainer framework."""

from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import Tensor

from .minigpt import MiniGPT


@dataclass(frozen=True)
class TrainingResult:
    train_losses: list[float]
    validation_loss: float
    tokens_seen: int


def sample_batch(data: Tensor, batch_size: int, context_length: int, device: torch.device) -> tuple[Tensor, Tensor]:
    if len(data) <= context_length:
        raise ValueError("data must contain more tokens than context_length")
    starts = torch.randint(0, len(data) - context_length, (batch_size,))
    x = torch.stack([data[i : i + context_length] for i in starts])
    y = torch.stack([data[i + 1 : i + context_length + 1] for i in starts])
    return x.to(device), y.to(device)


@torch.no_grad()
def estimate_loss(model: MiniGPT, data: Tensor, batch_size: int, batches: int = 4) -> float:
    model.eval()
    losses = []
    device = next(model.parameters()).device
    for _ in range(batches):
        x, y = sample_batch(data, batch_size, model.config.context_length, device)
        _, loss = model(x, y)
        assert loss is not None
        losses.append(loss.item())
    model.train()
    return sum(losses) / len(losses)


def train_steps(
    model: MiniGPT,
    train_data: Tensor,
    validation_data: Tensor,
    *,
    steps: int,
    batch_size: int,
    learning_rate: float = 3e-4,
) -> TrainingResult:
    device = next(model.parameters()).device
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)
    losses: list[float] = []
    for _ in range(steps):
        x, y = sample_batch(train_data, batch_size, model.config.context_length, device)
        _, loss = model(x, y)
        assert loss is not None
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        optimizer.step()
        losses.append(loss.item())
    validation_loss = estimate_loss(model, validation_data, batch_size, batches=2)
    return TrainingResult(losses, validation_loss, steps * batch_size * model.config.context_length)
