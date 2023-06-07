from answers import *
from database import *
from objects import *
from config import dis, sheduler
''''''
dis.register_message_handler(func_helper, commands=['help'])
dis.register_message_handler(func_starter, commands=['start'])
dis.register_message_handler(func_make_profile, commands=['profile'])
dis.register_message_handler(func_bonus, commands=['bonus'])
dis.register_message_handler(func_all_shop, commands=['shop'])
dis.register_callback_query_handler(func_all_shop, go_back_all_shop.filter())
dis.register_callback_query_handler(func_make_profile, back_to_profile.filter())
dis.register_callback_query_handler(func_shop_heroes, tradeheroes.filter())
dis.register_callback_query_handler(func_shop_items, tradeitems.filter())
dis.register_callback_query_handler(func_all_heroes_local_user, my_heroes.filter())
dis.register_callback_query_handler(func_inventory_hero, show_hero_in_inventory.filter())
dis.register_callback_query_handler(func_send_farm, send_hero_farm_callback.filter())
dis.register_callback_query_handler(func_show_items_hero, items_hero_inventory.filter())
dis.register_callback_query_handler(func_fight, send_hero_fight_callback.filter())
dis.register_callback_query_handler(func_shop_farm_item, callback_farm_item.filter())
dis.register_callback_query_handler(func_shop_fight_item, callback_fight_item.filter())
dis.register_callback_query_handler(func_show_n_item_in_shop, show_item_in_shop.filter())
dis.register_callback_query_handler(func_buy_in_shop, buy_item_shop_callback.filter())
dis.register_callback_query_handler(func_show_hero_in_shop, show_hero_in_shop.filter())
dis.register_callback_query_handler(func_ask_for_buy, wanna_d7e_hero.filter())
dis.register_callback_query_handler(func_buy_hero, buy_hero_shop.filter())
dis.register_callback_query_handler(func_profile_items, user_items_callback.filter())
dis.register_callback_query_handler(func_nowear_items_to_wear, start_wear_item.filter())
dis.register_callback_query_handler(func_wear_item, wear_n_shmot_on_hero.filter())
dis.register_callback_query_handler(func_wear_more_items,  wear_more_items.filter())
dis.register_callback_query_handler(func_remove_item, q_remove_item_from_hero.filter())
dis.register_callback_query_handler(func_snat_item, snat_shmotku_inventory.filter())
dis.register_callback_query_handler(func_srazu_vear, srazu_odet.filter())
dis.register_callback_query_handler(func_v2_wear, odet_v2.filter())

if __name__ == '__main__':
    sheduler.add_job(func=clean_bonus, trigger='cron', hour=0, )
    sheduler.start()
    aiogram.executor.start_polling(dis, )  # skip_updates=True
