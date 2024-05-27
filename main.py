import requests
import base64
import time
from random import randint
from aiogram import Bot, Dispatcher, executor, types
from shedevr import generate_image
from magik import get_response

bot = Bot(token='6650314598:AAEtbPwZYa6-E4UpTyQzsizvJs-pSqicf98')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message) :
    await message.reply('Привет, DALEE3 шедеврум')

@dp.message_handler()
async def analize_message() :
    response_text = await get_response(message.text)
    await message.reply(f"вот твой волшебный промпт: {response_text}")
    await message.reply('Идет генерация изображеия, подождите')
    try:
        image_data = generate_image(response_text)
        await message.reply_photo(photo=image_data)
    except Exception as e:
        await message.reply(f'Произошла ошибка {e}')

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)