from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from utils.states.admin import Admin

from keyboards.inline.admin.admin_panel import get_admin_panel

from filters.check_user_admin import IsUserInAdmin

router: Router = Router()


@router.message(Command('admin'), IsUserInAdmin())
async def admin_panel(message: Message, state: FSMContext) -> None:
    await state.set_state(Admin.admin_panel)
    await message.answer("Админ-панель: ", reply_markup=await get_admin_panel())


@router.callback_query(Admin.admin_panel, F.data == 'cancel_admin_panel')
async def cancel_admin_panel(callback: CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    await callback.message.delete()


@router.callback_query(F.data == 'back_to_admin_panel')
async def back_to_admin_panel(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Admin.admin_panel)
    await callback.message.edit_text(text='Админ-панель: ', reply_markup=await get_admin_panel())
