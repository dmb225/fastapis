from fastapi import APIRouter

from fastapis.health.views import health_router
from fastapis.root.views import root_router

api_router = APIRouter()

api_router.include_router(root_router, tags=["root"])
api_router.include_router(health_router, prefix="/health", tags=["health"])
