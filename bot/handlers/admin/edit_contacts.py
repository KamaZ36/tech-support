from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from database.commands.settings import get_settings_contacts, add_settings_contacts, update_contacts
from keyboards.inline.admin.admin_panel import back_to_admin_panel
from utils.states.admin import Admin, EditContacts


router: Router = Router()


@router.callback_query(Admin.admin_panel, F.data == 'edit_contact_button')
async def edit_contact(callback: CallbackQuery, state: FSMContext):
    await state.set_state(EditContacts.waiting_contact_title)
    await callback.message.edit_text("Введите новый текст: ", reply_markup=await back_to_admin_panel())


@router.message(EditContacts.waiting_contact_title, F.text)
async def edit_contact_handler(message: Message, state: FSMContext, session: AsyncSession):
    title = await get_settings_contacts(session=session)
    if not title:
        await add_settings_contacts(session=session, text=message.text)
        await message.answer(f"Вы успешно обновили контакты: {message.text}", reply_markup=await back_to_admin_panel())
        return
    else:
        await update_contacts(session=session, text=message.text)
        await message.answer(f"Вы успешно обновили контакты: {message.text}", reply_markup=await back_to_admin_panel())
        return
