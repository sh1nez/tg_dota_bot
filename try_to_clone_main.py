#таблица предметы
#CREATE TABLE `test_bot`.`items` (
# `id` MEDIUMINT NOT NULL AUTO_INCREMENT ,
# `hero_id` MEDIUMINT NULL DEFAULT NULL ,
# `tg_user_id` VARCHAR(15) NOT NULL ,
# `item_name` TINYINT NOT NULL ,
# `count` TINYINT NOT NULL ,
# PRIMARY KEY (`id`)) ENGINE = InnoDB;
#ALTER TABLE `items` CHANGE `count` `count` TINYINT(4) NULL DEFAULT NULL;

#таблица игроки sql код
#CREATE TABLE `test_bot`.`players` ( `user_id` INT NOT NULL , `tg_id` VARCHAR(15) NOT NULL , `money` INT NOT NULL , `status` INT NULL DEFAULT NULL , PRIMARY KEY (`user_id`)) ENGINE = InnoDB;
#ALTER TABLE `players` ADD `items` VARCHAR(100) NOT NULL AFTER `money`;

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
from texts import  item_dick, photo_links_for_shop, all_items#hero_dick,
import random
from aiogram import types
import aiogram
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import datetime
import asyncio
from database import connection, maker_menu, update_gold, starttttt, dis, bot, show_local_hero, del_callback#connect, cur,
from texts import item_dick, commands, new_reg_text, hero_dick



#print(cur)
#starttttt(ran_num)



#show_local_hero = CallbackData('hero', 'hero_id')
#send_hero_to_farm = CallbackData('farm', 'hero_id', 'tg_user_id')

# @dis.callback_query_handler(show_local_hero.filter())
# async def shower_local_hero(callback):
#     hero_id =  callback.data.split(':')[1]
#     #comand = callback.data.split('#')
#     #local_user_id = int(comand[1])
#     #user_tg_id = comand[2]
#     print(hero_id,)
#     chat_id = callback.message.chat.id
#     hero_buttons = InlineKeyboardMarkup(row_width=4)
#     hero_funk1 = InlineKeyboardButton(text='фармить', callback_data=f' # farm#{hero_id}#{user_tg_id}#{local_user_id}')
#     hero_funk2 = InlineKeyboardButton(text='драться', callback_data=f'fight#{hero_id}#{user_tg_id}#')
#     hero_funk3 = InlineKeyboardButton(text='шмотки',
#                                       callback_data=f'shmot#{hero_id}#{user_tg_id}#{chat_id}#{local_user_id}')
#     hero_funk4 = InlineKeyboardButton(text='назад', callback_data=  )#f'back_to_look#{user_tg_id}#{chat_id}#{hero_id}')
#     hero_buttons.add(hero_funk1, hero_funk2, hero_funk3).add(hero_funk4)
#     await bot.send_photo(caption='123312', photo=hero_dick[hero_id]['img'], chat_id=chat_id, reply_markup=hero_buttons)
#     await bot.answer_callback_query(callback.id)

tradeheroes = CallbackData('tradeheroes',)
tradeitems =CallbackData('tradeitems',)
go_to_shop_menu = CallbackData('go_to_shop')
go_to_items_menu = CallbackData('go_to_items')
callback_farm_item = CallbackData('farm_items_show_shop')
callback_fight_item = CallbackData('fight_items_show_shop')
callback_item_name = CallbackData('predmet_id', 'item_index', 'tg_user_id', 'hero_name', 'hero_id')

@dis.message_handler(commands=['start'])#создаём пользователя
async def start(message: aiogram.types):
    tg_user_id = message.from_user.id
    chat_id = message.chat.id
    await starttttt(tg_user_id=tg_user_id, chat_id=chat_id)

heroes_habdler = CallbackData('a', 'tg_user_id')

@dis.callback_query_handler(heroes_habdler.filter())
async def herrroo_hendler(callback):
    come = callback.data.split(':')
    tg_user_id = int(come[1])
    chat_id = callback.message.chat.id
    try:
        sql_code = f"SELECT user_id FROM `players` WHERE tg_id = {tg_user_id}"
        print(sql_code, 'пиздец')
        if connection.select_one(sql_code):
            print(callback.message.message_id, int(callback.id))
            await maker_menu(chat_id, tg_user_id, callback.message.message_id, int(callback.id))
            print(123)
        else:
            print('ERORRR')
            raise Exception('всё ')

    except:
        img = types.InputMediaPhoto(media=photo_links_for_shop[1], caption='aaaa')
        await bot.edit_message_media(chat_id=chat_id, media=img, message_id=callback.message.message_id)

