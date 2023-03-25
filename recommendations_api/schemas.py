from pydantic import BaseModel


class AccountPayload(BaseModel):
    id: int
