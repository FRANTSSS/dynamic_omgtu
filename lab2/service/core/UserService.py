
__all__ = [
    "UserService"
]


class UserService:
    async def get_my_notes(self):
        raise NotImplementedError()

    async def add_new_note(self):
        raise NotImplementedError()

