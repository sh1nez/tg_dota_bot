from database import *
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InputMediaPhoto


my_heroes = CallbackData('spmh', 'tg_id')
show_hero_in_inventory = CallbackData('shiip', 'tg_id', 'hero_id')
send_hero_farm_callback = CallbackData('shtfarm', 'tg_id', 'hero_id')
send_hero_fight_callback = CallbackData('shtfight', 'tg_id', 'hero_id')
items_hero_inventory = CallbackData('sliii', 'tg_id', 'hero_id')
wear_more_items = CallbackData('wmi', 'tg_id', 'hero_id')
wear_n_shmot_on_hero = CallbackData('wnsoh', 'tg_id', 'hero_id', 'item_id')
q_remove_item_from_hero = CallbackData('rifh', 'tg_id', 'hero_id', 'item_id')
snat_shmotku_inventory = CallbackData('ssivi', 'tg_id', 'hero_id', 'item_id')
back_to_profile = CallbackData('pbtp', 'tg_id')
users_inventory = CallbackData('suic', 'tg_id')
menu_work_items = CallbackData('mwis', 'tg_id')
go_back_all_shop = CallbackData('gbtms', 'tg_id')
tradeheroes = CallbackData('trher', 'tg_id')
tradeitems = CallbackData('tritm', 'tg_id')
callback_farm_item = CallbackData('cfarmis', 'tg_id')
callback_fight_item = CallbackData('cfightis', 'tg_id')
show_item_in_shop = CallbackData('rsiis', 'tg_id', 'item_id', 'fl')  # фл должен означать вернёмся в файт или фарм
buy_item_shop_callback = CallbackData('biscq', 'tg_id', 'item_id', 'fl', 'count')
del_callback = CallbackData('delcs', 'tg_id')
show_hero_in_shop = CallbackData('shns', 'tg_id', 'hero_id', )
wanna_d7e_hero = CallbackData('diwd', 'tg_id', 'hero_id')
buy_hero_shop = CallbackData('bhs', 'tg_id', 'hero_id')
snat_shmotku_inventory = CallbackData('ssivi', 'tg_id', 'hero_id', 'item_id')



async def hero_come_local_user(tg_id, hero_id, chat_id, money):
    username = 'эй, '
    event_text = f"{hero_dick[hero_id].name} пришёл, принеся с собой {money} деняк"
    update_money(tg_id, money)
    hero_back_farm_func(tg_id, hero_id)
    await bot.send_message(chat_id=chat_id, text=f"[{username}](tg://user?id={tg_id}){event_text}",
                           parse_mode='MarkdownV2')


async def all_heroes_local_user(tg_id, message_id, chat_id, callback_id):
    tup = find_id_name_all_heroes(tg_id)
    if not tup:
        ikm = InlineKeyboardMarkup().add(InlineKeyboardButton(text='бек', callback_data=back_to_profile.new(tg_id)))
        img = InputMediaPhoto(caption='у тебя нет героев', media=images['woman'])
    else:
        buttons = ((hero_dick[i[0]].name, show_hero_in_inventory, (tg_id, i[0],),) for i in tup)
        ikm = make_inline_keyboard(*buttons, row=3).add(
            InlineKeyboardButton(text='бек', callback_data=back_to_profile.new(tg_id)))
        img = InputMediaPhoto(caption='герои', media=images['woman'])
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=message_id,
                                 chat_id=chat_id)
    await bot.answer_callback_query(callback_id)


