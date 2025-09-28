import logging

from fastapi import FastAPI
import uvicorn

from fastapis.api import api_router
from fastapis.logging import configure_logging

log = logging.getLogger(__name__)

configure_logging()

app = FastAPI(
    description="Welcome to FastAPIs' documentation! Here you will able to discover all of the ways you can interact with the APIs.",
    root_path="/fastapis/v1",
    docs_url=None,
    openapi_url="/docs/openapi.json",
    redoc_url="/docs",
)
app.include_router(api_router)


def main() -> None:
    log.info("Starting FastAPIs...")
    uvicorn.run("fastapis.main:app", host="0.0.0.0")
