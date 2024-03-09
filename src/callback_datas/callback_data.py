from aiogram.filters.callback_data import CallbackData


class OrderActionCallback(CallbackData, prefix="order"):

    from_user_id: int
    action: str


class LanguageCallback(CallbackData, prefix="language"):

    language: str
