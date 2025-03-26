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
    if message.photo:
        file_name = f"photos/{message.photo[-1].file_id}.jpg"
        await bot.download(message.photo[-1], destination=file_name)
        with open(file_name, 'rb') as f:
            image_bytes = f.read()
        s = ocr_core(image_bytes)

        sum_score = 0
        count_score = 0

        for i in range(len(s) - 1):
            sum_score += int(s[i])
            count_score += 1

        avr_score = sum_score / count_score
        print(avr_score)

        question = input('До какого числа следует посчитать?(Введите цифру)\n')

        if question == '4':
            if 4.5 > avr_score >= 3.5:
                print('У вас уже 4 или 5')
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
                print(f'До {avr_score_4} вам нужно {count_score_5} пятёрок или {count_score_4} четвёрок')
        elif question == '5':
            if avr_score >= 4.5:
                print('У вас уже 5')
            else:
                sum_score_5_2 = sum_score
                count_score_5_2 = avr_score_5_2 = 0
                while avr_score_5_2 < 4.5:
                    sum_score_5_2 += 5
                    count_score_5_2 += 1
                    avr_score_5_2 = sum_score_5_2 / (count_score_5_2 + count_score)
                print(f'До {avr_score_5_2} вам осталось {count_score_5_2} пятерок')

'''@router.message(F.text=='выбор оценки')
async def grades_quest(message: Message):
   await message.answer('')
'''
