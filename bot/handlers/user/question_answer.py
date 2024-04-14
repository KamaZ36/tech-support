from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery

from sqlalchemy.ext.asyncio import AsyncSession

from database.commands.questions import get_question_by_tg_id

from keyboards.inline.user.questions_answers import get_questions_answers
from keyboards.inline.user.start_keyboards import start_keyboards
from keyboards.inline.user.back_to_questions_list import back_to_questions_list
from keyboards.inline.user.start_keyboards import get_back_to_menu_button

from utils.states.user import User

router: Router = Router()


@router.callback_query(StateFilter(None), F.data == 'base_answers')
async def show_base_questions(callback: CallbackQuery, state: FSMContext, session: AsyncSession) -> None:
    await state.set_state(User.questions_answers)
    try:
        await callback.message.edit_text("Частые вопросы: ", reply_markup=await get_questions_answers(session=session))
    except TypeError:
        await callback.message.edit_text("Вопросов не найдено.", reply_markup=await get_back_to_menu_button())


@router.callback_query(User.questions_answers, F.data.startswith('question_'))
async def show_base_answer(callback: CallbackQuery, state: FSMContext, session: AsyncSession) -> None:
    await state.set_state(User.question)
    answer_id = int(callback.data.split('_')[-1])
    question = await get_question_by_tg_id(session=session, answer_id=answer_id)
    await callback.message.edit_text(
        f'Вопрос: {question.question}\nОтвет: {question.answer}',
        reply_markup=await back_to_questions_list()
    )


@router.callback_query(StateFilter(User.questions_answers, User.contacts), F.data == 'back_main_in_questions')
async def back_in_main(callback: CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    await callback.message.edit_text(
        "Вас приветствует тех-поддержка сайта.",
        reply_markup=await start_keyboards()
    )


@router.callback_query(User.question, F.data == 'back_to_questions')
async def back_to_questions_list_callback(callback: CallbackQuery, state: FSMContext, session: AsyncSession) -> None:
    await state.set_state(User.questions_answers)
    await callback.message.edit_text("Частые вопросы: ", reply_markup=await get_questions_answers(session=session))
