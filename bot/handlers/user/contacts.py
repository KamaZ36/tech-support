from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from keyboards.inline.user.start_keyboards import get_back_to_menu_button

from database.commands.settings import get_settings_contacts

from utils.states.user import User

router: Router = Router()


@router.callback_query(F.data == 'contacts')
async def get_contacts(callback: CallbackQuery, state: FSMContext, session: AsyncSession) -> None:
    await state.set_state(User.contacts)
    title = await get_settings_contacts(session=session)
    if not title:
        await callback.message.edit_text("ПУСТО", reply_markup=await get_back_to_menu_button())
        return
    await callback.message.edit_text(title, reply_markup=await get_back_to_menu_button())

