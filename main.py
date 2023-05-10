import random

import aiogram
from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import pymysql
import datetime
import asyncio
from texts import *
from functions import *
from config import token, host, user, password, db_name
print('я начал')
bot = aiogram.Bot(token)
dis = aiogram.Dispatcher(bot)
try:
    connect = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
    )
except:  print('ConnectionError')
cur = connect.cursor()
@dis.message_handler(commands=['start'])#прост отвечает
async def start(message: aiogram.types):
    tg_user_id = message.from_user.id
    #sql_code =f"CREATE TABLE `{db_name}` .`players`  ENGINE = InnoDB;"
    sql_code = f"SELECT tg_id from players WHERE tg_id = {tg_user_id}"
    cur.execute(sql_code)
    result = list(cur.fetchall())
    bb = [j for i in result for j in i]
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
            new_hero_id = create_hero(local_user_id, hero_id, hero_lvl)
            print(new_hero_id)
            for i in range(6):
                create_slot(new_hero_id)
            await message.answer(text=f'теперь ты зареган \n{commands}')
        except:
            await message.answer(text=f'админ пидорас сломал всё')
    else:
        await message.answer(text=f'{reg_text} {commands}')

@dis.message_handler(commands=['gold'])#прост отвечает
async def gold(message):
    tg_user_id = message.from_user.id
    sql_code = f'SELECT tg_id FROM players WHERE tg_id = {tg_user_id}'
    print(sql_code)
    cur.execute(sql_code)  #если написать равно, то вернёт количество совпадений как я понял
    result =  [j for i in list(cur.fetchall()) for j in i]
    print(result)
    #вот тут удалёно комит если чёто сломается вставь хуй
    if result:
        return_to_user = update_gold(tg_user_id, plus_money=100)
        await message.answer(text=f'теперь голды {return_to_user}')
    else: await message.answer(text='сначала зарегестрируйся')
@dis.message_handler(commands=['profile'])
async def profile(message):
    tg_user_id = message.from_user.id
    #chat_id = message.chat.id
    sql_code = f'SELECT money, status, user_id FROM players WHERE tg_id = {tg_user_id}'
    print(sql_code)
    cur.execute(sql_code)
    result =  [j for i in list(cur.fetchall()) for j in i]
    try:
        print(result)
        local_user_id = result[2]
        sql_code = f'SELECT hero_id FROM heroes WHERE user_id = {local_user_id}'
        print(sql_code)
        cur.execute(sql_code)
        #heroe_names = [j for i in list(cur.fetchall()) for j in i]
        #print(heroe_names)
        print(local_user_id)
        await maker_menu(local_user_id, message.chat.id, tg_user_id)
    except: await bot.send_message(chat_id=message.chat.id, text='иди в хуй зарегайся сначала')

@dis.message_handler(commands =['shop'])
async def all_shop(message):
    chat_id = message.chat.id
    mes_id = message.message_id+1
    ikm = InlineKeyboardMarkup(row_width=3)
    ikb1 = InlineKeyboardButton(text='герои', callback_data=f'tradeheroes#{chat_id}#{mes_id}')
    ikb2 = InlineKeyboardButton(text='предметы', callback_data='tradeitems')
    ikb3 = InlineKeyboardButton(text='в зад', callback_data=f'del#{mes_id}#{chat_id}')
    ikm.add(ikb1, ikb2).add(ikb3)
    await bot.send_message( chat_id=chat_id, text='магаз у наташки', reply_markup=ikm)

