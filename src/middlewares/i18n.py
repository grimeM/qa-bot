import logging
from typing import Callable, Awaitable, Any, TYPE_CHECKING

from attrs import define, field
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from fluentogram import TranslatorHub

from database import models

if TYPE_CHECKING:
    from i18n.stub import TranslatorRunner  # type: ignore
else:
    from fluentogram import TranslatorRunner


logger = logging.getLogger(__name__)


@define
class I18nProvider(BaseMiddleware):
    """Provides `TranslatorRunner`. May use a `user` instance."""

    _Event = Message | CallbackQuery

    translator_hub: TranslatorHub
    default_locale: str = "en"

    _key: str = field(default="i18n", kw_only=True)
    _user_key: str = field(default="user", kw_only=True)

    async def __call__(
        self,
        handler: Callable[[_Event, dict[str, Any]], Awaitable[Any]],
        event: _Event,
        data: dict[str, Any],
    ):
        user = data.get(self._user_key)

        if isinstance(user, models.User):
            language_code = user.interface_language
        elif event.from_user and event.from_user.language_code:
            language_code = event.from_user.language_code
        else:
            language_code = self.default_locale

        i18n = self.translator_hub.get_translator_by_locale(language_code)
        data[self._key] = i18n
        return await handler(event, data)
