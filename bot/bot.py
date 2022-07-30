import logging
from aiogram import Bot, Dispatcher, types, executor
from messages import *
from local_settings import *
import requests

def main():
    logging.basicConfig(level=logging.INFO)

    # Init
    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher(bot)

    # Backend
    response = requests.get(API_URL)

    # Handlers
    @dp.message_handler(commands=['start'])

    # Functions
    async def start(message: types.Message):
        await message.reply(WELCOME_MESSAGE)

    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    main()