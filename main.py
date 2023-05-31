import aiogram
from answers import *
from database import *
# from aiogram.types import InputMediaPhoto
from objects import *
from config import bot, dis, sheduler


# @dis.message_handler(commands=['start'])

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

"""
async def shmot_on_hero_func(callback, tg_id, hero_id, item_id):
    wear_item_on_hero(tg_id, hero_id, item_id)
    await bot.edit_message_media()
    await bot.answer_callback_query(callback.id, 'итем одет чекай')


async def remove_item_func(callback, tg_id, hero_id, item_id):
    buttons = (('снять шмотку', snat_shmotku_inventory, (tg_id, hero_id, item_id)),
               ('отмена', items_hero_inventory, (tg_id, hero_id,)))
    ikm = make_inline_keyboard(*buttons, row=1)
    img = InputMediaPhoto(media=images['dyrachyo'],
                          caption='ты хочешь снять шмотку с героя? при снятии есь 10% шанс сломать шмотку')
    await bot.edit_message_media(media=img, reply_markup=ikm, message_id=callback.message.message_id,
                                 chat_id=callback.message.chat.id)
    await bot.answer_callback_query(callback.id)


async def wmot_shat_func(callback, tg_id, hero_id, item_id):
    snat_s_geroya_v_invantar(item_id, tg_id, hero_id)
    await bot.answer_callback_query(callback.id, 'шмотка снята')



async def wear_on_func(callback, tg_id):
    tup = find_id_name_all_heroes(tg_id)
    buttons = ((hero_dick[i[0]].name, '', (tg_id, i[0],)) for i in tup)

    вернёт сделанные кнопки для make_inline_keyboard которые будут перенаправлять на

    # ikm = make_inline_keyboard()
    await bot.answer_callback_query(callback.id)



'''


#
#
# # wear_n_shmot_on_hero = CallbackData('wnsoh', 'tg_id', 'hero_id', 'item_id')
#
#
# @dis.callback_query_handler(wear_n_shmot_on_hero.filter())
# async def rwnsoh(callback):
#     tg_id, hero_id, item_id = r_cbd(callback.data)
#     if tg_id != callback.from_user.id:
#         await bot.answer_callback_query(callback.id, enemy_click[rnum()])
#         return
#     await shmot_on_hero_func(callback, tg_id, hero_id, item_id)
#
#
# # q_remove_item_from_hero = CallbackData('rifh', 'tg_id', 'hero_id', 'item_id')
#
#
# @dis.callback_query_handler(q_remove_item_from_hero.filter())
# async def qrifh(callback):
#     tg_id, hero_id, item_id = r_cbd(callback.data)
#     if tg_id != callback.from_user.id:
#         await bot.answer_callback_query(callback.id, enemy_click[rnum()])
#         return
#     await remove_item_func(callback, tg_id, hero_id, item_id)
#
#
# snat_shmotku_inventory = CallbackData('ssivi', 'tg_id', 'hero_id', 'item_id')
# @dis.callback_query_handler(snat_shmotku_inventory.filter())
# async def rtshsg(callback):
#     tg_id, hero_id, item_id = r_cbd(callback.data)
#     if tg_id != callback.from_user.id:
#         await bot.answer_callback_query(callback.id, enemy_click[rnum()])
#         return
#     await shmot_on_hero_func(callback, tg_id, hero_id, item_id)
#

# '''###########################################----BUY_ITEMS-----############################################'''

#
# # del_callback = CallbackData('delcs', 'tg_id')
#
#
# @dis.callback_query_handler(del_callback.filter())
# async def rdcfs(callback):
#     tg_id = r_cbd(callback.data)
#     if tg_id != callback.from_user.id:
#         await bot.answer_callback_query(callback.id, enemy_click[rnum()])
#         return
#     await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
#     # хз нужно или нет но можно удалять сообщения с менюшкой и пользователем который их написал
#     # try: await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id-1)
#     # №except: await bot.send_message(chat_id=callback.message.chat.id, text=
#     # 'дайте админку чтобы я мог удалять сообщения (сейчас нужно удалить сообщение которым вызвали меню)')
#

"""
if __name__ == '__main__':
    sheduler.add_job(func=clean_bonus, trigger='cron', hour=0, )
    sheduler.start()
    aiogram.executor.start_polling(dis, )  # skip_updates=True
