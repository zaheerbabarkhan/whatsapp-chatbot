from fastapi import FastAPI
from app.api.v1.main import main_router

app = FastAPI()

app.include_router(main_router, prefix="/api")