from typing import Sequence, Any

from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.settings import Settings


async def add_settings_contacts(session: AsyncSession, text: str) -> None:
    setting = Settings(
        point='contacts',
        title=text
    )
    session.add(setting)
    await session.commit()


async def update_contacts(session: AsyncSession, text: str) -> None:
    query = update(Settings).where(Settings.point == 'contacts').values(title=text)
    await session.execute(query)
    await session.commit()


async def get_settings_contacts(session: AsyncSession) -> str | bool:
    query = select(Settings.title).where(Settings.point == 'contacts')
    try:
        response = await session.execute(query)
        title = response.scalar()
        return title
    except Exception as e:
        return False
