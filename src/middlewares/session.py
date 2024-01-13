import logging
from typing import Callable, Awaitable, Any

from attrs import define, field
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from sqlalchemy.orm import sessionmaker, Session


logger = logging.getLogger(__name__)


@define
class SessionProvider(BaseMiddleware):
    """Provides a `sqlalchemy.orm.Session` instance."""

    session_maker: sessionmaker[Session]

    _key: str = field(default="session", kw_only=True)

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ):
        with self.session_maker() as session:
            data[self._key] = session
            return await handler(event, data)
