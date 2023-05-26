import datetime
import pymysql
from config import *
import aiogram
from texts import *
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
from dota import LocalHero

heroes_sql = """CREATE TABLE IF NOT EXISTS `test_bot`.`heroes` (`id` INT NOT NULL AUTO_INCREMENT ,`tg_id` CHAR(11) , `hero_name` INT NOT NULL ,`lvl` INT NOT NULL ,`exp` INT NOT NULL ,`farm_time` DATETIME NULL ,`fight_time` DATETIME NULL ,PRIMARY KEY (`id`)) ENGINE = InnoDB;"""
profile_items_sql = """CREATE TABLE IF NOT EXISTS `test_bot`.`profile_items` ( `id` INT NOT NULL AUTO_INCREMENT , `tg_id` VARCHAR(11) NOT NULL , `item_name` INT NOT NULL , `count` INT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;"""
hero_items_sql = """CREATE TABLE IF NOT EXISTS `test_bot`.`hero_items` (`id` INT NOT NULL AUTO_INCREMENT ,`hero_id` INT NOT NULL ,`item_name` INT NOT NULL ,PRIMARY KEY (`id`)) ENGINE = InnoDB;"""
players_sql = """CREATE TABLE IF NOT EXISTS `test_bot`.`players` ( `id` INT NOT NULL AUTO_INCREMENT , `tg_id` CHAR(11) NOT NULL , `money` INT NOT NULL , `status` INT NULL DEFAULT NULL , `nick` CHAR(20) NULL DEFAULT NULL , `bg` TINYINT NULL DEFAULT NULL , `bonus` BOOLEAN NOT NULL, PRIMARY KEY (`id`)) ENGINE = InnoDB;"""
items_sql = """CREATE TABLE IF NOT EXISTS `test_bot`.`items` ( `id` MEDIUMINT NOT NULL AUTO_INCREMENT , `hero_id` MEDIUMINT NULL DEFAULT NULL , `tg_user_id` VARCHAR(15) NOT NULL , `item_name` TINYINT NOT NULL , `count` TINYINT(4) NULL DEFAULT NULL, PRIMARY KEY (`id`)) ENGINE = InnoDB;"""
'''##############################################---BASE---################################################'''


class Connect:
    def __init__(self):
        self.conn = pymysql.connect(host=host, port=3306, user=user, password=password, database=db_name,)

    def update_insert_del(self, sql_code,):
        self.conn.ping()
        with self.conn.cursor() as cur:
            # print(sql_code)
            cur.execute(sql_code)
            self.conn.commit()

    def select_one(self, sql_code):
        # print(sql_code)
        self.conn.ping()
        with self.conn.cursor() as cur:
            if cur.execute(sql_code):
                return cur.fetchone()
            return False

    def select_all(self, sql_code):
        # print(sql_code)
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


connection = Connect()
connection.make_many(heroes_sql, items_sql, profile_items_sql, hero_items_sql, players_sql)
print('я начал')

bot = aiogram.Bot(token)
dis = aiogram.Dispatcher(bot)


'''##############################################---PROFILE---###############################################'''


def find_nowear_items(tg_id):
    sql_code = f"SELECT id, item_name, count FROM profile_items WHERE tg_id = {tg_id}"
    items = connection.select_all(sql_code)
    return items


def find_wear_items(hero_id):
    sql_code = f"SELECT id, item_name FROM hero_items WHERE hero_id = {hero_id}"
    return connection.select_all(sql_code)


def make_text_inventory(items: tuple, *args):  # итемы в формате (хуйня, индекс, количество)
    text = str(args[0]) if args else ''
    for i in items:
        text += f"{all_items[i[1]].name} - {i[2]}шт\n"
    return text


def find_info_all_heroes(tg_id):
    sql_code = f"SELECT lvl, hero_name, farm_time, fight_time FROM heroes WHERE tg_id = {tg_id}"
    # мейби ещё ввести чтобы было видно кулдаун на фарм и другие вещи
    heroes = connection.select_all(sql_code)
    return heroes


def find_id_name_all_heroes(tg_id):
    sql_code = f"SELECT hero_name FROM heroes WHERE tg_id = {tg_id}"
    return connection.select_all(sql_code)


def check_time_farm(tg_id, hero_id):  # тру равно свободен
    sql_code = f"SELECT farm_time, fight_time FROM heroes WHERE tg_id = {tg_id} AND hero_name = {hero_id}"
    t1 = connection.select_one(sql_code)[0]
    if not t1:
        return True
    t2 = datetime.datetime.today().replace(microsecond=0)
    dt = (t2-t1).total_seconds()
    return True if dt > 3600 else False


