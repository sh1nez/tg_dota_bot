from answers import *
from database import *
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InputMediaPhoto
from apscheduler.schedulers.asyncio import AsyncIOScheduler


@dis.message_handler(commands=['start'])
async def start_funk(message: aiogram.types):
    await starter(tg_id=message.from_user.id, chat_id=message.chat.id)


@dis.message_handler(commands=['profile'])
async def profile_funk(message):
    tg_id = message.from_user.id
    await make_profile(tg_id, message.chat.id)


@dis.message_handler(commands=['bonus'])
async def bonus_funk(message):
    if check_bonus(tg_id=message.from_user.id):
        await message.answer('бонус получен')
        return
    await message.answer('ты уже использовал бонус, попробуй завтра')


# my_heroes = CallbackData('spmh', 'tg_id')


@dis.callback_query_handler(my_heroes.filter())
async def rsmhip(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    await all_heroes_local_user(tg_id, callback.message.message_id, callback.message.chat.id, callback.id)


# show_hero_in_inventory = CallbackData('shiip', 'tg_id', 'hero_id')


@dis.callback_query_handler(show_hero_in_inventory.filter())
async def dshii(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    await rshower_hero_i_i(tg_id, hero_id, callback.message.chat.id, callback.message.message_id, )
    await bot.answer_callback_query(callback.id)


# send_hero_farm_callback = CallbackData('shtfarm', 'tg_id', 'hero_id')


@dis.callback_query_handler(send_hero_farm_callback.filter())
async def shfarm(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    if check_time_farm(tg_id, hero_id):
        await all_heroes_local_user(tg_id, callback.message.message_id, callback.message.chat.id, callback.id)
        items = find_wear_items(hero_id)
        sec = farm_time_sec(hero_id, select_lvl_by_tg_id(tg_id, hero_id))
        end_time = (datetime.datetime.now() + datetime.timedelta(seconds=sec)).replace(microsecond=0)
        send_hero_farm_func(tg_id, hero_id, end_time)
        sheduler.add_job(func=hero_come_local_user, trigger='date', run_date=end_time,
                         args=(tg_id, hero_id, callback.message.chat.id, 100))

        cherez = text_from_seconds(sec)
        username = callback.from_user.first_name
        await callback.message.answer(f"[{username}](tg://user?id={tg_id}),"
                                      f" {hero_dick[hero_id].name} отправлен фармить\n"
                                      f" вернётся через {cherez}", parse_mode='MarkdownV2')
        await bot.answer_callback_query(callback.id,)



    else:
        await bot.answer_callback_query(callback.id, text=f"{hero_dick[hero_id].name} занят")


# send_hero_fight_callback = CallbackData('shtfight', 'tg_id', 'hero_id')


@dis.callback_query_handler(send_hero_fight_callback.filter())
async def shfight(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    if enemy := send_hero_fight(tg_id, hero_id, ):  # tuple, в формате id, tg_id, name_id
        """Вот такое пвп"""
        table_hero_id = find_hero_id_by_name_tg(tg_id, hero_id)
        items1 = find_wear_items(table_hero_id)
        items2 = find_wear_items(enemy[0])
        lvl1 = select_lvl(table_hero_id)
        lvl2 = select_lvl(enemy[0])
        hero_name1 = hero_id
        hero_name2 = enemy[2]
        print(items1, 'первый')
        print(items2, 'второй')
        # везде 1 - это тот, кто кликнул, 2- тот, кто уже искал врага
        fst_inf, scd_inf = pvp(hero_name1, lvl1, items1, hero_name2, lvl2, items2)
        print(fst_inf, 'первый')
        print(scd_inf, 'второй')
        winner = 1 if fst_inf[1] < scd_inf[1] else 0  # 1 если первый 0 если второй
        winner_name = hero_dick[hero_name1].name if winner else hero_dick[hero_name2].name
        text1_1 = f"твой {hero_dick[hero_name1].name} сражался с {hero_dick[hero_name2].name}.\n"
        text1_2 = f" \nПобедил {f'твой ' if winner else 'вражеский '} {winner_name}\n{'+'if winner else'-'}30 рейтинга"
        absolute_text = f"файт длился {max(fst_inf[1], scd_inf[1])} секунд. "
        text2_1 = f"твой {hero_dick[hero_name2].name} сражался с {hero_dick[hero_name1].name}.\n"
        text2_2 = f"\nПобедил {f'твой 'if not winner else'вражеский '} {winner_name}\n{'+' if not winner else '-'}30 рейтинга "

        await bot.send_message(tg_id, text1_1+absolute_text+text1_2)
        await bot.send_message(enemy[1], text2_1+absolute_text+text2_2)

        await bot.answer_callback_query(callback.id)

    else:
        await bot.answer_callback_query(callback.id, text=f"{hero_dick[hero_id].name} отправлен искать файт")


# items_hero_inventory = CallbackData('sliii', 'tg_id', 'hero_id')


@dis.callback_query_handler(items_hero_inventory.filter())
async def rihi(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    await show_items_hero(tg_id, hero_id, callback.message.chat.id, callback.message.message_id, callback.id)






# wear_more_items = CallbackData('wmi', 'tg_id', 'hero_id')
@dis.callback_query_handler(wear_more_items.filter())
async def rifhp(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    await a1234(tg_id, hero_id, callback.message.message_id, callback.message.chat.id)
    await bot.answer_callback_query(callback.id)


# wear_n_shmot_on_hero = CallbackData('wnsoh', 'tg_id', 'hero_id', 'item_id')


@dis.callback_query_handler(wear_n_shmot_on_hero.filter())
async def rwnsoh(callback):
    tg_id, hero_id, item_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    wear_item_on_hero(tg_id, hero_id, item_id)
    await bot.edit_message_media()
    await bot.answer_callback_query(callback.id, 'итем одет чекай')


# q_remove_item_from_hero = CallbackData('rifh', 'tg_id', 'hero_id', 'item_id')


@dis.callback_query_handler(q_remove_item_from_hero.filter())
async def qrifh(callback):
    tg_id, hero_id, item_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    buttons = (('снять шмотку', snat_shmotku_inventory, (tg_id, hero_id, item_id)),
               ('отмена', items_hero_inventory, (tg_id, hero_id,)))
    ikm = make_inline_keyboard(*buttons, row=1)
    img = InputMediaPhoto(media=images['dyrachyo'],
                          caption='ты хочешь снять шмотку с героя? при снятии есь 10% шанс сломать шмотку')
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id,
                                 chat_id=callback.message.chat.id)
    await bot.answer_callback_query(callback.id)


# snat_shmotku_inventory = CallbackData('ssivi', 'tg_id', 'hero_id', 'item_id')


@dis.callback_query_handler(snat_shmotku_inventory.filter())
async def rtshsg(callback):
    tg_id, hero_id, item_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    snat_s_geroya_v_invantar(item_id, tg_id, hero_id)
    # await bot
    await bot.answer_callback_query(callback.id, 'шмотка снята')


# back_to_profile = CallbackData('pbtp', 'tg_id')


@dis.callback_query_handler(back_to_profile.filter())
async def rbtpn(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    await make_profile(tg_id, callback.message.chat.id, callback.message.message_id, callback.id)


# users_inventory = CallbackData('suic', 'tg_id')


@dis.callback_query_handler(users_inventory.filter())
async def rsuif(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    item_text = find_nowear_items(tg_id)
    ikm = None
    if item_text:
        item_text = make_text_inventory(item_text)  #
        ikm = make_inline_keyboard(('одеть итемы', menu_work_items, (tg_id,)), )
    else:
        item_text = 'у тебя нет предметов'
    buttons = ('назад в профиль', back_to_profile, (tg_id,)), ('в магазин', go_back_all_shop, (tg_id,))
    ikm = make_inline_keyboard(*buttons, row=2, ikm=ikm)
    img = InputMediaPhoto(media=images['anime1'], caption=item_text)
    await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id)


# menu_work_items = CallbackData('mwis', 'tg_id')


@dis.callback_query_handler(menu_work_items.filter())
async def rmwwi(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    tup = find_id_name_all_heroes(tg_id)
    buttons = ((hero_dick[i[0]].name, '', (tg_id, i[0],)) for i in tup)
    ''' 
    вернёт сделанные кнопки для make_inline_keyboard которые будут перенаправлять на
    1. выбери героя на которого хочешь одеть ш 
    '''
    # ikm = make_inline_keyboard()
    await bot.answer_callback_query(callback.id)


'''############################################----SHOP-----############################################'''


@dis.message_handler(commands=['shop'])
async def all_shop_funk(message):
    money = money_of_user(message.from_user.id)
    if money is False:
        await bot.send_message(message.chat.id, 'ты не зарегистрирован, используй /start в личных сообщениях боту')
        return
    await show_main_menu(chat_id=message.chat.id, message_id=message.message_id, tg_id=message.from_user.id)


# go_back_all_shop = CallbackData('gbtms', 'tg_id')


@dis.callback_query_handler(go_back_all_shop.filter())
async def go_back_all_shop_funk(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    await show_main_menu(callback.message.chat.id, callback.message.message_id, tg_id, callback.id, )


# tradeheroes = CallbackData('trher', 'tg_id')


@dis.callback_query_handler(tradeheroes.filter())
async def tradeheroes_ne_funk(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    buttons = ((hero_dick[i].name, show_hero_in_shop, (tg_id, i,)) for i in hero_dick)
    ikm = make_inline_keyboard(*buttons, row=3)
    ikm.add(InlineKeyboardButton(text=f'назад',
                                 callback_data=go_back_all_shop.new(tg_id)))  # go_to_shop_menu.new()))
    img = InputMediaPhoto(caption='ураура', type='photo', media=images['bg1'])
    await bot.edit_message_media(reply_markup=ikm, media=img, message_id=callback.message.message_id,
                                 chat_id=callback.message.chat.id)
    await bot.answer_callback_query(callback.id)


# tradeitems = CallbackData('tritm', 'tg_id')


@dis.callback_query_handler(tradeitems.filter())
async def tradeitems_funk(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    buttons = (('фарми', callback_farm_item, (tg_id,)), ('дерсись', callback_fight_item, (tg_id,)),
               ('назад', go_back_all_shop, (tg_id,)))
    ikm = make_inline_keyboard(*buttons, row=2)
    img = InputMediaPhoto(media=images['items'], caption='шмотки (не ломать)')
    await bot.edit_message_media(media=img, chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                 reply_markup=ikm)
    await bot.answer_callback_query(callback.id)


# callback_farm_item = CallbackData('cfarmis', 'tg_id')


@dis.callback_query_handler(callback_farm_item.filter())
async def rcfarmis(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    buttons = ((item_dick['farm'][i].name, show_item_in_shop, (tg_id, item_dick['farm'][i].index, 1))
               for i in item_dick['farm'])
    ikm = make_inline_keyboard(*buttons, row=3).add(InlineKeyboardButton(text='бек',
                                                                         callback_data=tradeitems.new(tg_id)))
    img = InputMediaPhoto(media=images['items'], caption='фармила')
    await bot.edit_message_media(media=img, chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                 reply_markup=ikm)


# callback_fight_item = CallbackData('cfightis', 'tg_id')


@dis.callback_query_handler(callback_fight_item.filter())
async def rcfightis(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    buttons = ((item_dick['fight'][i].name, show_item_in_shop, (tg_id, i, 0)) for i in item_dick['fight'])
    ikm = make_inline_keyboard(*buttons, row=3).add(InlineKeyboardButton(text='бек',
                                                                         callback_data=tradeitems.new(tg_id)))
    img = InputMediaPhoto(media=images['items'], caption='дрочун')
    await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id)


'''###########################################----BUY_ITEMS-----############################################'''

# show_item_in_shop = CallbackData('rsiis', 'tg_id', 'item_id', 'fl')  # фл должен означать вернёмся в файт или фарм


@dis.callback_query_handler(show_item_in_shop.filter())
async def rsiisf(callback):
    tg_id, item_id, fl = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    back = callback_farm_item if fl else callback_fight_item
    ikm = make_inline_keyboard(('купить', buy_item_shop_callback, (tg_id, item_id, fl, 0)), )
    ikm = make_inline_keyboard(('бек', back, (tg_id,)), ('в профиль', back_to_profile, (tg_id,)), ikm=ikm, row=2)

    img = InputMediaPhoto(media=all_items[item_id].img1, caption=all_items[item_id].name)
    await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id)
    await bot.answer_callback_query(callback.id)


# buy_item_shop_callback = CallbackData('biscq', 'tg_id', 'item_id', 'fl', 'count')


@dis.callback_query_handler(buy_item_shop_callback.filter())
async def rbisc(callback):
    tg_id, item_id, fl, count = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    if money_of_user(tg_id) >= all_items[item_id].price:
        buy_item_user(tg_id, item_id, all_items[item_id].price)
    else:
        await bot.answer_callback_query(callback.id, f"денег малавата братишка")
        return
    # показывает профиль
    # await rcfightis(callback)
    back = callback_farm_item if fl else callback_fight_item
    ikm = make_inline_keyboard(('купить', buy_item_shop_callback, (tg_id, item_id, fl, count + 1)))
    ikm = make_inline_keyboard(('назад', back, (tg_id,)),
                               ('в профиль', back_to_profile, (tg_id,)), ikm=ikm)

    await bot.answer_callback_query(callback.id, f"ура ты успешно купил {all_items[item_id].name}")
    img = InputMediaPhoto(all_items[item_id].img1, caption=f'можешь чекнуть /profile\nты купил {count + 1} штук')
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id,
                                 chat_id=callback.message.chat.id)


# del_callback = CallbackData('delcs', 'tg_id')


@dis.callback_query_handler(del_callback.filter())
async def rdcfs(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    # хз нужно или нет но можно удалять сообщения с менюшкой и пользователем который их написал
    # try: await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id-1)
    # №except: await bot.send_message(chat_id=callback.message.chat.id, text=
    # 'дайте админку чтобы я мог удалять сообщения (сейчас нужно удалить сообщение которым вызвали меню)')


"""###########################################----BUY_HERO-----#############################################"""

# show_hero_in_shop = CallbackData('shns', 'tg_id', 'hero_id', )


@dis.callback_query_handler(show_hero_in_shop.filter())
async def show_hero_in_shop_funk(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if callback.from_user.id != tg_id:
        await bot.answer_callback_query(callback.id, text=enemy_click[rnum()])
        return
    buttons = (('купить', wanna_d7e_hero, (tg_id, hero_id)), ('назад', tradeheroes, (tg_id,)))
    ikm = make_inline_keyboard(*buttons, row=1)
    img = InputMediaPhoto(media=hero_dick[hero_id].img1, caption='asd')
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id,
                                 chat_id=callback.message.chat.id)


# wanna_d7e_hero = CallbackData('diwd', 'tg_id', 'hero_id')


@dis.callback_query_handler(wanna_d7e_hero.filter())
async def rfwannad7e(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if callback.from_user.id != tg_id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    if check_hero_user(tg_id, hero_id):
        img = InputMediaPhoto(media=images['dyrachyo'],
                              caption='баран, можно иметь только 1 героя 1 типа')
        ikm = make_inline_keyboard(('naZad', tradeheroes, (tg_id,)), )
        await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id,
                                     chat_id=callback.message.chat.id)
        await bot.answer_callback_query(callback.id)
        return
    elif money_of_user(tg_id) >= hero_dick[hero_id].price:
        img = InputMediaPhoto(media=images['dyrachyo'], caption='точно точно?')
        ikm = make_inline_keyboard(('да!!', buy_hero_shop, (tg_id, hero_id)),
                                   ('мисклик(', tradeheroes, (tg_id,)), row=1)
        await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id,
                                     chat_id=callback.message.chat.id)
        await bot.answer_callback_query(callback.id)
        return
    img = InputMediaPhoto(media=images['dyrachyo'], caption='у тебя не хватает денег(')  # чёто типо нищий
    ikm = make_inline_keyboard(('naZad', tradeheroes, (tg_id,)), row=3)
    # 'тут будет типо иди работй негр', buy_hero_shop, (tg_id, hero_id))
    await bot.edit_message_media(reply_markup=ikm, media=img, chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id)


# buy_hero_shop = CallbackData('bhs', 'tg_id', 'hero_id')


@dis.callback_query_handler(buy_hero_shop.filter())
async def rbhis(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if callback.from_user.id != tg_id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    buy_hero(tg_id, hero_id, hero_dick[hero_id].price)
    await rshower_hero_i_i(tg_id, hero_id, callback.message.chat.id, callback.message.message_id, )
    await bot.answer_callback_query(callback.id, f"ура ура ты купил {hero_dick[hero_id].name}а")


'''##############################################----WORK-----#############################################'''
if __name__ == '__main__':
    sheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    sheduler.add_job(func=clean_bonus, trigger='cron', hour=0, )
    sheduler.start()
    aiogram.executor.start_polling(dis, )  # skip_updates=True
