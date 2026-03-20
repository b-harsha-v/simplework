from app.services.llm_service import get_llm
from app.graph.state import SimpleWorkState


def scheduler_agent(state: SimpleWorkState):

    llm = get_llm()

    tasks = state.get("tasks")

    prompt = f"""
You are a productivity planner.

Convert the following study tasks into a daily study schedule.

Assume the student studies 2 hours per day.

Tasks:
{tasks}

Return the result in this format:

Day 1
6:00-7:00 PM -> Task
7:00-8:00 PM -> Task

Day 2
6:00-7:00 PM -> Task
7:00-8:00 PM -> Task
"""

    response = llm.invoke(prompt)

    schedule_text = response.content

    schedule = [line.strip() for line in schedule_text.split("\n") if line.strip()]

    state["schedule"] = schedule

    return state