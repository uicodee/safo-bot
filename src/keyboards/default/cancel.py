from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def cancel_keyboard() -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="🛑 Bekor qilish"))
    return builder.as_markup(resize_keyboard=True)
