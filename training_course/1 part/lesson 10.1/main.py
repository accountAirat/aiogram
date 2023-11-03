from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.filters import Text
from training_course.first_project.config import TOKEN_API
from keyboard import kb
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

HELP_COMMAND = """
<b>/help</b> - <em>список комманд</em>
<b>/start</b> - <em>начать работу с ботом</em>
<b>/id</b> - <em>возвращяет id пользователя</em>
"""


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('######SERVER_START######')


@dp.message_handler(Text(equals="Button"))


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND,
                        parse_mode='HTML',)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='<em>Добро пожаловать в наш <b>телеграм бот</b>!</em>',
                         parse_mode='HTML',
                         reply_markup=kb)
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
