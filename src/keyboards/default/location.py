from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def location_keyboard() -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="📍 Manzilni yuborish", request_location=True)
    )
    builder.row(
        types.KeyboardButton(text="⬅️ Asosiy menu"),
    )
    return builder.as_markup(resize_keyboard=True)
