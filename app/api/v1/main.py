from fastapi import APIRouter

from app.api.v1.router.webhook import webhook_router

main_router = APIRouter(prefix="/v1")

main_router.include_router(webhook_router, tags=["webhook"])