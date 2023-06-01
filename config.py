import aiogram
from apscheduler.schedulers.asyncio import AsyncIOScheduler
host = 'localhost'
user = 'root'
password = ''
db_name = 'test_bot'
token = '6065685536:AAHs04SSURkkRE74FdATgUzrudOlq6k_LX8'
sheduler = AsyncIOScheduler(timezone='Europe/Moscow')
print('Я создал шедулер')
bot = aiogram.Bot(token)
dis = aiogram.Dispatcher(bot)
print('Диспетчер и бот созданы')
