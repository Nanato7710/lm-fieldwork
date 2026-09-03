"""Trace a fixed toy chat template with a local character tokenizer."""

from __future__ import annotations

from lm_fieldwork.tokenization import CharacterTokenizer


MESSAGES = [
    {"role": "user", "content": "短く説明して"},
    {"role": "assistant", "content": "何を説明しますか"},
    {"role": "user", "content": "tokenについて"},
]


def apply_toy_chat_template(messages: list[dict[str, str]]) -> str:
    parts = [f"<|{message['role']}|>\n{message['content']}\n" for message in messages]
    parts.append("<|assistant|>\n")
    return "".join(parts)


def main() -> None:
    serialized = apply_toy_chat_template(MESSAGES)
    tokenizer = CharacterTokenizer.from_text(serialized)
    token_ids = tokenizer.encode(serialized)

    print("messages:")
    for message in MESSAGES:
        print(f"- {message['role']}: {message['content']}")
    print("\nserialized with the toy template:")
    print(serialized, end="")
    print(f"\ntoken count: {len(token_ids)}")
    print(f"token IDs: {token_ids}")
    print(f"decoded matches serialized: {tokenizer.decode(token_ids) == serialized}")
    print("This toy template and vocabulary do not represent a pretrained model.")


if __name__ == "__main__":
    main()
