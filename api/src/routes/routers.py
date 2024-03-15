from fastapi import APIRouter

from controller import stock_controller
from controller import user_controller

api_router = APIRouter(prefix="/api/v0")

api_router.include_router(user_controller.router, tags=["User"], prefix="/user")
api_router.include_router(stock_controller.router, tags=["Stocks"], prefix="/stocks")
