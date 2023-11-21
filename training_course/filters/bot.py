from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from filters import EmailCheck

bot = Bot(TOKEN_API)
dp = Dispatcher(bot=bot)


@dp.message_handler(EmailCheck)
async def check_mail(message: types.Message) -> None:
    await message.answer('It work!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
