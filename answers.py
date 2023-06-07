from database import *
from aiogram.types import InputMediaPhoto
import aiogram
from objects import *
from config import bot, sheduler
import random
import asyncio


async def func_helper(message):
    tg_id = message.from_user.id
    if message.chat.id != tg_id:
        asd = await bot.send_message(message.chat.id, 'команды:\n1. /bonus - Получить ежедневный бонус\n'
                                     '2. /profile - посмотреть свой профиль.\n3. /shop - Заглянуть в Магазин')
        await asyncio.sleep(10)
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await asd.delete()
        return
    asd = await bot.send_message(message.chat.id, 'команды:\n1. /bonus - Получить ежедневный бонус\n'
                                 '2. /profile - посмотреть свой профиль.\n3. /shop - Заглянуть в Магазин')


async def func_starter(message):
    tg_id = message.from_user.id
    if not reg_user(tg_id):
        if message.chat.id != tg_id:
            asd = await bot.send_message(message.chat.id, 'регистрироваться можно только в личных сообщениях')
            await asyncio.sleep(4)
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            await asd.delete()
            return
        sql_code1 = f"INSERT INTO `players` (`tg_id`, `money`) VALUES ('{tg_id}', '0')"
        hero_id = 0  # это типо пуджа выдаёт бесплатно
        sql_code2 = f"INSERT INTO heroes (`tg_id`, `hero_name`, `lvl`, `exp` ) VALUES " \
                    f"('{tg_id}', '{hero_id}', '1', '0');"
        connection.make_many(sql_code1, sql_code2)
        await bot.send_message(text=f'Ты успешно зарегистрирован,\nиспользуй /help', chat_id=message.chat.id)
        return
    else:
        await bot.send_message(text=f'Ты уже зарегистрирован\nИспользуй /help', chat_id=message.chat.id)



async def func_bonus(message):
    print(reg_user(message.from_user.id))
    if not reg_user(message.from_user.id):
        await bot.send_message(message.chat.id, 'для начала зарегайся в лс к боту /start')
        return
    if check_bonus(tg_id=message.from_user.id):
        await message.answer('бонус получен')
        take_bonus(message.from_user.id, 999999)
        return
    await message.answer('ты уже использовал бонус, попробуй завтра')


async def func_all_shop(something):
    tg_id = something.from_user.id
    money = money_of_user(something.from_user.id)
    if money is False:
        await bot.send_message(something.chat.id, 'ты не зарегистрирован, используй /start в личных сообщениях боту')
        return
    ikm = make_inline_keyboard(*(('👤Герои👤', tradeheroes, (tg_id,)), ('🛍предметы🛍', tradeitems, (tg_id,)),
                                 ('в профиль', back_to_profile, (tg_id,))), row=2)
    if isinstance(something, aiogram.types.message.Message):
        await bot.send_photo(something.chat.id, caption='магаз у наташки', reply_markup=ikm, photo=images['salesman'])
        return
    if isinstance(something, aiogram.types.callback_query.CallbackQuery):
        if r_cbd(something.data) != something.from_user.id:
            await bot.answer_callback_query(something.id, enemy_click[rnum()])
            return
        img = InputMediaPhoto(caption='магаз у наташки', media=images['salesman'], type='photo')
        await bot.edit_message_media(reply_markup=ikm, media=img, message_id=something.message.message_id,
                                     chat_id=something.message.chat.id)
    else:
        return Exception('Не сообщение и не кол◀️Наза▶️️️, это не отработает никогда нахуй я это пишу')


