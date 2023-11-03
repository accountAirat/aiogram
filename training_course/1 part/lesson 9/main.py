from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from training_course.first_project.config import TOKEN_API

HELP_COMMAND = """
<b>/help</b> - <em>список комманд</em>
<b>/start</b> - <em>начать работу с ботом</em>
<b>/id</b> - <em>возвращяет id пользователя</em>
<b>/sticker</b> - <em>возвращяет id стикера</em>
<b>/give</b> - <em>присылает котика</em>
"""


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=2)
ib_1 = InlineKeyboardButton(text='Button 1',
                            url='https://www.youtube.com/')
ib_2 = InlineKeyboardButton(text='Button 2',
                            url='https://www.youtube.com/')
ikb.add(ib_1, ib_2)


async def on_startup(_):
    print('####################SERVER_START####################')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND,
                        parse_mode='HTML',)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='<em>Добро пожаловать в наш <b>телеграм бот</b>!</em>',
                         parse_mode='HTML',
                         reply_markup=ikb)
    await message.delete()


@dp.message_handler(commands="photo")
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://daylapu.ru/text/img/schastlivaya_sobaka1.jpg")
    await message.delete()


@dp.message_handler(commands="location")
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            longitude=55,
                            latitude=74)
    await message.delete()


@dp.message_handler(commands=['id'])
async def id_command(message: types.Message):
    await bot.send_message(message.from_user.id, text=message.from_user.id)


@dp.message_handler(commands='give')
async def send_sticker(message: types.Message):
    await message.answer("Смотри какой котик ❤️")
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAIEtmPC7cDh_yPklztkHWmJS6hMgKRLAAJJAANZu_wl0SE8IplinAUtBA")


@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)


@dp.message_handler()
async def echo(message: types.Message):
    # await bot.send_message(chat_id=message.chat.id, text="Hello")
    await bot.send_message(chat_id=message.from_user.id, text="Hello")
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
