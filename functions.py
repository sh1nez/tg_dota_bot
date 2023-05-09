from config import *
import pymysql
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
