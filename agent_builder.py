import argparse
from pathlib import Path


def build_agent(name: str, goal: str) -> Path:
    """Create a simple agent file containing the goal.

    Parameters
    ----------
    name: str
        Name of the agent. The output file will be ``{name}.txt``.
    goal: str
        The text to write inside the file.
    """
    filename = Path(f"{name}.txt")
    filename.write_text(f"Goal: {goal}\n")
    return filename


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a basic agent file")
    parser.add_argument("name", help="Name of the agent")
    parser.add_argument("goal", help="Goal of the agent")
    args = parser.parse_args()

    path = build_agent(args.name, args.goal)
    print(f"Built agent {args.name} at {path}")
