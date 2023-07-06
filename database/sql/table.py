from dataclasses import dataclass
 

@dataclass(slots=True, frozen=True, repr=False)
class SqlDataBase:
    create: str
    select: dict
    insert: str or None = None
    index: str or None = None # trigger functions procedures
    update: dict or None = None
    delete: str or None  = None
    test: str or None = None


users = SqlDataBase(
    create='''CREATE TABLE IF NOT EXISTS users(
    tg BIGINT NOT NULL PRIMARY KEY
    , balance NUMERIC(14,2) NOT NULL DEFAULT 0 
    , mmr SMALLINT NOT NULL DEFAULT 0  -- его рейтинг
    , daily_bonus BOOLEAN NOT NULL DEFAULT false -- получил ли ежедневный бонус
    , status BIT(3) NOT NULL DEFAULT b'000' -- привелегии есть/нет
    CONSTRAINT users_money_must_be_more_then_zero CHECK (balance >= 0)
    CONSTRAINT users_mmr_must_be_more_then_zero CHECK (mmr >= 0));
''',
    index=''' ''',
    select={
        'one': '''SELECT {} FROM users WHERE tg = $1;''',
        'rich': '''SELECT tg, balance FROM users ORDER BY (balance)LIMIT 10;''',
        'total_balance': '''SELECT sum(balance) FROM users;''',
        'bonus': '''SELECT count(tg) FROM users group by (bonus);''',
        'guild_balance': '''SELECT guild, sum(balance) FROM USERS GROUP BY (guild);''',
        },
    insert= '''INSERT INTO users (tg) VALUES ($1);''',
    
    test='''INSERT INTO users VALUES (1234567890, 123456789012.34, 312, false, b'010'), 
     (10987654321, 13, 30000, true, b'111'), (07123678123, 0, 0, false, b'000'),
    (109231254321, 9999999.99, 0, false, b'101'); ''',
    update= {
        'one': '''UDPATE USERS SET {} WHERE tg = $1;''',
        'event_for_everyone': '''UDPATE users SET {};''',
            }
    )

guild = SqlDataBase(create='''CREATE TABLE IF NOT EXISTS guild (
    name varchar (25) NOT NULL PRIMARY KEY
    , status BIT(3) NOT NULL DEFAULT b'000' -- привелегии
    , owner BIGINT NOT NULL 
        REFERENCES users(tg)
            ON UPDATE CASCADE
            ON DELETE RESTRICT -- чтобы при удалении аккаунта владельца гильдия не удалилась
    , mmr SMALLINT NOT NULL DEFAULT 0
    , balance NUMERIC(14,2) NOT NULL
    , black_list BIGINT[] NULL DEFAULT NULL -- если игрока выгнали из гильдии, а не он вышел по своей поле, то пользователь заносится в чёрный список чтобы он не зашёл ещё раз
	, CONSTRAINT guild_mmr_must_be_more_then_zero CHECK(mmr >= 0));
''',
    insert='''INSERT INTO guild (%s) VALUES (%s)''',
    index='''CREATE INDEX IF NOT EXISTS ON users (owner)''',
    select={},
    update={},
    )


users_info = SqlDataBase(
    create='''CREATE TABLE IF NOT EXISTS info_users(
    tg BIGINT NOT NULL PRIMARY KEY 
        REFERENCES users(tg)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    , main_img VARCHAR NULL DEFAULT NULL
    , main_nik VARCHAR(25) NOT NULL UNIQUE
    , referal BIGINT NOT NULL
        REFERENCES users(tg)
            ON DELETE CASCADE
            ON UPDATE SET NULL
    , visual_status BIT(3) NOT NULL DEFAULT b'000' 
    , guild VARCHAR NULL DEFAULT NULL -- клан, команда
        REFERENCES guild(name)
            ON DELETE CASCADE
            ON UPDATE SET DEFAULT);
            ''',
    index= '''CREATE INDEX IF NOT EXISTS info_users_referal_index ON info_users(referal);
              CREATE INDEX IF NOT EXISTS guild_info_users_index ON info_users(guild);''',
    insert='''INSERT INTO info_users (%s) VALUES (%s);''',
    update= {
        '''UDPATE info_users SET WHERE {};''', 
        },
    select={}
)

