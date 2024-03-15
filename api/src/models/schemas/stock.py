from pydantic import BaseModel, EmailStr

class UserStockSchema(BaseModel):
    user_id: str
    name: str
    symbol: str
    amount: int

    class Config:
        extra = "forbid"

class StockSchema(BaseModel):
    name: str
    symbol: str
    amount: int
    price: float

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