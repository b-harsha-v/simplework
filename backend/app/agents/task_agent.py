from app.services.llm_service import get_llm
from app.graph.state import SimpleWorkState


def task_agent(state: SimpleWorkState):

    llm = get_llm()

    plan = state.get("plan")

    prompt = f"""
        Convert the following weekly study plan into daily tasks.

        Plan:
        {plan}

        Return ONLY a numbered list.

        Example:
        Day 1: Learn arrays
        Day 2: Solve two sum
        Day 3: Sliding window problems

        Do not include explanations.
        """

    response = llm.invoke(prompt)

    tasks_text = response.content

    tasks = [line.strip() for line in tasks_text.split("\n") if line.strip()]

    state["tasks"] = tasks

    return state