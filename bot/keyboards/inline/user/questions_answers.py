from typing import Sequence

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.question import Question
from database.commands.questions import get_keyboards


async def get_questions_answers(session: AsyncSession) -> InlineKeyboardMarkup | bool:
    buttons = []
    questions: Sequence[Question] = await get_keyboards(session=session)
    for question in questions:
        buttons.append([InlineKeyboardButton(text=question.question, callback_data=f'question_{str(question.id)}')])
    buttons.append([InlineKeyboardButton(text="Назад 🔙", callback_data='back_main_in_questions')])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
