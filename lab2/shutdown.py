from aiogram import Dispatcher

__all__ = [
    "shutdown"
]


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()