show_items_user = CallbackData('asd', 'tg_id')
@dis.callback_query_handler(show_items_user.filter())
async def really_show_all_items(callback):
    come = callback.data.split(':')
    #user_id = come[1]
    tg_user_id = come[1]
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    ikm = InlineKeyboardMarkup(row_width=111)
    sql_code = f'SELECT item_name, count, id FROM items WHERE hero_id is NULL AND tg_user_id = {tg_user_id}'
    turp = connection.select_all(sql_code) ##в формате (название, количество, название предмета)
    print(turp)
    ikb_arr = []
    text = ''
    if not turp:
        text+='у тебя пока не итемов'
        ikm.add(InlineKeyboardButton(text='купить ещё', callback_data=tradeitems.new()))
    else:
        for i in range(len(turp)):
            text+= f"{i+1}. {all_items[turp[i][0]]['name']} - {turp[i][1]} штуки\n"
            ikb_arr.append(InlineKeyboardButton(text=str(i+1), callback_data=show_local_item.new(tg_user_id, turp[i][2])))
        for i in range(0, len(ikb_arr), 3):
            if len(ikb_arr)-i>=3:
                ikm.add(ikb_arr[i],ikb_arr[i+1], ikb_arr[i+2])
            elif len(ikb_arr)-i==2:
                print(2)
                ikm.add(ikb_arr[i], ikb_arr[i + 1],)
            elif len(ikb_arr)-i == 1:
                ikm.add(ikb_arr[i])
            else:break
    ikm.add(InlineKeyboardButton(text='бек ту профиль', callback_data=f'бек ту профиль'))
    img = types.InputMediaPhoto(media=photo_links_for_shop[1], caption=text)
    await bot.edit_message_media(media=img, chat_id=chat_id, message_id=message_id, reply_markup=ikm)

show_local_item = CallbackData('ashda', 'tg_user_id', 'item_id')
@dis.callback_query_handler(show_local_item.filter())
async def really_show_local_item(callback):
    come = callback.data.split(':')
    tg_user_id = come[1]
    item_id = come[2]
    clcik_user_id = callback.from_user.id
    message_id = callback.message.message_id
    chat_id = callback.message.chat.id
    print(tg_user_id, item_id, clcik_user_id, chat_id)
    ikm = InlineKeyboardMarkup(row_width=11)
    img =types.InputMediaPhoto(media=photo_links_for_shop[3], caption='урруа')
    await bot.edit_message_media(message_id=message_id, chat_id=chat_id, media=img, reply_markup=ikm)
    await bot.answer_callback_query(callback.id)


async def for_profile(tg_user_id,chat_id, *args):
    #tg_user_id = message.from_user.id
    # = message.chat.id
    sql_code = f"SELECT money, status FROM players WHERE tg_id = {tg_user_id}"
    # cur.execute(sql_code) money = cur.fetchone()[0]
    money_status = connection.select_one(sql_code)
    sql_code = f"SELECT id, item_name FROM items WHERE tg_user_id = {tg_user_id} AND hero_id IS NULL;"
    arr = connection.select_all(sql_code)
    text = ''
    ikm = InlineKeyboardMarkup()
    ikm.add(InlineKeyboardButton(text='герои', callback_data=heroes_habdler.new(tg_user_id)))
    ikm.add(InlineKeyboardButton(text='купить ещё предметы', callback_data=f'ц'))
    if not arr:
        text = 'у тебя нет предметов'
    else:
        for i in arr:
            text += f"{i}"
        ikm.add(InlineKeyboardButton(text='одеть предметы', callback_data=f's'))
    print(arr)
    await bot.send_message(chat_id=chat_id, text=f"денег - З{money_status}\nбатлпас {money_status[1]}\n"
                                                 f"предметы\n{text}", reply_markup=ikm)

@dis.message_handler(commands=['profile'])
async def profile(message):
    tg_user_id = message.from_user.id
    chat_id = message.chat.id
    sql_code = f"SELECT money, status FROM players WHERE tg_id = {tg_user_id}"
    #cur.execute(sql_code) money = cur.fetchone()[0]
    money_status = connection.select_one(sql_code)
    sql_code = f"SELECT id, item_name FROM items WHERE tg_user_id = {tg_user_id} AND hero_id IS NULL;"
    arr = connection.select_all(sql_code)
    text = ''
    ikm = InlineKeyboardMarkup(row_width=2)
    ikm.add(InlineKeyboardButton(text='герои', callback_data=heroes_habdler.new(tg_user_id)), InlineKeyboardButton(text='инвентарь', callback_data=show_items_user.new(tg_user_id))) #go_to_shop_menu.new()))
    #ikm.add()
    if not arr:
        text= 'у тебя нет предметов'
    else:
        for i in arr:
            text = f"{i}"
        #ikm.add(InlineKeyboardButton(text='одеть предметы', callback_data=f's'))
    print(arr)
    print(ikm)
    img = types.InputMediaPhoto(media=photo_links_for_shop[1], caption=f"as")#
    #img = types.InputMediaPhoto(caption='магаз у наташки', media=photo_links_for_shop[0], type='photo')
    await bot.send_photo(chat_id=chat_id, reply_markup=ikm, photo=photo_links_for_shop[2], caption=f'денег - {money_status[0]}\nбатлпас {money_status[1]}\n{text}\n')

