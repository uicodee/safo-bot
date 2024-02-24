from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.database.dao.rdb import BaseDAO, UserDAO, OrderDAO


class HolderDao:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.base = BaseDAO
        self.user = UserDAO(self.session)
        self.order = OrderDAO(self.session)
