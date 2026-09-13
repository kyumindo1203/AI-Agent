from root.agents.runtime.model_adapter import LocalModelAdapter
from root.agents.runtime.runtime_agent import RuntimeAgent


def test_local_model_adapter_fallback_generates_structured_response():
    adapter = LocalModelAdapter(model_name="distilgpt2")
    reply = adapter.generate("Create a Python CLI project")
    assert isinstance(reply, str)
    assert len(reply) > 0


def test_runtime_agent_can_process_user_request_using_model_adapter():
    adapter = LocalModelAdapter(model_name="distilgpt2")
    runtime = RuntimeAgent(
        role="secretary",
        model_adapter=adapter,
    )
    result = runtime.execute(
        action="process_user_request",
        path="root/agents/",
        payload={"request": "Create a Python CLI project"},
    )
    assert result["status"] == "processed"
    assert "plan" in result
    assert "response" in result
