from fastapi import FastAPI
from utils import limiter
from src.routes.Azure import router as azure_router

app = FastAPI()

app.state.limiter = limiter

API_PREFIX = "/api"

app.include_router(azure_router, prefix=API_PREFIX)


