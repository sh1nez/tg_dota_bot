from aiogram.types import Message
import meat.texts as txt


async def start(message: Message):
    """проверка базы данных"""
    ans = txt.true_start_text if True else txt.false_start_text
    await message.answer(f'{ans}\nДоступные команды:{txt.txt_commands()}')


async def start1(message: Message):
    """проверка базы данных"""
    ans = txt.true_start_text if True else txt.false_start_text
    await message.answer(f'{ans}\nДоступные команды(тест):{txt.txt_commands()}')