async def func_make_profile(something):
    """message_id, callback_id если надо редактировать"""
    if isinstance(something, aiogram.types.Message):
        tg_id = something.from_user.id
        chat_id = something.chat.id
    else:
        if r_cbd(something.data) != something.from_user.id:
            await bot.answer_callback_query(something.id, enemy_click[rnum()])
            return
        tg_id = something.from_user.id
        chat_id = something.message.chat.id
    money = money_of_user(tg_id)
    if money is False:
        await bot.send_message(chat_id, 'ты не зарегистрирован, используй /start в личных сообщениях боту')
        return
    ikm = make_inline_keyboard(('👤Герои👤', my_heroes, (tg_id,)), ('🛍Предметы🛍', user_items_callback, (tg_id,)),
                               ('🛒Магазин🛒', go_back_all_shop, (tg_id,)), row=2)
    text = '⚠️Состояние фарма⚠️\n'
    asd = find_info_all_heroes(tg_id)
    if not asd:
        text += 'у тебя пока нет героев'
    else:
        for i in asd:
            a = text_time(i[2])
            print(a)
            #b = f'{a}\n' if a == 'Готов' else f'{a}🕒\n'
            smile = "✅" if a == 'Готов' else '🕒'
            text += f"{smile}{hero_dick[i[1]].name} {i[0]} LVL - {a}\n"
    caption_text = f'📊Рейтинг - {select_mmr(tg_id)} ммр\n💰Денег - {money}\n\n{text}\n'
    if isinstance(something, aiogram.types.Message):
        await bot.send_photo(chat_id=chat_id, reply_markup=ikm, photo=images['anime1'], caption=caption_text)
    else:
        img = InputMediaPhoto(media=images['anime1'], caption=caption_text)
        await bot.edit_message_media(media=img, chat_id=something.message.chat.id, reply_markup=ikm,
                                     message_id=something.message.message_id)


