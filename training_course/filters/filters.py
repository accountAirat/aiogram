import re

from aiogram.dispatcher.filters import Filter
from aiogram import types


class EmailCheck(Filter):
    key = 'is_email'

    pattern = re.compile(r'[\w.-]+@[\w-]\.(com|ru)')

    async def check(self, msg: types.Message) -> bool:
        return self.pattern.match(msg.text)
