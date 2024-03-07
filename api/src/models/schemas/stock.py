from pydantic import BaseModel, EmailStr

class UserStockSchema(BaseModel):
    user_id: str
    name: str | None
    symbol: str | None
    amount: int | None

    class Config:
        extra = "forbid"

class StockSchema(BaseModel):
    name: str | None
    symbol: str | None
    amount: int | None
    price: float | None

    class Config:
        extra = "forbid"

class BuyStockSchema(BaseModel):
    user_id: str
    symbol: str
    amount: int

    class Config:
        extra = "forbid"

class SellStockSchema(BaseModel):
    user_id: str
    symbol: str
    amount: int

    class Config:
        extra = "forbid"