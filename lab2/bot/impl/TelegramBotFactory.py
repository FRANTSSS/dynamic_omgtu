from ..core import IBotFactory
from aiogram import Bot

__all__ = [
    "TelegramBotFactory"
]


class TelegramBotFactory(IBotFactory):
    def __init__(self, token: str):
        self.bot = Bot(token=token)

    def get_telegram_bot(self):
        return self.bot
