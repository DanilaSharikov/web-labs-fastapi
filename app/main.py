from fastapi import FastAPI
from app.api.v1.tasks import router

app = FastAPI(title="Task Manager API")
app.include_router(router, prefix="/api/v1")