@dis.message_handler(commands=['heroes'])
async def my_heroes(message):
    tg_user_id = message.from_user.id
    #это нужно было для проверки локал ади, теперь используется тг айди для геров
    # sql_code = f'SELECT money, status, user_id FROM players WHERE tg_id = {tg_user_id}'
    try:
        sql_code = f"SELECT user_id FROM `players` WHERE tg_id = {tg_user_id}"
        print(sql_code, 'пиздец')
        if connection.select_one(sql_code):
            await maker_menu(chat_id=message.chat.id, tg_user_id=tg_user_id,)
            print(123)
        else:
            print('ERORRR')
            raise Exception('всё ')
    except: await bot.send_message(chat_id=message.chat.id, text='иди в хуй зарегайся сначала')


@dis.message_handler(commands=['gold'])#функция которая будет выдавать голду пользователю
async def gold(message):
    tg_user_id = message.from_user.id
    sql_code = f'SELECT tg_id FROM players WHERE tg_id = {tg_user_id}'
    print(sql_code)
    #cur.execute(sql_code)  #если написать равно, то вернёт количество совпадений как я понял
    result = connection.select_one(sql_code)
    print(result)
    if result:
        return_to_user = update_gold(tg_user_id=tg_user_id, plus_money=100)
        await message.answer(text=f'теперь голды {return_to_user}')
    else: await message.answer(text='сначала зарегестрируйся')

async def show_main_menu(chat_id, message_id, *args):
    print(chat_id, message_id, args)
    ikm = InlineKeyboardMarkup(row_width=3)
    ikb1 = InlineKeyboardButton(text='герои', callback_data=tradeheroes.new())
    ikb2 = InlineKeyboardButton(text='предметы', callback_data=tradeitems.new())
    ikb3 = InlineKeyboardButton(text='в зад', callback_data=del_callback.new())
    ikm.add(ikb1, ikb2).add(ikb3)
    if not args:
        print(123)
        await bot.send_photo(chat_id=chat_id, caption='магаз у наташки', reply_markup=ikm, photo=photo_links_for_shop[0])
        return
    print(11)
    img = types.InputMediaPhoto(caption='магаз у наташки', media=photo_links_for_shop[0], type='photo')
    await bot.edit_message_media(reply_markup=ikm, media=img, message_id=message_id, chat_id=chat_id)
    await bot.answer_callback_query(args[0])

@dis.callback_query_handler(del_callback.filter())
async def del_all_menu(callback):
    mes_id =  callback.message['message_id']
    await bot.delete_message(chat_id=callback.message.chat.id ,message_id=mes_id)
    try: await bot.delete_message(chat_id=callback.message.chat.id ,message_id=mes_id-1)
    except: await bot.send_message(chat_id=callback.message.chat.id, text='пидоры дайте админку')

@dis.message_handler(commands =['shop'])
async def all_shop(message):
    chat_id = message.chat.id
    mes_id = message.message_id
    await show_main_menu(chat_id=chat_id, message_id=mes_id)
    # ikm = InlineKeyboardMarkup(row_width=3)
    # ikb1 = InlineKeyboardButton(text='герои', callback_data=tradeheroes.new())
    # ikb2 = InlineKeyboardButton(text='предметы', callback_data=tradeitems.new())
    # ikb3 = InlineKeyboardButton(text='в зад', callback_data= del_callback.new())
    # ikm.add(ikb1, ikb2).add(ikb3)
    # await bot.send_message(chat_id=chat_id, text='магаз у наташки', reply_markup=ikm)

#########################################################################################
#МАГАЗИН
@dis.callback_query_handler(go_to_shop_menu.filter())
async def go_to_items_menu(callback):
    message_id = callback.message.message_id
    chat_id = callback.message.chat.id
    print(chat_id)
    await show_main_menu(chat_id, message_id, callback.id)
