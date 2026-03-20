from app.services.llm_service import get_llm
from app.graph.state import SimpleWorkState


def planner_agent(state: SimpleWorkState):

    llm = get_llm()

    goal = state.get("goal")
    duration = state.get("duration")

    prompt = f"""
Create a concise study roadmap.

Goal: {goal}
Duration: {duration} weeks

Return ONLY this format:

Week 1: Topic
Week 2: Topic
Week 3: Topic
Week 4: Topic

Do not include explanations.
"""

    response = llm.invoke(prompt)

    state["plan"] = response.content

    return state