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

# def create_new_hero(tg_user_id):
#     sql_code = f"INSERT INTO players tg_id VALUES {tg_user_id} "
#     cur.execute(sql_code)
#     #insert(table='players', all_coloniums=f'tg_id', all_values=f'{tg_user_id}')
#     time = datetime.datetime.today().replace(microsecond=0)
#     sql_code = f'SELECT user_id FROM players WHERE tg_id = {tg_user_id}'
#     cur.execute(sql_code)
#     local_user_id = cur.fetchall()[0]
#     #local_user_id = select(what_return='user_id', where_column='tg_id', table='players', value=f'{tg_user_id}')[0]
#     hero_id = 0
#     hero_lvl = 0
#     all_coloniums='`id`, `last_time`, `user_id`, `hero_id`, `hero_lvl`, `hero_activity`'
#     all_values=f"NULL, '{time}', '{local_user_id}', '{hero_id}', '{hero_lvl}', '0'"
#     table='`custom_heroes`'
#     insert_query = f"INSERT INTO {table} ({all_coloniums}) VALUES ({all_values});"
#     try:
#         cur.execute(insert_query)
#         next_hero_id = connect.insert_id() + 1
#         print(next_hero_id)
#
#         connect.commit()
#         print('стараюсь')
#         aa = cur.lastword()
#         print(aa)
#         print('всё кул')
#     except:
#         print('говно')
#     connect.commit()
def create_slot(hero_id):
    sql_code = f"INSERT INTO items (`hero_id`, `item_name`) VALUES ('{hero_id}',  NULL);"
    print(sql_code)
    cur.execute(sql_code)
    connect.commit()
def create_hero(local_user_id, name_hero_id, hero_lvl):
    sql_code = f"INSERT INTO heroes (`id`, `last_time`, `user_id`, `hero_id`, `hero_lvl`, `hero_activity`) VALUES (NULL, NULL, '{local_user_id}', '{name_hero_id}', '{hero_lvl}', '0');"
    print(sql_code)
    cur.execute(sql_code)
    hero_id = connect.insert_id()
    connect.commit()
    return hero_id
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




if __name__ == '__main__':
    aiogram.executor.start_polling(dis, )#skip_updates=True