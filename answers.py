from database import *
from aiogram.types import InputMediaPhoto
import aiogram
from objects import *
from config import bot, sheduler


async def starter(message):
    tg_id = message.from_user.id
    if not reg_user(tg_id):
        if message.chat.id != tg_id:
            await bot.send_message(message.chat.id, 'регистрироваться можно только в личных сообщениях')
            return
        sql_code1 = f"INSERT INTO `players` (`tg_id`, `money`) VALUES ('{tg_id}', '0')"
        hero_id = 0  # это типо пуджа выдаёт бесплатно
        sql_code2 = f"INSERT INTO heroes (`tg_id`, `hero_name`, `lvl`, `exp` ) VALUES " \
                    f"('{tg_id}', '{hero_id}', '1', '0');"
        connection.make_many(sql_code1, sql_code2)
        await bot.send_message(text=f'теперь ты зареган,\n{new_reg_text}', chat_id=message.chat.id)
        return
    else:
        await bot.send_message(text=f'ты уже зареган', chat_id=message.chat.id)


async def rsmhip(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    await all_heroes_local_user(tg_id, callback.message.message_id, callback.message.chat.id, callback.id)


async def bonus_func(message):
    if check_bonus(tg_id=message.from_user.id):
        await message.answer('бонус получен')
        return
    await message.answer('ты уже использовал бонус, попробуй завтра')


async def all_shop_func(something):
    tg_id = something.from_user.id
    money = money_of_user(something.from_user.id)
    if money is False:
        await bot.send_message(something.chat.id, 'ты не зарегистрирован, используй /start в личных сообщениях боту')
        return
    ikm = make_inline_keyboard(*(('герои', tradeheroes, (tg_id,)), ('предметы', tradeitems, (tg_id,)),
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
        return Exception('Не сообщение и не колбек, это не отработает никогда нахуй я это пишу')

async def make_profile(something):
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
    print(money)
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
    if isinstance(something, aiogram.types.Message):
        await bot.send_photo(chat_id=chat_id, reply_markup=ikm, photo=images['anime1'], caption=caption_text)
    else:
        img = InputMediaPhoto(media=images['anime1'], caption=caption_text)
        await bot.edit_message_media(media=img, chat_id=something.message.chat.id, reply_markup=ikm,
                                     message_id=something.message.message_id)


async def shop_heroes_func(callback):
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


async def shop_items_finc(callback):
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


async def all_heroes_local_user(callback):
    tg_id = r_cbd(callback.data)
    if tg_id != callback.from_user.id:
        await bot.answer_callback_query(callback.id, enemy_click[rnum()])
        return
    tup = find_id_name_all_heroes(tg_id)
    if not tup:
        ikm = InlineKeyboardMarkup().add(InlineKeyboardButton(text='бек', callback_data=back_to_profile.new(tg_id)))
        img = InputMediaPhoto(caption='у тебя нет героев', media=images['woman'])
    else:
        buttons = ((hero_dick[i[0]].name, show_hero_in_inventory, (tg_id, i[0],),) for i in tup)
        ikm = make_inline_keyboard(*buttons, row=3).add(
            InlineKeyboardButton(text='бек', callback_data=back_to_profile.new(tg_id)))
        img = InputMediaPhoto(caption='герои', media=images['woman'])
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id,
                                 chat_id=callback.message.chat.id)
    await bot.answer_callback_query(callback.id)


# show_hero_in_inventory = CallbackData('shiip', 'tg_id', 'hero_id')
async def inventory_hero_func(callback):
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
    await bot.answer_callback_query(callback.id)

