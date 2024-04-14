from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def back_to_questions_list() -> InlineKeyboardMarkup:
    """Кнопка назад из ответа на вопрос к списку вопросов"""

    buttons = [[InlineKeyboardButton(text='Назад 🔙', callback_data='back_to_questions')]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
