import logging

from aiogram import Bot, Dispatcher, executor, types
from checkwords import checkWords

API_TOKEN = '6219858226:AAG5jgRiukFpKmh7Pyom9D4vCaj14ySLcao'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dicpatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message:types.Message):
    await message.reply("Imlo botga xush kelibsiz!!!")

@dp.message_handler(commands='help')
async def send_welcome(message:types.Message):
    await message.reply("Botdan foydalanish uchun so'z yuboring")

@dp.message_handler()
async def checkImlo(message:types.Message):
    word = message.text
    result = checkWords(word)
    if result['available']:
        response = f"✅{word.capitalize()}"
    else:
        response = f"❌{word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅{text.capitalize()}\n"
    await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

