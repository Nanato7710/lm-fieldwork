from __future__ import annotations

import ast
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

from lm_fieldwork.paths import find_repository_root


ROOT = Path(__file__).resolve().parents[1]


def run_starter(relative_path: str) -> str:
    environment = os.environ.copy()
    environment["HF_HUB_OFFLINE"] = "1"
    environment["TRANSFORMERS_OFFLINE"] = "1"
    result = subprocess.run(
        [sys.executable, relative_path],
        cwd=ROOT,
        env=environment,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def test_tokenization_observation_runs_offline() -> None:
    output = run_starter("course/preweek/starter/tokenization_observation.py")
    assert "characters" in output
    assert "manual word-like proposal" in output
    assert "local BPE" in output
    counts = [int(value) for value in re.findall(r"token count: (\d+)", output)]
    assert len(counts) == 3
    assert len(set(counts)) == 3


def test_generation_observation_probabilities() -> None:
    output = run_starter("course/preweek/starter/generation_observation.py")
    distributions = []
    for line in output.splitlines():
        if line.startswith("temperature="):
            distributions.append(ast.literal_eval(line.split(": ", maxsplit=1)[1]))

    assert len(distributions) == 3
    for distribution in distributions:
        assert sum(distribution.values()) == pytest.approx(1.0, abs=0.002)
    assert [distribution["読む"] for distribution in distributions] == sorted(
        (distribution["読む"] for distribution in distributions), reverse=True
    )
    assert "toy perplexity: 2.520" in output


def test_chat_template_observation_runs_offline() -> None:
    output = run_starter("course/week04/starter/chat_template_observation.py")
    assert "<|user|>" in output
    assert output.count("<|assistant|>") == 2
    assert "token IDs:" in output
    assert "decoded matches serialized: True" in output


def test_repository_root_is_found_after_copy_to_work() -> None:
    copied_starter = ROOT / "work/week02/experiment.py"
    assert find_repository_root(copied_starter) == ROOT