def wear_item_on_hero(tg_id, hero_id, item_name,):
    # нужно отнять 1 от count и создать новый слот
    sql_code = f"SELECT count, id FROM profile_items WHERE item_name = {item_name} AND tg_id = {tg_id}"
    count, item_id = connection.select_one(sql_code)
    if not count:
        return Exception
    if count == 1:
        sql_code1 = f"DELETE FROM profile_items WHERE id = {item_id}"
    else:
        sql_code1 = f"UPDATE profile_items SET count = {count-1} WHERE id = {item_id}"
    sql_code2 = f"INSERT INTO hero_items (hero_id, item_name) VALUES ('{hero_id}', '{item_name}')"
    connection.make_many(sql_code1, sql_code2)


def snat_s_geroya_v_invantar(item_id, tg_id, hero_id):
    sql_code = f'UPDATE profile_items SET hero_id = NULL WHERE item_name = {item_id} AND tg_id = {tg_id} ' \
               f'AND hero_id = {hero_id}'
    connection.update_insert_del(sql_code)


"""###############################################---SHOP---###############################################"""


"""###############################################---BUY/SELL---#############################################"""


def buy_hero(tg_id, hero_id, price):
    money = money_of_user(tg_id)
    sql_code1 = f"UPDATE players SET money = {money - price} WHERE tg_id = {tg_id}"
    sql_code2 = f"INSERT INTO heroes (`tg_id`, `hero_name`, `lvl`, `exp` ) VALUES ('{tg_id}', '{hero_id}'," \
                f" '1', '0');"
    connection.make_many(sql_code1, sql_code2)


def buy_item_user(tg_id, item_id, price: int, count=1):
    sql_code1 = f"UPDATE players SET money = money - {price} WHERE tg_id = {tg_id}"
    value = connection.select_one(f"SELECT count FROM profile_items WHERE tg_id = {tg_id} and item_name = {item_id}")
    if value:
        sql_code2 = f'UPDATE profile_items SET count = {value[0]+count} WHERE tg_id = {tg_id} and item_name = {item_id}'
    else:
        sql_code2 = f"INSERT INTO profile_items (tg_id, item_name, count) VALUES ('{tg_id}', {item_id}, '{count}')"
    connection.make_many(sql_code1, sql_code2)


def create_hero(tg_id, hero_id):
    sql_code = f"INSERT INTO heroes (`tg_id`, `hero_name`, `lvl`, `exp` ) VALUES " \
                f"('{tg_id}', '{hero_id}', '1', '0');"
    connection.insert_id(sql_code)


def send_hero_fight(tg_id, hero_id,):
    t = datetime.datetime.today().replace(microsecond=0)
    sql_code = f"SELECT id, tg_id, hero_name FROM heroes WHERE fight_time IS NOT NULL"
    tup = connection.select_one(sql_code)
    print(tup) # id, tg_id, type
    if not tup:
        sql_code = f"UPDATE heroes SET fight_time = '{t}' WHERE tg_id = {tg_id} AND hero_name = {hero_id}"
        # print(sql_code)
        connection.update_insert_del(sql_code)
        return False  # значит нет врагов герой отправлен искать fight
    sql_code = f"UPDATE heroes SET fight_time = NULL WHERE id = {tup[0]}"
    connection.update_insert_del(sql_code)
    return tup  # значит герой нашёл противника


def check_fight():  # hero_id
    pass


def send_hero_farm_func(tg_id, hero_id, time):  # hero_id
    sql_code = f"UPDATE heroes SET farm_time = '{time}' WHERE tg_id = {tg_id} AND hero_name = {hero_id}"
    connection.update_insert_del(sql_code)


def send_hero_fight_func(tg_id, hero_id, time):  # hero_id
    sql_code = f"UPDATE heroes SET fight_time = '{time}' WHERE tg_id = {tg_id} AND hero_name = {hero_id}"
    connection.update_insert_del(sql_code)


def hero_back_farm_func(tg_id, hero_id):
    sql_code = f"UPDATE heroes SET farm_time = NULL WHERE tg_id = {tg_id} AND hero_name = {hero_id}"
    connection.update_insert_del(sql_code)


def hero_back_fight_funk(tg_id, hero_id):  # hero_id
    sql_code = f"UPDATE heroes SET fight_time = NULL WHERE tg_id = {tg_id} AND hero_name = {hero_id}"
    connection.update_insert_del(sql_code)

'''#############################################---menu's---###############################################'''


