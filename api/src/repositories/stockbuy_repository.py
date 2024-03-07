import logging
from typing import List

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from exceptions.database_exceptions import DatabaseExceptions
from models.models import StockBuy

logger = logging.getLogger(__name__)


class StockBuyRepository:
    
    @staticmethod
    async def create(stockBuy: StockBuy, db: Session) -> None:
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
    async def get_by_symbol(symbol: str, db: Session) -> List[StockBuy]:
        """Gets a single StockBuy's records from the DB by symbol"""
        try:
            StockBuy = db.query(StockBuy).filter(StockBuy.symbol == symbol).first()
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error(e)

        if not StockBuy:
            logger.error(f"The StockBuy_id: {id} does not exist")
            DatabaseExceptions.throw_not_found_error("StockBuy")
        return StockBuy
    

    @staticmethod
    async def get_by_user_id(user_id: str, db: Session) -> List[StockBuy]:
        """Gets a single StockBuy's records from the DB by symbol"""
        try:
            StockBuy = db.query(StockBuy).filter(StockBuy.user_id == user_id).first()
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error(e)

        if not StockBuy:
            logger.error(f"The StockBuy_id: {id} does not exist")
            DatabaseExceptions.throw_not_found_error("StockBuy")
        return StockBuy


    @staticmethod
    async def patch(stockBuy: StockBuy, db: Session):
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
