import subprocess
import sys
from pathlib import Path


def test_agent_builder_creates_file(tmp_path):
    script = Path(__file__).resolve().parent.parent / "agent_builder.py"
    result = subprocess.run(
        [sys.executable, str(script), "sample", "do things"],
        capture_output=True,
        text=True,
        cwd=tmp_path,
        check=True,
    )
    expected_file = tmp_path / "sample.txt"
    assert expected_file.exists()
    assert expected_file.read_text() == "Goal: do things\n"
    assert "Built agent sample" in result.stdout
    expected_file.unlink()


def test_architect_agent_creates_file(tmp_path):
    script = Path(__file__).resolve().parent.parent / "architect_agent.py"
    result = subprocess.run(
        [sys.executable, str(script), "blueprint", "great agent"],
        capture_output=True,
        text=True,
        cwd=tmp_path,
        check=True,
    )
    expected_file = tmp_path / "blueprint_architecture.txt"
    assert expected_file.exists()
    assert expected_file.read_text() == "Description: great agent\n"
    assert "Architected agent blueprint" in result.stdout
    expected_file.unlink()
