import os
from dotenv import load_dotenv
from aiogram.dispatcher import FSMContext
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import logging
import asyncio

from exception import EnvModuleError

from .bot import (
    IBotFactory,
    TelegramBotFactory
)

from .ioc_container import ioc

from .bot import TelegramBotFactory
import json

from model import EnvDTO

__all__ = [
    "bootstrap"
]


def bootstrap(path_env: str = "."):
    load_dotenv(path_env)
    config_path = os.environ.get("CONFIG_PATH")
    try:
        with open(config_path, 'r') as file:
            js = json.load(file)
        env = EnvDTO(bot=js.get("bot"),
                     memory=js.get("memory"))
    except Exception as e:
        raise EnvModuleError()

    memory = MemoryStorage()

    bot_factory = TelegramBotFactory(env.bot.get("token"))
    bot = bot_factory.get_telegram_bot()

    ioc.set_instance(Bot, bot)

    r = redis.Redis()
    ioc.set_instance(redis.Redis, r)



    token = os.environ.get("TOKEN")
    bot = Bot(token=TOKEN)

    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