async def func_shop_heroes(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    buttons = ((hero_dick[i].name, show_hero_in_shop, (tg_id, i,)) for i in hero_dick)
    ikm = make_inline_keyboard(*buttons, row=3)
    ikm.add(InlineKeyboardButton(text=f'назад',
                                 callback_data=go_back_all_shop.new(tg_id)))  # go_to_shop_menu.new()))
    img = InputMediaPhoto(type='photo', media=images['bg1'])
    await bot.edit_message_media(reply_markup=ikm, media=img, message_id=callback.message.message_id,
                                 chat_id=callback.message.chat.id)
    await bot.answer_callback_query(callback.id)


async def func_shop_items(callback):
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


async def func_all_heroes_local_user(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    tup = find_id_name_all_heroes(tg_id)
    if not tup:
        ikm = InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️Наза▶️️️', callback_data=back_to_profile.new(tg_id)))
        img = InputMediaPhoto(caption='у тебя нет героев', media=images['woman'])
    else:
        buttons = ((hero_dick[i[0]].name, show_hero_in_inventory, (tg_id, i[0],),) for i in tup)
        ikm = make_inline_keyboard(*buttons, row=2).add(
            InlineKeyboardButton(text='◀️Наза▶️️️', callback_data=back_to_profile.new(tg_id)))
        img = InputMediaPhoto(media=images['woman'])
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id,
                                 chat_id=callback.message.chat.id)
    await bot.answer_callback_query(callback.id)


async def func_inventory_hero(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    tg_id = callback.from_user.id
    buttons = (
        ('фармить', send_hero_farm_callback, (tg_id, hero_id,)), ('драться', send_hero_fight_callback, (tg_id,
                                                                                                        hero_id,)),
        ('шмотки', items_hero_inventory, (tg_id, hero_id,)), ('back', my_heroes, (tg_id,)))
    ikm = make_inline_keyboard(*buttons, row=3)
    last_time = (check_time(tg_id, hero_id))
    text_timer = 'Готов' if 0 < last_time else f"Вернётся через {text_from_seconds(abs(last_time))}"
    img = InputMediaPhoto(media=hero_dick[hero_id].img1, caption=f"вот твой {hero_dick[hero_id].name}\n"
                          f"Состояние - {text_timer}")
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id,
                                 chat_id=callback.message.chat.id)
    await bot.answer_callback_query(callback.id)


async def func_send_farm(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    if check_time(tg_id, hero_id) is True:
        items = find_wear_items(find_hero_id_by_name_tg(tg_id, hero_id))
        if items:
            items = (i[1] for i in find_wear_items(find_hero_id_by_name_tg(tg_id, hero_id)))
            sec, gold = farm_time_sec(hero_id, select_lvl_by_tg_id(tg_id, hero_id), *items)
        else:
            sec, gold = farm_time_sec(hero_id, select_lvl_by_tg_id(tg_id, hero_id))
        end_time = (datetime.datetime.now() + datetime.timedelta(seconds=sec)).replace(microsecond=0)
        send_hero_time(tg_id, hero_id, end_time)
        sheduler.add_job(func=hero_come_local_user, trigger='date', run_date=end_time,
                         args=(tg_id, hero_id, callback.message.chat.id, gold))
        cherez = text_from_seconds(sec)
        username = callback.from_user.first_name
        await callback.message.answer(f"[{username}](tg://user?id={tg_id}),"
                                      f" {hero_dick[hero_id].name} отправлен фармить\n"
                                      f" вернётся через {cherez}", parse_mode='MarkdownV2')
        tup = find_id_name_all_heroes(tg_id)
        if not tup:
            ikm = InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️Наза▶️️️', callback_data=back_to_profile.new(tg_id)))
            img = InputMediaPhoto(caption='у тебя нет героев', media=images['woman'])
        else:
            buttons = ((hero_dick[i[0]].name, show_hero_in_inventory, (tg_id, i[0],),) for i in tup)
            ikm = make_inline_keyboard(*buttons, row=3).add(
                InlineKeyboardButton(text='◀️Наза▶️️️', callback_data=back_to_profile.new(tg_id)))
            img = InputMediaPhoto(media=images['woman'])
        await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id,
                                     chat_id=callback.message.chat.id)
        await bot.answer_callback_query(callback.id)
    else:
        await bot.answer_callback_query(callback.id, text=f"{hero_dick[hero_id].name} занят")


async def hero_come_local_user(tg_id, hero_id, chat_id, money):
    username = 'эй, '
    event_text = f"{hero_dick[hero_id].name} пришёл, принеся с собой {money} деняк"
    update_money(tg_id, money)
    hero_back_funk(tg_id, hero_id)
    await bot.send_message(chat_id=chat_id, text=f"[{username}](tg://user?id={tg_id}){event_text}",
                           parse_mode='MarkdownV2')


async def hero_come_from_fight(tg_id, hero_id, chat_id):
    username = 'эй, '
    event_text = f"{hero_dick[hero_id].name} пришёл после драки"
    await bot.send_message(chat_id=chat_id, text=f"[{username}](tg://user?id={tg_id}){event_text}",
                           parse_mode='MarkdownV2')


async def func_show_items_hero(callback):
    tg_id, hero_id = r_cbd(callback.data)
    text = ''
    primary_id = find_hero_id_by_name_tg(tg_id, hero_id)
    items = find_wear_items(primary_id)
    if not items:
        text = 'у твоего героя нет предметов'
        ikm = make_inline_keyboard(('одеть ещё', srazu_odet, (tg_id, hero_id,)), row=3)
        ikm = make_inline_keyboard(('назад к герою', show_hero_in_inventory, (tg_id, hero_id,)),
                                   ('🛒Магазин🛒', go_back_all_shop, (tg_id,)), ikm=ikm)
    else:
        buttons = ((all_items[i[1]].name, q_remove_item_from_hero, (tg_id, hero_id, i[1])) for i in items)
        ikm = make_inline_keyboard(*buttons).add(
            InlineKeyboardButton(text='одеть ещё', callback_data=srazu_odet.new(tg_id, hero_id))).add(
            InlineKeyboardButton(text='назад к герою', callback_data=show_hero_in_inventory.new(tg_id, hero_id, )))
    img = InputMediaPhoto(media=images['items'], caption=text)
    await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id)
    await bot.answer_callback_query(callback.id)


async def func_wear_more_items(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    text = 'выбери предмет, который будет одет на твоего героя\n'
    items = find_nowear_items(tg_id)  # это неодетые
    already = find_wear_items(hero_id)  # это одетые
    if not already:
        le = 0
    else:
        le = len(already)
    if le >= 6:
        await bot.answer_callback_query(callback.id, 'у героя уже 6 слотов')
        return
    if not items:
        img = InputMediaPhoto(media=images['itemen'], caption='у тебя нет предметов')
        ikm = InlineKeyboardMarkup().add(InlineKeyboardButton(text='назад', callback_data=items_hero_inventory.new(
            tg_id, hero_id)), InlineKeyboardButton(text='🛒Магазин🛒', callback_data=go_back_all_shop.new(tg_id)))
        await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id)

    else:
        le = min(len(items), 9)
        for i in range(le):
            text += f"{all_items[items[i][1]].name} - {items[i][2]}\n"
        buttons = ((all_items[items[i][1]].name, wear_n_shmot_on_hero, (tg_id, hero_id, items[i][1],))
                   for i in range(le))
        ikm = make_inline_keyboard(*buttons).add(
            InlineKeyboardButton(text='назад', callback_data=items_hero_inventory.new(tg_id, hero_id)))
        img = InputMediaPhoto(media=images['bg2'], caption=text)
        await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id)


