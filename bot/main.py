import asyncio
import logging
import sys
from config.config import TOKEN
from message.message import message_router
from aiogram import Bot, Dispatcher

TOKEN = TOKEN

dp = Dispatcher()
dp.include_router(message_router)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
