from database import *
from aiogram.types import InputMediaPhoto
from objects import *
from config import bot

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

# async def send_farm_funk(tg_id, hero_id, message_id, chat_id, callback_id):
#     if check_time_farm(tg_id, hero_id):
#         await all_heroes_local_user(tg_id, message_id, chat_id, callback-id)
#         items = find_wear_items(hero_id)
#         sec = farm_time_sec(hero_id, select_lvl_by_tg_id(tg_id, hero_id))
#         end_time = (datetime.datetime.now() + datetime.timedelta(seconds=sec)).replace(microsecond=0)
#         send_hero_farm_func(tg_id, hero_id, end_time)
#         sheduler.add_job(func=hero_come_local_user, trigger='date', run_date=end_time,
#                          args=(tg_id, hero_id, chat_id, 100))
#         cherez = text_from_seconds(sec)
#         username = callback.from_user.first_name
#         await callback.message.answer(f"[{username}](tg://user?id={tg_id}),"
#                                       f" {hero_dick[hero_id].name} отправлен фармить\n"
#                                       f" вернётся через {cherez}", parse_mode='MarkdownV2')
#     else:
#         await bot.answer_callback_query(callback.id, text=f"{hero_dick[hero_id].name} занят")