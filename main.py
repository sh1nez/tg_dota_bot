from aiogram import Dispatcher, Bot, Router, F
from config import token
from aiogram.filters.command import Command, CommandStart
from messages.func_messages import start, helper, profile, shop, bonus, farm, fight
from messages.m_middleware import PrivateMessage, CheckTime, CheckReg

bot = Bot(token)
dp = Dispatcher(bot=bot)
message_private = Router()
message_looker = Router()
message_time = Router()
callback_router = Router()

message_private.message.register(start, CommandStart(), flags={'private': True})
dp.message.register(helper, Command(commands=['help']))
dp.message.register(helper, F.text == 'помргите')

message_looker.message.register(profile, Command(commands=['profile']))
message_looker.message.register(shop, Command(commands=['shop']))
message_time.message.register(bonus, Command(commands=['bonus']))

message_time.message.register(bonus, Command(commands=['bonus']), flags={'time': 'day'})
message_time.message.register(farm, Command(commands=['farm']), flags={'time': 'time'})
message_time.message.register(fight, Command(commands=['fight']), flags={'time': 'time'})

if __name__ == '__main__':
    print('run')
    message_private.message.middleware(PrivateMessage())
    message_looker.message.middleware(CheckReg())
    message_time.message.middleware(CheckReg())
    message_time.message.middleware(CheckTime())
    dp.include_routers(message_private, message_looker, message_time)
    dp.run_polling(bot)
