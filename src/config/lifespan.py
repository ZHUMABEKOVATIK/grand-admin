from contextlib import asynccontextmanager
from fastapi import FastAPI

from . import engine, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)
        
    yield
    await engine.dispose()