from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.infrastructure.database.dao.rdb import BaseDAO
from src.infrastructure.database.models import User


class UserDAO(BaseDAO[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def add_user(
        self, telegram_id: int, full_name: str, username: str, locale: str
    ) -> dto.User:
        user = User(telegram_id=telegram_id, full_name=full_name, username=username, locale=locale)
        self.session.add(user)
        await self.session.commit()
        return dto.User.model_validate(user)

    async def update_language(self, telegram_id: int, locale: str) -> None:
        await self.session.execute(
            update(User).where(User.telegram_id == telegram_id).values(locale=locale)
        )
        await self.session.commit()

    async def get_user_by_telegram_id(self, telegram_id: int) -> dto.User:
        result = await self.session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar()
        if user is not None:
            return dto.User.model_validate(user)
