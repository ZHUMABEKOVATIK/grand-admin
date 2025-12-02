from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, func
from datetime import datetime

class Base(AsyncAttrs, DeclarativeBase):
    pass

class DefaultDeclarativeBase(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

class FullDeclarativeBase(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())