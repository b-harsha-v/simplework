from app.agents.planner_agent import planner_agent

state = {
    "user_message": "create a plan",
    "intent": None,
    "goal": "Data Structures and Algorithms",
    "duration": 4,
    "plan": None,
    "tasks": None,
    "schedule": None,
    "response": None
}

result = planner_agent(state)

print(result["plan"])