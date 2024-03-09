from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.i18n import gettext as _


def main_menu_keyboard(**kwargs) -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text=_("🛍 Buyurtma berish", locale=kwargs.get('locale'))))
    builder.row(
        types.KeyboardButton(text=_("🛒 Buyurtmalarim", locale=kwargs.get('locale'))),
        types.KeyboardButton(text=_("✍️ Izoh qoldirish", locale=kwargs.get('locale'))),
    )
    builder.row(
        types.KeyboardButton(text=_("☎️ Kontaktlar", locale=kwargs.get('locale'))),
        types.KeyboardButton(text=_("⚙️ Sozlamalar", locale=kwargs.get('locale'))),
    )
    return builder.as_markup(resize_keyboard=True)
