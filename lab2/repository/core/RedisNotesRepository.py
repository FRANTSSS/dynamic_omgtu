from .models import Note
from typing import List

__all__ = [
    "RedisNotesRepository"
]


class RedisNotesRepository:
    def add(self, full_name: str) -> List[Note]:
        raise NotImplementedError

    def get(self, uuid: str) -> List[Note]:
        raise NotImplementedError

    def delete(self, uuid: str) -> None:
        raise NotImplementedError
