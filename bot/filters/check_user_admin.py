from aiogram.filters import BaseFilter
from aiogram.types import Message

from sqlalchemy.ext.asyncio import AsyncSession

from settings import settings


class IsUserInAdmin(BaseFilter):
    """Проверяем является ли пользователь администратором"""

    async def __call__(self, message: Message, session: AsyncSession) -> bool:
        if message.from_user.id == settings.admin_tg_id:
            return True
        return False
