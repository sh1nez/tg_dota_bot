from config import *
import pymysql
import aiogram
from texts import *
import random
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from try_to_clone_main import del_callback, dis, bot


try:
    connect = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
    )
except: print('ConnectionError')

cur = connect.cursor()



def give_item(hero_id, item_id):
    sql_code = f'SELECT id, item_name FROM items WHERE hero_id = {hero_id} AND item_name IS NULL'
    a = cur.execute(sql_code)
    print(a)
    if cur.execute(sql_code) == 0:
        print('все слоты заняты')
        return
    items_id_name = cur.fetchall()
    print(items_id_name)
    replace_item = items_id_name[0][0]
    sql_code = f"UPDATE items SET item_name = {item_id} WHERE id = {replace_item}"
    print(sql_code)
    cur.execute(sql_code)
    connect.commit()
    #item_names = [i[1] for i in items_id_name]
    #for i in range(len(item_names)):
    #    item_names[i] = 123
    # pustie_sloti = item_names.count(None)
    # if pustie_sloti==0:
    #     return False
    # else:
    #     #сейчас мне нужно сделать название первого попавшегося итема с хиро нейм не равно 0
    #     print(item_names)
    #print(not item_names)

    #for i in items_id_name:
    #    print(i)

#give_item(2, 1)

#print(cur)
def starttttt(tg_user_id):
    sql_code = f"SELECT tg_id from players WHERE tg_id = {tg_user_id}"
    cur.execute(sql_code)
    result = list(cur.fetchall())
    bb = [j for i in result for j in i]
    print(bb)
    #connect.commit()
    #проверил есть ли пользователь. Если есть
    if not bb:
        try:
            #create_player
            sql_code = f"INSERT INTO `players` (`tg_id`, `money`) VALUES ('{tg_user_id}', '0')"
            print(sql_code)
            cur.execute(sql_code)
            print(12)
            local_user_id = connect.insert_id()
            connect.commit()
            hero_id = 0
            hero_lvl = 0
            print(123)
            new_hero_id = create_hero(tg_user_id=tg_user_id, local_user_id=local_user_id, name_hero_id=hero_id)
            print(new_hero_id)
            for i in range(6):
                create_slot(new_hero_id, local_user_id=local_user_id)

        except:
            print('ты пидр ёпта')
#ran_num = random.randint(1,999999)
#starttttt(ran_num)

def make_user_lv(tg_user_id, text, image):
    sql_code = f"SELECT tg_id from players WHERE tg_id = {tg_user_id}"
    cur.execute(sql_code)
    result = cur.fetchone()
    #bb = [j for i in result for j in i]
    print(result)
    # connect.commit()
    # проверил есть ли пользователь. Если есть
    if not result:
        create_lepnardo_user(tg_user_id=tg_user_id, txt=f'{text}', image=f'{image}')
        print('cool')
    else: print('rdy')
#print(f'{"ahsdhkasd"}')
#make_user_lv(ran_num, 'asdasdasdasdasd', 'url')
#INSERT INTO `leonardo` (`
# id`, `tg_id`, `text`, `image`)
# VALUES (NULL, '113123', 'adasd sdgfoisdoi u234gsd hjgsdfkg kjsdgf', 'sdsbhdfhkdkfksdf')

def buyer_items(price, item_id, hero_id):

    sql_update = 'UPDATE '


def create_lepnardo_user(tg_user_id, txt, image):
    sql_code = f"INSERT INTO leonardo (tg_id, text, image) VALUES ('{tg_user_id}', '{txt}', '{image}')"
    print(sql_code)
    cur.execute(sql_code)
    connect.commit()
    print('1111')


def create_slot(hero_id, local_user_id):
    sql_code = f"INSERT INTO items (`hero_id`, `player_id`, `item_name`) VALUES ('{hero_id}', {local_user_id} , NULL);"
    print(sql_code)
    cur.execute(sql_code)
    connect.commit()
def create_hero(local_user_id, tg_user_id, name_hero_id):
    sql_code = f"INSERT INTO heroes ( `tg_user_id`, `local_user_id`,  `hero_name`, `hero_lvl`) VALUES ('{tg_user_id}'," \
               f" '{local_user_id}', '{name_hero_id}', '1');"
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
    sql_code = f'SELECT local_user_id, hero_name FROM heroes WHERE tg_user_id = {tg_user_id}'
    print(sql_code)
    cur.execute(sql_code)
    arrey_heroes = [j for i in list(cur.fetchall()) for j in i]
    print(arrey_heroes, 'asdasd')
    h = InlineKeyboardMarkup(row_width=len(arrey_heroes) // 2)
    for j in range(0, len(arrey_heroes)//2, ):
        print(j)
        try:
            h.add(InlineKeyboardButton(text=hero_dick[j]['name'], callback_data=f'hero'))
        except: print(111)
    h.add(InlineKeyboardButton(text='удалить', callback_data=del_callback.new()))
    await bot.send_message(text='вот твои герои', reply_markup=h, chat_id=chat_id)

