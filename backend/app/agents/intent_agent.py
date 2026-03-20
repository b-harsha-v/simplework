from app.services.llm_service import get_llm
from app.graph.state import SimpleWorkState


def intent_agent(state: SimpleWorkState):

    llm = get_llm()

    message = state["user_message"]

    prompt = f"""
Classify the user's intent.

User message:
{message}

Return only one of these labels:

create_plan
approve_plan
modify_plan
ask_question
"""

    response = llm.invoke(prompt)

    intent = response.content.strip()

    state["intent"] = intent

    return state