from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from utils.states.admin import Admin, AddNewQuestion

from keyboards.inline.admin.admin_panel import back_to_admin_panel, get_admin_panel

from database.commands.questions import add_keyboard

router: Router = Router()


@router.callback_query(Admin.admin_panel, F.data == 'add_new_question')
async def add_new_question_callback(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(AddNewQuestion.waiting_question)
    await callback.message.edit_text("Введите новый вопрос: ", reply_markup=await back_to_admin_panel())


@router.message(AddNewQuestion.waiting_question, F.text)
async def get_new_question(message: Message, state: FSMContext) -> None:
    await state.update_data(question=message.text)
    await state.set_state(AddNewQuestion.waiting_answer)
    await message.answer("Введите ответ на вопрос: ", reply_markup=await back_to_admin_panel())


@router.message(AddNewQuestion.waiting_answer, F.text)
async def get_answer_new_question(message: Message, state: FSMContext, session: AsyncSession) -> None:
    await state.update_data(answer=message.text)
    data = await state.get_data()
    await add_keyboard(session=session, data=data)
    await state.set_data({})
    await state.set_state(Admin.admin_panel)
    await message.answer("Вы успешно добавили новый вопрос.", reply_markup=await get_admin_panel())
