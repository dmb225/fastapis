from fastapi import APIRouter

root_router = APIRouter()


@root_router.get("/")
async def about() -> dict[str, str]:
    return {
        "message": "Welcome to FastAPIs!",
        "version": "0.1.0",
    }
