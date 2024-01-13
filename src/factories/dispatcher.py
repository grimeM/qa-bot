from aiogram import Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from redis.asyncio import Redis
from sqlalchemy.orm import sessionmaker

import middlewares as mw
from handlers import commands


def create_dispatcher(*, redis: Redis, session_maker: sessionmaker) -> Dispatcher:
    storage = RedisStorage(redis)

    dp = Dispatcher(storage=storage)

    session_mw = mw.SessionMiddleware(session_maker)
    dp.message.outer_middleware(session_mw)
    dp.callback_query.outer_middleware(session_mw)

    dp.callback_query.outer_middleware(mw.EnsureMessage())

    dp.callback_query.middleware(CallbackAnswerMiddleware())

    dp.include_routers(
        commands.router,
    )

    return dp