look_at_item = CallbackData('a', 'item_id', 'tg_user_id')
@dis.callback_query_handler(look_at_item.filter())
async def look_at_meeee_hate(callback):
    print('start')
    come = callback.data.split(':')
    item_id = int(come[1])
    tg_user_id = int(come[2])
    click_user_id = callback.from_user.id
    if tg_user_id != click_user_id:
        await bot.answer_callback_query(callback.id, 'пидор по своим кнопкам кликай')
        return
    ikm = InlineKeyboardMarkup()
    ikm.add(InlineKeyboardButton(text='купить', callback_data=f's'))
    ikm.add(InlineKeyboardButton(text='бек парни', callback_data=callback_fight_item.new()))

    img = types.InputMediaPhoto(media=photo_links_for_shop[0], caption='нихуя ты дрочун')
    await bot.edit_message_media(message_id=callback.message.message_id, media=img, chat_id=callback.message.chat.id, reply_markup=ikm)

@dis.callback_query_handler(callback_fight_item.filter())
async def show_fight(callback):
    print('я кончил')
    tg_user_id = callback.from_user.id
    fl = callback.from_user.is_bot
    message_id = callback.message.message_id
    # print(message_id)
    chat_id = callback.message.chat.id
    her = len(item_dick['farm'])
    print(her)
    ikm1 = InlineKeyboardMarkup(row_width=her)
    for i in range(0, her + 1, 2):
        print(i)
        try:
            #{fight_items_names[i]}
            ikm1.add(InlineKeyboardButton(text=f"{item_dick['fight'][i]['name']}", callback_data=look_at_item.new(i, tg_user_id)),#callback_item_name.new(i)),
                     InlineKeyboardButton(text=f"{item_dick['fight'][i+1]['name']}",
                                          callback_data=look_at_item.new(i+1, tg_user_id))#callback_item_name.new(i + 1))
                     )
            # print('lj,fdbk')
        except:
            try:
                ikm1.add(
                    InlineKeyboardButton(text=f"{item_dick['fight'][i]['name']}", callback_data= look_at_item.new(i, tg_user_id)))##callback_item_name.new(i)))  # '))
                # print('hui')
            except: break
    ikm1.add(
        InlineKeyboardButton(text=f'в зад', callback_data=tradeitems.new()))
    img = types.InputMediaPhoto(caption='нихуя ты дрочун', media=r'https://cq.ru/storage/uploads/posts/94692/cri/dota___media_library_original_1656_982.png', type='photo')
    await bot.edit_message_media(chat_id=chat_id, message_id=message_id, media=img, reply_markup=ikm1)
    await bot.answer_callback_query(callback.id)
@dis.callback_query_handler(callback_farm_item.filter())
async def show_farm(callback):
    print(callback)
    tg_user_id = callback.from_user.id
    fl = callback.from_user.is_bot
    message_id = callback.message.message_id
    # print(message_id)
    chat_id = callback.message.chat.id
    her = len(item_dick['farm'])
    ikm1 = InlineKeyboardMarkup(row_width=her)
    for i in range(0, her+1, 2):
        try:
            print(i)
            #{farm_items_names[i]}
            ikm1.add(InlineKeyboardButton(text=f"{item_dick['farm'][i]['name']}", callback_data=callback_item_name.new(i)),
                    InlineKeyboardButton(text=f"{item_dick['farm'][i+1]['name']}", callback_data=callback_item_name.new(i+1))
                     )
        except:
            try:
                ikm1.add(InlineKeyboardButton(text=f"{item_dick['farm'][i]['name']}", callback_data=callback_item_name.new(i)))
            except: break
    ikm1.add(InlineKeyboardButton(text=f'в зад', callback_data=tradeitems.new()))# f'#{chat_id}#{int(message_id)}'))
    img = types.InputMediaPhoto(caption='фармила', type='photo', media=r'https://cq.ru/storage/uploads/posts/94692/cri/dota___media_library_original_1656_982.png')
    await bot.edit_message_media(media=img, chat_id=chat_id, message_id=message_id, reply_markup=ikm1)
    await bot.answer_callback_query(callback.id)

@dis.callback_query_handler(callback_item_name.filter())
async def open_item(callback):
    come = callback.data.split(':')
    print(come)
    item_id = come[1]
    tg_user_id = come[2]
    hero_name = come[3]
    hero_id = come[4]
    print(item_id, tg_user_id)
    click_tg_user_id = callback.from_user.id
    fl = callback.from_user.is_bot
    message_id = callback.message.message_id
    chat_id = callback.message.chat.id
    ikm = InlineKeyboardMarkup(row_width=2)
    ikb1 = InlineKeyboardButton(text='полоижть в инвентарь', callback_data=f's')
    ikb2 = InlineKeyboardButton(text='бек бек парни', callback_data= show_local_hero.new( hero_id,hero_name, tg_user_id))
    img = types.InputMediaPhoto(media=photo_links_for_shop[0], caption='aaaaaaaa')
    ikm.add(ikb1, ikb2)
    await bot.edit_message_media(media=img, message_id=message_id, chat_id=chat_id, reply_markup=ikm)
    #await bot.send_message(chat_id=chat_id, text=f'{callback.data}')
    await bot.answer_callback_query(callback.id)
