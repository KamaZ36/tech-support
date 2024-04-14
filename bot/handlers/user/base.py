from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from keyboards.inline.user.start_keyboards import start_keyboards

router: Router = Router()


@router.message(CommandStart())
async def start_main(message: Message) -> None:
    await message.answer("Вас приветствует тех-поддержка сайта.",
                         reply_markup=await start_keyboards())


@router.message(Command('menu'))
async def start_menu(message: Message) -> None:
    await message.answer("Вас приветствует тех-поддержка сайта.",
                         reply_markup=await start_keyboards())
