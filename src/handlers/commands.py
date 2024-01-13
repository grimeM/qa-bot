import logging

from sqlalchemy.orm import Session
from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from i18n import TranslatorRunner
from database import models


router = Router(name=__name__)
logger = logging.getLogger(__name__)


@router.message(Command("start"))
async def start(
    message: Message,
    command: CommandObject,
    user: models.User | None,
    i18n: TranslatorRunner,
    session: Session,
):
    pass
    # if user:
    #     if user.wallet:
    #         page = pages.RegistrationOK(user, i18n)
    #     else:
    #         page = pages.RegisterWallet(i18n)
    #     return await page.answer(message)

    # telegram_user = message.from_user
    # if not telegram_user:
    #     logger.error("expected event.from_user to not be None")
    #     return await message.answer(i18n.error.try_again())

    # source = "empty" if not command.args else command.args
    # language_code = telegram_user.language_code if telegram_user.language_code else "en"

    # api_request = api.CreateUserAPIRequest(
    #     telegram_id=telegram_user.id,
    #     username=telegram_user.username,
    #     source=source,
    #     interface_language=language_code,
    #     language_code=language_code,
    # )

    # try:
    #     user = await crud.create_user(session, api_request)

    # except Exception as e:
    #     logger.error(e)
    #     text = i18n.error.unavailable()
    #     if not config.production:
    #         text += format_error(e)
    #     return await message.answer(text)

    # page = pages.RegisterWallet(i18n)
    # return await page.answer(message)


@router.message()
async def echo(message: Message) -> Message:
    return await message.answer(message.text or "Could you repeat that?")
