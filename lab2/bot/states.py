from aiogram.dispatcher.filters.state import State, StatesGroup

__all__ = [
    "UserStates"
]


class UserStates(StatesGroup):
    wait_add_note = State()
    wait_get_note = State()
    wait_log = State()