async def func_fight(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if check_time(tg_id, hero_id) is not True:
        await bot.answer_callback_query(callback.id, f"{hero_dick[hero_id].name} занят")
        return
    if enemy := send_hero_fight(tg_id, hero_id, ):  # tuple, в формате id, tg_id, name_id
        table_hero_id = find_hero_id_by_name_tg(tg_id, hero_id)
        print(enemy)
        i1 = find_wear_items(table_hero_id)
        items1 = None if not i1 else (i[1] for i in i1)
        i2 = find_wear_items(enemy[0])
        items2 = None if not i2 else (i[1] for i in i2)
        lvl1 = select_lvl(table_hero_id)
        lvl2 = select_lvl(enemy[0])
        hero_name1 = hero_id
        hero_name2 = enemy[2]
        # везде 1 - это тот, кто кликнул, 2- тот, кто уже искал врага
        fst_inf, scd_inf, time1, time2 = pvp(hero_name1, lvl1, items1, hero_name2, lvl2, items2)
        winner = 1 if fst_inf[1] < scd_inf[1] else 0  # 1 если первый 0 если второй
        winner_name = hero_dick[hero_name1].name if winner else hero_dick[hero_name2].name
        end_time1 = datetime.datetime.today() + datetime.timedelta(seconds=time1[0])
        send_hero_time(tg_id, hero_name1, end_time1)
        text1_1 = f"твой {hero_dick[hero_name1].name} сражался с {hero_dick[hero_name2].name}.\n"
        text1_2 = f" \nПобедил {f'твой ' if winner else 'вражеский '} {winner_name}\n{'+' if winner else '-'}" \
                  f"30 рейтинга\n герой отправляется домой, вернётся через\n{text_from_seconds(time1[0])}"
        end_time2 = datetime.datetime.today() + datetime.timedelta(seconds=time2[0])
        absolute_text = f"файт длился {max(fst_inf[1], scd_inf[1])} секунд. "
        text2_1 = f"твой {hero_dick[hero_name2].name} сражался с {hero_dick[hero_name1].name}.\n"
        text2_2 = f"\nПобедил {f'твой ' if not winner else 'вражеский '} {winner_name}\n{'+' if not winner else '-'}" \
                  f"30 рейтинга\n герой отправляется домой, вернётся через\n{text_from_seconds(time2[0])}"
        send_hero_time(enemy[1], hero_name2, end_time2)
        await bot.send_message(tg_id, text1_1 + absolute_text + text1_2)
        mmr_update(tg_id, 30 if winner else -30)
        print(end_time1)
        sheduler.add_job(func=hero_come_from_fight, trigger='date', run_date=end_time1,
                         args=(tg_id, hero_name1, callback.message.chat.id))
        await bot.send_message(enemy[1], text2_1 + absolute_text + text2_2)
        mmr_update(enemy[1], 30 if not winner else -30)
        print(end_time2)
        sheduler.add_job(func=hero_come_from_fight, trigger='date', run_date=end_time2,
                         args=(enemy[1], hero_name2, callback.message.chat.id))
        await bot.answer_callback_query(callback.id)

    else:
        await bot.answer_callback_query(callback.id, text=f"{hero_dick[hero_id].name} отправлен искать файт")
    tup = find_id_name_all_heroes(tg_id)
    if not tup:
        ikm = InlineKeyboardMarkup().add(InlineKeyboardButton(text='◀️Наза▶️️️', callback_data=back_to_profile.new(tg_id)))
        img = InputMediaPhoto(caption='у тебя нет героев', media=images['woman'])
    else:
        buttons = ((hero_dick[i[0]].name, show_hero_in_inventory, (tg_id, i[0],),) for i in tup)
        ikm = make_inline_keyboard(*buttons, row=3).add(
            InlineKeyboardButton(text='◀️Наза▶️️️', callback_data=back_to_profile.new(tg_id)))
        img = InputMediaPhoto(media=images['woman'])
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id,
                                 chat_id=callback.message.chat.id)
    await bot.answer_callback_query(callback.id)


