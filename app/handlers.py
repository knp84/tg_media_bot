from aiogram import  Router, F, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart

from io import BytesIO
from io import BytesIO

from PIL import Image
import pytesseract

from re import sub
from math import ceil


def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(BytesIO(filename)))  
    return text

def calculate_required_grades(total_score, count, target_avg, added_grade):
    required = (target_avg * count - total_score) / (added_grade - target_avg)
    n = max(0, ceil(required))
    new_avg = (total_score + added_grade * n) / (count + n)
    return n, round(new_avg, 2)

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
        digit = sub(r'\D', '' ,ocr_core(image_bytes))
        digit = [int(i) for i in digit]

    

    count_score, sum_score = int(len(digit)), sum(digit)

    avr_score = sum_score / count_score

    await message.reply(f'ваш средний балл {round(avr_score, 3)}\nКакую оценку вы хотите за четверть?(Введите цифру)')
    
    
@router.message(F.text)
async def having_grade(message: Message):

    if message.text == '5':
        if avr_score >= 4.5:
            await message.answer('У вас уже 5')
        else:
            n5, avg5 = calculate_required_grades(sum_score, count_score, 4.5, 5)
            await message.answer(f'Требуется {n5} пятёрок ➡️  средний {avg5}')
    elif message.text == 4:
        if avr_score >= 3.5:
            await message.answer('У вас уже оценка 4 или выше')
        else:
            n5, avg5 = calculate_required_grades(sum_score, count_score, 3.5, 5)
            n4, avg4 = calculate_required_grades(sum_score, count_score, 3.5, 4)
            
            await message.answer('Чтобы достичь среднего балла:')
            await message.answer(f'- Пятёрки: {n5} шт. ➡️  средний {avg4}')
            await message.answer(f'- Четвёрки: {n4} шт. ➡️  средний {avg5}')
    elif message.text == 3:
        if avr_score >= 2.5:
            print('У вас уже оцека 3 или больше')
        else:
            n5, avg5 = calculate_required_grades(sum_score, count_score, 2.5, 5)
            n4, avg4 = calculate_required_grades(sum_score, count_score, 2.5, 4)
            n3, avg3 = calculate_required_grades(sum_score, count_score, 2.5, 3)
    
            await message.answer('Чтобы достичь среднего балла:')
            await message.answer(f'- Пятёрки: {n5} шт. ➡️  средний {avg5}')
            await message.answer(f'- Четвёрки: {n4} шт. ➡️  средний {avg4}')
            await message.answer(f'- Тройки: {n3} шт. ➡️  средний {avg3}')
