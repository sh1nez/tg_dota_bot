import datetime

from database import *
##############################################----START-----#############################################
@dis.message_handler(commands=['start'])#создаём пользователя
async def start_funk(message: aiogram.types):
    await starter(tg_id=message.from_user.id, chat_id=message.chat.id)

##############################################----PROFILE-----#############################################

@dis.message_handler(commands=['profile'])
async def profile_funk(message):
    tg_id = message.from_user.id
    await make_profile(tg_id, message.chat.id)

#my_heroes = CallbackData('spmh', 'tg_id')
@dis.callback_query_handler(my_heroes.filter())
async def rsmhip(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    tup = find_id_name_all_heroes(tg_id)
    buttons = ((hero_dick[i[0]]['name'], show_hero_in_inventory, (tg_id, i[0],),) for i in tup)
    ikm = make_inline_keyboard(2, *buttons).add(InlineKeyboardButton(text='бек', callback_data=back_to_profile.new(tg_id)))
    img = InputMediaPhoto(caption='герои', media=photo_links_for_shop[3])
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id, chat_id=callback.message.chat.id)
    await bot.answer_callback_query(callback.id)


show_hero_in_inventory = CallbackData('shiip', 'tg_id', 'hero_id')
@dis.callback_query_handler(show_hero_in_inventory.filter())
async def dshii(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    buttons = (('фармить',send_hero_farm, (tg_id, hero_id,)), ('драться', send_hero_fight, (tg_id, hero_id,)),
     ('шмотки', items_hero_inventory, (tg_id, hero_id,)), ('back', my_heroes, (tg_id,)))
    ikm = make_inline_keyboard(3, *buttons)
    img = InputMediaPhoto(media=photo_links_for_shop[1], caption=f"вот твой {hero_dick[hero_id]['name']}")
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id, chat_id=callback.message.chat.id)
    await bot.answer_callback_query(callback.id)