die_vinchik = SqlDataBase(
    create='''CREATE TABLE IF NOT EXISTS die_vinchik(
    tg BIGINT NOT NULL PRIMARY KEY 
        REFERENCES users(tg)
            ON DELETE CASCADE -- т.к. таблица полностью зависит от users (дополняет её)
            ON UPDATE CASCADE
    , name VARCHAR(25) NOT NULL
	, image VARCHAR NOT NULL
    , about_text TEXT NOT NULL 
    , status BIT(3) NOT NULL DEFAULT b'000' -- например есть ли возможность искать по тексту анкет
    , last_profiles BIGINT[] -- последние люди, которых пользователь пролистал, чтобы не показывать по 10 раз одно и то же
    , gender BOOLEAN NULL DEFAULT NULL -- мальчик девочка или NULL
    , age SMALLINT NOT NULL
    , wish_gender BOOLEAN NULL DEFAULT NULL -- кто интересует (мальчик девочка), нулл - все
    , quality SMALLINT NOT NULL  -- тут я попытаюсь оценить насколько человек хороший
    CONSTRAINT die_age_must_be_normal CHECK(age > 10 AND age < 100)
    CONSTRAINT die_quality_must_be_normal CHECK(quality >= -10 AND quality <= 10));''',
    index='''CREATE INDEX IF NOT EXISTS gender_finder ON die_vinchik(gender, age); -- потому что поиск всех анкет будет происходить по этим 2 параметрам, потом сортироваться по quality, но он будет достаточно часто менятья
             CREATE INDEX IF NOT EXISTS name_finder ON die_vinchik(die_name, age); -- пропустили анкету, неприятно, нажали поиск по именам, ввели нужное имя, ''',
    select={},
)

print(10<=100)
# bit (3)
# 1 - destroy items 
# 2 - make guild
# 3 - own commands


# 1 - castom image
# 2 - referal bonus
# 3 - longer nikname (25)
info_hero = SqlDataBase(
    create='''CREATE TABLE IF NOT EXISTS hero_info(
    id SMALLINT NOT NULL PRIMARY KEY -- в моей программе это "табельный номер", возможно поменяю на bit или чёто такое - всёранво обращаться по ключу и автозаполнение почти бессмысленно
    , name SMALLINT NOT NULL
    , price INT NOT NULL
    , start_exp SMALLINT NOT NULL  -- сколько опыта у героя базово
    , exp_by_lvl SMALLINT NOT NULL -- на сколько опыта больше за каждый уровень (для поднятия 2 лвл нужно +1000, для поднятия 3 +1100)
	, CONSTRAINT hero_already_exists UNIQUE (name)
    -- тут могут быть ещё параметры героя, к которым может быть нужно обратиться в самой базе данных. 
    -- Например с помощью price можно посчитать сколько у пользователя капитала в героях
    );
    ''',
    select={}
    )

info_items = SqlDataBase(
    create='''CREATE TABLE IF NOT EXISTS item_info(
    id SMALLSERIAL PRIMARY KEY -- табельный номер, есть связь с прогой
    , name VARCHAR NOT NULL
    , price NUMERIC(7, 2) NOT NULL -- максимум 99,999.99
    , CONSTRAINT item_already_exists UNIQUE (name));
      ''',
    select={}
)
hero = SqlDataBase(
    create='''CREATE TABLE IF NOT EXISTS hero (
    id SERIAL PRIMARY KEY
    , tg BIGINT NOT NULL 
        REFERENCES users(tg)
            ON UPDATE CASCADE
            ON DELETE CASCADE -- если пользователь, например забанен, то и герои у него существовать не должны
    , hero_id SMALLINT NOT NULL 
		REFERENCES hero_info(id)
			ON UPDATE CASCADE 
			ON DELETE CASCADE -- если герой удалён, то он не должен оставаться у кого-то, будут тригеры котороые компенсируюдт потерю в случае чего
    , activity TIMESTAMPTZ NULL DEFAULT now()
    , fight BOOLEAN NOT NULL DEFAULT NULL 
    , lvl SMALLINT NOT NULL 
    , exp SMALLINT NOT NULL 
    CONSTRAINT hero_lvl_control CHECK (lvl > 0 AND lvl <= 30));
    ''',
    select={
        'one': '''SELECT {} WHERE tg = $1 ''',
        },
    update={
        'lvlup': ''' ''',}
        ,
    )
