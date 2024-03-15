import logging
from typing import List

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from exceptions.database_exceptions import DatabaseExceptions
from models.models import StockTransaction

logger = logging.getLogger(__name__)


class StockBuyRepository:
    
    @staticmethod
    async def create(stockBuy: StockTransaction, db: Session) -> None:
        """Creates a StockBuy record on the DB"""
        try:
            db.add(stockBuy)
            db.commit()
            db.refresh(stockBuy)
        except IntegrityError as integrity_error:
            logger.error(integrity_error, exc_info=True)
            DatabaseExceptions.throw_db_integrity_error(integrity_error)
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error(e)


    @staticmethod
    async def get_by_symbol(symbol: str, db: Session) -> List[StockTransaction]:
        """Gets a single StockBuy's records from the DB by symbol"""
        try:
            stockBuy = db.query(StockTransaction).filter_by(symbol = symbol).first()
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error(e)

        if not StockTransaction:
            logger.error(f"The StockBuy_id: {id} does not exist")
            DatabaseExceptions.throw_not_found_error("StockBuy")
        return stockBuy
    

    @staticmethod
    async def get_by_user_id(user_id: str, db: Session) -> List[StockTransaction]:
        """Gets a single StockBuy's records from the DB by symbol"""
        try:
            stockBuy = db.query(StockTransaction).filter_by(user_id = user_id).first()
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error(e)

        if not stockBuy:
            logger.error(f"The StockBuy_id: {id} does not exist")
            DatabaseExceptions.throw_not_found_error("StockBuy")
        return stockBuy


    @staticmethod
    async def patch(stockBuy: StockTransaction, db: Session):
        """Updates a StockBuy record in DB"""
        try:
            db.add(stockBuy)
            db.commit()
        except IntegrityError as integrity_error:
            logger.error(integrity_error, exc_info=True)
            DatabaseExceptions.throw_db_integrity_error(integrity_error)
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error(e)
