from aiogram.types import Message
# from aiogram.methods.send_message import SendMessage


async def start(message: Message):
    await message.answer('hello')