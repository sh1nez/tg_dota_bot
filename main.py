#from texts import photo_links_for_shop, all_items, item_dick, hero_dick
import datetime
import asyncio
from database import *

##############################################----START-----#############################################
@dis.message_handler(commands=['start'])#создаём пользователя
async def start_funk(message: aiogram.types):
    await starter(tg_user_id=message.from_user.id, chat_id=message.chat.id)

##############################################----PROFILE-----#############################################
@dis.message_handler(commands=['profile'])
async def profile_funk(message):
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
async def all_shop_funk(message):
    await show_main_menu(chat_id=message.chat.id, message_id=message.message_id, tg_id=message.from_user.id)

go_back_all_shop = CallbackData('gbtms', 'tg_user_id')
@dis.callback_query_handler(go_back_all_shop.filter())
async def go_back_all_shop_funk(callback):
    tg_id = int(callback.data.split(':')[1])
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return

    await show_main_menu(callback.message.chat.id, callback.message.message_id, callback.id, tg_id, callback.from_user.id)

#tradeheroes = CallbackData('trher', 'tg_user_id')
@dis.callback_query_handler(tradeheroes.filter())
async def tradeheroes_ne_funk(callback):
    tg_id = int(callback[1])
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    buttons = ((hero_dick[i]['name'], show_hero_n, (i, tg_id)) for i in hero_dick)
    ikm = make_inline_keyboard(3, *buttons)
    ikm.add(InlineKeyboardButton(text=f'в задницу хочу', callback_data=f"ss"))#go_to_shop_menu.new()))
    img = InputMediaPhoto(caption='ураура', type='photo', media=hero_dick[1]['event_img'])
    await bot.edit_message_media(reply_markup=ikm, media=img, message_id=callback.message.message_id,chat_id=callback.message.message_id)
    await bot.answer_callback_query(callback.id)

#tradeitems = CallbackData('tritm', 'tg_user_id')


@dis.callback_query_handler(tradeitems.filter())
async def tradeitems_funk(callback):
    tg_id = callback.data.split(':')[1]
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    buttons = (('фарми', callback_farm_item, (tg_id,)), ('дерсись', callback_fight_item, (tg_id,)),('бек', del_callback, (tg_id,)))
    ikm = make_inline_keyboard(2, *buttons)
    img = InputMediaPhoto(media=photo_links_for_shop[4], caption='шмотки (не ломать)')
    await bot.edit_message_media(media=img, chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=ikm)
    await bot.answer_callback_query(callback.id)




callback_farm_item = CallbackData('cfarmis', 'tg_id')
@dis.callback_query_handler(callback_farm_item.filter())
async def rcfarmis(callback):
    tg_id = int(callback.data.split(':')[1])
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    lens = len(item_dick['farm'])
    buttons = ((item_dick['farm'][i]['name']) for i in range(lens))
    ikm = make_inline_keyboard(2, *buttons)
    img = InputMediaPhoto(media=photo_links_for_shop[4], caption='фармила')
    await bot.edit_message_media(media=img, chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=ikm)


show_in_shop_items = CallbackData('sisi', 'tg_id')
@dis.callback_query_handler(show_in_shop_items.filter())
async def rsisi(callback):
    tg_id = callback.from_user.id
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]); return
    pass

callback_fight_item = CallbackData('cfightis', 'tg_id')
@dis.callback_query_handler(callback_fight_item.filter())
async def rcfightis(callback):
    tg_id = callback.data.split(':')
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    pass

#del_callback = CallbackData('del', 'tg_id')
@dis.callback_query_handler(del_callback.filter())
async def rdcfs(callback):
    tg_id = callback.data.split(':')
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return

show_hero_n = CallbackData('shns', 'hero_id', 'tg_user_id')
@dis.callback_query_handler(show_hero_n.filter())
async def show_hero_n_funk(callback):
    come =callback.data.split(':')
    hero_id = come[1]
    tg_id = come[2]
    if callback.from_user.id != tg_id:
        num = random.randint(0, len(enemy_click)-1)
        await bot.answer_callback_query(callback.id, text=enemy_click[num])
        return




##############################################----WORK-----#############################################
#if __name__ == '__main__':
#    aiogram.executor.start_polling(dis, )#skip_updates=True
