import logging
from typing import List

from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from exceptions.database_exceptions import DatabaseExceptions
from models.models import StockTransaction

logger = logging.getLogger(__name__)


class StockTransactionRepository:
    
    @staticmethod
    async def create(stockTransaction: StockTransaction, db: Session) -> None:
        try:
            db.add(stockTransaction)
            db.commit()
            db.refresh(stockTransaction)
        except IntegrityError as integrity_error:
            logger.error(integrity_error, exc_info=True)
            DatabaseExceptions.throw_db_integrity_error(integrity_error)
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error(e)


    @staticmethod
    async def get_by_symbol(symbol: str, db: Session) -> List[StockTransaction]:
        try:
            stockTransaction = db.query(StockTransaction).filter_by(symbol = symbol).first()
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error(e)

        if not StockTransaction:
            logger.error(f"The stockTransaction_id: {id} does not exist")
            DatabaseExceptions.throw_not_found_error("StockTransaction")
        return stockTransaction
    

    @staticmethod
    async def get_user_holdings(user_id: int, db: Session) -> List[StockTransaction]:
        try:
            holdings = db.query(StockTransaction.symbol, 
                                StockTransaction.user_id,
                                func.sum(StockTransaction.amount).label('amount')
                        ).filter_by(
                            user_id = user_id,
                        ).group_by(
                            StockTransaction.symbol, StockTransaction.user_id
                        ).having(
                            func.sum(StockTransaction.amount) > 0
                        ).all()
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error(e)

        if not holdings:
            logger.error(f"Can't retrieve holdings for user_id: {user_id}")
            DatabaseExceptions.throw_not_found_error("stockTransaction")
        return holdings


    @staticmethod
    async def patch(stockTransaction: StockTransaction, db: Session):
        """Updates a stockTransaction record in DB"""
        try:
            db.add(stockTransaction)
            db.commit()
        except IntegrityError as integrity_error:
            logger.error(integrity_error, exc_info=True)
            DatabaseExceptions.throw_db_integrity_error(integrity_error)
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error(e)
