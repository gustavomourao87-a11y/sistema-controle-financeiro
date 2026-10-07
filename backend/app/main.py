from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database.tables import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(lifespan=lifespan)