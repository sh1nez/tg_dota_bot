import psycopg2
from config import db_name, password, user, host

'''@dataclass
class CreateDb:
    heroes_sql: str
    profile_items: str
    hero_items: str
    players: str
'''
heroes_sql = """CREATE TABLE IF NOT EXISTS `yuralehl_dota`.`heroes` (`id` INT NOT NULL AUTO_INCREMENT ,`tg_id` CHAR(11), 
`hero_name` INT NOT NULL ,`lvl` INT NOT NULL ,`exp` INT NOT NULL ,`time` DATETIME NULL ,
`fight` BOOLEAN NULL DEFAULT NULL, PRIMARY KEY (`id`)) ENGINE = InnoDB;"""

profile_items_sql = """CREATE TABLE IF NOT EXISTS `yuralehl_dota`.`profile_items` ( `id` INT NOT NULL AUTO_INCREMENT ,
`tg_id` VARCHAR(11) NOT NULL , `item_name` INT NOT NULL , `count` INT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;"""
hero_items_sql = """CREATE TABLE IF NOT EXISTS `yuralehl_dota`.`hero_items` (`id` INT NOT NULL AUTO_INCREMENT ,
 `hero_id` INT NOT NULL ,`item_name` INT NOT NULL ,PRIMARY KEY (`id`)) ENGINE = InnoDB;"""
players_sql = """CREATE TABLE IF NOT EXISTS `yuralehl_dota`.`players` ( `id` INT NOT NULL AUTO_INCREMENT , 
`tg_id` CHAR(11) NOT NULL , `money` INT NOT NULL , `mmr` INT NOT NULL DEFAULT '0', `status` INT NULL DEFAULT NULL ,
`nick` CHAR(20) NULL DEFAULT NULL , `bg` TINYINT NULL DEFAULT NULL , `bonus` BOOLEAN NULL DEFAULT NULL , PRIMARY KEY (`id`))
  ENGINE = InnoDB;"""

com = (
    """CREATE TABLE IF NOT EXISTS cool_test(
    "time" timestamp without time zone,
    "num1" 
    "num1"
    );
    """,
)
conn = psycopg2.connect(database='postgres', user='postgres', password='pisapopa', host='localhost', port=5432)
with conn.cursor() as asd:
    asd.execute('''CREATE TABLE IF NOT EXISTS weather (
        city            varchar(80),
        temp_lo         int,           -- low temperature
        temp_hi         int,           -- high temperature
        prcp            real,          -- precipitation
        date            date
    );''')
    conn.commit()
# with conn.cursor() as asd:
#     sql2 = '''INSERT INTO weather(
#       city, temp_lo, temp_hi, prcp, date)
#       VALUES(
#        'San Francisco', 43, 57, 0.0, '1994-11-29');'''
#     asd.execute(sql2)
#     conn.commit()

with conn.cursor() as asd:
    sql = '''SELECT * from weather'''
    asd.execute(sql)
    print(asd.fetchall())
way = r'C:\prog\data_test.txt'
with conn.cursor() as asd:
    sql = f'''COPY (select city from weather)
    TO '{way}';'''
    asd.execute(sql)
"""
class Database:
    def __init__(self):  # pisapopa
        self.__conn = 
        with self.__conn.cursor() as cur:
            cur.execute(com[0])
            print('execute')


    #@classmethod
    #def select_lvl(cls)
    #    with cls.__conn.cursor()
asd = Database()
"""
print('end')


