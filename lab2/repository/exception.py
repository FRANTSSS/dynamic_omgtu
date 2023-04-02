
__all__ = [
    "RedisRepositoryError",
    "RedisNotesNotFoundError"
]


class RedisRepositoryError(Exception):
    pass


class RedisNotesNotFoundError(Exception):
    pass
