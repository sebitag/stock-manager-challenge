from typing import List
from services.user_service import UserService

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.database import get_db
from models.schemas.stock import StockTransactionSchema, UserStockSchema, StockSchema
from services.stocks_service import StocksService

router = APIRouter()

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    name="Get all available stocks",
    response_model=List[StockSchema]
)
async def get_all():
    return await StocksService.get_all()


@router.post(
    "/buy",
    status_code=status.HTTP_200_OK,
    name="Buy stocks for user",
)
async def buy(request: StockTransactionSchema, db: Session = Depends(get_db)):
    user = await UserService.get_by_id(request.user_id, db)
    stock_price = await StocksService.get_stock_price(request.symbol)
    new_balance = user.cash_balance - (stock_price * request.amount)

    if new_balance < 0:
        return "Insufficient balance"
    await StocksService.buy(request, db)
    
    user.cash_balance = new_balance
    await UserService.update(user, db)

    return user.cash_balance

@router.post(
    "/sell",
    status_code=status.HTTP_200_OK,
    name="Sell user's stocks",
)
async def sell(request: StockTransactionSchema, db: Session = Depends(get_db)):
    user = await UserService.get_by_id(request.user_id, db)
    stock_price = await StocksService.get_stock_price(request.symbol)
    new_balance = user.cash_balance + (stock_price * request.amount)

    await StocksService.sell(request, db)
    user.cash_balance = new_balance
    await UserService.update(user, db)

    return user.cash_balance

