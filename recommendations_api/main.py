from fastapi import Depends, FastAPI
from recommendations_api.dependencies import get_session
from recommendations_api.schemas import AccountPayload
from models.account import Account
from sqlalchemy.orm import Session

app = FastAPI()


@app.get("/")
def get_home() -> str:
    return "Hello world!"


@app.post("/")
def post_home(account: AccountPayload, session: Session = Depends(get_session)):
    session.add(Account(id=account.id))
    session.commit()
    return
