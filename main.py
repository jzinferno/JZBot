#!/usr/bin/env python3

from Modules.dispatcher import dp
from jzbot.bot import bot
import asyncio

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
