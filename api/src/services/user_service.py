from typing import List
from uuid import uuid4
from models.schemas.user import AddBalanceSchema
from repositories.user_repository import UserRepository

from sqlalchemy.orm import Session

from exceptions.database_exceptions import DatabaseExceptions
from models.models import User


class UserService:

    @staticmethod
    async def get_by_id(id: int, db: Session) -> User:
        user = await UserRepository.get_by_id(id, db)
        return user


    @staticmethod
    async def update(user: User, db: Session) -> User:
        user = await UserRepository.patch(user, db)
        return user    


    @staticmethod
    async def add_balance(request: AddBalanceSchema, db: Session) -> User:
        user = await UserRepository.get_by_id(request.userId, db)
        user.cash_balance += request.amount
        return await UserRepository.patch(user, db)
        
    