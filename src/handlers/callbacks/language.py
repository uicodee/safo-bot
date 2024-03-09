from aiogram import Router, types
from aiogram.utils.i18n import gettext as _
from src.callback_datas.callback_data import LanguageCallback
from src.infrastructure.database.dao import HolderDao
from src.keyboards.default import main_menu_keyboard

router = Router()


@router.callback_query(LanguageCallback.filter())
async def on_language(call: types.CallbackQuery, callback_data: LanguageCallback, dao: HolderDao):
    user = await dao.user.get_user_by_telegram_id(telegram_id=call.from_user.id)
    if user is None:
        await dao.user.add_user(
            telegram_id=call.from_user.id,
            full_name=call.from_user.full_name,
            username=call.from_user.username,
            locale=callback_data.language
        )
    else:
        await dao.user.update_language(
            telegram_id=call.from_user.id,
            locale=callback_data.language
        )
    await call.message.delete()
    await call.message.answer(
        text=_('⚡️ Asosiy menu ⚡️', locale=callback_data.language),
        reply_markup=main_menu_keyboard(locale=callback_data.language),
    )
