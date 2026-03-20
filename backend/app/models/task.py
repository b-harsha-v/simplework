from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    plan_id = Column(Integer, ForeignKey("study_plans.id"))
    description = Column(String)
    completed = Column(Boolean, default=False)