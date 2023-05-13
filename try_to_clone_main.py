#таблица предметы
#CREATE TABLE `test_bot`.`heroes` ( `id` MEDIUMINT NOT NULL AUTO_INCREMENT , `hero_id` MEDIUMINT NOT NULL ,
#`player_id` MEDIUMINT NOT NULL , `item_name` TINYINT NULL DEFAULT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

#таблица игроки sql код
#CREATE TABLE `test_bot`.`players` ( `user_id` INT NOT NULL , `tg_id` VARCHAR(15) NOT NULL , `money` INT NOT NULL , `status` INT NULL DEFAULT NULL , PRIMARY KEY (`user_id`)) ENGINE = InnoDB;

# таблица герои
# CREATE TABLE `test_bot`.`heroes` (
# `hero_id` MEDIUMINT NOT NULL AUTO_INCREMENT ,
# `tg_user_id` VARCHAR(15) NOT NULL ,
# `local_user_id` MEDIUMINT NOT NULL,
# `hero_name` TINYINT NOT NULL ,
# `last_time` DATETIME NULL DEFAULT NULL ,
# `hero_lvl` TINYINT NOT NULL DEFAULT '1' ,
# PRIMARY KEY (`hero_id`)) ENGINE = InnoDB;
#леонардо дайвинчик
#CREATE TABLE `test_bot`.`leonardo` (
# `id` INT NOT NULL AUTO_INCREMENT ,
# `tg_id` VARCHAR(15) NOT NULL ,
# `text` TEXT NOT NULL ,
# `image` TINYTEXT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

import random
import aiogram
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
import pymysql
import datetime
import asyncio
from texts import *
from database import *
from config import token

print('я начал')

tradeheroes = CallbackData('tradeheroes',)
tradeitems =CallbackData('tradeitems', )
del_callback = CallbackData('del',)
go_to_shop_menu = CallbackData('go_to_shop')
go_to_items_menu = CallbackData('go_to_items')
callback_farm_item = CallbackData('farm_items_show_shop')
callback_fight_item = CallbackData('fight_items_show_shop')
callback_item_name = CallbackData('predmet_id', 'item_index')

@dis.message_handler(commands=['start'])#создаём пользователя
async def start(message: aiogram.types):
    tg_user_id = message.from_user.id
    sql_code = f"SELECT tg_id from players WHERE tg_id = {tg_user_id}"
    cur.execute(sql_code)
    result = list(cur.fetchall())
    bb = [j for i in result for j in i]
    print(bb)
    #проверил есть ли пользователь. Если есть
    if not bb:
        await message.answer(text=new_reg_text)
        try:
            #create_player
            sql_code = f"INSERT INTO `players` (`tg_id`, `money`) VALUES ('{tg_user_id}', '0')"
            print(sql_code)
            cur.execute(sql_code)
            local_user_id = connect.insert_id()
            connect.commit()
            hero_id = 0
            hero_lvl = 0
            new_hero_id = create_hero(tg_user_id= tg_user_id, local_user_id=local_user_id, name_hero_id=hero_id)
            print(new_hero_id)
            for i in range(6):
                create_slot(new_hero_id, local_user_id=local_user_id)
            print(123)
            await message.answer(text=f'теперь ты зареган \n{commands}')
        except:
            await message.answer(text=f'админ пидорас сломал всё')
    else:        await message.answer(text=f'{reg_text} {commands}')

@dis.message_handler(commands=['profile'])
async def profile(message):
    tg_user_id = message.from_user.id
    #это нужно было для проверки локал ади, теперь используется тг айди для геров
    # sql_code = f'SELECT money, status, user_id FROM players WHERE tg_id = {tg_user_id}'
    try:
        sql_code = f'SELECT user_id FROM players WHERE tg_id = {tg_user_id}'
        print(sql_code)
        if  cur.execute(sql_code) >0:
            #print(123)
            await maker_menu(chat_id=message.chat.id, tg_user_id=tg_user_id,)
        else:
            #print(11)
            raise Exception
    except: await bot.send_message(chat_id=message.chat.id, text='иди в хуй зарегайся сначала')


