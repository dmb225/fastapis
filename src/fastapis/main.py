from fastapi import FastAPI
import uvicorn

from .api import api_router

app = FastAPI(
    description="Welcome to FastAPIs' documentation! Here you will able to discover all of the ways you can interact with the APIs.",
    root_path="/fastapis/v1",
    docs_url=None,
    openapi_url="/docs/openapi.json",
    redoc_url="/docs",
)
app.include_router(api_router)


def main() -> None:
    uvicorn.run("fastapis.main:app", host="0.0.0.0")
