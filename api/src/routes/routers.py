from fastapi import APIRouter

from controllers import user_controllers, stocks_controllers

api_router = APIRouter(prefix="/api/v0")

api_router.include_router(user_controllers.router, tags=["User"], prefix="/user")
api_router.include_router(stocks_controllers.router, tags=["Stocks"], prefix="/stocks")
