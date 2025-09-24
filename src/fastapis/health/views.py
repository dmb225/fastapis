from fastapi import APIRouter

health_router = APIRouter()


@health_router.get("/", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    """Simple healthcheck endpoint."""
    return {"status": "ok"}
