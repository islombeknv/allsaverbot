from aiogram.dispatcher.filters.state import StatesGroup, State


class myadminstate(StatesGroup):
    first_step = State()
    second_step = State()
    third_step = State()
    last_step = State()