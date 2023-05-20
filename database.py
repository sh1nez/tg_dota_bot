import pymysql
from config import *
import aiogram
from texts import *
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from aiogram.utils.callback_data import CallbackData
import random


################################################---BASE---################################################
class Connect:
    def __init__(self):
        self.conn = pymysql.connect(host=host, port=3306, user=user, password=password,database=db_name,)
    def update_insert_del(self, sql_code,):
        self.conn.ping()
        with self.conn.cursor() as cur:
            # print(sql_code)
            cur.execute(sql_code)
            self.conn.commit()
    def select_one(self, sql_code):
        #print(sql_code)
        self.conn.ping()
        with self.conn.cursor() as cur:
            if cur.execute(sql_code):
                return cur.fetchone()
            return False
    def select_all(self, sql_code):
        #print(sql_code)
        self.conn.ping()
        with self.conn.cursor() as cur:
            if cur.execute(sql_code):
                return cur.fetchall()
            return False
    def insert_id(self, sql_code):
        self.conn.ping()
        with self.conn.cursor() as cur:
            cur.execute(sql_code)
            r_id = connection.conn.insert_id()
            self.conn.commit()
        return r_id
    def make_many(self, *args):
        self.conn.ping()
        cur = self.conn.cursor()
        for i in args:
            cur.execute(i)
        cur.close()
        self.conn.commit()

import timeit


try: connection = Connect(); print('я начал');
except: print('нет конекта')


bot = aiogram.Bot(token)
dis = aiogram.Dispatcher(bot)

################################################---START---################################################

async def starter(tg_id, chat_id,):
    sql_code = f"SELECT tg_id from players WHERE tg_id = {tg_id}"
    result = connection.select_all(sql_code)
    #проверил есть ли пользователь. Если есть
    if not result:
        try:
            sql_code = f"INSERT INTO `players` (`tg_id`, `money`) VALUES ('{tg_id}', '0')"
            hero_id = 0#это типо пуджа выдаёт бесплатно
            new_hero_id = create_hero(tg_id=tg_id, hero_id=hero_id)
            await bot.send_message(text=f'теперь ты зареган, {new_reg_text}', chat_id=chat_id)
        except:
            await bot.send_message(text='админ пидор сломал всё', chat_id=chat_id)
    else: await bot.send_message(text=f'ты уже зареган, команды\n{commands}', chat_id=chat_id)



###############################################---PROFILE---###############################################



###############################################---SHOP---###############################################
async def show_main_menu(chat_id, message_id, tg_id, *args):
    ikm = make_inline_keyboard(2,(('герои', tradeheroes, (tg_id,)), ('предметы', tradeitems, (tg_id,)), ('в зад', del_callback, (tg_id,))))
    if not args:await bot.send_photo(chat_id=chat_id, caption='магаз у наташки', reply_markup=ikm, photo=photo_links_for_shop[0]); return
    img = InputMediaPhoto(caption='магаз у наташки', media=photo_links_for_shop[0], type='photo')
    await bot.edit_message_media(reply_markup=ikm, media=img, message_id=message_id, chat_id=chat_id)
    await bot.answer_callback_query(args[0])


tradeheroes = CallbackData('trher', 'tg_id')

tradeitems = CallbackData('tritm', 'tg_id')

del_callback = CallbackData('delcs', 'tg_id')

###############################################---BUY/SELL---###############################################

def buy_hero(tg_id, hero_id, price):
    money = money_of_user(tg_id)
    sql_code1 = f"UPDATE players SET money = {money - price} WHERE tg_id = {tg_id}"
    sql_code2 = f"INSERT INTO heroes (`tg_id`, `hero_name`, `hero_lvl`) VALUES ('{tg_id}', '{hero_id}', '1');"
    connection.make_many(sql_code1, sql_code2)

def buy_item_user(tg_id, item_id, price: int, count=1):
    money = money_of_user(tg_id)
    sql_code1 = f"UPDATE players SET money = {money-price} WHERE tg_id = {tg_id}"
    sql_code2 = f"INSERT INTO items (tg_id, item_name, count) VALUES ('{tg_id}', {item_id}, '{count}')"
    #"""INSERT INTO `players` (`tg_id`, `money`) VALUES ('{tg_id}', '0')"""
    connection.make_many(sql_code1, sql_code2)

def wear_item_on_hero(item_id, hero_id):
    sql_code = f"UPDATE items SET hero_id = {hero_id} WHERE id = {item_id}"
    connection.update_insert_del(sql_code)

def snat_s_geroya_v_invantar(item_id):
    sql_code = f'UPDATE items SET hero_id = NULL WHERE id = {item_id}'

def create_hero(tg_id, hero_id):
    sql_code = f"INSERT INTO heroes (`tg_id`, `hero_name`, `hero_lvl`) VALUES ('{tg_id}', '{hero_id}', '1');"
    return connection.insert_id(sql_code)

###############################################---menu's---###############################################

def make_inline_keyboard(row=3, *args):#передать инфу в формате n, (text, CallbackData, *args)
    return InlineKeyboardMarkup(row_width=row).add(*(InlineKeyboardButton(text=i[0],
                                callback_data=i[1].new(*i[2])) for i in args))
#использование
#tup = ((item_dick['farm'][i]['name'],tradeitems, (1,)) for i in item_dick['farm'])
#ikm = make_inline_keyboard(2, *tup)
#print(ikm)

###############################################---funks---###############################################
def rnum(): return random.randint(0, len(enemy_click)-1)
def r_cbd(callback): return map(int,(callback.split(':')[1:]))

def money_of_user(tg_id):
    sql_code = f"SELECT money FROM players WHERE tg_id = {tg_id}"
    return int(connection.select_one(sql_code)[0])
