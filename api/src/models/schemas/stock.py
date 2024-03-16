from pydantic import BaseModel, EmailStr

def to_camel(string: str) -> str:
    words = string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])

class CamelModel(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

class UserStockSchema(CamelModel):
    user_id: int
    symbol: str
    amount: int

class StockSchema(BaseModel):
    name: str
    symbol: str
    price: float

class StockTransactionSchema(CamelModel):
    user_id: int
    symbol: str
    amount: int

class SellStockSchema(BaseModel):
    user_id: int
    symbol: str
    amount: int