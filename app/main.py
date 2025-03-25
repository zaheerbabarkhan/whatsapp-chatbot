import logging

from fastapi import FastAPI

from app.api.v1.main import main_router
from app.core.config.logger_config import setup_logger

setup_logger()


logger = logging.getLogger(__name__)
app = FastAPI()

logger.info("Setting up routers")
app.include_router(main_router, prefix="/api")