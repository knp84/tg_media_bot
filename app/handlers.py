from aiogram import  Router, F, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart
from io import BytesIO

router = Router()

@router.message(CommandStart())
async def send_welcome(message: Message):
   await message.answer("Начало работы \nВышлите мне изображение ваших оценок")

@router.message(F.photo)
async def echo_photo_message(message: Message, bot: Bot):
    global image_bytes
    global file_name
    if message.photo:
        file_name = f"photos/{message.photo[-1].file_id}.jpg"
        await bot.download(message.photo[-1], destination=file_name)
        with open(file_name, 'rb') as f:
            image_bytes = f.read()