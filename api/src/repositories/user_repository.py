import logging
from typing import List

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from exceptions.database_exceptions import DatabaseExceptions
from models.models import User
from api.src.repositories.stockbuy_repository import CompanyRepository

logger = logging.getLogger(__name__)


class UserRepository:

    @staticmethod
    async def get_by_id(id: str, db: Session) -> User:
        try:
            user = db.query(User).filter(User.id == id).first()
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error(e)
        if not user:
            logger.error(f"The User_id: {id} does not exist")
            DatabaseExceptions.throw_not_found_error("User")
        return user

    @staticmethod
    async def create(user: User, db: Session):
        try:
            db.add(user)
            db.commit()
            db.refresh(user)
        except IntegrityError as integrity_error:
            logger.error(integrity_error, exc_info=True)
            DatabaseExceptions.throw_db_integrity_error(integrity_error)
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error()

    @staticmethod
    async def delete(id: str, db: Session) -> None:
        """Deletes an User record from DB"""
        company = await UserRepository.get_by_id(id, db)
        try:
            db.delete(company)
            db.commit()
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error()

    @staticmethod
    async def patch(user: User, db: Session):
        """Updates a company record in DB"""
        try:
            db.add(user)
            db.commit()
        except IntegrityError as integrity_error:
            logger.error(integrity_error, exc_info=True)
            DatabaseExceptions.throw_db_integrity_error(integrity_error)
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error()
