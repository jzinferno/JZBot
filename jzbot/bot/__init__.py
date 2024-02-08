from aiogram import Bot
from aiogram.enums import ParseMode
from os import getenv

bot = Bot(getenv('BOT_TOKEN'), parse_mode=ParseMode.HTML)

async def download_file(file_id: str, save_path: str) -> None:
    file = await bot.get_file(file_id)
    await bot.download_file(file.file_path, save_path)
