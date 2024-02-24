from src.dto import Base
from .types import OrderStatus


class Order(Base):

    telegram_id: int
    volume: str
    count: int
    total_price: float
    status: OrderStatus
