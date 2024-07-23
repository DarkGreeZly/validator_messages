from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

import asyncio
import logging
import re


BOT_TOKEN = '6745763283:AAEFR7c1W9N6jNzBPvAqIAdQhvmuRkU9we4'
router = Router()
keywords = ["шукаю групу", "лечу"]


def matching_keyword(message_text, keyword):
    pattern = r'\b' + re.escape(keyword) + r'\b'
    return bool(re.search(pattern, message_text, re.IGNORECASE))


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Hello! I'm can validate messages in tg groups and delete them")


@router.message()
async def message_handler(msg: Message):
    for keyword in keywords: 
        if matching_keyword(msg.text, keyword):
            await msg.delete()


if __name__ == "__main__":
    asyncio.run(main())