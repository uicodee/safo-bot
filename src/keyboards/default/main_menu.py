from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from src.helpers.constants import main_menu_buttons


def main_menu_keyboard() -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text=main_menu_buttons[0]))
    builder.row(
        types.KeyboardButton(text=main_menu_buttons[1]),
        types.KeyboardButton(text=main_menu_buttons[2]),
    )
    builder.row(
        types.KeyboardButton(text=main_menu_buttons[3]),
        types.KeyboardButton(text=main_menu_buttons[4]),
    )
    return builder.as_markup(resize_keyboard=True)
