#from texts import photo_links_for_shop, all_items, item_dick, hero_dick
import datetime
import asyncio
from database import *

##############################################----START-----#############################################
@dis.message_handler(commands=['start'])#создаём пользователя
async def start_funk(message: aiogram.types):
    await starter(tg_id=message.from_user.id, chat_id=message.chat.id)

##############################################----PROFILE-----#############################################
@dis.message_handler(commands=['profile'])
async def profile_funk(message):
    sql_code1 = f"SELECT money, status FROM players WHERE tg_id = {message.from_user.id}"
    sql_code2 = f"SELECT id, item_name FROM items WHERE tg_id = {message.from_user.id} AND hero_id IS NULL;"
    money_status, arr = connection.select_one(sql_code1), connection.select_all(sql_code2)
    ikm = make_inline_keyboard(2, *(('мои герои', tradeheroes, ()),('инвентарь', asd,()),))
    text = ''
    text = 'у тебя нет предметов' if not arr else text.join(i for i in arr)
    caption_text =f'денег - {money_status[0]}\nбатлпас {money_status[1]}\n{text}\n'
    #img = InputMediaPhoto(media=photo_links_for_shop[1], caption=)
    await bot.send_photo(chat_id=message.chat.id, reply_markup=ikm, photo=photo_links_for_shop[2], caption=caption_text)


##############################################----SHOP-----#############################################
@dis.message_handler(commands =['shop'])
async def all_shop_funk(message):
    await show_main_menu(chat_id=message.chat.id, message_id=message.message_id, tg_id=message.from_user.id)


go_back_all_shop = CallbackData('gbtms', 'tg_id')
@dis.callback_query_handler(go_back_all_shop.filter())
async def go_back_all_shop_funk(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return

    await show_main_menu(callback.message.chat.id, callback.message.message_id, callback.id, tg_id, callback.from_user.id)


#tradeheroes = CallbackData('trher', 'tg_id')
@dis.callback_query_handler(tradeheroes.filter())
async def tradeheroes_ne_funk(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    buttons = ((hero_dick[i]['name'], show_hero_in_shop, (i, tg_id)) for i in hero_dick)
    ikm = make_inline_keyboard(3, *buttons)
    ikm.add(InlineKeyboardButton(text=f'в задницу хочу', callback_data=f"ss"))#go_to_shop_menu.new()))
    img = InputMediaPhoto(caption='ураура', type='photo', media=hero_dick[1]['event_img'])
    await bot.edit_message_media(reply_markup=ikm, media=img, message_id=callback.message.message_id,chat_id=callback.message.message_id)
    await bot.answer_callback_query(callback.id)


#tradeitems = CallbackData('tritm', 'tg_id')
@dis.callback_query_handler(tradeitems.filter())
async def tradeitems_funk(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    buttons = (('фарми', callback_farm_item, (tg_id,)), ('дерсись', callback_fight_item, (tg_id,)),('удалить', del_callback, (tg_id,)))
    ikm = make_inline_keyboard(2, *buttons)
    img = InputMediaPhoto(media=photo_links_for_shop[4], caption='шмотки (не ломать)')
    await bot.edit_message_media(media=img, chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=ikm)
    await bot.answer_callback_query(callback.id)


#############################################----BUY_iTEMS-----############################################
callback_farm_item = CallbackData('cfarmis', 'tg_id')
@dis.callback_query_handler(callback_farm_item.filter())
async def rcfarmis(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return 
    buttons = ((item_dick['farm'][i]['name'],show_hero_in_shop, (i, tg_id)) for i in range(len(item_dick['farm'])))
    ikm = make_inline_keyboard(2, *buttons)
    img = InputMediaPhoto(media=photo_links_for_shop[4], caption='фармила')
    await bot.edit_message_media(media=img, chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=ikm)


show_in_shop_items = CallbackData('sisi', 'tg_id')
@dis.callback_query_handler(show_in_shop_items.filter())
async def rsisi(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]); return
    pass

callback_fight_item = CallbackData('cfightis', 'tg_id')
@dis.callback_query_handler(callback_fight_item.filter())
async def rcfightis(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    pass

#del_callback = CallbackData('del', 'tg_id')
@dis.callback_query_handler(del_callback.filter())
async def rdcfs(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return



##############################################----BUY_HERO-----#############################################

show_hero_in_shop = CallbackData('shns', 'tg_id', 'hero_id',)
@dis.callback_query_handler(show_hero_in_shop.filter())
async def show_hero_in_shop_funk(callback):
    tg_id,hero_id  = r_cbd(callback.data)
    if callback.from_user.id != tg_id:await bot.answer_callback_query(callback.id, text=enemy_click[rnum()]);return
    b = (('купить', wanna_d7e, (tg_id, hero_id)), ('назад', tradeheroes,(tg_id,)))
    ikm = make_inline_keyboard(2, *b)
    img = InputMediaPhoto(media=photo_links_for_shop[2], caption='asd')
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id, chat_id=callback.message.chat.id)

wanna_d7e = CallbackData('diwd', 'tg_id', 'hero_id')
@dis.callback_query_handler(wanna_d7e.filter())
async def rfwannad7e(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if callback.from_user.id != tg_id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]); return
    if money_of_user(tg_id) >= hero_dick[hero_id]['price']:
        img = InputMediaPhoto(media=photo_links_for_shop[1], caption='точно точно?') ##вопрос
        ikm = (1, (('да!!', buy_hero_shop, (tg_id, hero_id)),('мисклик(', show_hero_in_shop, (tg_id, hero_id,))))
        await bot.edit_message_media(media=img,reply_markup=ikm, message_id=callback.message.message_id, chat_id=callback.message.chat.id)
        await bot.answer_callback_query()
        return
    img = InputMediaPhoto(media=photo_links_for_shop[5], caption='у тебя не хватает денег(')#чёто типо нищий
    ikm = (1, (('naZad', show_hero_in_shop, (tg_id, hero_id,))))#)('тут будет типо иди работй негр', buy_hero_shop, (tg_id, hero_id))
    await bot.edit_message_media(reply_markup=ikm, media=img,)


buy_hero_shop = CallbackData('bhs', 'tg_id', 'hero_id')
@dis.callback_query_handler(buy_hero_shop.filter())
async def rbhis(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if callback.from_user.id!=tg_id:await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    buy_hero(tg_id, hero_id)
    #тут должно перекидывать на страницу с новым гером
    await bot.answer_callback_query(callback.id, text=f"ура ура ты купил {hero_dick[hero_id]['name']}")


##############################################----WORK-----#############################################
if __name__ == '__main__':
   aiogram.executor.start_polling(dis, )#skip_updates=True
