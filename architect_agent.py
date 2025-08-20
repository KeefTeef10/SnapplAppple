from __future__ import annotations

from importlib import util
from pathlib import Path
from typing import List

from agent_builder import MiniAgent


class ArchitectAgent:
    """Orchestrate multiple mini agents in a directory."""

    def __init__(self, directory: str = ".") -> None:
        self.directory = Path(directory)
        self.agents: List[MiniAgent] = []
        self._load_agents()

    def _load_agents(self) -> None:
        """Dynamically import all *_agent.py files and instantiate agents."""
        for path in self.directory.glob("*_agent.py"):
            spec = util.spec_from_file_location(path.stem, path)
            if spec and spec.loader:
                module = util.module_from_spec(spec)
                spec.loader.exec_module(module)
                for obj in module.__dict__.values():
                    if (
                        isinstance(obj, type)
                        and issubclass(obj, MiniAgent)
                        and obj is not MiniAgent
                    ):
                        self.agents.append(obj())

    def run(self, prompt: str) -> list[str]:
        """Run the prompt through all loaded agents."""
        return [agent.run(prompt) for agent in self.agents]


def _main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Run multiple mini agents")
    parser.add_argument("prompt", help="Prompt to pass to the agents")
    parser.add_argument(
        "--dir", default=".", help="Directory containing generated agents"
    )
    args = parser.parse_args()

    architect = ArchitectAgent(args.dir)
    for response in architect.run(args.prompt):
        print(response)


if __name__ == "__main__":
    _main()
