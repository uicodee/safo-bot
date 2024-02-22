from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.text_decorations import html_decoration

from src.helpers.constants import products
from src.keyboards.default import back_keyboard
from src.states.main import OrderForm

router = Router()


@router.message(F.text == "🛍 Buyurtma berish")
async def on_order(message: types.Message, state: FSMContext):
    text = (
        html_decoration.bold("🛍  Mahsulot haqida qisqacha:\n")
        + f"Hajmi: {html_decoration.bold(products[0]['volume'])}L\n"
        + f"Narxi (1 dona): {html_decoration.bold(products[0]['price'])} so'm\n\n"
        + "Mahsulot miqdorini kiriting\n"
        + f"Masalan: {html_decoration.bold('10; 20; 30')}"
    )
    await message.answer_photo(
        photo=products[0]["image"],
        caption=text,
        reply_markup=back_keyboard(),
    )
    await state.set_state(OrderForm.count)
