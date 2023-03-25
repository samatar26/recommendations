from models import Base
from sqlalchemy.orm import Mapped, mapped_column


class Account(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True)
