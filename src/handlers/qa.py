import logging

from aiogram import Router
from aiogram.types import Message

from qa.answer import QuestionItem, get_answer
from config import Config


router = Router(name=__name__)
logger = logging.getLogger(__name__)


@router.message()
async def handle_question(
    message: Message, question_items: list[QuestionItem], config: Config
):
    text = message.text or ""
    answer, score = get_answer(text, question_items)
    if not answer or score < config.answer_threshold:
        return await message.answer("Ответа на этот вопрос в базе данных нет.")
    return await message.answer(answer)
