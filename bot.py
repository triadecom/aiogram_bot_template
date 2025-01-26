from aiogram import Bot, executor

from dotenv import load_dotenv

import os

load_dotenv()
bot = Bot(os.getenv('TG_BOT_TOKEN'))