async def func_shop_farm_item(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    buttons = ((item_dick['farm'][i].name, show_item_in_shop, (tg_id, item_dick['farm'][i].index, 1))
               for i in item_dick['farm'])
    ikm = make_inline_keyboard(*buttons, row=3).add(InlineKeyboardButton(text='◀️Наза▶️️️',
                                                                         callback_data=tradeitems.new(tg_id)))
    img = InputMediaPhoto(media=images['items'], caption='фармила')
    await bot.edit_message_media(media=img, chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                 reply_markup=ikm)


# # callback_fight_item = CallbackData('cfightis', 'tg_id')
async def func_shop_fight_item(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return

    buttons = ((item_dick['fight'][i].name, show_item_in_shop, (tg_id, item_dick['fight'][i].index, 0))
               for i in item_dick['fight'])
    ikm = make_inline_keyboard(*buttons, row=3).add(InlineKeyboardButton(text='◀️Наза▶️️️',
                                                                         callback_data=tradeitems.new(tg_id)))
    img = InputMediaPhoto(media=images['items'], caption='дрочун')
    await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id)


async def func_show_n_item_in_shop(callback):
    tg_id, item_id, fl = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    back = callback_farm_item if fl else callback_fight_item
    ikm = make_inline_keyboard(('купить', buy_item_shop_callback, (tg_id, item_id, fl, 0)),
                               ('◀️Наза▶️️️', back, (tg_id,)), row=1)
    img = InputMediaPhoto(media=all_items[item_id].img1, caption=all_items[item_id].name)
    await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id)
    await bot.answer_callback_query(callback.id)


async def func_buy_in_shop(callback):
    tg_id, item_id, fl, count = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    if money_of_user(tg_id) >= all_items[item_id].price:
        buy_item_user(tg_id, item_id, all_items[item_id].price)
    else:
        await bot.answer_callback_query(callback.id, f"денег малавата братишка")
        return
    back = callback_farm_item if fl else callback_fight_item
    ikm = make_inline_keyboard(('купить', buy_item_shop_callback, (tg_id, item_id, fl, count + 1)))
    ikm = make_inline_keyboard(('назад', back, (tg_id,)),
                               ('в профиль', back_to_profile, (tg_id,)), ikm=ikm)

    await bot.answer_callback_query(callback.id, f"ура ты успешно купил {all_items[item_id].name}")
    img = InputMediaPhoto(all_items[item_id].img1, caption=f'ты купил {count + 1} штук')
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id,
                                 chat_id=callback.message.chat.id)


async def func_show_hero_in_shop(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if callback.from_user.id != tg_id:
        await bot.answer_callback_query(callback.id, text=enemy_click[rnum()])
        return
    buttons = (('купить', wanna_d7e_hero, (tg_id, hero_id)), ('назад', tradeheroes, (tg_id,)))
    ikm = make_inline_keyboard(*buttons, row=1)
    img = InputMediaPhoto(media=hero_dick[hero_id].img1, caption=hero_dick[hero_id].name)
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id,
                                 chat_id=callback.message.chat.id)


# wanna_d7e_hero = CallbackData('diwd', 'tg_id', 'hero_id')

async def func_ask_for_buy(callback):
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


#
# # buy_hero_shop = CallbackData('bhs', 'tg_id', 'hero_id')
#
async def func_buy_hero(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if callback.from_user.id != tg_id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    buy_hero(tg_id, hero_id, hero_dick[hero_id].price)
    tg_id, hero_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    tg_id = callback.from_user.id
    buttons = (
        ('фармить', send_hero_farm_callback, (tg_id, hero_id,)), ('драться', send_hero_fight_callback, (tg_id,
                                                                                                        hero_id,)),
        ('шмотки', items_hero_inventory, (tg_id, hero_id,)), ('back', my_heroes, (tg_id,)))
    ikm = make_inline_keyboard(*buttons, row=3)
    img = InputMediaPhoto(media=hero_dick[hero_id].img1, caption=f"вот твой {hero_dick[hero_id].name}")
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id,
                                 chat_id=callback.message.chat.id)
    await bot.answer_callback_query(callback.id, f"ура ура ты купил {hero_dick[hero_id].name}а")


