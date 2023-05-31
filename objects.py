from aiogram.utils.callback_data import CallbackData

"""############################################---profile---####################################################"""
my_heroes = CallbackData('spmh', 'tg_id')
show_hero_in_inventory = CallbackData('shiip', 'tg_id', 'hero_id',)
send_hero_farm_callback = CallbackData('shtfarm', 'tg_id', 'hero_id')
send_hero_fight_callback = CallbackData('shtfight', 'tg_id', 'hero_id')
items_hero_inventory = CallbackData('sliii', 'tg_id', 'hero_id')
back_to_profile = CallbackData('pbtp', 'tg_id')
user_items_callback = CallbackData('uii', 'tg_id')

wear_more_items = CallbackData('wmi', 'tg_id', 'hero_id')
wear_n_shmot_on_hero = CallbackData('wnsoh', 'tg_id', 'hero_id', 'item_id')
start_wear_item = CallbackData('swi', 'tg_id', 'item_id')
srazu_odet = CallbackData('wnsoh', 'tg_id', 'hero_id',)
q_remove_item_from_hero = CallbackData('rifh', 'tg_id', 'hero_id', 'item_id')
snat_shmotku_inventory = CallbackData('ssivi', 'tg_id', 'hero_id', 'item_id')
odet_v2 = CallbackData('jfa', 'tg_id', 'hero_id', 'ite,_id')
"""############################################---shop---####################################################"""
go_back_all_shop = CallbackData('gbtms', 'tg_id')
tradeheroes = CallbackData('trher', 'tg_id')
tradeitems = CallbackData('tritm', 'tg_id')
callback_farm_item = CallbackData('cfarmis', 'tg_id')
callback_fight_item = CallbackData('cfightis', 'tg_id')
show_item_in_shop = CallbackData('rsiis', 'tg_id', 'item_id', 'fl')  # фл должен означать вернёмся в файт или фарм
buy_item_shop_callback = CallbackData('biscq', 'tg_id', 'item_id', 'fl', 'count')
del_callback = CallbackData('delcs', 'tg_id')
show_hero_in_shop = CallbackData('shns', 'tg_id', 'hero_id', )
wanna_d7e_hero = CallbackData('diwd', 'tg_id', 'hero_id')
buy_hero_shop = CallbackData('bhs', 'tg_id', 'hero_id')


