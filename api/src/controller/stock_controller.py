from typing import List
from services.user_service import UserService

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.database import get_db
from models.schemas.stock import BuyStockSchema, SellStockSchema, UserStockSchema, StockSchema
from services.stocks_service import StocksService

router = APIRouter()

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    name="Get all available stocks",
    response_model=List[StockSchema]
)
async def get_all(db: Session = Depends(get_db)):
    # API hit to get all stocks
    return await StocksService.get_all(db)


@router.post(
    "/buy",
    status_code=status.HTTP_200_OK,
    name="Buy stocks for user",
    response_model=UserStockSchema
)
async def buy(request: BuyStockSchema, db: Session = Depends(get_db)):
    # get user balance
    user = await UserService.get_by_id(request.user_id, db)

    # get stock price
    stock_price = StocksService.get_stock_price(request.symbol, db)
    # if valid update user balance
    if (user.cash_balance - stock_price) < 0:
        return "Insufficient balance"
    # update user holdings
    await StocksService.buy(request, db)
    # update user balance
    user.cash_balance -= stock_price
    await UserService.update(user, db)

    return user.cash_balance


@router.post(
    "/sell/{user_id}/{symbol}",
    status_code=status.HTTP_200_OK,
    name="Sell user's stocks",
    response_model=UserStockSchema
)
async def sell(request: SellStockSchema, db: Session = Depends(get_db)):
    # get user holdings
    # get stock price
    # update user holdings
    # update user balance
    return await StocksService.sell(request, db)

