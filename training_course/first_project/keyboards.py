from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='/description')
b3 = KeyboardButton(text='Random photo')

kb.add(b1, b2).add(b3)

kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton(text='Рандом')
bp2 = KeyboardButton(text='Главное меню')

kb_photo.add(bp1, bp2)

ikb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton(text='❤️',
                          callback_data='Like'),
     InlineKeyboardButton(text='👎',
                          callback_data='Dislike')],
    [InlineKeyboardButton(text='Следующая фотография',
                          callback_data='next')],
    [InlineKeyboardButton(text='Главное меню',
                          callback_data='main')]
])
