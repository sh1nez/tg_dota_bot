from dataclasses import dataclass

@dataclass
class SqlDataBase():
    __slots__ = ('create', 'index_other', 'update', 'delete', 'select', 'insert')
    create: list
    index_other: list or None
    select: list
    insert: list
    update: list or None
    delete: list or None
    

users = SqlDataBase(create=[], index_other=None, select=[], insert=[], update=None, delete=None)
print(users.create)

'''CREATE TABLE IF NOT EXISTS users
(
    tg BIGINT NOT NULL PRIMARY KEY
    , money NUMERIC(14,2) NOT NULL DEFAULT 0 --12 before 2 after
    , mmr SMALLINT NOT NULL DEFAULT 0 
    , bonus BOOLEAN NOT NULL DEFAULT false
    , status BIT(3) NOT NULL DEFAULT b'000'
    , guild SMALLINT NULL DEFAULT NULL
    CONSTRAINT money_counter CHECK (money >= 0)
    CONSTRAINT mmr_counter CHECK( mmr >= 0)
    );
    '''

class UsersInfo:
    __create = '''CREATE TABLE IF NOT EXISTS iusers 
(
    tg BIGINT NOT NULL PRIMARY KEY 
        REFERENCES users(tg)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    , img VARCHAR[] NULL DEFAULT NULL
    , nik VARCHAR(25) NOT NULL
    , referal BIGINT NOT NULL
        REFERENCES users(tg)
            ON DELETE CASCADE
            On UPDATE CASCADE
    , status BIT(3) NOT NULL DEFAULT b'000'
    );
    '''
    __index = [ '''CREATE INDEX IF NOT EXISTS referal ON iusers(referal);''']


class DieVinchikInfo:
    pass


class Chats:
    pass


class Guild:
    pass


"""
INSERT INTO users VALUES (1234567890, 123456789012.12), (1987654321, 1), (7834901267, 0), 
(9991119991, 123.12);
"""
# bit (3)
# 1 - destroy items 
# 2 - make guild
# 3 - own commands


# 1 - castom image
# 2 - referal bonus
# 3 - longer nikname (25)


hero = '''CREATE TABLE IF NOT EXISTS hero 
(
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

guild = '''CREATE TABLE IF NOT EXISTS guild 
(
    id SMALLSERIAL NOT NULL PRIMARY KEY
    , name varchar (25) NOT NULL UNIQUE
    , status BIT(3) NOT NULL DEFAULT b'000'
    , owner BIGINT NOT NULL 
        REFERENCES users(tg)
            ON UPDATE CASCADE
            ON DELETE RESTRICT
    , mmr SMALLINT NOT NULL CONSTRAINT CHECH(mmr>0) DEFAULT 0
    , money NUMERIC(14,2) NOT NULL CHECK(money >= 0)
);
'''


