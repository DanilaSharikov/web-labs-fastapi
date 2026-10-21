from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.schemas.task import TaskCreate, TaskRead
from app.services import tasks as service

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("", response_model=list[TaskRead])
async def list_tasks(db: AsyncSession = Depends(get_session)):
    return await service.list_tasks(db)

@router.get("/{task_id}", response_model=TaskRead)
async def get_task(task_id: int, db: AsyncSession = Depends(get_session)):
    task = await service.get_task(db, task_id)
    if task is None:
        raise HTTPException(404, "Task not found")
    return task

@router.post("", response_model=TaskRead, status_code=201)
async def create_task(data: TaskCreate, db: AsyncSession = Depends(get_session)):
    return await service.create_task(db, data)

@router.put("/{task_id}", response_model=TaskRead)
async def update_task(task_id: int, data: TaskCreate, db: AsyncSession = Depends(get_session)):
    task = await service.update_task(db, task_id, data)
    if task is None:
        raise HTTPException(404, "Task not found")
    return task

@router.delete("/{task_id}", status_code=204)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_session)):
    if not await service.delete_task(db, task_id):
        raise HTTPException(404, "Task not found")
    return Response(status_code=204)
