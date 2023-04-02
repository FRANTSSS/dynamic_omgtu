from typing import List

from repository import (
    IRedisNotesRepository,
    Note,
    RedisRepositoryError,
    RedisNotesNotFoundError
)

from ..exception import *
from ..core import UserService

__all__ = [
    "UserServiceImpl"
]


#    async def add_free_note(self, note: Note) -> None:
#    async def get_note_by_user_id(self, user_id: str) -> List[Note]:
#    async def get_free_note(self) -> List[Note]:
#    async def add_user_note(self, note_id: str, user_id) -> None:

class UserServiceImpl(UserService):
    def __init__(self, notes_repository: IRedisNotesRepository):
        self.notes_repo = notes_repository

    async def get_my_notes(self, user_id: str) -> List[Note]:
        try:
            print(type(self.notes_repo))
            result = await self.notes_repo.get_note_by_user_id(user_id)
            return result
        except RedisNotesNotFoundError:
            raise UserServiceError()

    async def add_my_note(self, user_id: str, note: Note) -> None:
        try:
            await self.notes_repo.add_user_note(note.uuid, user_id)
        except RedisRepositoryError:
            raise UserServiceError()

    async def get_free_notes(self) -> List[Note]:
        try:
            result = await self.notes_repo.get_free_note()
            return result
        except RedisNotesNotFoundError:
            raise UserServiceError()
