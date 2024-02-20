from aiogram import Router, types
from aiogram.filters import CommandStart

from src.infrastructure.database.dao import HolderDao
from src.keyboards.default import main_menu_keyboard

router = Router()


@router.message(CommandStart())
async def on_cmd_start(message: types.Message, dao: HolderDao):
    await message.answer(
        text="⚡️ Asosiy menu ⚡️",
        reply_markup=main_menu_keyboard(),
    )
