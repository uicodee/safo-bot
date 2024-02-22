from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from src.keyboards.default import cancel_keyboard
from src.states import ReviewForm

router = Router()


@router.message(F.text == "✍️ Izoh qoldirish")
async def on_review(message: types.Message, state: FSMContext):
    await message.answer(
        text="Izoh qoldiring. Sizning fikringiz biz uchun muhim.",
        reply_markup=cancel_keyboard(),
    )
    await state.set_state(ReviewForm.review)
