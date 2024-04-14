import logging
import sys

from aiogram.fsm.storage.memory import MemoryStorage

import runners

from aiogram.fsm.storage.redis import Redis, RedisStorage
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from middlewares.outer.database import DataBaseSession
from middlewares.outer.throttling import ThrottlingMiddleware

from database.engine import create_database_pool

from settings import settings

from handlers.user import question_answer, base
from handlers.admin import admin, add_new_question, get_list_question, delete_question, edit_contacts
from handlers.user import contacts


def main():
    session_pool = create_database_pool(settings.create_dsn_postgresql(), settings.sqlalchemy_logging)

    if settings.use_redis:
        redis: Redis = Redis(host=settings.redis_host)
        storage: RedisStorage = RedisStorage(redis=redis)
        dp = Dispatcher(storage=storage)
    else:
        dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(
        base.router,
        question_answer.router,
        admin.router,
        add_new_question.router,
        get_list_question.router,
        delete_question.router,
        contacts.router,
        edit_contacts.router
    )
    dp.update.middleware(DataBaseSession(session_pool))
    dp.message.middleware(ThrottlingMiddleware(settings.throttle_time_spin, settings.throttle_time_other))

    bot = Bot(settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    if settings.use_webhook:
        return runners.run_webhook(dp=dp, bot=bot)
    else:
        return runners.run_polling(dp=dp, bot=bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()
