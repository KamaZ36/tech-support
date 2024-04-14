from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import settings


async def start_keyboards() -> InlineKeyboardMarkup:
    """Главное меню"""
    buttons = [
        [
            InlineKeyboardButton(text='Частые вопросы', callback_data='base_answers')
        ],
        [
            InlineKeyboardButton(text="Связь с Тех. Поддержкой", url='t.me/your_is_mine_ru')  # Укажите ссылку на вашу тех-поддержку в телеграмм
        ],
        [
            InlineKeyboardButton(text="Контакты", callback_data='contacts')
        ],
        [
            InlineKeyboardButton(text="Перейти на сайт", url='https://yours-is-mine.ru')  # Укажите ссылку на ваш сайт в ковычках
        ],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def get_back_to_menu_button() -> InlineKeyboardMarkup:
    buttons = [[InlineKeyboardButton(text="Назад 🔙", callback_data='back_main_in_questions')]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
