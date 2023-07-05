guild_log = '''CREATE OR REPLACE PROCEDURE money_updater(
    tg_id  BIGINT
    , plus NUMERIC
    , comment VARCHAR
    )
LANGUAGE plpgsql
AS $$

DECLARE
    new_balanse NUMERIC;

BEGIN
    UPDATE users SET money = money + plus WHERE tg = tg_id RETURNING money INTO new_balanse;
    INSERT INTO money_log (tg, change, result, comment) VALUES (tg_id, plus, new_balanse, comment);
COMMIT;
$$;'''
# call money_updater(1234567890, 111, 'asdasd');