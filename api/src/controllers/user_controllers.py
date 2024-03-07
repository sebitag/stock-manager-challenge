from typing import List
from api.src.models.schemas.stock import UserStockSchema

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.database import get_db
from api.src.models.schemas.user import AddBalanceSchema
from api.src.services.user_service import UserService

router = APIRouter()


@router.get(
    "/balance/{id}",
    status_code=status.HTTP_200_OK,
    name="Get user balance",
)
async def get_balance(id:str, db: Session = Depends(get_db)):
    user = await UserService.get_by_id(id, db)
    return user.cash_balance


@router.post(
    "/add-balance",
    status_code=status.HTTP_200_OK,
    name="Add balance to user",
)
async def add_balance(request: AddBalanceSchema, db: Session = Depends(get_db)):
    return await UserService.add_balance(id, request, db)


@router.get(
    "/holdings/{user_id}",
    status_code=status.HTTP_200_OK,
    name="Get user holdings",
    response_model=List[UserStockSchema]
)
async def get_user_holdings(user_id: str, db: Session = Depends(get_db)):
    return await UserService.get_holdings(db, user_id)

