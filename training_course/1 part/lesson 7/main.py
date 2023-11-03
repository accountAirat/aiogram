from aiogram import Bot, Dispatcher, types, executor
from training_course.first_project.config import TOKEN_API, ADMIN


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('####################SERVER_START####################')


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


@dp.message_handler()
async def echo(message: types.Message):
    # await bot.send_message(chat_id=message.chat.id, text="Hello")
    await bot.send_message(chat_id=message.from_user.id, text="Hello")
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
