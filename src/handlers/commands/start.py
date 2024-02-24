from aiogram import Router, types
from aiogram.filters import CommandStart

from src.infrastructure.database.dao import HolderDao
from src.keyboards.default import main_menu_keyboard

router = Router()


@router.message(CommandStart())
async def on_cmd_start(message: types.Message, dao: HolderDao):
    user = await dao.user.get_user_by_telegram_id(telegram_id=message.from_user.id)
    if user is None:
        await dao.user.add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username
        )
    await message.answer(
        text="⚡️ Asosiy menu ⚡️",
        reply_markup=main_menu_keyboard(),
    )
