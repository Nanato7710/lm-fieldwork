#!/usr/bin/env python3
"""Report the local LM Fieldwork runtime without network access."""

from __future__ import annotations

import importlib
import platform
import sys


def main() -> int:
    print("LM Fieldwork environment check")
    print(f"Python: {platform.python_version()}")
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Machine: {platform.machine()}")
    if sys.version_info[:2] != (3, 12):
        print("WARNING: project baseline is Python 3.12")

    try:
        import torch
    except ImportError:
        print("PyTorch: MISSING (blocking)")
        return 1

    from lm_fieldwork.device import select_device

    print(f"PyTorch: {torch.__version__}")
    print(f"MPS: {'available' if torch.backends.mps.is_available() else 'unavailable'}")
    cuda_available = torch.cuda.is_available()
    cuda_detail = "available" if cuda_available else "unavailable"
    if cuda_available:
        cuda_detail += f" ({torch.cuda.get_device_name(0)})"
    print(f"CUDA: {cuda_detail}")
    print(f"Selected device: {select_device()}")

    for package in ("transformers", "tokenizers"):
        try:
            module = importlib.import_module(package)
            print(f"{package}: OK ({getattr(module, '__version__', 'unknown version')})")
        except ImportError:
            print(f"{package}: MISSING")
    try:
        datasets = importlib.import_module("datasets")
        print(f"datasets: OK ({getattr(datasets, '__version__', 'unknown version')}) [optional]")
    except ImportError:
        print("datasets: not installed [optional]")

    print("Environment looks ready.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