def make_inline_keyboard(*args, row=3, ikm=None,):
    # передать инфу в формате n, (text, CallbackData, *args)
    b = (InlineKeyboardButton(text=i[0], callback_data=i[1].new(*i[2])) for i in args)
    if ikm:
        # если у нас уже была кнопка, значит к тому что дано нужно добавить
        return ikm.add(*b)

    # если ни хрена не дано, то просто верни добавив кнопки
    else:
        return InlineKeyboardMarkup(row_width=row).add(*b)


'''#############################################---funks---###############################################'''


def pvp(hero_id1: int, lvl1: int, items1: tuple or None, hero_id2: int, lvl2: int, items2: tuple[ShopItem] or None):
    """(pvp(hero_id1=0, lvl1=10, items1=None, hero_id2=1, lvl2=10, items2=None))"""
    hp1, farm1, fiz_dmg1, mag_dmg1, buffs1 = hero_dick[hero_id1].lvlup_hero(lvl1)
    hero1 = LocalHero(*hp1, *farm1, fiz_dmg1, mag_dmg1, *buffs1)
    if not items1:
        local_hero1 = hero1.no_items()
    else:
        local_hero1 = hero1.__dict__
        for i in items1:
            local_hero1 *= all_items[i[1]]

    hp2, farm2, fiz_dmg2, mag_dmg2, buffs2 = hero_dick[hero_id2].lvlup_hero(lvl2)
    hero2 = LocalHero(*hp2, *farm2, fiz_dmg2, mag_dmg2, *buffs2)
    if not items2:
        local_hero2 = hero2.no_items()
    else:
        local_hero2 = hero2.__dict__
        for i in items2:
            local_hero2 *= all_items[i[1]]
    print(local_hero1)
    print(local_hero2)
    return hero1.battle(local_hero1, local_hero2)


def rnum():
    return random.randint(0, len(enemy_click)-1)


def r_cbd(callback):
    return int(callback.split(':')[1]) if len(callback.split(':')) == 2 else map(int, callback.split(':')[1:])


def check_hero_user(tg_id, hero_id):
    sql_code = f"SELECT id FROM heroes WHERE tg_id = {tg_id} AND hero_name = {hero_id}"
    return True if connection.select_one(sql_code) else False


def money_of_user(tg_id):
    sql_code = f"SELECT money FROM players WHERE tg_id = {tg_id}"
    a = connection.select_one(sql_code)
    return False if a is False else a[0]


def update_money(tg_id, money):
    sql_code = f"UPDATE players SET money = money + {money} WHERE tg_id = {tg_id}"
    connection.update_insert_del(sql_code)


def text_time(t: datetime.datetime):
    if not t:
        return '- готов\n'
    s = 3600-(datetime.datetime.today().replace(microsecond=0) - t).total_seconds()
    if s <= 0:
        return ' - готов\n'
    text = '- '
    if s >= 3600:
        text += f'{int(s//3600)} часов '
        s %= 3600
    if s >= 60:
        text += f"{int(s//60)} мин "
        s %= 60
    text += f"{int(s)} сек\n"
    return text


def select_lvl(hero_id):
    sql_code = f"SELECT lvl FROM heroes WHERE id = {hero_id}"
    return connection.select_one(sql_code)[0]


def chek_bp(tg_id):
    sql_code = f"SELECT status FROM players WHERE tg_id = {tg_id}"
    a = connection.select_one(sql_code)[0]
    return a if a else False


def check_bonus(tg_id) -> bool:
    sql_code = f"SELECT bonus FROM players WHERE tg_id = {tg_id}"
    a = connection.select_one(sql_code)[0]
    print(a)
    if not a:
        sql_code1 = f"UPDATE players SET bonus = 1 WHERE tg_id = {tg_id}"
        sql_code2 = f"UPDATE players SET money = money+100 WHERE tg_id = {tg_id}"
        connection.make_many(sql_code1, sql_code2)
        return True
    return False


def find_hero_id_by_name_tg(tg_id, hero_name):
    sql_code = f"SELECT id FROM heroes WHERE tg_id = {tg_id} AND hero_name = {hero_name}"
    return connection.select_one(sql_code)[0]


def select_name_by_id(hero_id):
    sql_code = f"SELECT hero_name FROM heroes WHERE id = {hero_id}"
    return connection.select_one(sql_code)[0]


def reg_user(tg_id):
    sql_code = f"SELECT tg_id from players WHERE tg_id = {tg_id}"
    return True if connection.select_one(sql_code) else False


def clean_bonus():
    sql_code = f"UPDATE players SET bonus = NULL"
    connection.update_insert_del(sql_code)
