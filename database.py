import datetime
import pymysql
from config import *
import aiogram
from texts import *
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
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

"""CREATE TABLE IF NOT EXISTS 
 `test_bot`.`items` (
`id` MEDIUMINT NOT NULL AUTO_INCREMENT ,
`hero_id` MEDIUMINT NULL DEFAULT NULL ,
`tg_user_id` VARCHAR(15) NOT NULL ,
`item_name` TINYINT NOT NULL ,
`count` TINYINT(4) NULL DEFAULT NULL,
PRIMARY KEY (`id`)) ENGINE = InnoDB;
"""
try: connection = Connect(); print('я начал');
except: print('нет конекта')


bot = aiogram.Bot(token)
dis = aiogram.Dispatcher(bot)




###############################################---PROFILE---###############################################

def find_nowear_items(tg_id):
    sql_code = f"SELECT id, item_name, count FROM items WHERE tg_id = {tg_id} AND hero_id IS NULL"
    items = connection.select_all(sql_code)#((id, name, count))
    return items
def find_wear_items(tg_id, hero_id):
    sql_code = f"SELECT item_name FROM items WHERE tg_id = {tg_id} AND hero_id = {hero_id}"
    return connection.select_all(sql_code)

def make_text_inventory(items: tuple, *args):#итемы в формате (хуйня, индекс, количество)
    text=str(args[0]) if args else ''
    for i in items:
        text+=f"{all_items[i[1]]['name']} - {i[2]}шт\n"
    return text
def find_info_all_heroes(tg_id):
    sql_code = f"SELECT hero_lvl, hero_name, last_time FROM heroes WHERE tg_id = {tg_id}"
    #мейби ещё ввести чтобы было видно кулдаун на фарм и другие вещи
    heroes = connection.select_all(sql_code)
    return heroes
def find_id_name_all_heroes(tg_id):
    sql_code = f"SELECT hero_name FROM heroes WHERE tg_id = {tg_id}"
    return connection.select_all(sql_code)

def f_s_hero_farm(tg_id, hero_id):
    t = datetime.datetime.today().replace(microsecond=0)
    sql_code = f"UPDATE heroes SET last_time = '{t}' WHERE tg_id = {tg_id} AND hero_name ={hero_id}"
    connection.update_insert_del(sql_code)

def check_time_farm(tg_id, hero_id): #тру равно свободен
    sql_code = f"SELECT last_time FROM heroes WHERE tg_id = {tg_id} AND hero_name = {hero_id}"
    t1 = connection.select_one(sql_code)[0]
    if not t1: return True
    t2 = datetime.datetime.today().replace(microsecond=0)
    dt = (t2-t1).total_seconds()
    return True if dt > 3600 else False

def wear_item_on_hero(tg_id, hero_id, item_id, ):
    sql_code = f"UPDATE items SET hero_id = {hero_id} WHERE item_name = {item_id} AND tg_id = {tg_id}"
    connection.update_insert_del(sql_code)

def snat_s_geroya_v_invantar(item_id, tg_id, hero_id):
    sql_code = f'UPDATE items SET hero_id = NULL WHERE item_name = {item_id} AND tg_id = {tg_id} AND hero_id = {hero_id}'
    connection.update_insert_del(sql_code)

###############################################---SHOP---###############################################


###############################################---BUY/SELL---###############################################

def buy_hero(tg_id, hero_id, price):
    money = money_of_user(tg_id)
    sql_code1 = f"UPDATE players SET money = {money - price} WHERE tg_id = {tg_id}"
    sql_code2 = f"INSERT INTO heroes (`tg_id`, `hero_name`, `hero_lvl`) VALUES ('{tg_id}', '{hero_id}', '1');"
    connection.make_many(sql_code1, sql_code2)

def buy_item_user(tg_id, item_id, price: int, count=1):
    money = money_of_user(tg_id)
    sql_code1 = f"UPDATE players SET money = {money-price} WHERE tg_id = {tg_id}"
    value = connection.select_one(f"SELECT count FROM items WHERE tg_id = {tg_id} and item_name = {item_id}")
    if value:sql_code2 = f'UPDATE items SET count = {value[0]+count} WHERE tg_id = {tg_id} and item_name = {item_id}'
    else:sql_code2 = f"INSERT INTO items (tg_id, item_name, count) VALUES ('{tg_id}', {item_id}, '{count}')"
    connection.make_many(sql_code1, sql_code2)

def create_hero(tg_id, hero_id):
    sql_code = f"INSERT INTO heroes (`tg_id`, `hero_name`, `hero_lvl`) VALUES ('{tg_id}', '{hero_id}', '1');"
    connection.insert_id(sql_code)


###############################################---menu's---###############################################

def make_inline_keyboard(row=3, *args):#передать инфу в формате n, (text, CallbackData, *args)
    return InlineKeyboardMarkup(row_width=row).add(*(InlineKeyboardButton(text=i[0],
                                callback_data=i[1].new(*i[2])) for i in args))



###############################################---funks---###############################################
def rnum(): return random.randint(0, len(enemy_click)-1)
def r_cbd(callback): return int(callback.split(':')[1]) if len(callback.split(':')) == 2 else map(int,callback.split(':')[1:])




def chek_hero_user(tg_id, hero_id):
    sql_code = f"SELECT id FROM heroes WHERE tg_id = {tg_id} AND hero_name = {hero_id}"
    return True if connection.select_one(sql_code) else False

def money_of_user(tg_id):
    sql_code = f"SELECT money FROM players WHERE tg_id = {tg_id}"
    return connection.select_one(sql_code)[0]

def text_time(t: datetime.datetime):
    if not t: return '- готов\n'
    s = 3600-(datetime.datetime.today().replace(microsecond=0) - t).total_seconds()
    if s<=0: return ' - готов\n'
    text = '- '
    if s >= 3600: text+=f'{int(s//3600)} часов '; s %= 3600
    if s >= 60: text+=f"{int(s//60)} мин "; s %= 60
    text+=f"{int(s)} сек\n"
    return text

def chek_bp(tg_id):
    sql_code = f"SELECT status FROM players WHERE tg_id"
    a =connection.select_one(sql_code)[0]
    return a if a else False

def reg_user(tg_id):
    sql_code = f"SELECT tg_id from players WHERE tg_id = {tg_id}"
    return True if connection.select_one(sql_code) else False