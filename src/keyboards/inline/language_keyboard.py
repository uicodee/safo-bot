from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.callback_datas.callback_data import LanguageCallback


def language_keyboard() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="🇺🇿 O'zbek tili",
        callback_data=LanguageCallback(language="uz")
    )
    builder.button(
        text="🇷🇺 Русский",
        callback_data=LanguageCallback(language="ru")
    )
    builder.button(
        text="🇺🇸 English",
        callback_data=LanguageCallback(language="en")
    )
    return builder.as_markup()