@dis.message_handler(commands=['gold'])#функция которая будет выдавать голду пользователю
async def gold(message):
    tg_user_id = message.from_user.id
    sql_code = f'SELECT tg_id FROM players WHERE tg_id = {tg_user_id}'
    print(sql_code)
    cur.execute(sql_code)  #если написать равно, то вернёт количество совпадений как я понял
    result = [j for i in list(cur.fetchall()) for j in i]
    print(result)
    if result:
        return_to_user = update_gold(tg_user_id=tg_user_id, plus_money=100)
        await message.answer(text=f'теперь голды {return_to_user}')
    else: await message.answer(text='сначала зарегестрируйся')

@dis.message_handler(commands =['shop'])
async def all_shop(message):
    chat_id = message.chat.id
    mes_id = message.message_id
    ikm = InlineKeyboardMarkup(row_width=3)
    ikb1 = InlineKeyboardButton(text='герои', callback_data=tradeheroes.new())
    ikb2 = InlineKeyboardButton(text='предметы', callback_data=tradeitems.new())
    ikb3 = InlineKeyboardButton(text='в зад', callback_data= del_callback.new())
    ikm.add(ikb1, ikb2).add(ikb3)
    await bot.send_message(chat_id=chat_id, text='магаз у наташки', reply_markup=ikm)

#########################################################################################
#МАГАЗИН
@dis.callback_query_handler(go_to_shop_menu.filter())
async def go_to_items_menu(callback):
    message_id = callback.message.message_id
    chat_id = callback.message.chat.id
    ikm = InlineKeyboardMarkup(row_width=3)
    ikb1 = InlineKeyboardButton(text='герои', callback_data=tradeheroes.new())
    ikb2 = InlineKeyboardButton(text='предметы', callback_data=tradeitems.new())
    ikb3 = InlineKeyboardButton(text='в зад', callback_data=del_callback.new())
    ikm.add(ikb1, ikb2).add(ikb3)
    await bot.edit_message_text(chat_id=chat_id, text='магаз у наташки', message_id=message_id, reply_markup=ikm)
    await bot.answer_callback_query(callback.id)

@dis.callback_query_handler(callback_fight_item.filter())
async def show_fight(callback):
    print('я кончил')
    tg_user_id = callback.from_user.id
    fl = callback.from_user.is_bot
    message_id = callback.message.message_id
    # print(message_id)
    chat_id = callback.message.chat.id
    her = len(farm_items_names)
    ikm1 = InlineKeyboardMarkup(row_width=her)
    her = len(fight_items_names)
    ikm1 = InlineKeyboardMarkup(row_width=her)
    for i in range(0, her + 1, 2):
        try:
            ikm1.add(InlineKeyboardButton(text=f'{fight_items_names[i]}', callback_data=callback_item_name.new(i)),
                     InlineKeyboardButton(text=f'{fight_items_names[i + 1]}',
                                          callback_data=callback_item_name.new(i + 1))
                     )
            # print('lj,fdbk')
        except:
            try:
                ikm1.add(
                    InlineKeyboardButton(text=f'{fight_items_names[i]}', callback_data=callback_item_name.new(i)))  # '))
                # print('hui')
            except: break
    ikm1.add(
        InlineKeyboardButton(text=f'в зад', callback_data=tradeitems.new()))
    await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='нихуя ты дрочун', reply_markup=ikm1)
    await bot.answer_callback_query(callback.id)
@dis.callback_query_handler(callback_farm_item.filter())
async def show_farm(callback):
    print(callback)
    tg_user_id = callback.from_user.id
    fl = callback.from_user.is_bot
    message_id = callback.message.message_id
    # print(message_id)
    chat_id = callback.message.chat.id
    her = len(farm_items_names)
    ikm1 = InlineKeyboardMarkup(row_width=her)
    for i in range(0, her+1, 2):
        try:
            ikm1.add(InlineKeyboardButton(text=f'{farm_items_names[i]}', callback_data=callback_item_name.new(i)),
                    InlineKeyboardButton(text=f'{farm_items_names[i+1]}', callback_data=callback_item_name.new(i+1))
                     )
        except:
            ikm1.add(InlineKeyboardButton(text=f'{farm_items_names[i]}', callback_data=callback_item_name.new(i)))
            break
    ikm1.add(InlineKeyboardButton(text=f'в зад', callback_data=tradeitems.new()))# f'#{chat_id}#{int(message_id)}'))
    await bot.edit_message_text(text='ща', chat_id=chat_id, message_id=message_id, reply_markup=ikm1)
    await bot.answer_callback_query(callback.id)

