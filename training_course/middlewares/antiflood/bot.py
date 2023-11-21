from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from middlewares import ThrottlingMiddleware

storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler()
async def just_handler(msg: types.Message) -> None:
    await msg.answer(text='Okay')


if __name__ == '__main__':
    dp.middleware.setup(ThrottlingMiddleware())
    executor.start_polling(dp, skip_updates=True)
