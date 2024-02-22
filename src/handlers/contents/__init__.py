from .review import router as review_router
from .order import router as order_router

from aiogram import Dispatcher


def setup(dp: Dispatcher):
    dp.include_router(review_router)
    dp.include_router(order_router)