# # wear_more_items = CallbackData('wmi', 'tg_id', 'hero_id')
async def func_profile_items(callback):
    """это локально для уже полученного героя"""
    tg_id = r_cbd(callback.data)
    if callback.from_user.id != tg_id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    items = find_nowear_items(tg_id)
    text = ''
    if not items:
        text = 'У тебя нет предметов'
        ikm = InlineKeyboardMarkup().add(InlineKeyboardButton(text='назад',  callback_data=back_to_profile.new(tg_id)))
    else:
        le = min(len(items), 9)
        for i in range(le):
            text += f"{all_items[items[i][1]].name} - {items[i][2]}\n"
        buttons = ((all_items[items[i][1]].name, start_wear_item, (tg_id, items[i][1],)) for i in range(le))
        ikm = make_inline_keyboard(*buttons).add(
            InlineKeyboardButton(text='назад', callback_data=back_to_profile.new(tg_id)))
        text += 'Нажми на название предмета, чтобы одеть его'
    img = InputMediaPhoto(media=images['itemen'], caption=text)
    await bot.edit_message_media(media=img, chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                 reply_markup=ikm)


async def func_nowear_items_to_wear(callback):
    tg_id, item_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    heroes = find_id_name_all_heroes(tg_id)
    buttons = ((hero_dick[i[0]].name, wear_n_shmot_on_hero, (tg_id, i[0], item_id)) for i in heroes)
    ikm = make_inline_keyboard(*buttons).add(InlineKeyboardButton(text='назад',
                                                                  callback_data=user_items_callback.new(tg_id,)))

    img = InputMediaPhoto(media=all_items[item_id].img1, caption='выбери героя на которого одеть шмотку')
    await bot.edit_message_media(media=img, chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                 reply_markup=ikm)
    await bot.answer_callback_query(callback.id)


async def func_wear_item(callback):
    """это из профиля"""
    tg_id, hero_id, item_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    primary = find_hero_id_by_name_tg(tg_id, hero_id)
    already = find_wear_items(primary)
    already = 0 if not already else len(already)
    if already >= 6:
        await bot.answer_callback_query(callback.id, 'у этого героя уже 6 слотов')
        return
    wear_item_on_hero(tg_id, primary, item_id)
    items = find_nowear_items(tg_id)
    text = ''
    if not items:
        text = 'У тебя нет предметов'
        ikm = InlineKeyboardMarkup().add(InlineKeyboardButton(text='назад', callback_data=back_to_profile.new(tg_id)))
    else:
        le = min(len(items), 9)
        for i in range(le):
            text += f"{all_items[items[i][1]].name} - {items[i][2]}\n"
        buttons = ((all_items[items[i][1]].name, start_wear_item, (tg_id, items[i][1],)) for i in range(le))
        ikm = make_inline_keyboard(*buttons).add(
            InlineKeyboardButton(text='назад', callback_data=back_to_profile.new(tg_id)))
    text += 'Нажми на название предмета, чтобы одеть его'
    img = InputMediaPhoto(media=images['itemen'], caption=text)
    await bot.edit_message_media(media=img, chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                 reply_markup=ikm)

    await bot.answer_callback_query(callback.id, 'Предмет одет')


async def func_remove_item(callback):
    tg_id, hero_id, item_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    buttons = (('Снять', snat_shmotku_inventory, (tg_id, hero_id, item_id)),
               ('отмена', items_hero_inventory, (tg_id, hero_id)))
    ikm = make_inline_keyboard(*buttons, row=1)
    text = 'с 10% вероятностью шмотка при снятии разобьётся'
    img = InputMediaPhoto(media=images['items'], caption=text)
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id,
                                 chat_id=callback.message.chat.id)


