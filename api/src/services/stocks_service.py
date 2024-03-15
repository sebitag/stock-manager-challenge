from typing import List
from uuid import uuid4

from sqlalchemy.orm import Session

from models.models import StockTransaction
from models.schemas.stock import StockTransactionSchema, SellStockSchema, StockSchema
from repositories.stockbuy_repository import StockBuyRepository


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
    async def buy(request: StockTransactionSchema, db: Session) -> StockTransaction:
        stock = StockTransaction()
        stock.amount = request.amount
        stock.symbol = request.symbol
        stock.user_id = request.user_id
        stock.price = await StocksService.get_stock_price(request.symbol, db)
        await StockBuyRepository.create(stock, db)
        return stock
    
    @staticmethod
    async def sell(request: StockTransactionSchema, db: Session) -> StockTransaction:
        stock = StockTransaction()
        stock.amount = -(request.amount) # negative or a new type?
        stock.symbol = request.symbol
        stock.user_id = request.user_id
        stock.price = await StocksService.get_stock_price(request.symbol, db)
        await StockBuyRepository.create(stock, db)
        return stock