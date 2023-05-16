import pymysql
from config import host, user, password, db_name
# from try_to_clone_main import bot, show_local_hero, del_callback, InlineKeyboardButton, InlineKeyboardMarkup
# from config import host, password,db_name,user
# from texts import hero_dick, item_dick, commands, new_reg_text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
import aiogram
from texts import *
try:
    connect = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
    )
    print(123)
except: print('ConnectionError')
cur = connect.cursor()

from config import token
bot = aiogram.Bot(token)
dis = aiogram.Dispatcher(bot)

show_local_hero = CallbackData('shmot_of_hero', 'local_hero_id',)
del_callback = CallbackData('del',)

def replace_items(new_item_name, tg_user_id):
    sql_code =f"SELECT items FROM players WHERE tg_id = {tg_user_id}"
    a = cur.execute(sql_code)
    items = cur.fetchone()[0].split()
    new_items = []
    for i in items:
        a = i.split('x')
        print(a)
        new_items.append([a[0], a[1]])

    new_str = ''
    for i in new_items:
        new_str+=f"{i[0]}x{i[1]} "
    print(new_str)
    return new_items

print(replace_items(1, 1664371560))

def give_item(tg_user_id, item_id_name):
    sql_code = f'SELECT id, item_name FROM items WHERE hero_id = {tg_user_id} AND item_name IS NULL'
    #это старая функция где я хотел заменять итем. Сейчас я хочу этой функцией просто выдать итем в инветарь
    a = cur.execute(sql_code)
    print(a)
    #if cur.execute(sql_code) == 0:#проверили все ли слоты пустые
    #    print('все слоты заняты')
    #    return
    items_id_name = cur.fetchall()
    print(items_id_name)
    replace_item = items_id_name[0][0]
    sql_code = f"UPDATE items SET item_name = {item_id_name} WHERE id = {replace_item}"
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


#print(cur)
async def starttttt(tg_user_id,chat_id ):
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
            await bot.send_message(text=new_reg_text, chat_id=chat_id)
            await bot.send_message(text='теперь ты зареган', chat_id=chat_id)
        except:
            await bot.send_message(text='админ пидор сломал всё', chat_id=chat_id)
    else: await bot.send_message(text=f'ты уже зареган, команды\n{commands}', chat_id=chat_id)
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
    sql_code = f'SELECT hero_id, hero_name FROM heroes WHERE tg_user_id = {tg_user_id}'
    print(sql_code)
    cur.execute(sql_code)
    #print(cur.fetchall())
    arrey_heroes = cur.fetchall()##[j for i in list(cur.fetchall()) for j in i]
    print(arrey_heroes, 'asdasd')
    print(len(arrey_heroes))
    h = InlineKeyboardMarkup(row_width=len(arrey_heroes))
    #print(len(arrey_heroes))
    #arrey_heroes[0]
    for j in range(len(arrey_heroes),):
        print(arrey_heroes[j][0])
        print(arrey_heroes[j][1])
        print(type(arrey_heroes[j][0]))
        try:
            h.add(InlineKeyboardButton(text=hero_dick[j]['name'], callback_data=show_local_hero.new(arrey_heroes[j][0], arrey_heroes[j][1])))
        except: print(111)
        h.add(InlineKeyboardButton(text='удалить', callback_data=del_callback.new()))
    await bot.send_message(text='вот твои герои', reply_markup=h, chat_id=chat_id)
