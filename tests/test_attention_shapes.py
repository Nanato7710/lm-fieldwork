import torch

from lm_fieldwork.attention import ToySelfAttention, scaled_dot_product_attention


def test_attention_output_shapes() -> None:
    layer = ToySelfAttention(d_model=8, n_heads=2)
    output, weights = layer(torch.randn(2, 4, 8))
    assert output.shape == (2, 4, 8)
    assert weights.shape == (2, 2, 4, 4)


def test_causal_mask_blocks_future_values() -> None:
    q = torch.ones(1, 1, 3, 2)
    k = torch.ones(1, 1, 3, 2)
    original_v = torch.tensor([[[[1.0, 1.0], [2.0, 2.0], [3.0, 3.0]]]])
    changed_future_v = original_v.clone()
    changed_future_v[..., 1:, :] = 1000.0
    causal_a, causal_weights = scaled_dot_product_attention(q, k, original_v, causal=True)
    causal_b, _ = scaled_dot_product_attention(q, k, changed_future_v, causal=True)
    unmasked_a, _ = scaled_dot_product_attention(q, k, original_v, causal=False)
    unmasked_b, _ = scaled_dot_product_attention(q, k, changed_future_v, causal=False)
    assert torch.allclose(causal_a[..., 0, :], causal_b[..., 0, :])
    assert not torch.allclose(unmasked_a[..., 0, :], unmasked_b[..., 0, :])
    assert torch.equal(causal_weights[..., 0, 1:], torch.zeros(1, 1, 2))
