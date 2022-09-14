from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv, find_dotenv
import os, hashlib
from random import randint
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle

load_dotenv(find_dotenv())

bot = Bot(os.getenv('token'))
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    min = 0
    max = 100
    overall = randint(min, max)
    if overall == 0:
        text = 'Ты ебаный натурал...'
    if overall < 30:
        text = '🤡 Я гей на: ' + str(overall) + '%'
    if overall >= 30 and overall < 70:
        text = '😋Я гей на: ' + str(overall) + '%'
    if overall >= 70:
        text = '😎 Я гей на: ' + str(overall) + '%'
    result_gay_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [InlineQueryResultArticle(
    id = result_gay_id,
    title = 'Насколько ты гей',
    input_message_content = types.InputTextMessageContent(message_text = text))]

    await query.answer(articles, cache_time = 1, is_personal = True)








# @dp.message_handler(commands=['gay'])
# async def gay_test(message):
#     min = 0
#     max = 100
#     overall = randint(min, max)
#     if overall == 0:
#         await message.reply('Ты ебаный натурал...')
#     if overall < 30:
#         await message.reply('🤡 Я гей на: ' + str(overall) + '%')
#     if overall >= 30 and overall < 70:
#         await message.reply('😋Я гей на: ' + str(overall) + '%')
#     if overall >= 70:
#         await message.reply('😎 Я гей на: ' + str(overall) + '%')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
