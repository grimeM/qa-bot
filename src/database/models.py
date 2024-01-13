from __future__ import annotations

from datetime import datetime
from typing import Any

from sqlalchemy import BigInteger, UUID
from sqlalchemy.sql import functions as func
from sqlalchemy.sql import expression as expr
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import declared_attr
from sqlalchemy.schema import FetchedValue


class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id: Mapped[str] = mapped_column(
        UUID,
        primary_key=True,
        server_default="gen_random_uuid()",
        sort_order=-10,
    )

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), sort_order=99
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), server_onupdate=FetchedValue(), sort_order=99
    )

    def __repr__(self) -> str:
        properties = [
            f"{column.name}={getattr(self, column.name)!r}"
            for column in self.__table__.columns
        ]
        return f"<{self.__class__.__name__}({', '.join(properties)})>"

    def __str__(self) -> str:
        properties = [
            f"{name}={value!r}"
            for column in self.__table__.columns
            if (name := column.name) not in ("created_at", "updated_at")
            and (value := getattr(self, name)) is not None
        ]
        return f"{self.__class__.__name__}({', '.join(properties)})"


class User(Base):
    telegram_id: Mapped[BigInteger] = mapped_column(unique=True, index=True)
    username: Mapped[str | None]

    wallet: Mapped[str | None]

    is_admin: Mapped[bool]
    is_active: Mapped[bool]
    is_banned: Mapped[bool]

    source: Mapped[str]

    language_code: Mapped[str]
    interface_language: Mapped[str]
