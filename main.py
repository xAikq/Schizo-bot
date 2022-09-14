from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv, find_dotenv
import os
from random import randint

load_dotenv(find_dotenv())

bot = Bot(os.getenv('token'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['gay'])
async def gay_test(message):
    min = 0
    max = 100
    overall = randint(min, max)
    if overall == 0:
        await message.reply('Ты ебаный натурал...')
    if overall < 30:
        await message.reply('🤡 Я гей на: ' + str(overall) + '%')
    if overall >= 30 and overall < 70:
        await message.reply('😋Я гей на: ' + str(overall) + '%')
    if overall >= 70:
        await message.reply('😎 Я гей на: ' + str(overall) + '%')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
