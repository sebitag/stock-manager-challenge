from typing import List
from uuid import uuid4
from api.src.models.schemas.user import AddBalanceSchema
from api.src.repositories.user_repository import UserRepository

from sqlalchemy.orm import Session

from exceptions.database_exceptions import DatabaseExceptions
from models.models import User


class UserService:

    @staticmethod
    async def get_by_id(id: str, db: Session) -> User:
        user = await UserRepository.get_by_id(id, db)
        return user


    @staticmethod
    async def update(user: User, db: Session) -> User:
        return await UserRepository.patch(user, db)