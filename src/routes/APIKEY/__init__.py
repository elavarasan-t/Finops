from fastapi import APIRouter

from . import testAPIKEY, generateAPIKEY

router = APIRouter()

router.include_router(testAPIKEY.router)
router.include_router(generateAPIKEY.router)