from unittest.mock import patch

import torch

from lm_fieldwork.device import select_device


def test_cpu_fallback() -> None:
    with patch("torch.backends.mps.is_available", return_value=False), patch(
        "torch.cuda.is_available", return_value=False
    ):
        assert select_device() == torch.device("cpu")


def test_mps_has_priority() -> None:
    with patch("torch.backends.mps.is_available", return_value=True), patch(
        "torch.cuda.is_available", return_value=True
    ):
        assert select_device() == torch.device("mps")