async def show_items_hero(tg_id, hero_id, chat_id, message_id, callback_id):
    text = 'к этому добавить итемы'
    aa = find_wear_items(hero_id)
    if not aa:
        text = 'у твоего героя нет предметов'
        ikm = make_inline_keyboard(('одеть ещё', wear_more_items, (tg_id, hero_id,)), row=3)
        ikm = make_inline_keyboard(('назад к герою', show_hero_in_inventory, (tg_id, hero_id,)),
                                   ('в магазин', go_back_all_shop, (tg_id,)), ikm=ikm)
    else:
        items = find_wear_items(hero_id)
        buttons = ((all_items[i[1]].name, q_remove_item_from_hero, (tg_id, hero_id, i[0])) for i in items)
        ikm = make_inline_keyboard(*buttons).add(
            InlineKeyboardButton(text='одеть ещё', callback_data=wear_more_items.new(tg_id, hero_id))).add(
            InlineKeyboardButton(text='назад к герою', callback_data=show_hero_in_inventory.new(tg_id, hero_id, )))
    img = InputMediaPhoto(media=images['items'], caption=text)
    await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=chat_id,
                                 message_id=message_id)
    await bot.answer_callback_query(callback_id)


async def show_main_menu(chat_id, message_id, tg_id, *args):
    ikm = make_inline_keyboard(*(('герои', tradeheroes, (tg_id,)), ('предметы', tradeitems, (tg_id,)),
                                 ('в профиль', back_to_profile, (tg_id,))), row=2)
    if not args:
        await bot.send_photo(chat_id, caption='магаз у наташки', reply_markup=ikm, photo=images['salesman'])
        return
    img = InputMediaPhoto(caption='магаз у наташки', media=images['salesman'], type='photo')
    await bot.edit_message_media(reply_markup=ikm, media=img, message_id=message_id, chat_id=chat_id)
    await bot.answer_callback_query(args[0])


async def make_profile(tg_id, chat_id, *args):
    """message_id, callback_id если надо редактировать"""
    money = money_of_user(tg_id)
    if money is False:
        await bot.send_message(chat_id, 'ты не зарегистрирован, используй /start в личных сообщениях боту')
        return
    ikm = make_inline_keyboard(('мои герои', my_heroes, (tg_id,)), ('инвентарь', users_inventory, (tg_id,)),
                               ('магазин', go_back_all_shop, (tg_id,)), row=2)
    text = 'состояние фарма\n'
    asd = find_info_all_heroes(tg_id)
    if not asd:
        text += 'у тебя пока нет героев'
    else:
        for i in asd:
            text += f"{hero_dick[i[1]].name} {i[0]} LVL {text_time(i[2])}"
    caption_text = f'денег - {money}\n{text}\n'
    if not args:
        await bot.send_photo(chat_id=chat_id, reply_markup=ikm, photo=images['anime1'], caption=caption_text)
        return
    img = InputMediaPhoto(caption=caption_text, media=images['anime1'])
    await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=chat_id, message_id=args[0])
    await bot.answer_callback_query(args[1])


async def starter(tg_id, chat_id):
    if not reg_user(tg_id):
        if chat_id != tg_id:
            await bot.send_message(chat_id, 'регистрироваться можно только в личных сообщениях')
            return
        sql_code1 = f"INSERT INTO `players` (`tg_id`, `money`) VALUES ('{tg_id}', '0')"
        hero_id = 0  # это типо пуджа выдаёт бесплатно
        sql_code2 = f"INSERT INTO heroes (`tg_id`, `hero_name`, `lvl`, `exp` ) VALUES " \
                    f"('{tg_id}', '{hero_id}', '1', '0');"
        connection.make_many(sql_code1, sql_code2)
        await bot.send_message(text=f'теперь ты зареган,\n{new_reg_text}', chat_id=chat_id)
        return
    else:
        await bot.send_message(text=f'ты уже зареган', chat_id=chat_id)



async def rshower_hero_i_i(tg_id, hero_id, chat_id, mesage_id):
    buttons = (
    ('фармить', send_hero_farm_callback, (tg_id, hero_id,)), ('драться', send_hero_fight_callback, (tg_id, hero_id,)),
    ('шмотки', items_hero_inventory, (tg_id, hero_id,)), ('back', my_heroes, (tg_id,)))
    ikm = make_inline_keyboard(*buttons, row=3)
    img = InputMediaPhoto(media=hero_dick[hero_id].img1, caption=f"вот твой {hero_dick[hero_id].name}")
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=mesage_id, chat_id=chat_id)
