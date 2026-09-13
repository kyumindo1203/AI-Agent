from root.agents.runtime.message_bus import MessageBus
from root.agents.runtime.task_scheduler import TaskScheduler
from root.agents.runtime.workflow_state import WorkflowState


def test_message_bus_and_scheduler_shape():
    bus = MessageBus()
    scheduler = TaskScheduler(max_workers=2)

    def handle(msg):
        return {"status": "ok", "topic": msg.get("topic")}

    bus.register_handler("planner", handle)
    bus.publish("planner", {"topic": "planner", "request": "plan"})
    result = bus.dispatch("planner")

    assert isinstance(result, list)
    assert result[0]["status"] == "ok"

    def work():
        return "done"

    future = scheduler.submit(work)
    assert future.result() == "done"

    state = WorkflowState(workflow_id="wf-1")
    state.add_task({"task_id": "t-1", "title": "draft"})
    assert state.status == "created"

    scheduler.shutdown()
