from pydantic import TypeAdapter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.infrastructure.database.dao.rdb import BaseDAO
from src.infrastructure.database.models import Order


class OrderDAO(BaseDAO[Order]):
    def __init__(self, session: AsyncSession):
        super().__init__(Order, session)

    async def add_order(
        self, telegram_id: int, volume: str, count: int, total_price: float
    ) -> dto.Order:
        order = Order(telegram_id=telegram_id, volume=volume, count=count, total_price=total_price)
        self.session.add(order)
        await self.session.commit()
        return dto.Order.model_validate(order)

    async def get_orders_by_telegram_id(self, telegram_id: int) -> list[dto.Order]:
        result = await self.session.execute(
            select(Order).where(Order.telegram_id == telegram_id)
        )
        adapter = TypeAdapter(list[dto.Order])
        return adapter.validate_python(result.scalars().all())
