from texts import photo_links_for_shop, all_items, item_dick, hero_dick
import random
import aiogram
#from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import datetime
import asyncio
from database import connection, maker_menu, update_gold, starttttt, dis, bot, show_local_hero, del_callback
@dis.message_handler(commands=['start'])#создаём пользователя
async def start(message: aiogram.types):
    tg_user_id = message.from_user.id
    chat_id = message.chat.id
    await starttttt(tg_user_id=tg_user_id, chat_id=chat_id)