from fastapi import APIRouter
from pydantic import BaseModel

from app.services.auth_service import verify_google_token
from app.services.db_service import get_or_create_user

router = APIRouter(prefix="/auth", tags=["auth"])


class GoogleAuthRequest(BaseModel):
    id_token: str


@router.post("/google")
def google_auth(req: GoogleAuthRequest):

    user_info = verify_google_token(req.id_token)

    if not user_info:
        return {"error": "Invalid token"}

    user = get_or_create_user(
        user_info["email"],
        user_info["name"]
    )

    return {
        "user_id": user.id,
        "email": user.email,
        "name": user.name
    }