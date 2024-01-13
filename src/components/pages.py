from collections.abc import Sequence

from attrs import define
from aiogram import html
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.filters.callback_data import CallbackData
from i18n import TranslatorRunner
from components import BaseComponent
from components import keyboards as K


@define
class Page(BaseComponent):
    text: str
    kb: InlineKeyboardMarkup | None = None

    def render(self) -> tuple[str, InlineKeyboardMarkup | None]:
        return self.text, self.kb


@define
class ReplyKBPage(Page):
    kb: ReplyKeyboardMarkup | None = None

    def render(self) -> tuple[str, ReplyKeyboardMarkup | None]:
        return self.text, self.kb
