"""Small path helpers used by starter scripts copied into learner work."""

from __future__ import annotations

from pathlib import Path


def find_repository_root(start: Path) -> Path:
    """Find the nearest parent containing the LM Fieldwork project file."""
    for candidate in (start, *start.parents):
        if (candidate / "pyproject.toml").is_file():
            return candidate
    raise FileNotFoundError(f"Could not find pyproject.toml above {start}")
