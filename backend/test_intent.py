from app.agents.intent_agent import intent_agent

state = {
    "user_message": "Create a 4 week DSA study plan",
    "intent": None,
    "goal": None,
    "duration": None,
    "plan": None,
    "tasks": None,
    "schedule": None,
    "response": None
}

result = intent_agent(state)

print(result["intent"])