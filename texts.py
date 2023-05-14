
start_text = """
привет, ты хочешь зарегестрироваться в боте?
/registr
"""

next_text = """
ты зареган 
доступные команды:
"""

gold_user = 'голда выдана, итого сейчас'

reg_text = 'ты уже зареган\n'


new_reg_text = f'Также тебе выдан бонусный герой - пудж, не забудь заглянуть в профиль'

commands = '''/gold
/profile
/shop
'''

# name_of_heroes = [
# 'пудж',
# 'тетчис',
# 'снайпер',
# ]
# stats_of_heroes = [
#
# ]
#
# prices_of_heroes = [
#     8000,
#     5000,
#     3000,
# ]
# description_of_heroes = [
#     'это рудгерс он фармить круто драться круто',
#     'это тетчис он хуй',
#     'это снайпер (как пудж)',
# ]
# 'description '
#{'name': '', 'description': '', 'price':1, 'stats':'', img:'',  }
hero_dick = {
    1: {'name': 'pudge', 'description': 'самый секс перс доты имба покупай', 'price': 8800,
        'stats': 'asasd', 'img':r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp'},
    2: {'name': 'tetchis', 'description': 'говно ', 'price':5000,
        'stats':'инвалид', 'img':r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp' },
    3: {'name': 'sf', 'description': 'негр', 'price':10000,
        'stats':'НЕГР', 'img':r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp' },
}
#шаблон
    #{'name': '', 'global_id': 0, 'price': 0, 'description': '', 'dis_stats': '', 'farm': 1 },
item_dick = {
    'farm': {
        1: {'name': 'топорик', 'global_id': 0, 'price': 100, 'description': 'шшаа', 'dis_stats':'немного фарма', 'farm': 5},
        2: {'name': 'мидас', 'global_id': 1, 'price': 2250, 'description': 'вс антиагаа', 'dis_stats': 'много фарма', 'farm': 100 },
    },
    'fight':{
        1: {'name': 'дезолятор', 'global_id': 2, 'price': 3500, 'description': '', 'dis_stats': '', 'fight': 20 },
        2: {'name': 'лотар','global_id': 3, 'price': 2700, 'description': 'неуязвимость', 'dis_stats': 'нет', 'fignt':15},
    },
    'netral': {
        1: {'name': 'веточка', 'global_id': 4, 'price': 50, 'description': 'имба', 'dis_stats': 'много статов', 'farm': 1, 'fight': 1 },
    }
}
all_items ={
    0: {'name': 'топорик', 'price': 100, 'description': 'шшаа', 'dis_stats':'немного фарма', 'farm': 5, 'fight':0},
    1: {'name': 'мидас', 'price': 2250, 'description': 'вс антиагаа', 'dis_stats': 'много фарма', 'farm': 100, 'fight':0 },
    2: {'name': 'дезолятор', 'price': 3500, 'description': '', 'dis_stats': '', 'fight': 20, 'farm':0 },
    3: {'name': 'лотар', 'price': 2700, 'description': 'неуязвимость', 'dis_stats': 'нет', 'fignt':15, 'farm':0},
    4: {'name': 'веточка', 'price': 50, 'description': 'имба', 'dis_stats': 'много статов', 'farm': 1, 'fight': 1 },
    }
# items_names = [
#     'топорик',
#     'мидас',
#     'мом',
# ]
# netral_tems_names = [
#     'веточка',
#     ''
# ]
# farm_items_names = [
#     'топорик',
#     'мидас',
#     'жопа',
#     'попа',
#     'сися'
# ]
# fight_items_names = [
#     'дезолятор',
#     'лотар'
# ]
#
# prices_of_items = [
#     100,
#     2250,
#     1800,
#
# ]

photo_links_for_shop = [
    'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp',
    'https://mmo13.ru/download/content/202004/15/11/image_5e96c4956372a8.29507748.jpg?1586944173',
]