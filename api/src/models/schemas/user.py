from pydantic import BaseModel, EmailStr, HttpUrl

class AddBalanceSchema(BaseModel):
    id: str
    amount: float

    class Config:
        extra = "forbid"
