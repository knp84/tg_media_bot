from aiogram import  Router, F, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart
from io import BytesIO
from PIL import Image
import pytesseract
from io import BytesIO

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(BytesIO(filename)))  
    return text

pytesseract.pytesseract.tesseract_cmd = r'D:\Pyton310\Project\venv\Lib\TES\tesseract.exe'

router = Router()

@router.message(CommandStart())
async def send_welcome(message: Message):
   await message.answer("Начало работы \nВышлите мне изображение ваших оценок")


@router.message(F.photo)
async def photo_message(message: Message, bot: Bot):
    global avr_score
    global sum_score
    global count_score
    if message.photo:
        file_name = f"photos/{message.photo[-1].file_id}.jpg"
        await bot.download(message.photo[-1], destination=file_name)
        with open(file_name, 'rb') as f:
            image_bytes = f.read()
        s = ocr_core(image_bytes)

        sum_score = 0
        count_score = 0

        for i in range(len(s.strip('\n'))):
            sum_score += int(s[i])
            count_score += 1

        avr_score = sum_score / count_score
    await message.reply(f'ваш средний балл {round(avr_score, 3)}\nКакую оценку вы хотите за четверть?(Введите цифру)')
    
    
@router.message(F.text)
async def having_grade(message: Message):

    if message.text == '4':
        if 4.5 > avr_score >= 3.5:
            await message.answer('У вас уже 4 или 5')
        else:
            count_score_5 = count_score_4 = avr_score_5 = avr_score_4 = 0
            sum_score_5 = sum_score_4 = sum_score
            while avr_score_5 < 3.5:
                sum_score_5 += 5
                count_score_5 += 1
                avr_score_5 = sum_score_5 / (count_score_5 + count_score)
            while avr_score_4 < 3.5:
                sum_score_4 += 4
                count_score_4 += 1
                avr_score_4 = sum_score_4 / (count_score_4 + count_score)
            await message.answer(f'До {round(avr_score_4, 3)} вам нужно {count_score_5} "5" или {count_score_4} "4"')
    elif message.text == '5':
        if avr_score >= 4.5:
            await message.answer('У вас уже 5')
        else:
            sum_score_5_2 = sum_score
            count_score_5_2 = avr_score_5_2 = 0
            while avr_score_5_2 < 4.5:
                sum_score_5_2 += 5
                count_score_5_2 += 1
                avr_score_5_2 = sum_score_5_2 / (count_score_5_2 + count_score)
            await message.answer(f'До {round(avr_score_5_2, 3)} вам осталось {count_score_5_2} "5"')