hero_items = SqlDataBase(
    create='''CREATE TABLE IF NOT EXISTS hero_items(
    owner_hero INT NOT NULL 
        REFERENCES hero (id)
            ON DELETE CASCADE
    , item_id SMALLINT NOT NULL 
        REFERENCES item_info(id)
            ON UPDATE CASCADE -- при обновлении предметы тоже обновляются
            ON DELETE CASCADE -- при удалении предмет тоже удалиться, но будет тригер на удаление предметов, который выдаст компенсацию
    , item_quantity SMALLINT -- количество дубликатов
    , CONSTRAINT quantity_is_ziro CHECK (item_quantity > 0)
    , PRIMARY KEY (owner_hero, item_id));
    ''',
    select={}
)

user_items = SqlDataBase(
   create='''CREATE TABLE IF NOT EXISTS user_item(
    tg BIGINT NOT NULL
        REFERENCES users(tg)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    -- то он останется крутым навсегда, даже после выхода обновления т.к. обновление будет - новая версия предмета,
    , name VARCHAR NOT NULL
        REFERENCES item_info (name)
            ON UPDATE CASCADE
            ON DELETE CASCADE
    , quantity SMALLINT NOT NULL DEFAULT 1
    , CONSTRAINT counter CHECK (quantity > 0) -- должна удаляться если равна нулю
    , PRIMARY KEY (tg, name));
    ''', 
    select = {},
    index= '''CREATE INDEX IF NOT EXISTS telegrem ON uitems (tg)''',
)


chats = SqlDataBase(
    create='''CREATE TABLE IF NOT EXISTS chat(
    id BIGINT NOT NULL PRIMARY KEY
    , own BOOLEAN NOT NULL -- админ ли бот в беседе
    , name VARCHAR (25) NOT NULL
    , status BIT NOT NULL DEFAULT b'000'
    , img VARCHAR NULL DEFAULT NULL);
    ''',
    select={},
    update={},
    delete='''DROP FROM chat WHERE id=$1 LIMIT 1''',
    test="""INSERT INTO chat"""
)

### log
fight_heroes = SqlDataBase(
    create='''
    CREATE TABLE IF NOT EXISTS hero_fights
    fight_id INT NOT NULL 
    ''',
    select={}
)

fight_item = SqlDataBase(
    create='''''',
    select={},
)
fights = SqlDataBase(
    create='''CREATE TABLE IF NOT EXISTS fight (
    , fight_time TIMESTAMPTZ NOT NULL DEFAULT now()
    , first_user BIGINT NOT NULL
        REFERENCES users(tg)
            ON UPDATE CASCADE 
            ON DELETE RESTRICT не хочу чтобы история удалялась при удалении пользователя
    , first_hero BIT NOT NULL
    , first_items BIT[] NOT NULL
    , fgold SMALLINT NOT NULL DEFAULT 0
    , fexp SMALLINT NOT NULL DEFAULT 0
    , second_user BIGINT NOT NULL
        REFERENSEC users(tg)
            ON UPDATE CASCADE 
            ON DELETE RESTRICT
    , second_hero BIT NOT NULL
    , second_items BIT[] NOT NULL
    , second_gold SMALLINT NOT NULL DEFAULT 0
    , sexp SMALLINT NOT NULL DEFAULT 0
    , result BOOLEAN NOT NULL -- результат драки
    );''',
    update={},
    select={
        '''SELECT''',
        },
    test = ''' ''',
    )
guild_log = SqlDataBase(
    create='''CREATE TABLE IF NOT EXISTS guild_log(
    id smallserial NOT NULL
        REFERENCES guild(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    ,tg BIGINT NULL DEFAULT NULL
        REFERENCES users(tg)
            ON DELETE CASCADE 
            ON UPDATE CASCADE
    , join BOOLEAN NOT NULL
    , kicked OOLEAN NOT NULL
    , operation_time TIMESTAMPTZ NOT NULL DEFAULT now()
    PRIMARY KEY (id, tg, operation_time)
    ); ''',
    select = {},
    update=None,
    insert='',
    test= ''
)

money_log = SqlDataBase(
    create='''CREATE TABLE IF NOT EXISTS money_log (
    tg BIGINT NOT NULL
        REFERENCES users(tg)
                ON DELETE CASCADE
                ON UPDATE CASCADE
    , change numeric(14,2) NOT NULL
    , result numeric(14,2) NOT NULL
    , transaction_time TIMESTAMPTZ NOT NULL DEFAULT now()
    , description VARCHAR NULL DEFAULT NULL
    , PRIMARY KEY (tg, transaction_time));''',
    index='''CREATE INDEX IF NOT EXISTS''',
    select = {},
    update=None ,
)
