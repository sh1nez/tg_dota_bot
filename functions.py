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
