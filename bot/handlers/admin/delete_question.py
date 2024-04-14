from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery

from sqlalchemy.ext.asyncio import AsyncSession

from database.commands.questions import delete_question_by_id

from utils.states.admin import Admin, DeleteQuestion

from keyboards.inline.admin.admin_panel import back_to_admin_panel, get_admin_panel

router: Router = Router()


@router.callback_query(Admin.admin_panel, F.data == 'delete_question')
async def delete_question(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(DeleteQuestion.waiting_question_id)
    await callback.message.edit_text("Введите ид вопроса: ", reply_markup=await back_to_admin_panel())


@router.message(DeleteQuestion.waiting_question_id, F.text)
async def delete_question_id(message: Message, state: FSMContext, session: AsyncSession) -> None:
    response = await delete_question_by_id(session=session, answer_id=int(message.text))
    if not response:
        await message.answer("❗ Ошибка! Вопроса с таким ID не существует!", reply_markup=await get_admin_panel())
        return
    await message.answer(f"Вы успешно удалили вопрос с ID: {message.text}", reply_markup=await back_to_admin_panel())
