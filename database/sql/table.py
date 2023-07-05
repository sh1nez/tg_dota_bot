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
    , mmr SMALLINT NOT NULL DEFAULT 0  -- rating
    , bonus BOOLEAN NOT NULL DEFAULT false -- daily bonus (got or no)
    , status BIT(3) NOT NULL DEFAULT b'000' 
    CONSTRAINT money_counter CHECK (balance >= 0)
    CONSTRAINT mmr_counter CHECK (mmr >= 0));''',
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
    id SMALLSERIAL NOT NULL PRIMARY KEY
    , name varchar (25) NOT NULL UNIQUE
    , status BIT(3) NOT NULL DEFAULT b'000'
    , owner BIGINT NOT NULL 
        REFERENCES users(tg)
            ON UPDATE CASCADE
            ON DELETE RESTRICT
    , mmr SMALLINT NOT NULL CONSTRAINT CHECH(mmr>0) DEFAULT 0
    , money NUMERIC(14,2) NOT NULL CHECK(money >= 0)
    , black_list BIGINT[] NULL DEFAULT NULL);''',
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
    , img VARCHAR NULL DEFAULT NULL
    , nik VARCHAR(25) NOT NULL UNIQUE
    , referal BIGINT NOT NULL
        REFERENCES users(tg)
            ON DELETE CASCADE
            On UPDATE CASCADE
    , status BIT(3) NOT NULL DEFAULT b'000'
    , guild SMALLSERIAL NULL DEFAULT NULL
        REFERENCES guild(id)
            ON DELETE CASCADE
            ON UPDATE SET DEFAULT);''',
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
            ON DELETE CASCADE
            ON UPDATE CASCADE
    , die_image VARCHAR NOT NULL
    , die_text TEXT(500) NOT NULL 
    , die_status BIT(3) NOT NULL DEFAULT b'000' -- например есть ли возможность искать по тексту анкет
    , last_profiles BIGINT[] -- последние люди, которых пользователь пролистал, чтобы не показывать по 10 раз одно и то же
    , gender BOOLEAN NULL DEFAULT NULL -- мальчик девочка или NULL
    , age SMALLINT NOT NULL
    , quality SMALLINT NOT NULL D  -- тут я попытаюсь оценить насколько человек хороший
    CONSTRAINT die_age_must_be_normal CHECK(age > 10 AND age < 100)
    CONSTRAINT die_quality_must_be_normal CHECK(quality >= -10 AND quality <= 10)
    );''',
    select={}
)

print(10<=100)
# bit (3)
# 1 - destroy items 
# 2 - make guild
# 3 - own commands


# 1 - castom image
# 2 - referal bonus
# 3 - longer nikname (25)

hero = SqlDataBase(
    create='''CREATE TABLE IF NOT EXISTS hero (
    tg BIGINT NOT NULL PRIMARY KEY
        REFERENCES users(tg)
            ON DELETE CASCADE
            ON DELETE CASCADE
    , name BIT NOT NULL
    , activity TIMESTAMPTZ NULL DEFAULT now()
    , fight BOOLEAN NOT NULL DEFAULT NULL
    , lvl SMALLINT NOT NULL DEAULT 1
    , exp SMALLINT NOT NULL DEFAULT 0
    , items bit[] NULL DEFAULT NULL
    CONSTRAINT arrey_len CHECK (array_length(items) <= 6));''',
    select={
        'one': '''SELECT {} WHERE tg = $1 ''',
        },
    update={
        'lvlup': ''' ''',}
        ,
    )


user_items = SqlDataBase(
   create=''' CREATE TABLE IF NOT EXISTS uitem(
    tg BIGINT NOT NULL
        REFERENCES users(tg)
            ON DELETE CASCADE
            ON UDPATE CASCADE
    , name BIT NOT NULL
    , count SMALLINT NOT NULL DEFAULT 1
    CONSTRAINT counter CHECK (count > 0)
    PRIMARY KEY (tg, name));''', 
    select = {},
    other_for_create= '''CREATE INDEX IF NOT EXISTS telegrem ON uitems (tg)''',
)


chats = SqlDataBase(
    create='''CREATE TABLE IF NOT EXISTS chat(
    id BIGINT NOT NULL PRIMARY KEY, 
    , own BOOLEAN NOT NULL
    , name VARCHAR (25) NOT NULL,
    , status BIT NOT NULL DEFAULT b'000'
    , img VARCHAR NULL DEFAULT NULL, 
    , users BIGINT[] NOT NULL);''',
    select={},
    update={},
    delete='''DROP FROM chat WHERE id=$1 LIMIT 1''',
    test="""INSERT INTO chat"""
)

### log
fights = SqlDataBase(
    create='''CREATE TABLE IF NOT EXISTS fight (
    time TIMESTAMPTZ NOT NULL DEFAULT now()
    , fuser BIGINT NOT NULL
        REFERENSEC users(tg)
            ON UPDATE CASCADE 
            ON DELETE RESTRICT
        USING HASH
    , fhero BIT NOT NULL
    , flvl SMALLINT NOT NULL
    , fitems BIT[] NOT NULL
    , fgold SMALLINT NOT NULL DEFAULT 0
    , fexp SMALLINT NOT NULL DEFAULT 0
    , suser BIGINT NOT NULL
        REFERENSEC users(tg)
            ON UPDATE CASCADE 
            ON DELETE RESTRICT
    , shero BIT NOT NULL
    , slvl SMALLINT NOT NULL
    , sitems BIT[] NOT NULL
    , sgold SMALLINT NOT NULL DEFAULT 0
    , sexp SMALLINT NOT NULL DEFAULT 0
    , result BOOLEAN NOT NULL);''',
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
