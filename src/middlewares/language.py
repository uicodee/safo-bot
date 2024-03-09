from typing import Dict, Any

from aiogram import types
from aiogram.utils.i18n import I18nMiddleware

from src.infrastructure.database.dao import HolderDao


class LanguageMiddleware(I18nMiddleware):
    async def get_locale(self, event: types.Update, data: Dict[str, Any]) -> str:
        if event.message is not None:
            event = event.message
        elif event.callback_query is not None:
            event = event.callback_query
        dao: HolderDao = data.get("dao")
        user = await dao.user.get_user_by_telegram_id(telegram_id=event.from_user.id)
        if user is not None:
            return user.locale
        else:
            return event.from_user.language_code
