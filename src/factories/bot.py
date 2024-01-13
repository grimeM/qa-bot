from aiogram import Bot
from aiogram.enums import ParseMode


def create_bot(token: str) -> Bot:
    bot = Bot(
        token=token,
        disable_web_page_preview=True,
        parse_mode=ParseMode.HTML,
    )
    return bot
