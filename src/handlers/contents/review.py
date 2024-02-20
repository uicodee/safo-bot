from aiogram import Router, types

from src.states import ReviewForm

router = Router()


@router.message(ReviewForm.review)
async def on_review_write(message: types.Message):
    await message.bot.send_message(
        chat_id=-1002128337999,
        text=f"👤 {message.from_user.full_name}:\n"
        f"{message.text}\n\n"
    )
    await message.answer(text="Izoh qoldirildi ✅")
