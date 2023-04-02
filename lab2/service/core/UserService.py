from typing import List

from repository import Note

__all__ = [
    "UserService"
]


class UserService:
    async def get_my_notes(self, user_id: str) -> List[Note]:
        raise NotImplementedError()

    async def add_my_note(self, user_id: str, note: Note) -> None:
        raise NotImplementedError()

    async def get_free_notes(self) -> List[Note]:
        raise NotImplementedError()
