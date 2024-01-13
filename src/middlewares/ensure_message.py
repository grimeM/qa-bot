import logging
from typing import Callable, Awaitable, Dict, Any

from attrs import define
from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery


logger = logging.getLogger(__name__)


@define
class EnsureMessage(BaseMiddleware):
    """Exposes `CallbackQuery.message` to handlers."""

    message_key: str = "message"

    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any],
    ):
        if not event.message:
            logger.error(f"event does not contain message: {event=}")
            return

        data[self.message_key] = event.message

        return await handler(event, data)
