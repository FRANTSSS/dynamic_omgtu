from aiogram.contrib.fsm_storage.memory import MemoryStorage


__all__ = [
    "MemoryStorageFactory"
]


class MemoryStorageFactory:
    def __init__(self):
        pass

    def get_storage(self):
        storage = MemoryStorage()
        return storage
