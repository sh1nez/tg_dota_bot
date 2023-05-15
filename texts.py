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

#{'name': '', 'description': '', 'price':1, 'stats':'', img:'',  }
hero_dick = {
    0: {'name': 'pudge', 'description': 'самый секс перс доты имба покупай', 'price': 8800,
        'stats': 'asasd', 'img':r'https://cq.ru/storage/uploads/images/1530144/1.jpg',
        'event_img': r'https://hsto.org/getpro/habr/post_images/6fc/750/e38/6fc750e38c21f9dc6a777c15cbf4be43.jpg', },
    1: {'name': 'tetchis', 'description': 'говно ', 'price':5000,
        'stats':'инвалид', 'img':r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp',
        'event_img': r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp', },

    2: {'name': 'sf', 'description': 'негр', 'price':10000,
        'stats':'НЕГР', 'img':r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp',
        'event_img': r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp',},
}
#шаблон
    #{'name': '', 'global_id': 0, 'price': 0, 'description': '', 'dis_stats': '', 'farm': 1 },
item_dick = {
    'farm': {
        0: {'name': 'топорик', 'global_id': 0, 'price': 100, 'description': 'шшаа', 'dis_stats':'немного фарма', 'farm': 5},
        1: {'name': 'мидас', 'global_id': 1, 'price': 2250, 'description': 'вс антиагаа', 'dis_stats': 'много фарма', 'farm': 100 },
    },
    'fight':{
        0: {'name': 'дезолятор', 'global_id': 2, 'price': 3500, 'description': '', 'dis_stats': '', 'fight': 20 },
        1: {'name': 'лотар','global_id': 3, 'price': 2700, 'description': 'неуязвимость', 'dis_stats': 'нет', 'fignt':15},
    },
    'netral': {
        0: {'name': 'веточка', 'global_id': 4, 'price': 50, 'description': 'имба', 'dis_stats': 'много статов', 'farm': 1, 'fight': 1 },
    }
}

all_items ={
    0: {'name': 'топорик', 'price': 100, 'description': 'шшаа', 'dis_stats':'немного фарма', 'farm': 5, 'fight':0},
    1: {'name': 'мидас', 'price': 2250, 'description': 'вс антиагаа', 'dis_stats': 'много фарма', 'farm': 100, 'fight':0 },
    2: {'name': 'дезолятор', 'price': 3500, 'description': '', 'dis_stats': '', 'fight': 20, 'farm':0 },
    3: {'name': 'лотар', 'price': 2700, 'description': 'неуязвимость', 'dis_stats': 'нет', 'fignt':15, 'farm':0},
    4: {'name': 'веточка', 'price': 50, 'description': 'имба', 'dis_stats': 'много статов', 'farm': 1, 'fight': 1 },
    }
photo_links_for_shop = [
    'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp',
    'https://mmo13.ru/download/content/202004/15/11/image_5e96c4956372a8.29507748.jpg?1586944173',
]