from attrs import define
from aiogram.filters import BaseFilter
from aiogram.types import Message

from i18n import TranslatorRunner


@define
class I18nFilter(BaseFilter):
    key: str

    async def __call__(self, message: Message, i18n: TranslatorRunner) -> bool:
        return message.text == i18n.get(self.key)
