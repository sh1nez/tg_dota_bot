from texts import photo_links_for_shop, all_items, item_dick, hero_dick
import random
import datetime
import asyncio
from database import *#connection, dis, bot, InputMediaPhoto, InlineKeyboardButton, InlineKeyboardMarkup, aiogram

##############################################----START-----#############################################
@dis.message_handler(commands=['start'])#создаём пользователя
async def start(message: aiogram.types):
    await starter(tg_user_id=message.from_user.id, chat_id=message.chat.id)

##############################################----PROFILE-----#############################################
@dis.message_handler(commands=['profile'])
async def profile(message):
    sql_code1 = f"SELECT money, status FROM players WHERE tg_id = {message.from_user.id}"
    sql_code2 = f"SELECT id, item_name FROM items WHERE tg_user_id = {message.from_user.id} AND hero_id IS NULL;"
    money_status, arr = connection.select_one(sql_code1), connection.select_all(sql_code2)
    ikm = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='герои', callback_data=heroes_habdler.new(message.from_user.id)),
            InlineKeyboardButton(text='инвентарь', callback_data=show_items_user.new(message.from_user.id))) #go_to_shop_menu.new()))
    text = ''
    text = 'у тебя нет предметов' if not arr else text.join(i for i in arr)
    #if not arr:
    #    text= 'у тебя нет предметов'
    #else:
    #    for i in arr:
    #        text = f"{i}"
    caption_text = f'денег - {money_status[0]}\nбатлпас {money_status[1]}\n{text}\n'
    img = InputMediaPhoto(media=photo_links_for_shop[1], caption=f"as")
    await bot.send_photo(chat_id=message.chat.id, reply_markup=ikm, photo=photo_links_for_shop[2], caption=caption_text)

##############################################----SHOP-----#############################################
@dis.message_handler(commands =['shop'])
async def all_shop(message):
    await show_main_menu(chat_id=message.chat.id, message_id=message.message_id, tg_id=message.from_user.id)

go_back_all_shop = CallbackData('gbtms', 'tg_user_id')
@dis.callback_query_handler(go_back_all_shop.filter())
async def rlygbtmm(callback):
    tg_id = int(callback.data.split(':')[1])
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, text=enemy_click)
    await show_main_menu(callback.message.chat.id, callback.message.message_id, callback.id, tg_id, callback.from_user.id)

#tradeheroes = CallbackData('trher', 'tg_user_id')
@dis.callback_query_handler(tradeheroes.filter())
async def tradeheroes_ne_funk(callback):
    tg_id = int(callback[1])
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, text=enemy_click)
    buttons = tuple((hero_dick[i]['name'], show_hero_n, (i, tg_id) ) for i in hero_dick)
    ikm = make_inline_keyboard(3, *buttons)
    ikm.add(InlineKeyboardButton(text=f'в задницу хочу', callback_data=f"ss"))#go_to_shop_menu.new()))
    img = InputMediaPhoto(caption='ураура', type='photo', media=hero_dick[1]['event_img'])
    await bot.edit_message_media(reply_markup=ikm, media=img, message_id=callback.message.message_id,chat_id=callback.message.message_id)
    await bot.answer_callback_query(callback.id)

show_hero_n = CallbackData('heron', 'hero_id', 'tg_user_id')
@dis.callback_query_handler(show_hero_n.filter())
async def rshn(callback):
    come =callback.data.split(':')
    hero_id = come[1]
    tg_id = come[2]
    if callback.from_user.id != tg_id:
        await bot.answer_callback_query(callback.id, text=enemy_click)
        return

#tradeitems = CallbackData('tritm', 'tg_user_id')
@dis.callback_query_handler(tradeitems.filter())
async def rsri(callback):
    tg_id = callback.data.split(':')[1]
    if callback.from_user.id != tg_id:
        await bot.answer_callback_query(callback.id, text=enemy_click)
        return


##############################################----WORK-----#############################################
if __name__ == '__main__':
    aiogram.executor.start_polling(dis, )#skip_updates=True