@dis.callback_query_handler(callback_item_name.filter())
async def open_item(callback):
    print(callback)
    #шаблон
    tg_user_id = callback.from_user.id
    fl = callback.from_user.is_bot
    message_id = callback.message.message_id
    chat_id = callback.message.chat.id
    await bot.send_message(chat_id=chat_id, text=f'{callback.data}')
    await bot.answer_callback_query(callback.id)
@dis.callback_query_handler(tradeitems.filter())
async def all_items(callback):
    message_id = callback.message.message_id
    chat_id = callback.message.chat.id
    her = len(farm_items_names)
    ikm = InlineKeyboardMarkup(row_width=3)
    ikm.add(InlineKeyboardButton(text='фарми', callback_data=callback_farm_item.new()),InlineKeyboardButton(text='дерсись', callback_data=callback_fight_item.new()))
    ikm.add(InlineKeyboardButton(text='в зад', callback_data=go_to_shop_menu.new()))
    #await bot.edit_message_text(text='на фрифармычах', reply_markup=ikm, message_id=int(message_id), chat_id=chat_id)
    await bot.edit_message_text(text='предметы от дяди пети', chat_id=chat_id, reply_markup=ikm, message_id=message_id)
    await bot.answer_callback_query(callback.id)


# @dis.callback_query_handler(go_to_shop_menu.filter())
# async def back_to_shop(callback):
#     tg_user_id = callback.from_user.id
#     fl = callback.from_user.is_bot
#     message_id = callback.message.message_id
#     print(message_id)
#     chat_id = callback.message.chat.id
#     print(chat_id)
#     ikm = InlineKeyboardMarkup(row_width=3)
#     ikb1 = InlineKeyboardButton(text='герои', callback_data= tradeheroes.new())
#     ikb2 = InlineKeyboardButton(text='предметы', callback_data= tradeitems.new())
#     ikb3 = InlineKeyboardButton(text='в зад', callback_data= del_callback.new() )
#     ikm.add(ikb1, ikb2).add(ikb3)
#     await bot.edit_message_text(chat_id=chat_id, reply_markup=ikm, message_id=int(message_id), text="магаз у наташки")
# @dis.callback_query_handler(lambda mes: mes.data.startswith('del'))
# async def deleter(callback):
#     message_id = callback.message.message_id
#     print(message_id)
#     chat_id = callback.message.chat.id
#     print(chat_id)
#     await bot.delete_message(chat_id=chat_id, message_id=message_id)
#     await bot.delete_message(chat_id=chat_id, message_id=message_id-1) #удаляет ещё и сообщение пидора
# @dis.callback_query_handler(lambda m: m.data.startswith('back'))
# async def back(callback):
#     callback_arr = callback.data.split('#')
#     zapros = callback_arr[0]
#     user_tg_id = callback_arr[1]
#     chat_id = callback_arr[2]
#     sql_code = f'SELECT user_id FROM players WHERE tg_id = {user_tg_id}'
#     print(sql_code)
#     cur.execute(sql_code)  # если написать равно, то вернёт количество совпадений как я понял
#     result = [j for i in list(cur.fetchall()) for j in i]
#     if zapros=='back_to_look':
#         await bot.answer_callback_query(callback.id)
#         print(123)


########################################################################################################
#магазин героев
go_to_all_heroes = CallbackData('predprosmotr',)
show_hero_n = CallbackData('hero', 'hero_id')
@dis.callback_query_handler(go_to_all_heroes)
async def show_heroes(callback):
    tg_user_id = callback.from_user.id
    fl = callback.from_user.is_bot
    message_id = callback.message.message_id
    chat_id = callback.message.chat.id
    print(callback)
    her = len(name_of_heroes)
    ikm1 = InlineKeyboardMarkup(row_width=her)
    for i in range(0, her + 1, 2):
        try:
            ikm1.add(InlineKeyboardButton(text=f'{name_of_heroes[i]}', callback_data=show_hero_n.new(i)), #f'geroi#{i}'),
                     InlineKeyboardButton(text=name_of_heroes[i + 1], callback_data=show_hero_n.new(i+1))) #f'geroi{i + 1}'))
            print('lj,fdbk')
        except:
            ikm1.add(InlineKeyboardButton(text=f'{name_of_heroes[i]}', callback_data=show_hero_n.new(i)))#f'geroi#{i}'))
            print('hui')
            break
    print(message_id)
    ikm1.add(InlineKeyboardButton(text=f'в зад', callback_data= go_to_shop_menu.new()))# f'back_to_shop#{chat_id}#{message_id}'))
    await bot.edit_message_text(text='предметы долбоёбыча', chat_id=chat_id, reply_markup=ikm1,
                                message_id=int(message_id))
    await bot.answer_callback_query(callback.id)

