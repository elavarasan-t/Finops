from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse
from fastapi.concurrency import run_in_threadpool
from utils import authenticate
from utils import limiter
from src.controller import get_azure_subscriptions

router = APIRouter(tags=["Azure/Inventory"])

@router.get('/subscriptions')
@limiter.limit("50/minute")
async def list_subscriptions(
    request: Request,
    response: Response
):
    try:
        credentials = authenticate()
        response_body = await run_in_threadpool(get_azure_subscriptions, credentials)
        
        return {
            "response" : response_body
        }
    
    except Exception as error:
        return JSONResponse(
            status_code=500,
            content={"detail": str(error)},
            headers=dict(response.headers)
        )
    