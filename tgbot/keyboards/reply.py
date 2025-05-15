from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='О проекте'),
            KeyboardButton(text = 'Участники'),
        ],
        [
            KeyboardButton(text='О партнерах'),
            KeyboardButton(text='Ход проекта'),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Напиши, что хочешь узнать!'
)

del_kb = ReplyKeyboardRemove()

start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text = "О проекте"),
    KeyboardButton(text = "Участники"),
    KeyboardButton(text = "О партнерах"),
    KeyboardButton(text = "Ход проекта"),
)
start_kb2.adjust(2,2)
