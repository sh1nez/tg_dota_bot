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
    """CREATE TABLE IF NOT EXISTS players(
    id integer serial PRIMARY KEY,
    "time" timestamp without time zone
    );
    """,
)
print(com[0])

class Database:
    def __init__(self):
        self.__conn = psycopg2.connect(database='test', user='127.0.0.1', password='pisapopa', host='5432')
        with self.__conn.cursor() as cur:

            cur.execute(com[0])
            #for i in com:
            #    cur.execute(i)


    #@classmethod
    #def select_lvl(cls)
    #    with cls.__conn.cursor()



asd = Database()