@dis.callback_query_handler(show_hero_n)
async def show_hero_n(callback):
    hero_id = callback.data['hero_id']
    tg_user_id = callback.from_user.id
    fl = callback.from_user.is_bot
    message_id = callback.message.message_id
    chat_id = callback.message.chat.id
    await bot.edit_message_text()


########################################################################################################
#профиль действия с героем

menu_hero = CallbackData('hero', 'hero_name_id', 'local_user_id')
send_to_farm_hero = CallbackData('send_to_farm', 'hero_name_id', 'main_user_id','local_user_id')
buy_more = CallbackData('buy_more_items', 'hero_id')
buy_item = CallbackData('buy_for_hero')
show_local_hero = CallbackData('shmot_of_hero', 'hero_name_id')

@dis.callback_query_handler(send_to_farm_hero)
async def fermer(callback):
    heroe_name = callback.data['hero_name_id']
    tg_main_user_id = int(callback.data['main_user_id'])
    tg_click_user_id = int(callback.from_user.id)
    local_user_id = callback.data['local_user_id']
    if tg_main_user_id != tg_click_user_id:
        await bot.answer_callback_query('пидор по своим ссылкам кликай чужое не трож')
        return
    sql_code = f'SELECT last_time FROM heroes WHERE user_id = {tg_click_user_id} AND hero_id = {heroe_name}'
    cur.execute(sql_code)
    last_time = [j for i in list(cur.fetchall()) for j in i][0]
    print(last_time)
    try:
        aq = (datetime.datetime.today() - last_time).total_seconds()
        if aq>10:
            raise Exception#поменял
        else:
            await bot.send_message(chat_id=callback.message.chat.id, text=f'бро зачилься {name_of_heroes[heroe_name]} уже фармит')
            await  bot.answer_callback_query(callback.id)
    except:
        date = datetime.datetime.today()
        print(date)
        await bot.send_message(chat_id=callback.message.chat.id, text=f'{name_of_heroes[heroe_name]} отправился на 285 мса за крипами')
        await bot.answer_callback_query(callback.id)
        await asyncio.sleep(3)
        rand_num = random.randint(50,150)
        sql_code = f'SELECT money FROM players WHERE user_id = {local_user_id}'
        cur.execute(sql_code)
        asd =cur.fetchone()
        print(asd[0])
        await bot.send_message(chat_id=callback.message.chat.id, text=f'твой {name_of_heroes[heroe_name]} вернусля, залутав {rand_num} голды')
        sql_code = f"UPDATE heroes SET last_time = '{datetime.datetime.today().replace(microsecond=0)}' WHERE hero_id = {heroe_name} AND user_id = {local_user_id}"
        print(sql_code)
        cur.execute(sql_code)
        connect.commit()
        await bot.answer_callback_query(callback.id)

@dis.callback_query_handler(menu_hero.filter())
async def hero_show(callback):
    #comand = callback.data.split('#')
    #local_user_id =int(comand[1])
    hero_id = int(callback.data['hero_name_id'])
    local_user_id = int(callback.data['local_user_id'])
    user_tg_id = callback.from_user.id
    chat_id = callback.message.chat.id
    print(user_tg_id, hero_id, local_user_id)

    hero_buttons = InlineKeyboardMarkup(row_width=4)
    hero_funk1 = InlineKeyboardButton(text='фармить', callback_data=f'farm#{hero_id}#{user_tg_id}#{local_user_id}')
    hero_funk2 = InlineKeyboardButton(text='драться', callback_data=f'fight#{hero_id}#{user_tg_id}#')
    hero_funk3 = InlineKeyboardButton(text='шмотки', callback_data=f'shmot#{hero_id}#{user_tg_id}#{chat_id}#{local_user_id}')
    hero_funk4 = InlineKeyboardButton(text='назад', callback_data=f'back_to_look#{user_tg_id}#{chat_id}#{hero_id}')
    hero_buttons.add(hero_funk1, hero_funk2, hero_funk3).add(hero_funk4)
    await bot.send_photo(caption='123312', photo=photo_links[hero_id], chat_id=chat_id, reply_markup=hero_buttons)
    await bot.answer_callback_query(callback.id)


