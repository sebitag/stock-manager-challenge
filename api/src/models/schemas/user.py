from pydantic import BaseModel, EmailStr, HttpUrl

class AddBalanceSchema(BaseModel):
    user_id: str
    amount: float

    class Config:
        extra = "forbid"
