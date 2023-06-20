import asyncio
from aiogram.filters import CommandStart, Command
from aiogram import Bot, Dispatcher, Router, F
from configparser import ConfigParser
from management.middlewares import PrivateMessage
from answers.messages.starting import start


config = ConfigParser()
config.read('bot_config.cfg')
print(config['bot']['token'])
bot = Bot(config['bot']['token'])
private_router = Router()
private_router.message.middleware(PrivateMessage())
dp = Dispatcher()
dp.include_routers(private_router)

a = private_router.message.register(start, CommandStart())
print(a)


async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(dp.start_polling(bot))


if __name__ == '__main__':
    asyncio.run(main())