from app.graph.workflow import build_workflow

graph = build_workflow()

state = {
    "user_message": "Create a 4 week DSA plan",
    "intent": None,
    "goal": "Data Structures and Algorithms",
    "duration": 4,
    "plan": None,
    "tasks": None,
    "schedule": None,
    "response": None
}

result = graph.invoke(state)

print(result["plan"])