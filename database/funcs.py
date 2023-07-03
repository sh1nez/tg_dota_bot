users = '''CREATE TABLE IF NOT EXISTS users
(
    tg BIGINT NOT NULL PRIMARY KEY
    , money NUMERIC(14,2) NOT NULL DEFAULT 0 --12 before 4 after
    , mmr SMALLINT NOT NULL DEFAULT 0 
    , bonus BOOLEAN NOT NULL DEFAULT false
    , status BIT(3) NOT NULL DEFAULT b'000'
    , guild SMALLINT NULL DEFAULT NULL
    CONSTRAINT money_counter CHECK (money > 0)
    CONSTRAINT mmr_counter  CHECK( mmr > 0))

);
'''
# INSERT INTO users VALUES (1234567890, 123_456_789_012.12), (0987654321, 1), (7834901267, 0);
# bit (3)
# 1 - destroy items 
# 2 - make guild
# 3 - own commands


iusers = '''CREATE TABLE IF NOT EXISTS iusers 
(
    tg BIGINT NOT NULL UNIQUE
        REFERENCES users(tg)
            ON DELETE CASCADE
            ON UPDATE CASCADE
        UNIQUE USING BTREE
    , img VARCHAR[] NULL DEFAULT NULL
    , nik VARCHAR(25) NOT NULL
    , referal BIGINT NOT NULL 
        REFERENCES users(tg)
            ON DELETE CASCADE
            On UPDATE CASCADE
    , status BIT(3) NOT NULL DEFAULT b'000'
);
'''
# 1 - castom image
# 2 - referal bonus
# 3 - longer nikname (25)


hero = '''CREATE TABLE IF NOT EXISTS hero 
(
    tg BIGINT NOT NULL UNIQUE
        REFERENCES users(tg)
            ON DELETE CASCADE
            ON DELETE CASCADE
    , name BIT NOT NULL
    , activity TIMESTAMPTZ NULL DEFAULT now()
    , fight BOOLEAN NOT NULL DEFAULT NULL
    , lvl SMALLINT NOT NULL DEAULT 1
    , exp SMALLINT NOT NULL DEFAULT 0
    , items bit[] NULL DEFAULT NULL
);
'''

uitems = ''' CREATE TABLE IF NOT EXISTS uitem
(
    tg BIGINT NOT NULL UNIQUE
        REFERENCES users(tg)
            ON DELETE CASCADE
            ON UDPATE CASCADE
    , name BIT NOT NULL
    , count SMALLINT NOT NULL DEFAULT 1
    CONSTRAINT counter CHECK (count > 0)
);
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
    id smallserial NOT NULL PRIMARY KEY
    , name varchar (25) NOT NULL
    , status BIT(3) NOT NULL DEFAULT b'000'
    , owner BIGINT NOT NULL 
        REFERENCES users(tg)
            ON UPDATE CASCADE
            ON DELETE RESTRICT
    , mmr SMALLINT NOT NULL CONSTRAINT CHECH(mmr>0) DEFAULT 0
    , money
);
'''


log = {
    'fight': """CREATE TABLE IF NOT EXISTS fight (
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
    , result BOOLEAN NOT NULL
);""",
    'money': """CREATE TABLE IF NOT EXISTS lmoney 
    (
        tg BIGINT NOT NULL
            REFERENCES users(tg)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        , start numeric(14,2) NOT NULL
        , change numeric(14,2) NUT NULL
        , time TIMESTAMPTZ NOT NULL DEFAULT now()
        , comment VARCHAR NULL DEFAULT NULL
    );
    """,
    'guild': """CREATE TABLE IF NOT EXISTS lguild (
        id smallserial NOT NULL
            REFERENCES guild(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
        tg BIGINT NULL DEFAULT NULL
            REFERENCES users(tg)
                ON DELETE CASCADE 
                ON UPDATE CASCADE
        live_jount BOOLEAN NULL DEFAULT NULL
    ); 
    """,
    'p2p' : """
    CREATE TABLE IF NOT EXISTS p2p (
        
    
    );
    """,
    'items': """CREATE TABLE IF NOT EXISTS lguild (
    
    );
    """,

}


function = '''CREATE OR REPLACE FUNCTION money()
RETURNS TRIGGER AS $$
BEGIN
    insert into 
'''
triger = '''CREATE TRIGER
'''
