from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse
from fastapi.concurrency import run_in_threadpool
from utils import AzureAuth
from src.schema import ResourceGroupIdRequest, Credentials
from utils import limiter
from src.controller import get_azure_resource_group

router = APIRouter(tags=["Azure/Inventory"])

@router.post('/resourceGroup')
@limiter.limit("50/minute")
async def resource_group(Credential: Credentials, Data: ResourceGroupIdRequest, request: Request, response: Response):
    try:
        azure_auth = AzureAuth(Credential=Credential)
        credentials = azure_auth.authenticate()
        response_body = [await run_in_threadpool(get_azure_resource_group, credentials, Data.resource_group_id)]
        
        return { 
            "success": True, 
            "status_code": 200,
            "data": response_body,
            "errors": None
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