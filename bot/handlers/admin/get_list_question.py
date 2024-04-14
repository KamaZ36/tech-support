from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from sqlalchemy.ext.asyncio import AsyncSession

from database.commands.questions import get_keyboards

from keyboards.inline.admin.admin_panel import back_to_admin_panel

from utils.states.admin import Admin

router: Router = Router()


@router.callback_query(Admin.admin_panel, F.data == 'get_list_question')
async def get_list_questions(callback: CallbackQuery, session: AsyncSession, state: FSMContext) -> None:
    questions = await get_keyboards(session=session)
    if not questions:
        await callback.message.edit_text("Вопросы не найдены.", reply_markup=await back_to_admin_panel())
        return
    text = {}
    i = 1
    for question in questions:
        text[f'{str(i)}'] = (
            f"🆔: {question.id}\n"
            f"Вопрос: {question.question}\n"
            f"Ответ: {question.answer}\n\n"
        )
        i += 1
    await state.update_data(questions=text)
    await state.update_data(all_pages=str(i-1))

    buttons = [
        [InlineKeyboardButton(text='Предыдущий', callback_data=f'prev_1'),
         InlineKeyboardButton(text=f'1/{str(i-1)}', callback_data='null'),
         InlineKeyboardButton(text='Следующий', callback_data=f'next_2')],
        [InlineKeyboardButton(text='Назад 🔙', callback_data='back_to_admin_panel')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.message.edit_text(text['1'], reply_markup=keyboard)


@router.callback_query(F.data.startswith('next_'))
async def next_gape_question(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    page = int(callback.data.split('_')[-1])
    if page == int(data['all_pages']) + 1:
        return
    number_next = page + 1
    number_prev = page - 1
    buttons = [[
        InlineKeyboardButton(text='Предыдущий', callback_data=f'prev_{number_prev}'),
        InlineKeyboardButton(text=f'{page}/{data["all_pages"]}', callback_data='null'),
        InlineKeyboardButton(text='Следующий', callback_data=f'next_{number_next}')],
        [InlineKeyboardButton(text='Назад 🔙', callback_data='back_to_admin_panel')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    try:
        await callback.message.edit_text(data['questions'][f'{str(page)}'], reply_markup=keyboard)
    except KeyError:
        pass


@router.callback_query(F.data.startswith('prev_'))
async def prev_gape_question(callback: CallbackQuery, session: AsyncSession, state: FSMContext) -> None:
    data = await state.get_data()
    page = int(callback.data.split('_')[-1])
    if page == 0:
        return
    number_next = page + 1
    number_prev = page
    if page != 0:
        number_prev -= 1
    buttons = [[
        InlineKeyboardButton(text='Предыдущий', callback_data=f'prev_{number_prev}'),
        InlineKeyboardButton(text=f'{page}/{data["all_pages"]}', callback_data='null'),
        InlineKeyboardButton(text='Следующий', callback_data=f'next_{number_next}')],
        [InlineKeyboardButton(text='Назад 🔙', callback_data='back_to_admin_panel')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    try:
        await callback.message.edit_text(data['questions'][f'{str(page)}'], reply_markup=keyboard)
    except KeyError:
        pass
