from aiogram.dispatcher.filters.state import State, StatesGroup

__all__ = [
    "UserStates"
]


class UserStates(StatesGroup):
    wait_create_note = State()
    wait_delete_note = State()
