import torch

from lm_fieldwork.minigpt import MiniGPT, MiniGPTConfig
from lm_fieldwork.training import train_steps


def test_two_training_steps_on_cpu() -> None:
    torch.manual_seed(0)
    model = MiniGPT(MiniGPTConfig(vocab_size=20, context_length=8, d_model=16, n_heads=4, n_layers=1)).cpu()
    train_data = torch.randint(0, 20, (128,))
    validation_data = torch.randint(0, 20, (64,))
    result = train_steps(model, train_data, validation_data, steps=2, batch_size=2)
    assert len(result.train_losses) == 2
    assert result.tokens_seen == 32
    assert result.validation_loss > 0
