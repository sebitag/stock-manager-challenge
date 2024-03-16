from pydantic import BaseModel, EmailStr, HttpUrl

class AddBalanceSchema(BaseModel):
    userId: int
    amount: float

    class Config:
        extra = "forbid"
