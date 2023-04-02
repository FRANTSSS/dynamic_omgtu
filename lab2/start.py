import asyncio

from aiogram import Dispatcher
from aiogram.utils import executor

from bootstrap import bootstrap
from shutdown import shutdown
from ioc_container import ioc


if __name__ == "__main__":
    bootstrap()

    dispatcher = ioc.get_instance(Dispatcher)
    from bot.impl.handlers import *

    loop = asyncio.get_event_loop()
    executor.start_polling(dispatcher, on_shutdown=shutdown, loop=loop)
