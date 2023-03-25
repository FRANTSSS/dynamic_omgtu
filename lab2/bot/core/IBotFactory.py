from abc import ABC

__all__ = [
    "IBotFactory"
]


class IBotFactory(ABC):
    def get_telegram_bot(self):
        raise NotImplementedError
