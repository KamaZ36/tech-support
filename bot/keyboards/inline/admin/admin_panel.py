from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_admin_panel() -> InlineKeyboardMarkup:
    """Админ-панель"""

    buttons = [
        [
            InlineKeyboardButton(text="Добавить вопрос", callback_data="add_new_question")
        ],
        [
            InlineKeyboardButton(text="Удалить вопрос", callback_data='delete_question')
        ],
        [
            InlineKeyboardButton(text="Список вопросов", callback_data='get_list_question')
        ],
        [
            InlineKeyboardButton(text="Редактировать контакты", callback_data='edit_contact_button')
        ],
        [
            InlineKeyboardButton(text='Выйти', callback_data='cancel_admin_panel')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def back_to_admin_panel() -> InlineKeyboardMarkup:
    buttons = [[
        InlineKeyboardButton(text='Назад 🔙', callback_data='back_to_admin_panel')
    ]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
