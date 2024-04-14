from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery

from settings import settings

from keyboards.inline.user.start_keyboards import get_back_to_menu_button

from utils.states.user import User

router: Router = Router()


@router.callback_query(F.data == 'contacts')
async def get_contacts(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(User.contacts)
    await callback.message.edit_text(settings.contact_text, reply_markup=await get_back_to_menu_button())

