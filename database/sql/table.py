from dataclasses import dataclass

@dataclass(slots=True, frozen=True, repr=False, )
class SqlDataBase:
    create: str
    select: dict
    insert: str
    other_for_create: list or None = None # trigger functions procedures
    update: dict or None = None
    delete: dict or None  = None
    test: str or None = None

users = SqlDataBase(
    create=''''CREATE TABLE IF NOT EXISTS users(
    tg BIGINT NOT NULL PRIMARY KEY
    , money NUMERIC(14,2) NOT NULL DEFAULT 0 --12 before 2 after
    , mmr SMALLINT NOT NULL DEFAULT 0 
    , bonus BOOLEAN NOT NULL DEFAULT false
    , status BIT(3) NOT NULL DEFAULT b'000'
    CONSTRAINT money_counter CHECK (money >= 0)
    CONSTRAINT mmr_counter CHECK (mmr >= 0));
    ''',
    select={
        'one': '''SELECT {} FROM users WHERE tg = $1;''',
        'rich': '''SELECT tg, money FROM users ORDER BY (money)LIMIT 10;''',
        'all_money': '''SELECT sum(money) FROM users;''',
        'bonus': '''SELECT count(tg) FROM users group by (bonus);''',
        'guild_balance': '''SELECT guild, sum(money) FROM USERS GROUP BY (guild);''',
        },
    insert= '''INSERT INTO users (tg) VALUES ($1)''',
    other_for_create='''CREATE INDEX IF NOT EXISTS users_guild''',    
    test = '''INSERT INTO users VALUES (1234567890, 123456789012.34, 312, false, b'010', 12), 
     (10987654321, 13, 30000, true, b'111', 12), (07123678123, 0, 0, false, b'000', 11),
    (109231254321, 9999999.99, 0, false, b'101', 0); ''',
    )

print(users.create)
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
    other_for_create= '''CREATE INDEX IF NOT EXISTS info_users_referal_index ON info_users(referal);
                         CREATE INDEX IF NOT EXISTS guild_info_users_index ON info_users(guild);''',
    insert='''INSERT INTO info_users (%s) VALUES (%s)''',
    update='''UDPATE info_users SET WHERE {}''',
    select={}
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
    , black_list BIGINT[] NULL DEFAULT NULL
    );''',
    insert='''INSERT INTO guild (%s) VALUES (%s)''',
    other_for_create='''CREATE INDEX IF NOT EXISTS ON users (owner)''',
    select={}
    )

# bit (3)
# 1 - destroy items 
# 2 - make guild
# 3 - own commands


# 1 - castom image
# 2 - referal bonus
# 3 - longer nikname (25)


hero = '''CREATE TABLE IF NOT EXISTS hero (
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
    CONSTRAINT arrey_len CHECK (array_length(items) <= 6)
);
'''

uitems = ''' CREATE TABLE IF NOT EXISTS uitem
(
    tg BIGINT NOT NULL
        REFERENCES users(tg)
            ON DELETE CASCADE
            ON UDPATE CASCADE
    , name BIT NOT NULL
    , count SMALLINT NOT NULL DEFAULT 1
    CONSTRAINT counter CHECK (count > 0)
    PRIMARY KEY (tg, name)
);
CREATE INDEX IF NOT EXISTS telegrem ON uitems (tg)
'''

chats = '''CREATE TABLE IF NOT EXISTS chat
(
    id BIGINT NOT NULL PRIMARY KEY, 
    , own BOOLEAN NOT NULL
    , name VARCHAR (25) NOT NULL,
    , status BIT NOT NULL DEFAULT b'000'
    , img VARCHAR NULL DEFAULT NULL, 
    , users BIGINT[] NOT NULL
);
'''

