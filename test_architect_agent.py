from agent_builder import AgentBuilder
from architect_agent import ArchitectAgent


def test_architect_runs_agents(tmp_path):
    builder = AgentBuilder()
    builder.build("Alpha", "echoes", tmp_path)
    builder.build("Beta", "echoes", tmp_path)

    architect = ArchitectAgent(tmp_path)
    responses = architect.run("ping")
    assert len(responses) == 2
    assert any("Alpha" in r for r in responses)
    assert any("Beta" in r for r in responses)
