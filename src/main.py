import asyncio
import logging

from redis.asyncio import Redis
from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator

from config import Config
from database import init_db
from factories.bot import create_bot
from factories.dispatcher import create_dispatcher
from log import setup_base_logging, setup_file_logging


logger = logging.getLogger(__name__)


def setup_translation() -> TranslatorHub:
    en_translator = FluentTranslator(
        "en", FluentBundle.from_files("en-US", ("./i18n/en.ftl",))
    )
    ru_translator = FluentTranslator(
        "ru", FluentBundle.from_files("ru", ("./i18n/ru.ftl",))
    )
    return TranslatorHub(
        {"en": ("en",), "ru": ("ru", "en")},
        [en_translator, ru_translator],
    )


async def main() -> None:
    config = Config.model_validate({})
    config.run_dir.mkdir(exist_ok=True)

    log_level = logging.INFO if config.production else logging.DEBUG
    log_file = config.run_dir / "telegram-bot.log"
    log_file.touch(exist_ok=True)

    setup_base_logging(level=log_level)
    setup_file_logging(log_file)

    redis = Redis.from_url(config.redis_url)
    session_maker = init_db(config.database_url)

    dp = create_dispatcher(redis=redis, session_maker=session_maker)
    bot = create_bot(token=config.telegram_api_token.get_secret_value())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
