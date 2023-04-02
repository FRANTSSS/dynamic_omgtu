from ..core import UserService
from lab2.repository import IRedisNotesRepository

__all__ = [
    "UserServiceImpl"
]


class UserServiceImpl(UserService):
    def __init__(self, notes_repository: IRedisNotesRepository):
        self.notes_repo = notes_repository

    async def get_my_notes(self):
        raise NotImplementedError()

    async def add_new_note(self):
        raise NotImplementedError()

    async def get_free_notes(self):
        raise NotImplementedError()
