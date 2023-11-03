from aiogram import executor, Dispatcher, Bot, types
from  aiogram.contrib.fsm_storage.memory import MemoryStorage


from config import TOKEN_API


storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot=bot,
                storage=storage)





if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)