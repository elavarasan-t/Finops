from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse
from fastapi.concurrency import run_in_threadpool
from utils import authenticate
from utils import limiter
from src.controller import get_tenent_data

router = APIRouter(tags=["Azure/Tenant"])

@router.get('/tenant')
@limiter.limit("50/minute")
async def tenent_details(request: Request, response: Response):
    try:
        credentials = authenticate()
        response = await get_tenent_data(credentials)
    
        return { "response": response }
        
    except Exception as error:
        return JSONResponse(
            status_code=500,
            content={"detail": str(error)},
            headers=dict(response.headers)
        )