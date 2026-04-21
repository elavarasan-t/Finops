import os
from dotenv import load_dotenv
from fastapi.security.api_key import APIKeyHeader
from fastapi import HTTPException, Security
from datetime import datetime, timezone

load_dotenv()

API_KEY_NAME = os.getenv("API_KEY_NAME")
API_KEY = os.getenv("API_KEY")
EXPIRY_TIME = os.getenv("API_KEY_EXP")

API_KEY_HEADER = APIKeyHeader(name=API_KEY_NAME,auto_error=False)

async def  validate_api_key(api_key: str = Security(API_KEY_HEADER)):

    expiry_at = datetime.fromisoformat(EXPIRY_TIME)

    now = datetime.now(timezone.utc)

    if api_key != API_KEY:
        raise HTTPException(
            status_code=400,
            detail="Invalid API KEY"
        )
    
    if now > expiry_at:
        raise HTTPException(status_code=403, detail="API Key Expired")