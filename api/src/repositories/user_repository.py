import logging

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from exceptions.database_exceptions import DatabaseExceptions
from models.models import User

logger = logging.getLogger(__name__)


class UserRepository:

    @staticmethod
    async def get_by_id(id: int, db: Session) -> User:
        try:
            user = db.query(User).filter_by(id = id).first()
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
            DatabaseExceptions.throw_internal_server_error(e)

    @staticmethod
    async def delete(id: int, db: Session) -> None:
        """Deletes an User record from DB"""
        company = await UserRepository.get_by_id(id, db)
        try:
            db.delete(company)
            db.commit()
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error(e)

    @staticmethod
    async def patch(user: User, db: Session) -> User:
        """Updates a company record in DB"""
        try:
            db.add(user)
            db.commit()
        except IntegrityError as integrity_error:
            logger.error(integrity_error, exc_info=True)
            DatabaseExceptions.throw_db_integrity_error(integrity_error)
        except Exception as e:
            logger.error(e, exc_info=True)
            DatabaseExceptions.throw_internal_server_error(e)
        return user