async def func_snat_item(callback):
    tg_id, hero_id, item_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    text = ''
    primaty = find_hero_id_by_name_tg(tg_id, hero_id)
    num = random.randint(0, 9)
    if not num:
        slomat_shmotki(primaty, item_id)
        await bot.answer_callback_query(callback.id, 'ты чё дибил зачем ты шмотки сломал')
    else:
        snat_s_geroya_v_invantar(item_id, tg_id, primaty)
        await bot.answer_callback_query(callback.id, 'шмотка успешно снята')
    # итем айди настоящий айди гпредмета
    primary_id = find_hero_id_by_name_tg(tg_id, hero_id)
    items = find_wear_items(primary_id)
    if not items:
        text = 'у твоего героя нет предметов'
        ikm = make_inline_keyboard(('одеть ещё', srazu_odet, (tg_id, hero_id,)), row=3)
        ikm = make_inline_keyboard(('назад к герою', show_hero_in_inventory, (tg_id, hero_id,)),
                                   ('в 🛒Магазин🛒', go_back_all_shop, (tg_id,)), ikm=ikm)
    else:
        buttons = ((all_items[i[1]].name, q_remove_item_from_hero, (tg_id, hero_id, i[1])) for i in items)
        ikm = make_inline_keyboard(*buttons).add(
            InlineKeyboardButton(text='одеть ещё', callback_data=srazu_odet.new(tg_id, hero_id))).add(
            InlineKeyboardButton(text='назад к герою', callback_data=show_hero_in_inventory.new(tg_id, hero_id, )))
    img = InputMediaPhoto(media=images['items'], caption=text)
    await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id)


async def func_srazu_vear(callback):
    tg_id, hero_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    text = 'выбери предмет, который будет одет на твоего героя\n'
    items = find_nowear_items(tg_id)  # это неодетые
    already = find_wear_items(find_hero_id_by_name_tg(tg_id, hero_id))  # это одетые
    if not already:
        le = 0
    else:
        le = len(already)
    if le >= 6:
        await bot.answer_callback_query(callback.id, 'у героя уже 6 слотов')
        return
    if not items:  # мб магаз добавить
        img = InputMediaPhoto(media=images['itemen'], caption='у тебя нет предметов')
        ikm = InlineKeyboardMarkup().add(InlineKeyboardButton(text='назад',
                                                              callback_data=items_hero_inventory.new(tg_id, hero_id)))
        await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id)
    else:
        le = min(len(items), 9)
        for i in range(le):
            text += f"{all_items[items[i][1]].name} - {items[i][2]}\n"
        buttons = ((all_items[items[i][1]].name, odet_v2, (tg_id, hero_id, items[i][1],))
                   for i in range(le))
        ikm = make_inline_keyboard(*buttons).add(InlineKeyboardButton(text='назад',
                                                                      callback_data=items_hero_inventory.new(tg_id,
                                                                                                             hero_id)))
        img = InputMediaPhoto(media=images['bg2'], caption=text)
        await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id)


async def func_v2_wear(callback):
    tg_id, hero_id, item_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    text = ''

    primary = find_hero_id_by_name_tg(tg_id, hero_id)
    wear_item_on_hero(tg_id, primary, item_id)
    items = find_wear_items(primary)
    if not items:
        text = 'у твоего героя нет предметов'
        ikm = make_inline_keyboard(('одеть ещё', srazu_odet, (tg_id, hero_id,)), row=3)
        ikm = make_inline_keyboard(('назад к герою', show_hero_in_inventory, (tg_id, hero_id,)),
                                   ('в 🛒Магазин🛒', go_back_all_shop, (tg_id,)), ikm=ikm)
    else:
        buttons = ((all_items[i[1]].name, q_remove_item_from_hero, (tg_id, hero_id, i[1])) for i in items)
        ikm = make_inline_keyboard(*buttons).add(
            InlineKeyboardButton(text='одеть ещё', callback_data=srazu_odet.new(tg_id, hero_id))).add(
            InlineKeyboardButton(text='назад к герою', callback_data=show_hero_in_inventory.new(tg_id, hero_id, )))
    img = InputMediaPhoto(media=images['items'], caption=text)
    await bot.edit_message_media(media=img, reply_markup=ikm, chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id)

    await bot.answer_callback_query(callback.id, 'шмотка одета')
