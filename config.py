from tzlocal import get_localzone
import aiogram
from apscheduler.schedulers.asyncio import AsyncIOScheduler
sheduler = AsyncIOScheduler(timezone=get_localzone())
host = 'yuralehl.beget.tech'  #localhost
user = 'yuralehl_dota'  # root
password = 'P0pAp1sA' #
db_name = 'yuralehl_dota' #test_bot
token = '6241515938:AAHRAYFoUP7oWDMqJ4pEynnB0OWp6CBlq8k' # 6065685536:AAHs04SSURkkRE74FdATgUzrudOlq6k_LX8
print('Я создал шедулер')
bot = aiogram.Bot(token)
dis = aiogram.Dispatcher(bot)
print('Диспетчер и бот созданы')
