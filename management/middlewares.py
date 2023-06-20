from aiogram import flags, BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from typing import Any, Callable, Dict, Awaitable
from aiogram.dispatcher.event.handler import HandlerObject
from aiogram.types import Message


class PrivateMessage(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
       ) -> Any:
        if await self.private(event):
            return await handler(event, data)
        else: print('false')

    @staticmethod
    def private(message: Message):
        if message.chat.type != 'private':
            return False
        else:
            return True
