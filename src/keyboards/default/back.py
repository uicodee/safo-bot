from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def back_keyboard() -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(
        text="⬅️ Asosiy menu",
    )
    return builder.as_markup(resize_keyboard=True)