send_hero_farm = CallbackData('shtfarm', 'tg_id', 'hero_id')
@dis.callback_query_handler(send_hero_farm.filter())
async def shfarm(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    if check_time_farm(tg_id, hero_id):
        await bot.answer_callback_query(callback.id,text=f"{hero_dick[hero_id]['name']} отправлен фармить")
        f_s_hero_farm(tg_id, hero_id)
    else: await bot.answer_callback_query(callback.id, text=f"{hero_dick[hero_id]['name']} занят")



send_hero_fight = CallbackData('shtfight', 'tg_id', 'hero_id')
@dis.callback_query_handler(send_hero_fight.filter())
async def shfight(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return

    await bot.answer_callback_query(callback.id, text=f"{hero_dick[hero_id]['name']}")


items_hero_inventory = CallbackData('sliii', 'tg_id', 'hero_id')
@dis.callback_query_handler(items_hero_inventory.filter())
async def rihi(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    text = 'к этому добавит итемы'
    aa = find_wear_items(tg_id, hero_id)
    #print(aa, hero_id)
    if not aa:
        text = 'у твоего героя нет предметов'
        ikm = make_inline_keyboard(1, ('назад к герою', show_hero_in_inventory, (tg_id,hero_id,)),
                                   ('одеть ещё', wear_from_inventory, (tg_id, hero_id,)))
    else:
        items = find_wear_items(tg_id, hero_id)
        b = ((all_items[i[0]]['name'], remove_item_from_hero, (tg_id, hero_id, i[0])) for i in items)
        print(b)
        #if len(items)<6:
        #    b+=(1,2,3)
        ikm = make_inline_keyboard(3, *b).add(InlineKeyboardButton(text='одеть ещё', callback_data=wear_from_inventory.new(tg_id, hero_id))).add(
            InlineKeyboardButton(text='назад к герою', callback_data=show_hero_in_inventory.new(tg_id,hero_id,)))
    img = InputMediaPhoto(media=photo_links_for_shop[0], caption=text)
    await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.answer_callback_query(callback.id)

wear_from_inventory = CallbackData('wfi', 'tg_id', 'hero_id')


remove_item_from_hero = CallbackData('rifh', 'tg_id', 'hero_id', 'item_id')
@dis.callback_query_handler(remove_item_from_hero.filter())
async def rifhp(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return


back_to_profile = CallbackData('pbtp', 'tg_id')
@dis.callback_query_handler(back_to_profile.filter())
async def rbtpn(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    await make_profile(tg_id, callback.message.chat.id, callback.message.message_id, callback.id)


# users_inventory = CallbackData('suic', 'tg_id')
@dis.callback_query_handler(users_inventory.filter())
async def rsuif(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    text = f"батлпас - {'есть' if chek_bp(tg_id) else 'нет'}\nк этому добавит итемы\n"
    text = make_text_inventory(find_wear_items(tg_id), text)#
    buttons = ('одеть итемы', menu_work_items, (tg_id,)), ('назад в профиль', back_to_profile, (tg_id,))
    ikm = make_inline_keyboard(1, *buttons)
    img = InputMediaPhoto(media=photo_links_for_shop[0], caption=text)
    await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=callback.message.chat.id, message_id=callback.message.message_id)

menu_work_items = CallbackData('mwis', 'tg_id')
@dis.callback_query_handler(menu_work_items.filter())
async def rmwwi(callback):
    tg_id = r_cbd(callback.data)
    #print(123)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return

    await bot.answer_callback_query(callback.id)
##############################################----SHOP-----#############################################
@dis.message_handler(commands =['shop'])
async def all_shop_funk(message):
    await show_main_menu(chat_id=message.chat.id, message_id=message.message_id, tg_id=message.from_user.id)


go_back_all_shop = CallbackData('gbtms', 'tg_id')
@dis.callback_query_handler(go_back_all_shop.filter())
async def go_back_all_shop_funk(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    await show_main_menu(callback.message.chat.id, callback.message.message_id, tg_id, callback.id, )


#tradeheroes = CallbackData('trher', 'tg_id')
@dis.callback_query_handler(tradeheroes.filter())
async def tradeheroes_ne_funk(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    buttons = ((hero_dick[i]['name'], show_hero_in_shop, (tg_id, i,)) for i in hero_dick)
    ikm = make_inline_keyboard(3, *buttons)
    ikm.add(InlineKeyboardButton(text=f'в задницу хочу', callback_data=go_back_all_shop.new(tg_id)))#go_to_shop_menu.new()))
    img = InputMediaPhoto(caption='ураура', type='photo', media=hero_dick[1]['event_img'])
    await bot.edit_message_media(reply_markup=ikm, media=img, message_id=callback.message.message_id,chat_id=callback.message.chat.id)
    await bot.answer_callback_query(callback.id)


#tradeitems = CallbackData('tritm', 'tg_id')
@dis.callback_query_handler(tradeitems.filter())
async def tradeitems_funk(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    buttons = (('фарми', callback_farm_item, (tg_id,)), ('дерсись', callback_fight_item, (tg_id,)),('назад', go_back_all_shop, (tg_id,)))
    ikm = make_inline_keyboard(2, *buttons)
    img = InputMediaPhoto(media=photo_links_for_shop[4], caption='шмотки (не ломать)')
    await bot.edit_message_media(media=img, chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=ikm)
    await bot.answer_callback_query(callback.id)


callback_farm_item = CallbackData('cfarmis', 'tg_id')
@dis.callback_query_handler(callback_farm_item.filter())
async def rcfarmis(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    buttons = ((item_dick['farm'][i]['name'],show_item_in_shop, (tg_id, i, 1)) for i in item_dick['farm'])
    ikm = make_inline_keyboard(2, *buttons).add(InlineKeyboardButton(text='бек', callback_data=tradeitems.new(tg_id)))
    img = InputMediaPhoto(media=photo_links_for_shop[4], caption='фармила')
    await bot.edit_message_media(media=img, chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=ikm)


callback_fight_item = CallbackData('cfightis', 'tg_id')
@dis.callback_query_handler(callback_fight_item.filter())
async def rcfightis(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    buttons = ((item_dick['fight'][i]['name'],show_item_in_shop,(tg_id, i,0)) for i in item_dick['fight'])
    ikm = make_inline_keyboard(3, *buttons).add(InlineKeyboardButton(text='бек', callback_data=tradeitems.new(tg_id)))
    img = InputMediaPhoto(media=photo_links_for_shop[4], caption='дрочун')
    await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=callback.message.chat.id, message_id=callback.message.message_id)

#############################################----BUY_iTEMS-----############################################

show_item_in_shop = CallbackData('rsiis', 'tg_id', 'item_id', 'fl')#фл должен означать вернёмся в файт или фарм
@dis.callback_query_handler(show_item_in_shop.filter())
async def rsiisf(callback):
    tg_id, item_id, fl = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    back = callback_farm_item if fl else callback_fight_item
    ikm = make_inline_keyboard(1, ('купить', buy_item_shop_callback, (tg_id, item_id, fl,0)),('бек', back, (tg_id,)))
    img = InputMediaPhoto(media=photo_links_for_shop[2],caption='sss')
    await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.answer_callback_query(callback.id)

buy_item_shop_callback = CallbackData('biscq', 'tg_id', 'item_id', 'fl', 'count')
@dis.callback_query_handler(buy_item_shop_callback.filter())
async def rbisc(callback):
    tg_id, item_id, fl, count = r_cbd(callback.data)
    #print(tg_id, type(tg_id))
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    if money_of_user(tg_id)>=all_items[item_id]['price']:
        buy_item_user(tg_id, item_id, all_items[item_id]['price'])
    else:await bot.answer_callback_query(callback.id, f"денег малавата братишка")
    #показывает профиль
    #await rcfightis(callback)
    back = callback_farm_item if fl else callback_fight_item
    ikm = make_inline_keyboard(1, ('купить', buy_item_shop_callback,(tg_id, item_id, fl,count+1)), ('бек',back,(tg_id,)))
    await bot.answer_callback_query(callback.id, f"ура ты успешно купил {all_items[item_id]['name']}")
    img = InputMediaPhoto(photo_links_for_shop[1], caption=f'можешь чекнуть /profile\n ты купил {count+1} штук')
    await bot.edit_message_media(media=img,reply_markup=ikm, message_id=callback.message.message_id, chat_id=callback.message.chat.id)

@dis.callback_query_handler(del_callback.filter())
async def rdcfs(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    #хз нужно или нет но можно удалять сообщения с менюшкой и пользователем который их написал
    #try: await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id-1)
    #№except: await bot.send_message(chat_id=callback.message.chat.id, text=
    # 'дайте админку чтобы я мог удалять сообщения (сейчас нужно удалить сообщение которым вызвали меню)')



##############################################----BUY_HERO-----#############################################


show_hero_in_shop = CallbackData('shns', 'tg_id', 'hero_id',)
@dis.callback_query_handler(show_hero_in_shop.filter())
async def show_hero_in_shop_funk(callback):
    tg_id,hero_id = r_cbd(callback.data)
    if callback.from_user.id != tg_id:await bot.answer_callback_query(callback.id, text=enemy_click[rnum()]);return
    b = (('купить', wanna_d7e_hero, (tg_id, hero_id)), ('назад', tradeheroes,(tg_id,)))
    ikm = make_inline_keyboard(1, *b)
    img = InputMediaPhoto(media=photo_links_for_shop[2], caption='asd')
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id, chat_id=callback.message.chat.id)


wanna_d7e_hero = CallbackData('diwd', 'tg_id', 'hero_id')
@dis.callback_query_handler(wanna_d7e_hero.filter())
async def rfwannad7e(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if callback.from_user.id != tg_id: await bot.answer_callback_query(callback.id, enemy_click[rnum()]); return
    if money_of_user(tg_id) >= hero_dick[hero_id]['price']:
        img = InputMediaPhoto(media=photo_links_for_shop[1], caption='точно точно?') ##вопрос
        ikm = make_inline_keyboard(1, ('да!!', buy_hero_shop, (tg_id, hero_id)),('мисклик(', show_hero_in_shop, (tg_id, hero_id,)))
        await bot.edit_message_media(media=img,reply_markup=ikm, message_id=callback.message.message_id, chat_id=callback.message.chat.id)
        await bot.answer_callback_query(callback.id)
        return
    img = InputMediaPhoto(media=photo_links_for_shop[3], caption='у тебя не хватает денег(')#чёто типо нищий
    ikm = make_inline_keyboard(1, ('naZad', show_hero_in_shop, (tg_id, hero_id,)))  #)('тут будет типо иди работй негр', buy_hero_shop, (tg_id, hero_id))
    #print(ikm)
    await bot.edit_message_media(reply_markup=ikm, media=img, chat_id=callback.message.chat.id, message_id=callback.message.message_id)


buy_hero_shop = CallbackData('bhs', 'tg_id', 'hero_id')
@dis.callback_query_handler(buy_hero_shop.filter())
async def rbhis(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if callback.from_user.id!=tg_id:await bot.answer_callback_query(callback.id, enemy_click[rnum()]);return
    buy_hero(tg_id, hero_id, hero_dick[hero_id]['price'])
    #тут должно перекидывать на страницу с новым гером #в профиль
    #ikm =
    #await bot.edit_message_media()
    await bot.answer_callback_query(callback.id, text=f"ура ура ты купил {hero_dick[hero_id]['name']}")



##############################################----WORK-----#############################################
if __name__ == '__main__':
   aiogram.executor.start_polling(dis, )#skip_updates=True
