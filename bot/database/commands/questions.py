from typing import Sequence, Any

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.question import Question


async def get_keyboards(session: AsyncSession) -> Sequence[Question] | bool:
    query = select(Question)
    response = await session.execute(query)
    keyboards = response.scalars().all()
    if not keyboards:
        return False
    return keyboards


async def get_answer_text(session: AsyncSession, answer_id: int) -> str:
    query = select(Question.answer).where(Question.id == answer_id)
    response = await session.execute(query)
    answer_text = response.scalar()
    return answer_text


async def add_keyboard(session: AsyncSession, data: dict[str, Any]) -> None:
    question = Question(
        question=data["question"],
        answer=data["answer"],
    )
    session.add(question)

    await session.commit()


async def delete_question_by_id(session: AsyncSession, answer_id: int) -> bool:
    query = delete(Question).where(Question.id == answer_id)
    try:
        await session.execute(query)
        await session.commit()
        return True
    except Exception as e:
        return False
