from pydantic import BaseModel, EmailStr, HttpUrl

class AddBalanceSchema(BaseModel):
    userId: str
    amount: float

    class Config:
        extra = "forbid"
