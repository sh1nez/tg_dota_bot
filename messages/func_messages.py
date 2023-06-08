from aiogram.types import Message
import meat.texts as txt


async def start(message: Message):
    """проверка базы данных"""
    ans = txt.true_start_text if True else txt.false_start_text
    description = txt.start_desc if True else ''
    await message.answer(f'{ans}\n{description}')


async def helper(message: Message):
    await message.answer(f"Все доступные на данный момент команды:\n{txt.txt_commands()}")


async def profile(message: Message):
    pass


async def shop(message: Message):
    pass


async def bonus(message: Message):
    pass


async def farm(message: Message):
    pass


async def fight(message: Message):
    pass