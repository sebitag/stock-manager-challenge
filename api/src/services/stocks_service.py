from typing import List
from uuid import uuid4

from sqlalchemy.orm import Session

from models.models import StockBuy
from api.src.models.schemas.stock import BuyStockSchema, StockSchema
from api.src.repositories.stockbuy_repository import StockBuyRepository


class StocksService:


    @staticmethod
    async def get_all(db: Session) -> List[StockSchema]:
        # hit API to get all stocks with their prices
        return []

    @staticmethod
    async def get_stock_price(symbol: str, db: Session) -> float:
        # hit API to get stock price by symbol
        return 1.1

    @staticmethod
    async def buy(request: BuyStockSchema, db: Session) -> StockBuy:
        # await CompanyRepository.create(request, db)
        stock = StockBuy(
            # id=uuid4(),
            user_id=request.user_id,
            symbol=request.symbol,
            amount=request.amount
        )
        StockBuyRepository.create(stock, db)