import logging

from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message


router = Router(name=__name__)
logger = logging.getLogger(__name__)


@router.message(Command("start"))
async def start(message: Message, command: CommandObject):
    return await message.answer(
        "Привет! Задай мне вопрос, и я постараюсь на него ответить."
    )
