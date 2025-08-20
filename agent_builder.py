from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import textwrap


@dataclass
class MiniAgent:
    """A tiny agent that can perform very basic tasks."""

    name: str
    behavior: str

    def run(self, prompt: str) -> str:
        """Return a simple response based on the agent's behavior."""
        return f"{self.name} ({self.behavior}) received: {prompt}"


class AgentBuilder:
    """Create new mini agents as standalone Python files."""

    template = textwrap.dedent(
        """\
        from agent_builder import MiniAgent


        class {class_name}(MiniAgent):
            def __init__(self):
                super().__init__(name="{name}", behavior="{behavior}")


        if __name__ == "__main__":
            agent = {class_name}()
            print(agent.run("Hello"))
        """
    )

    def build(self, name: str, behavior: str, directory: str = ".") -> Path:
        """Generate a new mini agent file.

        Args:
            name: Name of the new agent class/file.
            behavior: Short description of how the agent behaves.
            directory: Where to write the new file.

        Returns:
            Path to the created Python file.
        """
        class_name = f"{name}Agent"
        content = self.template.format(
            class_name=class_name,
            name=name,
            behavior=behavior,
        )
        path = Path(directory) / f"{name.lower()}_agent.py"
        path.write_text(content)
        return path


def _main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Build mini agents")
    parser.add_argument("name", help="Name of the agent to create")
    parser.add_argument("behavior", help="Behavior description")
    parser.add_argument(
        "--dir", default=".", help="Directory to place the generated agent file"
    )
    args = parser.parse_args()

    builder = AgentBuilder()
    path = builder.build(args.name, args.behavior, args.dir)
    print(f"Created agent at {path}")


if __name__ == "__main__":
    _main()
