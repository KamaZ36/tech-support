from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Question(Base):
    __tablename__ = 'questions'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    question: Mapped[str] = mapped_column(unique=False, nullable=False)
    answer: Mapped[str] = mapped_column(unique=False, nullable=False)
