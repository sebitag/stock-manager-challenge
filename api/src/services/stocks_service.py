import os
from typing import List
from uuid import uuid4

import aiohttp
from sqlalchemy.orm import Session
from models.models import StockTransaction
from models.schemas.stock import StockTransactionSchema, StockSchema
from repositories.stocktransaction_repository import StockTransactionRepository
from sqlalchemy import func

FMP_API_KEY = os.getenv('FMP_API_KEY')

class StocksService:

    @staticmethod
    async def get_all() -> List[StockSchema]:
        # Limited to ten stocks to avoid overloading the API
        url = f'https://financialmodelingprep.com/api/v3/quote/AAPL,MSFT,PHM,NFLX,RCL,AVGO,NRG,LRCX,AMZN,GE?apikey={str(FMP_API_KEY or "")}'
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    output = await response.json()
                else:
                    raise Exception("Failed to fetch stocks. Response status:" + str(response.status))
        return output

    @staticmethod
    async def get_stock_price(symbol: str) -> float:
        url = f'https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={str(FMP_API_KEY or "")}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    output = await response.json()
        return output[0]['price']

    @staticmethod
    async def buy(request: StockTransactionSchema, db: Session) -> StockTransaction:
        stock = StockTransaction()
        stock.amount = request.amount
        stock.symbol = request.symbol
        stock.user_id = request.user_id
        stock.price = await StocksService.get_stock_price(request.symbol)
        await StockTransactionRepository.create(stock, db)
        return stock
    
    @staticmethod
    async def sell(request: StockTransactionSchema, db: Session) -> StockTransaction:
        stock = StockTransaction()
        stock.amount = -(request.amount)
        stock.symbol = request.symbol
        stock.user_id = request.user_id
        stock.price = await StocksService.get_stock_price(request.symbol)
        await StockTransactionRepository.create(stock, db)
        return stock
    
    @staticmethod
    async def get_user_holdings(user_id: int, db: Session) -> List[StockTransaction]:
        return await StockTransactionRepository.get_user_holdings(user_id, db)