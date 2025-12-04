from ..config import DefaultDeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, BigInteger

class Users(DefaultDeclarativeBase):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BigInteger, unique = True)
    username: Mapped[str] = mapped_column(String(150), unique = True, nullable = False)
    password: Mapped[str] = mapped_column(String(150), nullable = False)