from root.agents.runtime.agent_runtime import AgentRuntime
from root.agents.runtime.model_adapter import LocalModelAdapter


def test_agent_runtime_process_returns_structured_output():
    runtime = AgentRuntime(role="secretary", model_adapter=LocalModelAdapter(model_name="distilgpt2"))
    result = runtime.process("Create a Python CLI project", path="root/agents/", action="process_user_request")

    assert result["status"] == "processed"
    assert result["workflow_id"] == "wf-local"
    assert result["role"] == "secretary"
    assert result["plan"]
    assert "response" in result
