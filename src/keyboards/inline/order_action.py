from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.callback_datas.callback_data import OrderActionCallback


def order_action_keyboard(from_user_id: int) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="✅ Qabul qilish",
        callback_data=OrderActionCallback(from_user_id=from_user_id, action="accept"),
    )
    builder.button(
        text="❌ Bekor qilish",
        callback_data=OrderActionCallback(from_user_id=from_user_id, action="decline"),
    )
    return builder.as_markup()
# @router.callback_query(OrderActionCallback.filter())
# async def ...(call: types.CallbackQuery, callback_data: OrderActionCallback):
# if callback_data.action == "accept":
#await call.message.bot.send_message(chat_id=int(callback_data.from_user_id)))
