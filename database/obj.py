# import asyncpg

from configparser import ConfigParser
# import asyncio


# settings 
# pwd pisapopa
# user aivan


config = ConfigParser()
config.read('config.cfg')
user = config['database']['user']
pwd = config['database']['password']
host = config['database']['host']
port = config['database']['port']

print(user, pwd, host, port)



class Database:
    __pool = None

    def __new__(cls, *args, **kwargs):
        if not cls.__pool:
            cls.__pool = asyncio.run(cls.connect())
            print('not')
        else:
            print('yyeye')
            return cls.__pool

    @staticmethod
    async def connect():
        __link = f"postgres://{user}:{password}@{host}:{port}/{db_name}"
        return await asyncpg.create_pool(dsn=__link, min_size=3,  max_size=15,)

    async def execute(self, sql, *args):
        async with self.__pool.acquire() as conn:
            await conn.execute(sql, *args)

    async def select(self, sql, *args):
        async with self.__pool.acquire() as conn:
            return await conn.fetch(sql, *args)


