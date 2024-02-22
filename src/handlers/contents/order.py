import uuid
from datetime import datetime

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.utils.text_decorations import html_decoration

from src.keyboards.default import location_keyboard, main_menu_keyboard
from src.states.main import OrderForm

router = Router()


@router.message(OrderForm.count)
async def on_count(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        if int(message.text) > 0:
            await state.update_data(count=message.text)
            await message.answer(
                text=html_decoration.italic(
                    "📍 Buyurtma yetkazib beriladigan manzil lokatsiyasini yuboring!"
                ),
                reply_markup=location_keyboard(),
            )
            await state.set_state(OrderForm.location)
        else:
            await message.answer(
                text="⚠️ Iltimos 0 dan katta bo'lgan sonni kiriting!",
            )
    else:
        await message.answer(
            text="⚠️ Iltimos to'g'ri son kiriting!",
        )


@router.message(OrderForm.location, F.location)
async def on_location(message: types.Message, state: FSMContext):
    data = await state.get_data()
    order_number = uuid.uuid4().hex
    await message.answer(
        text=html_decoration.italic(
            f"✅ Buyurtma qabul qilindi. Buyurtma raqami: {order_number}"
        )
    )
    await message.answer(
        text=f"<b>💸  To\'lov qilish!</b>\n"
             f"<b>📍 Buyurtma turi: <i>18.9 L</i></b>\n"
             f"<b>📄 Buyurtma raqami: <i>{order_number}</i></b>\n"
             f"<b>📦 Buyurtma miqdori: <i>{data.get('count')}</i> ta</b>\n"
             f"<b>💰 Umumiy narx: <i>{int(data.get('count')) * 10000}</i> so'm</b>\n"
             f"<b>🕓 Buyurtma sanasi: <i>{datetime.now().strftime('%d.%m.%Y %H:%M')}</i></b>",
        reply_markup=main_menu_keyboard(),
    )
