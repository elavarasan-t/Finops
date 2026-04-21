from fastapi import FastAPI
from utils import limiter
from src.routes.APIKEY import router as api_key_router
from src.routes.Azure import router as azure_router

#import logging

#logging.basicConfig(level=logging.DEBUG)
#logging.getLogger("azure.core.pipeline.policies.retry").setLevel(logging.DEBUG)

app = FastAPI()

app.state.limiter = limiter

API_PREFIX = "/api"

app.include_router(api_key_router, prefix=API_PREFIX)

app.include_router(azure_router, prefix=API_PREFIX)


