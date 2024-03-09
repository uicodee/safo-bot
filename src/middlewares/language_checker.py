from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject

from src.infrastructure.database.dao import HolderDao
from src.keyboards.inline import language_keyboard


class LanguageChecker(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: types.Message,
        data: Dict[str, Any],
    ) -> Any:
        dao: HolderDao = data.get('dao')
        user = await dao.user.get_user_by_telegram_id(
            telegram_id=event.from_user.id
        )
        if user is None:
            await event.answer(
                text="🇺🇿 Tilni tanlang\n"
                     "🇷🇺 Выберите язык\n"
                     "🇺🇸 Select language",
                reply_markup=language_keyboard(),
            )
        else:
            result = await handler(event, data)
            return result
