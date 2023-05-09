import aiogram
from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import pymysql
import datetime
import asyncio
from texts import *
from functions import *
from config import token, host, user, password, db_name
print('я начал')
bot = aiogram.Bot(token)
dis = aiogram.Dispatcher(bot)
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

@dis.message_handler(commands=['start'])#прост отвечает
async def start(message: aiogram.types):
    tg_user_id = message.from_user.id
    #sql_code =f"CREATE TABLE `{db_name}` .`players`  ENGINE = InnoDB;"
    sql_code = f"SELECT tg_id from players WHERE tg_id = {tg_user_id}"
    cur.execute(sql_code)
    result = list(cur.fetchall())
    bb = [j for i in result for j in i]
    #проверил есть ли пользователь. Если есть
    if not bb:
        await message.answer(text=new_reg_text)
        try:
            #create_player
            sql_code = f"INSERT INTO `players` (`tg_id`, `money`) VALUES ('{tg_user_id}', '0')"
            print(sql_code)
            cur.execute(sql_code)
            local_user_id = connect.insert_id()
            connect.commit()
            hero_id = 0
            hero_lvl = 0
            new_hero_id = create_hero(local_user_id, hero_id, hero_lvl)
            print(new_hero_id)
            for i in range(6):
                create_slot(new_hero_id)
            await message.answer(text=f'теперь ты зареган \n{commands}')
        except:
            await message.answer(text=f'админ пидорас сломал всё')
    else:
        await message.answer(text=f'{reg_text} {commands}')


@dis.message_handler(commands=['gold'])#прост отвечает
async def gold(message):
    tg_user_id = message.from_user.id
    sql_code = f'SELECT tg_id FROM players WHERE tg_id = {tg_user_id}'
    print(sql_code)
    cur.execute(sql_code)  #если написать равно, то вернёт количество совпадений как я понял
    result =  [j for i in list(cur.fetchall()) for j in i]
    connect.commit()
    print(result)
    if result:
        return_to_user = update_gold(tg_user_id, plus_money=100)
        await message.answer(text=f'теперь голды {return_to_user}')
    else: await message.answer(text='сначала зарегестрируйся')

@dis.message_handler(commands=['profile'])
async def gold(message):
    tg_user_id = message.from_user.id
    sql_code = f'SELECT money, status FROM players WHERE tg_id = {tg_user_id}'
    print(sql_code)
    cur.execute(sql_code)
    result =  [j for i in list(cur.fetchall()) for j in i]
    await message.answer(text=f'{result}')










if __name__ == '__main__':
    aiogram.executor.start_polling(dis, )#skip_updates=True
