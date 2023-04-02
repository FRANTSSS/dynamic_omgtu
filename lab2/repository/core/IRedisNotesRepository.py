from .models import Note
from typing import List

__all__ = [
    "IRedisNotesRepository"
]


class IRedisNotesRepository:
    async def add_free_note(self, note: Note) -> None:
        raise NotImplementedError()

    async def get_note_by_user_id(self, user_id: str) -> List[Note]:
        raise NotImplementedError()

    async def get_free_note(self) -> List[Note]:
        raise NotImplementedError()

    async def add_user_note(self, note_id: str, user_id) -> None:
        raise NotImplementedError()
