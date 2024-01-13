import logging
from pathlib import Path

from aiogram import Dispatcher

from handlers import commands, qa
from qa.parse import parse_questions
from config import Config


logger = logging.getLogger(__name__)


def create_dispatcher(config: Config) -> Dispatcher:
    question_items = parse_questions(config.questions_file)

    if not question_items:
        logger.warn("No questions detected!")

    dp = Dispatcher(question_items=question_items, config=config)

    dp.include_routers(
        commands.router,
        qa.router,
    )

    return dp
