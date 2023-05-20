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

import timeit


try: connection = Connect(); print('я начал');
except: print('нет конекта')


bot = aiogram.Bot(token)
dis = aiogram.Dispatcher(bot)

################################################---START---################################################
async def starter(tg_user_id, chat_id,):
    sql_code = f"SELECT tg_id from players WHERE tg_id = {tg_user_id}"
    result = connection.select_all(sql_code)
    #проверил есть ли пользователь. Если есть
    if not result:
        try:
            sql_code = f"INSERT INTO `players` (`tg_id`, `money`) VALUES ('{tg_user_id}', '0')"
            local_user_id = connection.insert_id(sql_code)
            hero_id = 0
            hero_lvl = 0
            new_hero_id = create_hero(tg_user_id=tg_user_id, local_user_id=local_user_id, name_hero_id=hero_id)
            #print(new_hero_id)
            await bot.send_message(text='теперь ты зареган', chat_id=chat_id)
            await bot.send_message(text=new_reg_text, chat_id=chat_id)
        except:
            await bot.send_message(text='админ пидор сломал всё', chat_id=chat_id)
    else: await bot.send_message(text=f'ты уже зареган, команды\n{commands}', chat_id=chat_id)

def create_hero(local_user_id, tg_user_id, name_hero_id):
    sql_code = f"INSERT INTO heroes ( `tg_user_id`, `local_user_id`,  `hero_name`, `hero_lvl`) VALUES ('{tg_user_id}'," \
               f" '{local_user_id}', '{name_hero_id}', '1');"
    return connection.insert_id(sql_code)


###############################################---PROFILE---###############################################



###############################################---SHOP---###############################################
async def show_main_menu(chat_id, message_id, tg_id, *args):
    ikm = make_inline_keyboard(2,(('герои', tradeheroes, (tg_id,)), ('предметы', tradeitems, (tg_id,)), ('в зад', del_callback, (tg_id,))))
    # InlineKeyboardMarkup(row_width=3).add(InlineKeyboardButton(text='герои', callback_data=tradeheroes.new()),
    #     InlineKeyboardButton(text='предметы', callback_data=tradeitems.new())).add(
    #     InlineKeyboardButton(text='в зад', callback_data=del_callback.new()))
    if not args:await bot.send_photo(chat_id=chat_id, caption='магаз у наташки', reply_markup=ikm, photo=photo_links_for_shop[0]); return
    img = InputMediaPhoto(caption='магаз у наташки', media=photo_links_for_shop[0], type='photo')
    await bot.edit_message_media(reply_markup=ikm, media=img, message_id=message_id, chat_id=chat_id)
    await bot.answer_callback_query(args[0])
tradeheroes = CallbackData('trher', 'tg_user_id')

tradeitems = CallbackData('tritm', 'tg_user_id')

del_callback = CallbackData('delcs', 'tg_user_id')



###############################################---menu's---###############################################
def make_inline_keyboard(row=3, *args):#передать инфу в формате n, (text, CallbackData, *args)
    return InlineKeyboardMarkup(row_width=row).add(*(InlineKeyboardButton(text=i[0],
                                callback_data=i[1].new(*i[2])) for i in args))
#использование
#tup = ((item_dick['farm'][i]['name'],tradeitems, (1,)) for i in item_dick['farm'])
#ikm = make_inline_keyboard(2, *tup)
#print(ikm)

###############################################---funks---###############################################
def rnum():
    return random.randint(0, len(enemy_click)-1)