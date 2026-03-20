from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.database.db import Base


class StudyPlan(Base):
    __tablename__ = "study_plans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id")) 
    goal = Column(String)
    duration = Column(Integer)
    plan_text = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)