@dis.callback_query_handler(tradeitems.filter())
async def all_items_show(callback):
    message_id = callback.message.message_id
    chat_id = callback.message.chat.id
    print(message_id, chat_id)
    #her = len(farm_items_names)
    ikm = InlineKeyboardMarkup(row_width=3)
    ikm.add(InlineKeyboardButton(text='фарми', callback_data=callback_farm_item.new()),InlineKeyboardButton(text='дерсись', callback_data=callback_fight_item.new()))
    ikm.add(InlineKeyboardButton(text='в зад', callback_data=go_to_shop_menu.new()))
    #await bot.edit_message_text(text='на фрифармычах', reply_markup=ikm, message_id=int(message_id), chat_id=chat_id)
    img = types.InputMediaPhoto(media=r'https://cq.ru/storage/uploads/posts/94692/cri/dota___media_library_original_1656_982.png', type='photo', caption='предметы дяди васи')
    await bot.edit_message_media(chat_id=chat_id, reply_markup=ikm, message_id=message_id,media=img)
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
show_hero_n = CallbackData('hero', 'hero_id', )
buy_hero = CallbackData('buy', 'hero_id',)
show_all_heroes = CallbackData('show',)
@dis.callback_query_handler(show_all_heroes.filter())
async def shower_all(callback):
    print(123)
@dis.callback_query_handler(buy_hero.filter())
async def try_to_buy_hero(callback):
    come = callback.data.split(':')[1]
    hero_id = callback.data['hero_id']
    tg_user_id = callback.from_user.id
    message_id = callback.message.message_id
    chat_id = callback.message.chat.id
    sql_code = f"SELECT money FROM players WHERE tg_id = {tg_user_id}"
    #with connect.cursor() as cur: ЗАТЕСТИТЬ ЭТУ ХУЙНЮ
    money = connection.select_one(sql_code)[0]
    price_hero = hero_dick[hero_id]['price']
    if money<price_hero:
        await bot.answer_callback_query(callback.id, text='бро подкопи денег ты нищеброд')
        return
    update_gold(tg_user_id=tg_user_id, plus_money=-price_hero)
    img = types.InputMediaPhoto(caption='ураура', type='photo', media=hero_dick[hero_id]['event_img'])
    await bot.edit_message_media(media=img, chat_id=chat_id, message_id=message_id)
    await bot.answer_callback_query(callback.id)


@dis.callback_query_handler(show_hero_n.filter())
async def show_hero_nniy(callback):
    arr = callback.data.split(':')
    print(arr)
    #print(type(arr[1]))
    hero_id = int(arr[1])
    print(hero_id)
    tg_user_id = callback.from_user.id
    fl = callback.from_user.is_bot
    message_id = callback.message.message_id
    chat_id = callback.message.chat.id
    ikm = InlineKeyboardMarkup(row_width=2)
    ikb1 = InlineKeyboardButton(text='купить', callback_data=buy_hero.new(hero_id))
    ikb2 = InlineKeyboardButton(text='в попку', callback_data=tradeheroes.new())
    ikm.add(ikb1).add(ikb2)
    print(123)
    print(hero_dick[hero_id]['img']) #f'{hero_id}'])
    img = types.InputMediaPhoto(type='photo', media=hero_dick[hero_id]['img'], caption=f"{hero_dick[hero_id]['name']}")
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=message_id, chat_id=chat_id) #discription_of_heroes[hero_id]
@dis.callback_query_handler(tradeheroes.filter())
async def tradeheroes_ne_funk(callback):
    print(callback.data)
    print()
    print(callback.data)
    message_id = callback.message.message_id
    chat_id = callback.message.chat.id
    her = len(hero_dick)
    print(her)
    print(hero_dick[0])
    ikm = InlineKeyboardMarkup(row_width=her+1)
    for i in range(0, her, 2):
        print(i)
        print(type(hero_dick[i]['name']))
        try:
            ikm.add(InlineKeyboardButton(text=hero_dick[i]['name'], callback_data=show_hero_n.new(i)),# f'geroi#{i}'),
                InlineKeyboardButton(text=hero_dick[i+1]['name'], callback_data=show_hero_n.new(i+1)))
            print('lj,fdbk')
        except:
            try:
                ikm.add(
                    InlineKeyboardButton(text=hero_dick[i]['name'], callback_data=show_hero_n.new(i)))  # f'geroi#{i}'))
                print('hui')
            except:
                print('(((')
                break
    ikm.add(InlineKeyboardButton(text=f'в задницу хочу', callback_data=go_to_shop_menu.new()))  #f'back_to_shop#{chat_id}#{mesas_id}'))
    #img = types.InputMediaPhoto(caption='asd', media=photo_links_for_shop[0], type='photo')
    img = types.InputMediaPhoto(caption='ураура', type='photo', media=hero_dick[1]['event_img'])
    await bot.edit_message_media(reply_markup=ikm, media=img, message_id=message_id, chat_id=chat_id)
    await bot.answer_callback_query(callback.id)

