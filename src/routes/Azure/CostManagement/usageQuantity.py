from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse
from fastapi.concurrency import run_in_threadpool
from utils import AzureAuth
from src.schema import CostRequest, Credentials
from utils import limiter
from src.controller import get_usage

router = APIRouter(tags=["Azure/CostManagement/Usage"])

@router.post('/usage')
@limiter.limit("50/minute")
async def usage(Credential: Credentials, Data: CostRequest, request: Request, response: Response):
    try:
        azure_auth = AzureAuth(Credential=Credential)
        credentials = azure_auth.authenticate()
        data = []
        usage_response = await run_in_threadpool(
            get_usage,
            Data.scope,
            credentials,
            Data.grouping,
            Data.start_date,
            Data.end_date,
            Data.granularity
        )

        return {
            "success": True, 
            "status_code": 200,
            "data": data.append(usage_response),
            "errors": None
        }
    
    except Exception as error:
        return JSONResponse(
            status_code=500,
            content={"detail": str(error)},
            headers=dict(response.headers)
        )