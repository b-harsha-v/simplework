from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from app.graph.state import SimpleWorkState
from app.agents.intent_agent import intent_agent
from app.agents.planner_agent import planner_agent
from app.agents.task_agent import task_agent
from app.agents.scheduler_agent import scheduler_agent


def route_intent(state: SimpleWorkState):

    intent = state.get("intent")

    if intent == "create_plan":
        return "planner"
    if intent == "approve_plan":
        return "task"

    return END


def build_workflow():

    workflow = StateGraph(SimpleWorkState)

    workflow.add_node("intent", intent_agent)
    workflow.add_node("planner", planner_agent)
    workflow.add_node("task", task_agent)
    workflow.add_node("scheduler", scheduler_agent)

    workflow.set_entry_point("intent")

    workflow.add_conditional_edges(
        "intent",
        route_intent
    )

    workflow.add_edge("planner", "task")
    workflow.add_edge("task", "scheduler")
    workflow.add_edge("scheduler", END)

    memory = MemorySaver()

    graph = workflow.compile(checkpointer=memory)

    return graph