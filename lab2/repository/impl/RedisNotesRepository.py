from ..core import (
    IRedisNotesRepository,
    Note
)
from typing import List
from aioredis import Redis
from uuid import uuid4
from ..exception import (
    RedisRepositoryError,
    RedisNotesNotFoundError
)

__all__ = [
    "RedisNotesRepository"
]


def convert_to_note(note_dict: dict) -> Note:
    return Note(
        date=note_dict.get("date"),
        time=note_dict.get("time"),
        speciality=note_dict.get("speciality"),
        doctor=note_dict.get("doctor"),
        patient=note_dict.get("patient")
    )


class RedisNotesRepository(IRedisNotesRepository):
    def __init__(self, r: Redis):
        self.r = r

    async def add_free_note(self, note: Note) -> None:
        r = await self.r.set(
            f"free-{str(uuid4())}",
            note.json()
        )
        if not r:
            raise RedisRepositoryError

    async def get_note_by_user_id(self, user_id: str) -> List[Note]:
        user_notes = []
        try:
            result = await self.r.keys(f"{user_id}*")
        except Exception:
            raise RedisRepositoryError
        if len(result) == 0:
            raise RedisNotesNotFoundError
        for id_ in result:
            note = await self.r.get(str(id_))
            if not note:
                raise RedisNotesNotFoundError
            note = convert_to_note(note)
            user_notes.append(note)
        return user_notes

    async def get_free_note(self) -> List[Note]:
        notes = []
        try:
            result = await self.r.keys("free*")
        except Exception:
            raise RedisRepositoryError
        if len(result) == 0:
            raise RedisNotesNotFoundError
        for id_ in result:
            note = await self.r.get(str(id_))
            if not note:
                raise RedisNotesNotFoundError
            note = convert_to_note(note)
            notes.append(note)
        return notes

    async def add_user_note(self, note_id: str, user_id) -> None:
        result = await self.r.get(note_id)
        if not result:
            raise RedisNotesNotFoundError
        new_note_id = f"{user_id}-{note_id}"
        r = await self.r.set(new_note_id, result)
        if not r:
            raise RedisNotesNotFoundError
