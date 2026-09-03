import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/make_context.py"
SPEC = importlib.util.spec_from_file_location("make_context", SCRIPT)
assert SPEC and SPEC.loader
make_context = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(make_context)


def test_context_contains_week_notes_and_question() -> None:
    output, warnings = make_context.build_context("week01", [], "mask は何を防ぐ？")
    assert not warnings
    assert "Week 1 — GPTを分解する" in output
    assert "## Current tasks" in output
    assert "## My notes" in output
    assert output.rstrip().endswith("mask は何を防ぐ？")


def test_notebook_include_is_skipped() -> None:
    output, warnings = make_context.build_context("week01", [Path("demo.ipynb")], None)
    assert "## Question" in output
    assert any("notebook" in warning.lower() or "Could not read" in warning for warning in warnings)
