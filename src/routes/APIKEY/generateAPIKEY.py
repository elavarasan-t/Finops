from fastapi import APIRouter, HTTPException
from core.APIKEYGENERATION import generate_api_key


router = APIRouter(prefix='/auth', tags=["Auth"])


@router.get('/generateKey')
async def read_api_key():
    try:
        generate_api_key()
        return {
        "response": "API KEY Generated Successfully."
    }
    except Exception as e:
        raise HTTPException(status_code=400, detail="API KEY Creation Failed")