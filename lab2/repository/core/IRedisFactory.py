from .IRedisNotesRepository import IRedisNotesRepository

__all__ = [
    "IRedisFactory"
]


class IRedisFactory:
    async def get_notes_repository(self) -> IRedisNotesRepository:
        raise NotImplementedError()
