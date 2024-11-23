from aiogram import Router, Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards import reply
import text

dp = Dispatcher()
router = Router()

def webapp() -> InlineKeyboardBuilder:
    bildak = InlineKeyboardBuilder()
    bildak.button(
        text="Запустить Максон Кликер", web_app=WebAppInfo(
            url="https://5u4w5m-178-65-123-144.ru.tuna.am"
        )
    )
    return bildak.as_markup()

@router.message(Command(commands=["start"]))
async def command_start(message: Message):
    await message.answer(text.salam, reply_markup=webapp())