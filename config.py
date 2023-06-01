import aiogram
from apscheduler.schedulers.asyncio import AsyncIOScheduler
host = 'localhost'
user = 'root'
password = ''
db_name = 'test_bot'
token = '6241515938:AAHRAYFoUP7oWDMqJ4pEynnB0OWp6CBlq8k'
sheduler = AsyncIOScheduler(timezone='Europe/Moscow')
print('Я создал шедулер')
bot = aiogram.Bot(token)
dis = aiogram.Dispatcher(bot)
print('Диспетчер и бот созданы')
