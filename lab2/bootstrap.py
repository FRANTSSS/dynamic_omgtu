import os

from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv

from bot import TelegramBotFactory
from ioc_container import ioc
from repository import (
    MemoryStorageFactory,
    RedisFactory
)
from service import (
    UserService,
    UserServiceImpl
)

__all__ = [
    "bootstrap"
]


def bootstrap():
    load_dotenv()
    bot_token = os.environ.get("TOKEN")
    host = os.environ.get("REDIS_HOST")
    port = os.environ.get("REDIS_PORT")
    db = os.environ.get("REDIS_DB")

    db_factory = RedisFactory(
        host=host,
        port=int(port),
        db=int(db)
    )
    repository = db_factory.get_notes_repository()

    service = UserServiceImpl(repository)
    ioc.set_instance(UserService, service)

    storage = MemoryStorageFactory().get_storage()
    bot = TelegramBotFactory(bot_token).get_telegram_bot()
    dp = Dispatcher(bot, storage=storage)

    ioc.set_instance(Dispatcher, dp)
