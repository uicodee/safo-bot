from aiogram.fsm.state import StatesGroup, State


class ReviewForm(StatesGroup):

    review = State()


class OrderForm(StatesGroup):

    count = State()
    location = State()
