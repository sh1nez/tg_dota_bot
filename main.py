import aiogram
from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import pymysql
import datetime
import asyncio
from texts import *
from functions import *
from config import token, host, user, password, db_name
print('я начал')
bot = aiogram.Bot(token)
dis = aiogram.Dispatcher(bot)

try:
    connect = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
    )
except:  print('ConnectionError')

@dis.message_handler(commands=['start'])#прост отвечает
async def start(message: aiogram.types):
    await message.answer(text=start_text)


if __name__ == '__main__':
    aiogram.executor.start_polling(dis, )#skip_updates=True