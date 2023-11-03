from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
import random

from config import *
from keyboards import *

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

arr_photos = ['https://daylapu.ru/text/img/schastlivaya_sobaka1.jpg',
              'https://imgtest.mir24.tv/uploaded/images/crops/2022/August/870x489_0x52_detail_crop_20220807215642_0750dd20_2aba15503c60b7979a19f4329aeb1b4c8698c544c6227a198cd62e216a3288c3.jpg',
              'https://avatars.dzeninfra.ru/get-zen_doc/5219035/pub_6433f9bd612a72592a87f6f2_6433fa17d0f4b4792617848e/scale_1200']

photos = dict(zip(arr_photos, ['Пупсик', 'Красавчик', 'Рыжик']))
random_photo = random.choice(list(photos.keys()))


async def on_startup(_):
    print('######SERVER_START######')


async def send_random(message: types.Message):
    global random_photo
    random_photo = random.choice(list(photos.keys()))
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_photo,
                         caption=photos[random_photo],
                         reply_markup=ikb)


@dp.message_handler(Text(equals='Random photo'))
async def open_kb_photo(message: types.Message):
    await message.answer(text='Рандомная фотография!',
                         reply_markup=ReplyKeyboardRemove())
    await send_random(message)
    await message.delete()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text='Добро пожаловать в наш бот! 🕺',
                         reply_markup=kb)
    await message.delete()

    
@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.answer(text=HELP_COMMAND,
                         parse_mode='HTML')
    await message.delete()

    
@dp.message_handler(commands=['description'])
async def cmd_description(message: types.Message):
    await message.answer(text=DESCRIPTION)
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker="CAACAgIAAxkBAAIEtmPC7cDh_yPklztkHWmJS6hMgKRLAAJJAANZu_wl0SE8IplinAUtBA")
    await message.delete()


@dp.callback_query_handler(text='main')
async def callback_open_main_kb(callback: types.CallbackQuery):
    await callback.message.answer(text='Добро пожаловать в главное меню!',
                                  reply_markup=kb)
    await callback.message.delete()
    await callback.answer()


@dp.message_handler(Text(equals='Главное меню'))
async def open_main_kb(message: types.Message):
    await message.answer(text='Добро пожаловать в главное меню!',
                         reply_markup=kb)
    await message.delete()


@dp.callback_query_handler()
async def callback_random_photo(callback: types.CallbackQuery):
    global random_photo
    if callback.data == 'Like' or callback.data == 'Dislike':
        await callback.answer(callback.data)
    elif callback.data == 'next':
        random_photo = random.choice(list(filter(lambda x: x != random_photo, list(photos.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo,
                                                           types='photo',
                                                           caption=photos[random_photo]),
                                          reply_markup=ikb)
        await callback.answer()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
