from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.task import Task
from app.schemas.task import TaskCreate

async def list_tasks(db: AsyncSession):
    result = await db.execute(select(Task).order_by(Task.id))
    return result.scalars().all()

async def get_task(db: AsyncSession, task_id: int):
    return await db.get(Task, task_id)

async def create_task(db: AsyncSession, data: TaskCreate):
    task = Task(**data.model_dump())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def update_task(db: AsyncSession, task_id: int, data: TaskCreate):
    task = await db.get(Task, task_id)
    if task is None:
        return None
    for key, value in data.model_dump().items():
        setattr(task, key, value)
    await db.commit()
    await db.refresh(task)
    return task

async def delete_task(db: AsyncSession, task_id: int):
    task = await db.get(Task, task_id)
    if task is None:
        return False
    await db.delete(task)
    await db.commit()
    return True
