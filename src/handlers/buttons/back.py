from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from src.keyboards.default import main_menu_keyboard

router = Router()


@router.message(F.text.in_(["⬅️ Asosiy menu", "🛑 Bekor qilish"]))
async def on_back(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="⚡️ Asosiy menu ⚡️",
        reply_markup=main_menu_keyboard(),
    )
