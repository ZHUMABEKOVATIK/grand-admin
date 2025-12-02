import uvicorn

from fastapi import FastAPI

from .api import routers
from .config import _lifespan, setup_cors

app = FastAPI(
    title="Grand",
    version="1.0.1",
    lifespan=_lifespan
)

setup_cors(
    app=app
)

app.include_router(routers)

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        port=8030
    )