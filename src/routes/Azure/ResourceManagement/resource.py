from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse
from fastapi.concurrency import run_in_threadpool
from utils import AzureAuth
from src.schema import ResourceIdRequest, Credentials
from utils import limiter
from src.controller import get_azure_ressource

router = APIRouter(tags=["Azure/Inventory"])

@router.post('/resource')
@limiter.limit("50/minute")
async def resource(Credential: Credentials, Data: ResourceIdRequest, request: Request, response: Response):
    try:
        azure_auth = AzureAuth(Credential=Credential)
        credentials = azure_auth.authenticate()
        response_body = [await run_in_threadpool(get_azure_ressource, credentials, Data.resource_id)]
        
        return {
            "success": True, 
            "data": response_body,
            "errors": None,
            "status_code": 200 
        }
        
    except Exception as error:
        return JSONResponse(
            status_code=404,
            detail={
                "success": False,
                "status_code": 404,
                "data": [],
            },
            headers=dict(response.headers)
        )