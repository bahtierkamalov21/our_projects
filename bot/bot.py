import logging
from aiogram import Bot, Dispatcher, types, executor
from messages import *
from global_settings import *
import requests

def main():
    logging.basicConfig(level=logging.INFO)

    # Init
    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher(bot)

    # Backend
    response = requests.get(API_URL).json()
    index = 0

    # Functions
    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["List of projects"]
        keyboard.add(*buttons)
        await message.reply(WELCOME_MESSAGE, reply_markup=keyboard)

    # Inline buttons
    inline_buttons = [
        types.InlineKeyboardButton(text="Next project", callback_data="next_project"),
    ]

    # Add inline buttons in keyboard
    def get_keyboard():
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*inline_buttons)
        return keyboard

    # Get a list of projects
    @dp.message_handler(lambda message: message.text == "List of projects")
    async def get_projects(message: types.Message):
        images = response[index]["images"]
        message_caption = f"{response[index]['title']}\n{response[index]['stack']}\n{response[index]['description']}"
        await bot.send_photo(message.chat.id, types.InputFile.from_url(images), caption=message_caption, reply_markup=get_keyboard())

    # Get the next project in the response list
    @dp.callback_query_handler(text="next_project")
    async def get_next_project(call: types.CallbackQuery):
        index = +1
        images = response[index]["images"]
        message_caption = f"{response[index]['title']}\n{response[index]['stack']}\n{response[index]['description']}"

        # Check inline_buttons
        if len(inline_buttons) == 1:
            inline_buttons.append(types.InlineKeyboardButton(text="Prev project", callback_data="prev_project"))

        await call.message.edit_caption(message_caption, reply_markup=get_keyboard())
        await call.answer()

    # Get the previous project in the response list
    @dp.callback_query_handler(text="prev_project")
    async def get_prev_project(call: types.CallbackQuery):
        index = -1
        message_caption = f"{response[index]['title']}\n{response[index]['stack']}\n{response[index]['description']}"
        await call.message.edit_caption(message_caption, reply_markup=get_keyboard())
        await call.answer()

    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    main()
