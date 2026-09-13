from root.agents.runtime.agent_runtime import AgentRuntime
from root.agents.runtime.model_adapter import LocalModelAdapter


def main():
    runtime = AgentRuntime(
        role="secretary",
        model_adapter=LocalModelAdapter(model_name="distilgpt2"),
    )
    request = "Create a Python CLI project"
    result = runtime.process(request, path="root/agents/", action="process_user_request")
    print(result)


if __name__ == "__main__":
    main()
