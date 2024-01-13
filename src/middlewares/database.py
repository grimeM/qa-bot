import logging
from typing import Callable, Awaitable, Any

from attrs import define
from sqlalchemy.orm import Session, sessionmaker
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


logger = logging.getLogger(__name__)


@define
class SessionMiddleware(BaseMiddleware):
    """Provides a `sqlalchemy.orm.Session` instance."""

    session_maker: sessionmaker[Session]
    session_key: str = "session"

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        with self.session_maker() as session:
            data[self.session_key] = session
            return await handler(event, data)