########################################################################################################
#профиль действия с героем

menu_hero = CallbackData('hero', 'hero_name_id', 'tg_user_id')
send_hero_to_farm = CallbackData('send', 'tg_user_id', 'hero_id', 'hero_name')#'hero_name',
send_hero_to_fight = CallbackData('farm', 'hero_id', 'tg_user_id')
buy_more = CallbackData('buy_more_items', 'hero_id', 'tg_user_id')
buy_item = CallbackData('buy_for_hero', 'tg_user_id')
show_item = CallbackData('show', 'item_id', 'hero_id', 'tg_user_id')
polojit_item_v_inventory = CallbackData('put', 'tg_user_id')

#@dis.callback_query_handler()
@dis.callback_query_handler(show_item.filter())
async def swho_local_item_of_local_hero(callback):
    #тут я должен показать предмет, его статы описание и должны быть кнопки
    #положить в инвентарь, назад, пока так потом ещё мб
    come = callback.data.split(':')
    item_id = come[1]
    hero_id = come[2]
    #item_name = come ##Я ЕГО ЕЩЁ НЕ ПЕРЕДАЛ
    #local_hero_id = come[3]
    tg_user_id = come[3]
    ikm = InlineKeyboardMarkup(row_width=2)
    ikb1 = InlineKeyboardButton(text="положить в инвентарь", callback_data=polojit_item_v_inventory.new())
    ikn2 = InlineKeyboardButton(text="бек", callback_data=show_local_hero.new(hero_id, tg_user_id, ))
    text = f" это {all_items[item_id]['name']}\n{all_items[item_id]['description']}"


@dis.callback_query_handler(send_hero_to_farm.filter())
async def fermer(callback):
    come = callback.data.split(':')
    print(come)
    #hero_name = int(come[2])
    tg_user_id = int(come[1])
    hero_id = int(come[2])
    hero_name = int(come[3])
    tg_click_user_id = int(callback.from_user.id)
    print(tg_click_user_id)
    if tg_user_id != tg_click_user_id:
        await bot.answer_callback_query(callback_query_id=callback.id, text='пидор по своим ссылкам кликай чужое не трож')
        return
    sql_code = f'SELECT last_time FROM heroes WHERE hero_id = {hero_id}'
    #print(sql_code)
    #cur.execute(sql_code)
    last_time = connection.select_one(sql_code)[0]#[j for i in list(cur.fetchall()) for j in i][0]
    print(last_time)
    aq = 1
    if last_time is not None:
        aq = (datetime.datetime.today() - last_time).total_seconds()
    if last_time is None or aq>10:
        date = datetime.datetime.today()
        print(date)
        await bot.send_message(chat_id=callback.message.chat.id,
                               text=f" {hero_dick[hero_name]['name']} отправился на 285 мса за крипами")  # name_of_heroes[heroe_name]
        await bot.answer_callback_query(callback.id)
        await asyncio.sleep(3)
        rand_num = random.randint(50, 150)
        sql_code = f"SELECT money FROM players WHERE tg_id = {tg_user_id}"
        money = connection.select_one(sql_code)[0]
        await bot.send_message(chat_id=callback.message.chat.id,
                               text=f"твой {hero_dick[hero_name]['name']} вернусля, залутав {rand_num} голды")
        sql_code = f"UPDATE heroes SET last_time = '{datetime.datetime.today().replace(microsecond=0)}' WHERE hero_id = {hero_id}"
        connection.update_insert_del(sql_code)
        sql_code = f"UPDATE players SET money = {money + rand_num} WHERE tg_id = {tg_user_id}"
        connection.update_insert_del(sql_code)
        await bot.answer_callback_query(callback.id)
    else:
        await bot.send_message(chat_id=callback.message.chat.id, text=f"бро зачилься {hero_dick[hero_name]['name']} уже фармит")#name_of_heroes[heroe_name]
        await bot.answer_callback_query(callback.id)

