import torch

from lm_fieldwork.minigpt import MiniGPT, MiniGPTConfig


def test_minigpt_forward_shape_and_loss() -> None:
    model = MiniGPT(MiniGPTConfig(vocab_size=31, context_length=8, d_model=16, n_heads=4, n_layers=1))
    tokens = torch.randint(0, 31, (2, 8))
    logits, loss = model(tokens, tokens)
    assert logits.shape == (2, 8, 31)
    assert loss is not None and loss.ndim == 0
