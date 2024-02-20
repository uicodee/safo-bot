from aiogram import Dispatcher

from .order import router as order_router
from .contacts import router as contacts_router
from .review import router as review_router


def setup(dp: Dispatcher):
    dp.include_router(order_router)
    dp.include_router(contacts_router)
    dp.include_router(review_router)