shmotki_local_hero = CallbackData('s', 'hero_id', 'hero_name', 'tg_user_id', )
@dis.callback_query_handler(shmotki_local_hero.filter())
async def shdhsdf(callback):
    come = callback.data.split(':')
    hero_id = come[1]
    hero_name = come[2]
    tg_user_id = come[3]
    chat_id = callback.message.chat.id
    message_id=callback.message.message_id
    print('ssssssssssssssss')
    sql_code = f"SELECT item_name, count FROM items WHERE hero_id = {hero_id}"
    arr = connection.select_all(sql_code)

    if not arr:
        print('у тебя нет шмоток')
        ikm1 = InlineKeyboardMarkup(row_width=2)
    else:
        ikm1 = InlineKeyboardMarkup(row_width=len(arr)+2)
        for i in range(0,len(arr), 2):
            try:
                print(all_items[arr[i][0]])
                # {fight_items_names[i]}
                ikm1.add(
                    InlineKeyboardButton(text=f"{all_items[arr[i][0]]['name']}", callback_data=callback_item_name.new(arr[i][0], tg_user_id, hero_name, hero_id,)),
                    InlineKeyboardButton(text=f"{all_items[arr[i+1][0]]['name']}",
                                         callback_data=callback_item_name.new(arr[i][0], tg_user_id, hero_name, hero_id, ))
                    )
            except:
                try:
                    ikm1.add(
                        InlineKeyboardButton(text=f"{all_items[arr[i][0]]['name']}", callback_data=callback_item_name.new(arr[i][0], tg_user_id, hero_name, hero_id,)))
                                               # '))
                    # print('hui')
                except:
                    break
    #ikm1.
    ikm1.add(InlineKeyboardButton(text=f'в зад ыы', callback_data=show_local_hero.new(hero_id, hero_name, tg_user_id)), InlineKeyboardButton(text='одеть еще', callback_data=f's'))
    img = types.InputMediaPhoto(media=photo_links_for_shop[1], caption='урурара')
    await bot.edit_message_media(media=img, message_id=message_id, chat_id=chat_id, reply_markup=ikm1)




    #ikm = InlineKeyboardMarkup(row_width=3)  # len(index_items))
    #ikm.add(InlineKeyboardButton(text=f'\nОдеть ещё пердметы', callback_data=buy_more.new(local_hero_id, tg_user_id)))
        # # тут пользователь должен перенаправляться в хуинку где он одевает предметы из своего inventory
    # # elif len(new_items)<6:
    # #     ikm.add(KeyboardButton(text=f'\nКупить ещё', callback_data=buy_more(hero_id)))   #f'buymore#{hero_id}'))
    # # print()
    # img = types.InputMediaPhoto(media=photo_links_for_shop[0], caption='вот твой герой')
    # await bot.edit_message_media(message_id=message_id, chat_id=chat_id, media=img, reply_markup=ikm)
    # # bot.send_message(chat_id=chat_id, text=textik, reply_markup=ikm)
    # await bot.answer_callback_query(callback.id)




    # sql_code = f"SELECT id, item_name FROM items WHERE hero_id = {local_hero_id}"
    # print(sql_code)
    # cur.execute(sql_code)
    # index_items = list(cur.fetchall())
    # if not index_items:
    #     await bot.answer_callback_query(callback.id, text='БАГ')
    #     return
    # print(index_items)
    # new_items = []
    # #при нажатии на шмотку она должна перемещаться в инвентарь
    # for i in index_items:
    #     new_items.append(i)
    #     #        if i[1] is None:
    #     #     pass
    #     #else:
    # #то что сверху теперь не нужно т.к. у меня в бд нет пустых слотов
    # #print(hero_name_id, 123123)
    # #print(hero_dick[int(hero_name_id)])
    # textik = f"вот предметы твоего {hero_dick[hero_name_id]['name']}\n Нажми на предмет чтобы снять его" \
    #          f" в инвентарь или 'одеть', чтобы выбрать предметы из своего инвентаря " # {name_of_heroes[hero_id]}
    # for i in range(0, len(new_items),2):
    #     print(new_items[i])
    #
    #     try:
    #         print(all_items[new_items[i][1]], print(all_items[new_items[i][1+1]]))
    #         #тут я хочу чтобы под картинкой героя были предметы.
    #         #а сверху что ты делал пидор тупоголовый
    #         #при нажатии на него можно будет посмотреть статы (?) переместить в инвентарь
    #         #наверное хорошо бы передать айди героя чтобы узнать сочетаемость предметов
    #         #БЛЯТЬ ПРИДЕЛАЙ В КОЛБЕК приедлывание
    #         #ДА СУКЕА СВЕРХУ ТОЛЬКО ЁБАНЫЙ МАССИВ ГДЕ ЕГО ДЕГЕНАРТ СМОТРЯЩИЙ ТИПО ТЕБЯ БУДЕТ СМОТРЕТЬ
    #         ikm.add(InlineKeyboardButton(text=f"{all_items[new_items[i][1]]['name']}", callback_data=show_item.new(new_items[i][1], hero_name_id, tg_user_id,)),
    #                 InlineKeyboardButton(text=f"{all_items[new_items[i+1][1]]['name']}", callback_data=show_item.new(new_items[i+1][1], hero_name_id, tg_user_id,)))
    #         print('cool')
    #     except:
    #         try:
    #             print(print(all_items[new_items[i][1]]['name']))
    #             ikm.add(InlineKeyboardButton(text=f"{all_items[new_items[i][1]]['name']}", callback_data=show_item.new(new_items[i][1], hero_name_id, tg_user_id,)))
    #         except:
    #             print('not cool')
    #             pass
    #     #окей тут есть предметы с сылками на их подробный осмотр
    # print(len(new_items))
    #тут я напихал предметы чела к уторого есть
    #а нахуя сверху уже всё есть
    # if len(new_items) == 0:
    #    textik=f"у {hero_dick[hero_name_id]['name']}а нет предметов"



    await bot.answer_callback_query(callback.id)


