
__all__ = [
    "UserService"
]


class UserService:
    async def login(self):
        raise NotImplementedError

    async def exit(self):
        raise NotImplementedError

    async def get_record(self):
        raise NotImplementedError

    async def set_record(self):
        raise NotImplementedError

    async def delete_record(self):
        raise NotImplementedError
