from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.chat_router import router as chat_router
from app.routers.auth_router import router as auth_router
from app.routers.task_router import router as task_router
from app.routers.progress_router import router as progress_router

from app.database.db import engine, Base

# ✅ Import ALL models BEFORE create_all
import app.models.user
import app.models.plan
import app.models.task


app = FastAPI(title="SimpleWork AI Planner")

# ✅ CORS immediately after app creation
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔥 TEMP: allow all (fix CORS completely)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Create tables AFTER app init
Base.metadata.create_all(bind=engine)

# ✅ Register routers
app.include_router(chat_router)
app.include_router(auth_router)
app.include_router(task_router)
app.include_router(progress_router)


@app.get("/")
def root():
    return {"message": "SimpleWork backend running"}