from aiogram import Dispatcher, Bot, Router
from config import token
from aiogram.filters.command import Command, CommandStart
from messages.func_messages import start, start1
from messages.m_middleware import PrivateMessage

bot = Bot(token)
dp = Dispatcher(bot=bot)
message_router = Router()
callback_router = Router()

message_router.message.register(start, CommandStart(), flags={'private': True})
message_router.message.register(start, Command(prefix='/', commands='profile'), flags={'private': False})
#message_router.message.register(start1)
#message_router.message.register(start1, F.text, flags={'pisapopa': 'asdasd', 'private': False})

if __name__ == '__main__':
    print('run')
    message_router.message.middleware(PrivateMessage())
    dp.include_routers(message_router, callback_router)
    dp.run_polling(bot)
