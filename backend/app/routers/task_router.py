from fastapi import APIRouter
from pydantic import BaseModel

from app.services.db_service import (
    get_tasks_by_user,
    mark_task_complete
)

router = APIRouter(prefix="/tasks", tags=["tasks"])


class TaskCompleteRequest(BaseModel):
    task_id: int


@router.get("/")
def get_tasks(user_id: int):

    tasks = get_tasks_by_user(user_id)

    return [
        {
            "id": t.id,
            "description": t.description,
            "completed": t.completed
        }
        for t in tasks
    ]


@router.post("/complete")
def complete_task(req: TaskCompleteRequest):

    task = mark_task_complete(req.task_id)

    if not task:
        return {"error": "Task not found"}

    return {
        "message": "Task completed",
        "task_id": task.id
    }