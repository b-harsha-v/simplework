from app.database.db import SessionLocal
from app.models.plan import StudyPlan
from app.models.task import Task
from app.models.user import User


def get_or_create_user(email, name):

    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    if not user:
        user = User(email=email, name=name)
        db.add(user)
        db.commit()
        db.refresh(user)

    db.close()

    return user


def save_plan(session_id, goal, duration, plan_text):

    db = SessionLocal()

    plan = StudyPlan(
        session_id=session_id,
        goal=goal,
        duration=duration,
        plan_text=plan_text
    )

    db.add(plan)
    db.commit()
    db.refresh(plan)

    db.close()

    return plan.id


def save_tasks(plan_id, tasks):

    db = SessionLocal()

    for task in tasks:
        db_task = Task(
            plan_id=plan_id,
            description=task
        )
        db.add(db_task)

    db.commit()
    db.close()

def get_tasks_by_user(user_id):

    db = SessionLocal()

    tasks = (
        db.query(Task)
        .join(StudyPlan, Task.plan_id == StudyPlan.id)
        .filter(StudyPlan.user_id == user_id)
        .all()
    )

    db.close()

    return tasks

def mark_task_complete(task_id):

    db = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if task:
        task.completed = True
        db.commit()

    db.close()

    return task


def get_progress(user_id):

    db = SessionLocal()

    tasks = (
        db.query(Task)
        .join(StudyPlan, Task.plan_id == StudyPlan.id)
        .filter(StudyPlan.user_id == user_id)
        .all()
    )

    total = len(tasks)
    completed = sum(1 for t in tasks if t.completed)

    db.close()

    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "completion_rate": (completed / total * 100) if total > 0 else 0
    }

def get_tasks_by_session(session_id):

    db = SessionLocal()

    tasks = (
        db.query(Task)
        .join(StudyPlan, Task.plan_id == StudyPlan.id)
        .filter(StudyPlan.session_id == session_id)
        .all()
    )

    db.close()

    return tasks