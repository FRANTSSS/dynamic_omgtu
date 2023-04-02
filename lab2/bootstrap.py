import os

from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv

from bot import TelegramBotFactory
from ioc_container import ioc
from repository import MemoryStorageFactory

__all__ = [
    "bootstrap"
]


def bootstrap():
    load_dotenv()
    bot_token = os.environ.get("TOKEN")
    storage = MemoryStorageFactory().get_storage()
    bot = TelegramBotFactory(bot_token).get_telegram_bot()
    dp = Dispatcher(bot, storage=storage)
    ioc.set_instance(Dispatcher, dp)
