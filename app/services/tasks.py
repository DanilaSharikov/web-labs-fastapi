from app.schemas.task import TaskCreate, TaskRead

storage: dict[int, TaskRead] = {}
next_id = 1

def list_tasks() -> list[TaskRead]:
    return list(storage.values())

def get_task(task_id: int) -> TaskRead | None:
    return storage.get(task_id)

def create_task(data: TaskCreate) -> TaskRead:
    global next_id
    task = TaskRead(id=next_id, **data.model_dump())
    storage[next_id] = task
    next_id += 1
    return task

def update_task(task_id: int, data: TaskCreate) -> TaskRead | None:
    if task_id not in storage:
        return None
    task = TaskRead(id=task_id, **data.model_dump())
    storage[task_id] = task
    return task

def delete_task(task_id: int) -> bool:
    return storage.pop(task_id, None) is not None
