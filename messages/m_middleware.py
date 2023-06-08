from typing import Any, Callable, Dict, Awaitable
from aiogram.dispatcher.event.handler import HandlerObject
from aiogram import BaseMiddleware
from aiogram.methods.send_message import SendMessage
from aiogram.types import Message
from aiogram.dispatcher.flags import get_flag
import asyncio


class PrivateMessage(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
       ) -> Any:
        if get_flag(data, 'private'):
            return await handler(event, data) if await self.stop(event) else None
        else:
            return await handler(event, data)

    @classmethod
    async def stop(cls, message):
        if message.chat.type == 'private':
            return True
        mes = await message.reply('Дружище, используй эту команду в лс')
        try:
            await asyncio.sleep(3)
            await message.delete()
            await mes.delete()
        except:
            await message.answer('❗️Выдайте боту права администратора❗️\n'
                                 '⚠️Сейчас у него нет возможности модерировать чат⚠️')

        else:
            pass
        finally:
            return False


class CheckReg(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:

        pass


class CheckTime(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        pass

