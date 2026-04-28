from fastapi import APIRouter

from . import generateAPIKEY

router = APIRouter()

router.include_router(generateAPIKEY.router)