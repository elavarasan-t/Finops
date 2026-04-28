from fastapi import APIRouter, Request, Response, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.concurrency import run_in_threadpool
from src.schema import Credentials
from src.controller import get_azure_subscriptions
from utils import AzureAuth
from utils import limiter

router = APIRouter(tags=["Azure/Inventory"])

@router.post('/subscriptions')
@limiter.limit("50/minute")
async def list_subscriptions(
    Credential: Credentials,
    request: Request,
    response: Response
):
    try:

        azure_auth = AzureAuth(Credential=Credential)
        credentials = azure_auth.authenticate()
        response_body = await run_in_threadpool(get_azure_subscriptions, credentials)

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
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "data": [],
                "error" : str(error)
                },
            headers=dict(response.headers)
        )
    