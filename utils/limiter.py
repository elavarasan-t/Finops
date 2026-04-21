from slowapi import Limiter
from fastapi import Request

def get_api_key(request: Request):
    return request.headers.get("x-api-key", request.client.host)

limiter = Limiter(
    key_func=get_api_key,
    headers_enabled=True
)