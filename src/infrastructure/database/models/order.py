from sqlalchemy import String, Integer, Float, BigInteger, Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.dto import OrderStatus
from src.infrastructure.database.models import BaseModel


class Order(BaseModel):

    __tablename__ = "order"

    telegram_id: Mapped[int] = mapped_column(BigInteger)
    volume: Mapped[str] = mapped_column(String)
    count: Mapped[int] = mapped_column(Integer)
    total_price: Mapped[float] = mapped_column(Float)
    status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus), default=OrderStatus.NEW)
