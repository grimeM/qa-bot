import asyncio
import logging

from factories.bot import create_bot
from factories.dispatcher import create_dispatcher
from config import Config
from log import setup_base_logging, setup_file_logging


logger = logging.getLogger(__name__)


async def main() -> None:
    config = Config.model_validate({})
    config.run_dir.mkdir(exist_ok=True)

    log_level = logging.INFO if config.production else logging.DEBUG
    log_file = config.run_dir / "telegram-bot.log"
    log_file.touch(exist_ok=True)

    setup_base_logging(level=log_level)
    setup_file_logging(log_file, level=log_level)

    dp = create_dispatcher(config)
    bot = create_bot(token=config.telegram_api_token.get_secret_value())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
