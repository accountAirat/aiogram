from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text


from training_course.first_project.config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

if_voted = False

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='❤️', callback_data='like'), InlineKeyboardButton(text='👎', callback_data='dislike')],
    [InlineKeyboardButton(text='Closed keyboard', callback_data='close')]
])


async def on_startup(_):
    print('######SERVER_START######')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://fs.getcourse.ru/fileservice/file/download/a/570864/sc/18/h/a69f4d26b766e5373351495d5f54333d.jpg',
                         caption='Do you like?',
                         reply_markup=ikb)


@dp.callback_query_handler(text='close')
async def close_cl(callback: types.CallbackQuery):
    await callback.message.delete()


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    global if_voted
    if not if_voted:
        if callback.data == 'like':
            await callback.answer(text='like')
            if_voted = True
        await callback.answer(text='dislike')
        if_voted = True
    await callback.answer(show_alert=True,
                          text='Ты уже голосовал!')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
