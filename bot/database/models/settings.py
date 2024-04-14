from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Settings(Base):
    __tablename__ = 'settings'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    point: Mapped[str] = mapped_column(unique=False, nullable=False)
    title: Mapped[str] = mapped_column(unique=False, nullable=False)
