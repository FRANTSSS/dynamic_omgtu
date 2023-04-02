from ..core import (
    IRedisFactory,
    IRedisNotesRepository
)
from .RedisNotesRepository import RedisNotesRepository
from aioredis import Redis

__all__ = [
    "RedisFactory"
]


class RedisFactory(IRedisFactory):
    def __init__(self, host: str, port: int, db: int):
        self.r = Redis(host=host, port=port, db=db)

    async def get_notes_repository(self) -> IRedisNotesRepository:
        repository = RedisNotesRepository(self.r)
        return repository
