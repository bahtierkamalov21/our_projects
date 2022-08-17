import logging
import requests
from configuration import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Initialize bot and dispatcher
    bot = Bot(settings.TOKEN)
    dispatcher = Dispatcher(bot)

    # API request index
    index = 0

    # API answers
    response = requests.get(f"{settings.API_URL}projects").json()
    title = response[index]["title"]
    git_url = response[index]["git_url"]
    stack = response[index]["stack"]
    images = response[index]["images"]
    description = response[index]["description"]

    # Start function
    @dispatcher.message_handler(commands=["start"])
    async def start(message: types.Message):
        # Inline buttons
        inline_buttons = [
            types.InlineKeyboardButton(text="Список проектов", callback_data="project_list"),
        ]
        keyboard = InlineKeyboardMarkup()
        keyboard.add(*inline_buttons)
        # Await
        await message.answer(text=f"{settings.WELCOME_MESSAGE}", reply_markup=keyboard)

    @dispatcher.callback_query_handler(lambda c: c.data == "project_list")
    async def send_project_list(call: types.CallbackQuery):
        # Inline buttons
        inline_buttons = [
            types.InlineKeyboardButton(text="Назад", callback_data="prev_project"),
            types.InlineKeyboardButton(text="Далее", callback_data="next_project"),
        ]
        keyboard = InlineKeyboardMarkup()
        keyboard.add(*inline_buttons)
        # Await
        await bot.send_photo(
            call.message.chat.id,
            types.InputFile.from_url(f"{response[index]['images']}"),
            caption=f"{title} \nGit: {git_url} \nStack: {stack} \nОписание: {description}",
            reply_markup=keyboard
        )

    # Run long polling.
    executor.start_polling(dispatcher, skip_updates=True)


if __name__ == "__main__":
    main()
