from aiogram import Bot, Dispatcher, executor, types
from training_course.first_project.config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_upper(message: types.Message):
    if message.text.count(' ') >= 1:
        await message.answer(text=message.text)
    else:
        await message.answer(text=message.text.upper())


if __name__ == '__main__':
    print('####################SERVER_START####################')
    executor.start_polling(dp)
