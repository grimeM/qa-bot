from abc import ABC, abstractmethod

from aiogram.types import InlineKeyboardMarkup, Message


class BaseComponent(ABC):
    @abstractmethod
    def render(self) -> tuple[str, InlineKeyboardMarkup | None]:
        ...

    async def answer(self, message: Message) -> Message:
        text, kb = self.render()
        return await message.answer(text=text, reply_markup=kb)
