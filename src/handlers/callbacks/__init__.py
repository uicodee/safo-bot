from aiogram import Dispatcher

from .language import router as language_router


def setup(dp: Dispatcher):
    dp.include_router(language_router)
