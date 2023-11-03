from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


from training_course.first_project.config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('######SERVER_START######')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/vote')
kb.add(b1, b2)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Welcome',
                         reply_markup=kb)


@dp.message_handler(commands=['vote'])
async def vote_command(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='❤️',
                               callback_data='like')
    ib2 = InlineKeyboardButton(text='👎',
                               callback_data='dislike')
    ikb.add(ib1, ib2)
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://daylapu.ru/text/img/schastlivaya_sobaka1.jpg',
                         caption='Do you like?',
                         reply_markup=ikb)


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text='like')
    await callback.answer(text='dislike')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
