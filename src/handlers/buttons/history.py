from aiogram import Router, types, F

from src.infrastructure.database.dao import HolderDao

router = Router()


@router.message(F.text == "🛒 Buyurtmalarim")
async def on_orders_history(message: types.Message, dao: HolderDao):
    orders = await dao.order.get_orders_by_telegram_id(
        telegram_id=message.from_user.id
    )
    text = ""
    for index, order in enumerate(orders, start=1):
        text += f"{index}. <b>{order.volume}</b> x <b>{order.count}</b> = <b>{order.total_price}</b>\n"
    await message.answer(
        text=text
    )
