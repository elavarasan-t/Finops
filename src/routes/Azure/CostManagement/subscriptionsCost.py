from fastapi import APIRouter, Request, Response
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import JSONResponse
from utils import authenticate
from fastapi.concurrency import run_in_threadpool
from utils import limiter
from src.controller import get_subscriptions_cost

router = APIRouter(tags=["Azure/CostManagement/Cost"])

@router.get('/subscriptionsCost')
@limiter.limit("50/minute")
async def subscriptions_cost(request: Request, response: Response):
    try:
        credential = authenticate()

        cost_response = await run_in_threadpool(get_subscriptions_cost, credential)

        return { "response": cost_response }
    
    except Exception as error:
        return JSONResponse(
            status_code=500,
            content={"detail": str(error)},
            headers=dict(response.headers)
        )