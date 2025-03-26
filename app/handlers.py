from aiogram import  Router, F, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart
from app.keyboard import main

router = Router()

@router.message(CommandStart())
async def send_welcome(message: Message):
   await message.answer("Начало работы \nВышлите мне изображение ваших оценок", reply_markup=main)

@router.message(F.photo)
async def dowload_photo(message: Message, bot: Bot):
    await bot.download(
        message.photo[-1],
        destination=f"/photo/{message.photo[-1].file_id}.jpg"
    )
