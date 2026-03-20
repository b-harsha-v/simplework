from fastapi import APIRouter
from app.services.db_service import get_progress

router = APIRouter(prefix="/progress", tags=["progress"])


@router.get("/")
def progress(user_id: int):

    return get_progress(user_id)