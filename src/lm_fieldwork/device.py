"""Device choice shared by scripts and tests."""

from __future__ import annotations

import torch


def select_device(preferred: str | None = None) -> torch.device:
    """Choose MPS first on Mac, then CUDA, with a required CPU fallback."""
    if preferred is not None:
        if preferred == "mps" and torch.backends.mps.is_available():
            return torch.device("mps")
        if preferred == "cuda" and torch.cuda.is_available():
            return torch.device("cuda")
        if preferred == "cpu":
            return torch.device("cpu")
        raise RuntimeError(f"Requested device is unavailable: {preferred}")

    if torch.backends.mps.is_available():
        return torch.device("mps")
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")
