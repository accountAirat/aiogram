from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text


from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

number = 0


def get_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Увеличить', callback_data='btn_increase'), InlineKeyboardButton('Уменьшить', callback_data='btn_decrease')]
    ])
    return ikb


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer(f'Текущее число {number}',
                         reply_markup=get_ikb())


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn'))
async def ikb_cb_handler(callback: types.CallbackQuery):
    global number
    if callback.data == "btn_increase":
        number+=1
        await callback.message.edit_text(f'Текущее число {number}',
                                         reply_markup=get_ikb())
    elif callback.data == "btn_decrease":
        number-=1
        await callback.message.edit_text(f'Текущее число {number}',
                                         reply_markup=get_ikb())
    else:
        1/0


async def on_startup(_):
    print('######SERVER_START######')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
