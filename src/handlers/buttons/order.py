from aiogram import Router, F, types

from src.helpers.constants import products

router = Router()


@router.message(F.text == "🛍 Buyurtma berish")
async def on_order(message: types.Message):
    await message.answer_photo(
        photo=products[0]["image"],
        caption=f"Hajmi: {products[0]['volume']}L\n"
        f"Narxi: {products[0]['price']} so'm",
    )
