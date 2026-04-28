from fastapi import APIRouter, Request, Response, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.concurrency import run_in_threadpool
from utils import AzureAuth
from src.schema import ResourceGroupIdRequest, Credentials
from utils import limiter
from src.controller import get_azure_resources

router = APIRouter(tags=["Azure/Inventory"])

@router.post('/resources')
@limiter.limit("50/minute")
async def list_resources(Credential: Credentials, Data: ResourceGroupIdRequest, request: Request, response: Response):
    try:
        azure_auth = AzureAuth(Credential=Credential)
        credentials = azure_auth.authenticate()
        response_body = await run_in_threadpool(get_azure_resources, credentials, Data.resource_group_id)
        
        return { 
            "success": True, 
            "status_code": status.HTTP_200_OK,
            "data": response_body,
            "errors": None
         }
    except HTTPException as exc:
        raise exc
    
    except Exception as error:
        return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={
            "success": False,
            "status_code": status.HTTP_404_NOT_FOUND,
            "data": [],
            "error": str(error)
        },
        headers=dict(response.headers)
    ) 