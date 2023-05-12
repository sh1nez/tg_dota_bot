from config import *
import pymysql
import aiogram
from texts import *
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



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

def create_lepnardo_user(tg_user_id, txt, image):
    sql_code = f"INSERT INTO leonardo (tg_id, text, image) VALUES ('{tg_user_id}', '{txt}', '{image}')"
    print(sql_code)
    cur.execute(sql_code)
    connect.commit()
    print('1111')


def create_slot(hero_id):
    sql_code = f"INSERT INTO items (`hero_id`, `item_name`) VALUES ('{hero_id}',  NULL);"
    print(sql_code)
    cur.execute(sql_code)
    connect.commit()
def create_hero(tg_user_id, name_hero_id):
    sql_code = f"INSERT INTO heroes ( `user_id`, `hero_name`, `hero_lvl`) VALUES ('{tg_user_id}', '{name_hero_id}', '1');"
    print(sql_code)
    cur.execute(sql_code)
    hero_id = connect.insert_id()
    connect.commit()
    return hero_id
def update_gold(tg_user_id, plus_money):
    sql_code = f'SELECT money FROM players WHERE tg_id = {tg_user_id}'
    print(sql_code)
    cur.execute(sql_code)
    start_money = [j for i in list(cur.fetchall()) for j in i][0]
    sql_code = f'UPDATE players SET money = {start_money + plus_money} WHERE players.tg_id = {tg_user_id}'
    print(sql_code)
    cur.execute(sql_code)
    connect.commit()
    return start_money

async def maker_menu(chat_id, tg_user_id):
    i = InlineKeyboardMarkup(row_width=3)
    sql_code = f'SELECT id, hero_id FROM heroes WHERE user_id = {tg_user_id}'
    cur.execute(sql_code)
    arrey_heroes = [j for i in list(cur.fetchall()) for j in i]
    print(arrey_heroes, 'asdasd')
    h = InlineKeyboardMarkup(row_width=len(arrey_heroes) // 2)
    for j in range(0, len(arrey_heroes) - 1, 2):
        h.add(InlineKeyboardButton(text=name_of_heroes[arrey_heroes[j + 1]],
                                   callback_data=f'hero#{tg_user_id}#{j // 2}'))
    await bot.send_message(text='вот твои герои', reply_markup=h, chat_id=chat_id)

