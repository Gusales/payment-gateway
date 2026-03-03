from fastapi import APIRouter

from .base_responses import BASE_RESPONSES

router = APIRouter(
    prefix="/api",
    responses=BASE_RESPONSES
)