@dis.callback_query_handler(lambda c: c.data.startswith('tradeheroes'))
async def heroes_shop(callback):
    come = callback.data.split('#')
    chat_id = come[1]
    mes_id = come[2]
    text_heroes = 'вот все доступные герои'
    her = len(name_of_heroes)
    print(her)
    ikm1 = InlineKeyboardMarkup(row_width=her)
    for i in range(0, her+1, 2):
        try:
            ikm1.add(InlineKeyboardButton(text=f'{name_of_heroes[i]}', callback_data=f'geroi#{i}'), InlineKeyboardButton(text=name_of_heroes[i+1], callback_data=f'geroi{i+1}'))
            print('lj,fdbk')
        except:
            ikm1.add(InlineKeyboardButton(text=f'{name_of_heroes[i]}', callback_data=f'geroi#{i}'))
            print('hui')
            break
    ikm1.add(InlineKeyboardButton(text=f'в зад', callback_data=f'back_to_shop#{chat_id}#{mes_id}'))
    await bot.edit_message_text(text='герои от дяди васи', chat_id=chat_id, reply_markup=ikm1, message_id=mes_id)
    await bot.answer_callback_query(callback.id)
@dis.callback_query_handler(lambda mes: mes.data.startswith('back_to_shop'))
async def back_to_shop(callback):
    come = callback.data.split('#')
    chat_id = come[1]
    mes_id = come[2]
    ikm = InlineKeyboardMarkup(row_width=3)
    ikb1 = InlineKeyboardButton(text='герои', callback_data=f'tradeheroes#{chat_id}#{mes_id}')
    ikb2 = InlineKeyboardButton(text='предметы', callback_data='tradeitems')
    ikb3 = InlineKeyboardButton(text='в зад', callback_data=f'del#{mes_id}#{chat_id}')
    ikm.add(ikb1, ikb2).add(ikb3)
    await bot.edit_message_text(chat_id=chat_id, reply_markup=ikm, message_id=mes_id, text="магаз у наташки")
@dis.callback_query_handler(lambda mes: mes.data.startswith('del'))
async def deleter(callback):
    come = callback.data.split('#')
    mes_id = int(come[1])
    chat_id = come[2]
    await bot.delete_message(chat_id=chat_id, message_id=mes_id)
@dis.callback_query_handler(lambda m: m.data.startswith('back'))
async def back(callback):
    callback_arr = callback.data.split('#')
    zapros = callback_arr[0]
    user_tg_id = callback_arr[1]
    chat_id = callback_arr[2]
    sql_code = f'SELECT user_id FROM players WHERE tg_id = {user_tg_id}'
    print(sql_code)
    cur.execute(sql_code)  # если написать равно, то вернёт количество совпадений как я понял
    result = [j for i in list(cur.fetchall()) for j in i]
    print(result, 123132)
    # async def maker_menu(local_user_id, chat_id, tg_user_id):
    #     i = InlineKeyboardMarkup(row_width=3)
    #     sql_code = f'SELECT id, hero_id FROM heroes WHERE user_id = {local_user_id}'
    #     cur.execute(sql_code)
    #     arrey_heroes = [j for i in list(cur.fetchall()) for j in i]
    #     print(arrey_heroes, 'asdasd')
    #     h = InlineKeyboardMarkup(row_width=len(arrey_heroes) // 2)
    #     for j in range(0, len(arrey_heroes) - 1, 2):
    #         h.add(InlineKeyboardButton(text=heroes[arrey_heroes[j + 1]],
    #                                    callback_data=f'hero#{local_user_id}#{tg_user_id}#{j // 2}'))
    #     await bot.send_message(text='вот твои герои', reply_markup=h, chat_id=chat_id)

    #await bot.edit_message_text()
    if zapros=='back_to_look':
        await bot.answer_callback_query(callback.id)
        print(123)

@dis.callback_query_handler(lambda m: m.data.startswith('hero'))
async def hero_show(callback):
    comand = callback.data.split('#')
    #print(comand, 123123)
    local_user_id =int(comand[1])
    hero_id = int(comand[3])
    user_tg_id = comand[2]
    print(user_tg_id, hero_id, local_user_id)
    chat_id = callback.message.chat.id
    hero_buttons = InlineKeyboardMarkup(row_width=4)
    hero_funk1 = InlineKeyboardButton(text='фармить', callback_data=f'farm#{hero_id}#{user_tg_id}#{local_user_id}')
    hero_funk2 = InlineKeyboardButton(text='драться', callback_data=f'fight#{hero_id}#{user_tg_id}#')
    hero_funk3 = InlineKeyboardButton(text='шмотки', callback_data=f'shmot#{hero_id}#{user_tg_id}#{chat_id}#{local_user_id}')
    hero_funk4 = InlineKeyboardButton(text='назад', callback_data=f'back_to_look#{user_tg_id}#{chat_id}#{hero_id}')
    hero_buttons.add(hero_funk1, hero_funk2, hero_funk3).add(hero_funk4)
    await bot.send_photo(caption='123312', photo=photo_links[hero_id], chat_id=chat_id, reply_markup=hero_buttons)
    await bot.answer_callback_query(callback.id)
