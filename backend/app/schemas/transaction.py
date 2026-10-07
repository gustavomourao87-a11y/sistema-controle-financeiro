from pydantic import BaseModel


class TransactionCreate(BaseModel):
    user_id: int
    amount: float
    description: str
    type: str
    category: str
    date: str