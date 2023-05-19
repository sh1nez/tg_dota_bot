from texts import photo_links_for_shop, all_items, item_dick, hero_dick
import random
#import aiogram
#from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import datetime
import asyncio
#from database import connection, maker_menu, update_gold, starttttt, dis, bot, show_local_hero, del_callback
from database import *#connection, dis, bot, InputMediaPhoto, InlineKeyboardButton, InlineKeyboardMarkup, aiogram

##############################################----START-----#############################################
@dis.message_handler(commands=['start'])#создаём пользователя
async def start(message: aiogram.types):
    tg_user_id = message.from_user.id
    chat_id = message.chat.id
    await starter(tg_user_id=tg_user_id, chat_id=chat_id)

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
    await show_main_menu(chat_id=message.chat.id, message_id=message.message_id)



#tradeheroes = CallbackData('trher', 'tg_user_id')
def make_menu(ikm:InlineKeyboardMarkup, text, call_data:CallbackData, *args):
    print(args)
    print(*args)
    return ikm.add(InlineKeyboardButton(text=text, callback_data=call_data.new(*args)))

show_hero_n = CallbackData('hero', 'hero_id', 'tg_user_id')
@dis.callback_query_handler(tradeheroes.filter())
async def tradeheroes_ne_funk(callback):
    tg_user_id = callback[1]
    ikm = InlineKeyboardMarkup(row_width=len(hero_dick)+1)
    buttons = tuple()
    print(tup)
    make_inline_keyboard(3, )

    for i in range(0, len(hero_dick), 2):
        if len(hero_dick)-i>=2:
            ikm = make_menu(make_menu(ikm, hero_dick[i]['name'], show_n_hero, i),hero_dick[i+1]['name'], show_hero_n, i)
        elif len(hero_dick)-i==1:
            ikm = make_menu(ikm, hero_dick[i]['name'], show_hero_n, i)
        else: break
        # ikm.add(InlineKeyboardButton(text=hero_dick[i]['name'], callback_data=show_hero_n.new(i)))  # f'geroi#{i}'))
        #
        # ikm.add(InlineKeyboardButton(text=hero_dick[i]['name'], callback_data=show_hero_n.new(i)),
        #        InlineKeyboardButton(text=hero_dick[i + 1]['name'], callback_data=show_hero_n.new(i + 1)))

                    #             InlineKeyboardButton(text=hero_dick[i+1]['name'], callback_data=show_hero_n.new(i+1)))
    # for i in range(0, len(hero_dick), 2):
    #     try:
    #         ikm.add(InlineKeyboardButton(text=hero_dick[i]['name'], callback_data=show_hero_n.new(i)),# f'geroi#{i}'),
    #             InlineKeyboardButton(text=hero_dick[i+1]['name'], callback_data=show_hero_n.new(i+1)))
    #         #print('lj,fdbk')
    #     except:
    #         try:
    #             ikm.add(
    #                 InlineKeyboardButton(text=hero_dick[i]['name'], callback_data=show_hero_n.new(i)))  # f'geroi#{i}'))
    #             #print('hui')
    #         except:
    #             #print('(((')
    #             break
    ikm.add(InlineKeyboardButton(text=f'в задницу хочу', callback_data=go_to_shop_menu.new()))  #f'back_to_shop#{chat_id}#{mesas_id}'))
    #img = types.InputMediaPhoto(caption='asd', media=photo_links_for_shop[0], type='photo')
    img = InputMediaPhoto(caption='ураура', type='photo', media=hero_dick[1]['event_img'])
    await bot.edit_message_media(reply_markup=ikm, media=img, message_id=callback.message.message_id, chat_id=callback.message.message_id)
    await bot.answer_callback_query(callback.id)
##############################################----WORK-----#############################################
if __name__ == '__main__':
    aiogram.executor.start_polling(dis, )#skip_updates=True