@dis.callback_query_handler(lambda m: m.data.startswith('farm'))
async def fermer(callback):
    arr = callback.data.split('#')
    heroe_name =  int(arr[1])
    tg_user_id = arr[2]
    local_user_id = arr[3]
    sql_code = f'SELECT last_time FROM heroes WHERE user_id = {local_user_id} AND hero_id = {heroe_name}'
    cur.execute(sql_code)
    last_time = [j for i in list(cur.fetchall()) for j in i][0]
    print(last_time)
    try:
        aq = (datetime.datetime.today() - last_time).total_seconds()
        if aq>10:
            #print('гыгыгы')
            raise ZeroDivisionError
        else:
            await bot.send_message(chat_id=callback.message.chat.id, text=f'бро зачилься {name_of_heroes[heroe_name]} уже фармит')
            await  bot.answer_callback_query(callback.id)
    except:
        date = datetime.datetime.today()
        print(date)
        await bot.send_message(chat_id=callback.message.chat.id, text=f'{name_of_heroes[heroe_name]} отправился на 285 мса за крипами')
        await bot.answer_callback_query(callback.id)
        await asyncio.sleep(3)
        #update_money мб потом кд
        rand_num = random.randint(50,150)
        sql_code = f'SELECT money FROM players WHERE user_id = {local_user_id}'
        cur.execute(sql_code)
        asd =cur.fetchone()
        print(asd[0])
        #last_money = [j for i in list(cur.fetchall()) for j in i]
        #print(last_money)
        #sql_code = f"UPDATE players SET money={}"
        await bot.send_message(chat_id=callback.message.chat.id, text=f'твой {name_of_heroes[heroe_name]} вернусля, залутав {rand_num} голды')
        sql_code = f"UPDATE heroes SET last_time = '{datetime.datetime.today().replace(microsecond=0)}' WHERE hero_id = {heroe_name} AND user_id = {local_user_id}"
        print(sql_code)
        cur.execute(sql_code)
        connect.commit()
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
    #index_items = [j for i in list(cur.fetchall()) for j in i]
    #print(asd,1111)
    ikm = InlineKeyboardMarkup(row_width=len(index_items))
    print(index_items)
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
                ikm.add(KeyboardButton(text=f'{items[new_items[i][1]]}', callback_data=f'item#{new_items[i][1]}#{hero_id}#'), KeyboardButton(text=f'{items[new_items[i+1][1]]}', callback_data=f'item##{hero_id}#'))
            except: ikm.add(KeyboardButton(text=f'{items[new_items[i][1]]}', callback_data=f'item#{new_items[i][1]}#{hero_id}#'))
    print(len(new_items))
    if len(new_items) == 0:
        textik=f'у {name_of_heroes[hero_name]}а нет предметов'
        ikm.add(KeyboardButton(text=f'\nКупить', callback_data=f'buymore#{hero_id}'))
    elif len(new_items)<6:
        ikm.add(KeyboardButton(text=f'\nКупить ещё', callback_data=f'buymore#{hero_id}'))
    await bot.send_message(chat_id=chat_id, text=textik, reply_markup=ikm)
    await bot.answer_callback_query(callback.id)

@dis.callback_query_handler(lambda c: c.data.startswith('buymore'))
async def shop(callback):
    come = callback.data.split('#')


if __name__ == '__main__':
    aiogram.executor.start_polling(dis, )#skip_updates=True
