from fastapi import APIRouter, HTTPException, Depends
from dependency import validateAPIKEY

router = APIRouter(prefix='/auth', tags=["Auth"], dependencies=[Depends(validateAPIKEY.validate_api_key)])

@router.get('/secure')
async def read_api_key():
    try:
        return {
        "Response": "Access Granted"
    }
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid API")