@dis.callback_query_handler(show_local_hero)
async def shmotki_of_hero(callback):
    hero_id = callback.data[1]
    print(hero_id)
    message_id = callback.message.message_id
    chat_id = callback.message.chat.id
    sql_code = f"SELECT item_id, item_name FROM items WHERE hero_id = {hero_id} "
    print(sql_code)
    cur.execute(sql_code)
    index_items = list(cur.fetchall())
    ikm = InlineKeyboardMarkup(row_width=len(index_items))
    #print(index_items)
    new_items = []
    for i in index_items:
        if i[1] is None:
             pass#
        else: new_items.append(i)
    textik = f'вот предметы твоего {name_of_heroes[hero_id]}'
    print(new_items)
    for i in range(0, len(new_items), 2):
        if index_items[i+1] is None:
                print(None)
        else:
            a = True
            print(new_items[i][1])
            try:
                ikm.add(KeyboardButton(text=f'{items_names[new_items[i][1]]}', callback_data=f'item#{new_items[i][1]}#{hero_id}#'), KeyboardButton(text=f'{items_names[new_items[i+1][1]]}', callback_data=f'item##{hero_id}#'))
            except: ikm.add(KeyboardButton(text=f'{items_names[new_items[i][1]]}', callback_data=f'item#{new_items[i][1]}#{hero_id}#'))
    print(len(new_items))
    #тут я напихал предметы чела к уторого есть
    if len(new_items) == 0:
        textik=f'у {name_of_heroes[hero_id]}а нет предметов'
        ikm.add(KeyboardButton(text=f'\nОдеть пердметы', callback_data=buy_more.new(hero_id))) #  f'buymore#{hero_id}'))
    # elif len(new_items)<6:
    #     ikm.add(KeyboardButton(text=f'\nКупить ещё', callback_data=buy_more(hero_id)))   #f'buymore#{hero_id}'))

    await bot.send_message(chat_id=chat_id, text=textik, reply_markup=ikm)
    await bot.answer_callback_query(callback.id)

@dis.callback_query_handler(lambda m: m.data.startswith('shmot'))
async def shmotki(callback):
    come = callback.data.split('#')
    print(come)
    hero_name = int(come[1])
    tg_user_id = come[2]
    chat_id = come[3]
    hero_id = chat_id[4]
    sql_code = f"SELECT item_id, item_name FROM items WHERE hero_id = {hero_id} "
    print(sql_code)
    cur.execute(sql_code)
    index_items = list(cur.fetchall())
    ikm = InlineKeyboardMarkup(row_width=len(index_items))
    #print(index_items)
    new_items = []
    for i in index_items:
        if i[1] is None:
             pass#
        else: new_items.append(i)
    textik = f'вот предметы твоего {name_of_heroes[hero_name]}'
    print(new_items)
    for i in range(0, len(new_items), 2):
        if index_items[i+1] is None:
                print(None)
        else:
            a = True
            print(new_items[i][1])
            try:
                ikm.add(KeyboardButton(text=f'{items_names[new_items[i][1]]}', callback_data=f'item#{new_items[i][1]}#{hero_id}#'), KeyboardButton(text=f'{items_names[new_items[i+1][1]]}', callback_data=f'item##{hero_id}#'))
            except: ikm.add(KeyboardButton(text=f'{items_names[new_items[i][1]]}', callback_data=f'item#{new_items[i][1]}#{hero_id}#'))
    print(len(new_items))
    if len(new_items) == 0:
        textik=f'у {name_of_heroes[hero_name]}а нет предметов'
        ikm.add(KeyboardButton(text=f'\nКупить', callback_data=buy_more.new(hero_id))) #  f'buymore#{hero_id}'))
    elif len(new_items)<6:
        ikm.add(KeyboardButton(text=f'\nКупить ещё', callback_data=buy_more(hero_id)))   #f'buymore#{hero_id}'))
    await bot.send_message(chat_id=chat_id, text=textik, reply_markup=ikm)
    await bot.answer_callback_query(callback.id)

@dis.callback_query_handler(buy_more.filter())
async def shop_to_by_items(callback):
    print(callback)

#@dis.callback_query_handler()

if __name__ == '__main__':
    aiogram.executor.start_polling(dis, )#skip_updates=True
