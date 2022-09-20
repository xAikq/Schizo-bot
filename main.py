from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv, find_dotenv
import os, hashlib
from random import randint
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle

load_dotenv(find_dotenv())

bot = Bot(os.getenv('token'))
dp = Dispatcher(bot)

toaster_result = {'0': 'Нихуя ты не тостер',
                  '1': 'Нихуя ты не тостер',
                  '2': 'Нихуя ты не тостер',
                  '3': 'Нихуя ты не тостер',
                  '4': 'Нихуя ты не тостер',
                  '5': 'Нихуя ты не тостер',
                  '6': 'Нихуя ты не тостер',
                  '7': 'Ты лох какой-то, а не тостер',
                  '8': 'Ты киберспортивный тостер',
                  '9': 'Ты обычный тостер'}

def inline_gay_handler():
    min_gay = 0
    max_gay = 100
    overall_gay = randint(min_gay, max_gay)
    if overall_gay == 0:
        gay_text = 'Ты ебаный натурал...'
    if overall_gay > 0 and overall_gay < 30:
        gay_text = '🤡 Я гей на: ' + str(overall_gay) + '%'
    if overall_gay >= 30 and overall_gay < 70:
        gay_text = '😋Я гей на: ' + str(overall_gay) + '%'
    if overall_gay >= 70:
        gay_text = '😎 Я гей на: ' + str(overall_gay) + '%'
    result_gay_id: str = hashlib.md5(gay_text.encode()).hexdigest()

    gay_articles = [InlineQueryResultArticle(
    id = result_gay_id,
    title = 'Насколько ты гей',
    description = 'Насколько ты любишь в попу',
    thumb_url = 'https://i.ytimg.com/vi/jy0bm4rXXQ0/maxresdefault_live.jpg',
    input_message_content = types.InputTextMessageContent(message_text = gay_text))]
    return gay_articles

def inline_beer_handler():
    min_beer = 0
    max_beer = 100
    overall_beer = randint(min_beer, max_beer)
    if overall_beer == 0:
        beer_text = 'Нихуя ты не пиво...'
    if overall_beer > 0 and overall_beer < 30:
        beer_text = '🤡 Я пиво на: ' + str(overall_beer) + '%'
    if overall_beer >= 30 and overall_beer < 70:
        beer_text = '😋Я пиво на: ' + str(overall_beer) + '%'
    if overall_beer >= 70:
        beer_text = '😎 Я пиво на: ' + str(overall_beer) + '%'
    result_beer_id: str = hashlib.md5(beer_text.encode()).hexdigest()

    beer_articles = [InlineQueryResultArticle(
    id = result_beer_id,
    title = 'Насколько ты пиво',
    description = 'Покажи своё пивное пузо',
    thumb_url = 'https://headtopics.com/images/2019/3/18/lentaruofficial/105010861085109120479-1107539910196674560.webp?w=1280&h=853&q=1',
    input_message_content = types.InputTextMessageContent(message_text = beer_text))]
    return beer_articles

def inline_deadinside_handler():
    min_deadinside = 0
    max_deadinside = 100
    overall_deadinside = randint(min_deadinside, max_deadinside)
    if overall_deadinside == 0:
        deadinside_text = 'Нихуя ты не дединсайд...'
    if overall_deadinside > 0 and overall_deadinside < 30:
        deadinside_text = '🤡 Я дединсайд на: ' + str(overall_deadinside) + '%'
    if overall_deadinside >= 30 and overall_deadinside < 70:
        deadinside_text = '😋Я дединсайд на: ' + str(overall_deadinside) + '%'
    if overall_deadinside >= 70:
        deadinside_text = '😎 Я дединсайд на: ' + str(overall_deadinside) + '%'
    result_deadinside_id: str = hashlib.md5(deadinside_text.encode()).hexdigest()

    deadinside_articles = [InlineQueryResultArticle(
    id = result_deadinside_id,
    title = 'Насколько ты дединсайд',
    description = 'ТЫСЯЧА... МИНУС... СЕМЬ...',
    thumb_url = 'https://headtopics.com/images/2019/3/18/lentaruofficial/105010861085109120479-1107539910196674560.webp?w=1280&h=853&q=1',
    input_message_content = types.InputTextMessageContent(message_text = deadinside_text))]
    return deadinside_articles

def inline_toaster_handler():
        min_toaster = 0
        max_toaster = 9
        overall_toaster = str(randint(min_toaster, max_toaster))
        toaster_text = toaster_result.get(f'{overall_toaster}')
        result_toaster_id: str = hashlib.md5(toaster_text.encode()).hexdigest()

        toaster_articles = [InlineQueryResultArticle(
        id = result_toaster_id,
        title = 'Насколько ты тостер',
        description = 'Чё, тостер дохуя?',
        thumb_url = 'https://headtopics.com/images/2019/3/18/lentaruofficial/105010861085109120479-1107539910196674560.webp?w=1280&h=853&q=1',
        input_message_content = types.InputTextMessageContent(message_text = toaster_text))]
        return toaster_articles

@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    articles = inline_gay_handler() + inline_beer_handler() +  inline_deadinside_handler() + inline_toaster_handler()
    await query.answer(results = articles, cache_time = 60, is_personal = True)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
