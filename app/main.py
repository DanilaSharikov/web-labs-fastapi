from fastapi import FastAPI
from app.api.v1.tasks import router
from contextlib import asynccontextmanager
from app.db.session import engine
from app.models.task import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title="Task Manager API", lifespan=lifespan)
app.include_router(router, prefix="/api/v1")