go_to_all_heroes = CallbackData('all', 'tg_user_id',)



@dis.callback_query_handler(go_to_all_heroes.filter())
async def come_to_heroe(callback):
    #tg_user_id = message.from_user.id
    #print()
    come = callback.data.split(':')
    tg_user_id = come[1]
    chat_id = callback.message.chat.id
    print(tg_user_id, chat_id)
    # это нужно было для проверки локал ади, теперь используется тг айди для геров
    # sql_code = f'SELECT money, status, user_id FROM players WHERE tg_id = {tg_user_id}'
    try:
        sql_code = f'SELECT user_id FROM players WHERE tg_id = {tg_user_id}'
        if connection.select_one(sql_code):
            print(1231231)
            print(callback.id, callback.message.message_id)
            await maker_menu(chat_id, tg_user_id,callback.message.message_id, int(callback.id))
            print(123)
        else:
            print('ERORRR')
            raise Exception('всё ')
    except:
        await bot.send_message(chat_id=chat_id, text='иди в хуй зарегайся сначала ss')

#show_all_local_heroes = CallbackData('a', )
@dis.callback_query_handler(show_local_hero.filter())
#эта хрень должна показать локального героя со своими предметами, возможностью одеть/снять ещё.
async def shmotki_of_hero(callback):
    print('PISAPOPA')
    come = callback.data.split(':')
    # main_user_tg = []
    hero_id = come[1]  # int(callback.data['hero_name_id'])
    # local_user_id = int(callback.data['local_user_id'])
    tg_user_id = int(come[3])
    hero_name =int( come[2])
    click_user_tg_id = callback.from_user.id
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    print(tg_user_id, hero_id, hero_name)
    #print(hero_dick)
    #print(hero_dick[hero_name])
    hero_buttons = InlineKeyboardMarkup(row_width=3)
    hero_funk1 = InlineKeyboardButton(text='фармить', callback_data=send_hero_to_farm.new(tg_user_id, hero_id, hero_name,))
    hero_funk2 = InlineKeyboardButton(text='драться', callback_data=send_hero_to_fight.new(hero_id, tg_user_id))
    hero_funk3 = InlineKeyboardButton(text='шмотки', callback_data=shmotki_local_hero.new(hero_id, hero_name, tg_user_id)) # пока тоже хз, но шмотки должны показываться
    hero_funk4 = InlineKeyboardButton(text='назад', callback_data=go_to_all_heroes.new(tg_user_id))  # пока так, потом возвращение туда откуда он пришёл
    # f'back_to_look#{user_tg_id}#{chat_id}#{hero_id}')
    hero_buttons.add(hero_funk1, hero_funk2, hero_funk3).add(hero_funk4) #, hero_funk2).add(hero_funk4)
    #await bot.send_photo(caption='123312', photo=hero_dick[hero_name]['img'], chat_id=chat_id, reply_markup=hero_buttons)
    img = types.InputMediaPhoto(media=hero_dick[hero_name]['img'], caption='123123',)
    await bot.edit_message_media(media=img, message_id=message_id, chat_id=chat_id, reply_markup=hero_buttons)
    await bot.answer_callback_query(callback.id)



###########################################################################################################
@dis.callback_query_handler(buy_more.filter())
async def shop_to_wear_items(callback):
    #вот и тут мы должны показать пользоваетелю его предметы
    hero_id = callback.data.split(':')[1]
    #теперь ищем все неодетые предметы
    sql_code = f"SELECT id FROM items WHERE "
#@dis.callback_query_handler()

if __name__ == '__main__':
    aiogram.executor.start_polling(dis, )#skip_updates=True
