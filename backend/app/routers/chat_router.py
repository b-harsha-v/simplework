from fastapi import APIRouter
from pydantic import BaseModel
from app.graph.workflow import build_workflow
from app.services.db_service import save_plan, save_tasks

router = APIRouter()

graph = build_workflow()


class ChatRequest(BaseModel):
    message: str
    goal: str | None = None
    duration: int | None = None
    user_id: str


@router.post("/chat")
def chat(req: ChatRequest):

    state = {
        "user_message": req.message
    }

    if req.goal:
        state["goal"] = req.goal

    if req.duration:
        state["duration"] = req.duration

    result = graph.invoke(
        state,
        config={"configurable": {"thread_id": req.user_id}}
    )

    intent = result.get("intent")

    if intent == "create_plan":
        plan_id = save_plan(
            req.user_id,
            req.goal,
            req.duration,
            result.get("plan")
        )
        return {
            "intent": intent,
            "plan_id":plan_id,
            "study_plan": result.get("plan")
        }

    if intent == "approve_plan":
        plan_id = save_plan(
            req.user_id,
            result.get("goal"),
            result.get("duration"),
            result.get("plan")
        )

        save_tasks(plan_id, result.get("tasks"))
        return {
            "intent": intent,
            "tasks": result.get("tasks"),
            "schedule": result.get("schedule")
        }

    return {
        "intent": intent,
        "message": "Unhandled intent"
    }