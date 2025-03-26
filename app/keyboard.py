from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

main = ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text='Выбрать уровень сложности')]],
                        resize_keyboard=True)