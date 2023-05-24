from dota import NewHero, LocalHero, ShopItem  # FightItems

sf_dick = {'exp': 300, 'hp': 50, 'fiz_armor': 1, 'mag_armor': 1,
           'fiz_tuple': ((10, 2),), 'mag_tuple': ((7, 0.21), (21, 0.27),),  # можно уменьшат кд (0 - не уменьшать)
           'total_farm': 5, 'farm_speed': 1, }
sf_urls = (r'https://dota2ok.ru/wp-content/uploads/2021/01/SF-1024x576.jpg',
           )
sf = NewHero(name='негр', price=80000, description=None, img1=sf_urls[0], img2=None, img3=None,
             hp=500, fiz_armor=15, mag_armor=15,
             farm_speed=250, total_farm=150, kef_farm=1.2, fiz_tuple=((50, 1),), mag_tuple=((100, 30,), (300, 20),),
             fiz_buf=0.7, mag_buf=1.4, exp=1000, lvl_up=sf_dick)
'''
(def __init__(self, price: int, description: str or None, img1: str, img2: str or None,
                 main_stat: int or None,
                 hp: int or None, fiz_armor: float or None, mag_armor: float or None,
                 fiz_tuple: tuple or None, mag_tuple: tuple or None, mag_buf: float or None,
                 farm_speed: int or None, total_farm: int or None,
                 ):

midas_stats = (2250, 'IMBA', 'img', None,    # price desc img1 img2
               None, 100, 5, 5,  # stat, hp, fiz_armor, mag_armor
               (None, None,), (None, None,),  # (fiz_tup,), (mag_tup,)
               None, None, None)  # mag_buf, farm_speed, total_far
'''
midas_urls = (
    'https://avatars.dzeninfra.ru/get-zen_doc/3126430/pub_604f9ae70a7d51654a5834d3_604f9b59011181447bd702d5/scale_1200',

)
midas = ShopItem(price=2250, name='мидас', description=None, img1=midas_urls[0], img2=None, main_stat=None, hp=500,
                 fiz_armor=None, mag_armor=None, fiz_tuple=(None, 0.2), mag_tuple=(None, None),
                 mag_buf=None, farm_speed=None, total_farm=None)
"""price=0, name=None, description=None, img1=None, img2=None, main_stat=None, hp=None,
               fiz_armor=None, mag_armor=None, fiz_tuple=(None, None), mag_tuple=(None, None),
               mag_buf=None, farm_speed=None, total_farm=None"""
mom = ShopItem(price=2000, name='мом', description=None, img1=None, img2=None, main_stat=None, hp=None,
               fiz_armor=None, mag_armor=None, fiz_tuple=(None, None), mag_tuple=(None, None),
               mag_buf=None, farm_speed=None, total_farm=None)

'''
hp, farm, fiz_dmg, mag_dmg, mag_buf = sf.lvlup_hero(5)
# print(hp, farm, fiz_dmg, mag_dmg, mag_buf, sep='\n')
local_hero1 = LocalHero(*hp, *farm, fiz_dmg, mag_dmg, mag_buf)
local_hero2 = LocalHero(*hp, *farm, fiz_dmg, mag_dmg, mag_buf)
hero_dick1 = local_hero1.__dict__
hero_dick1 *= midas
hero_dick1 *= midas
hero_dick2 = local_hero2.no_items()
# сейчас у меня есть
print(LocalHero.battle(hero_dick1, hero_dick2))

'''
hero_dick = {
    0: sf
}


item_dick = {
    'farm': {0: midas,
             1: mom},
    'fight': {}
}
all_items = {
    0: midas,
    1: mom
}

images = {
    'dyrachyo': 'https://meta-ratings.kz/_images/insecure/w-680:h-512/bG9jYWw6Ly8vaW1hZ2VzL2MzLzQzL2MzNDNjZmZ'
                'mMmZmOTU4MjdmNGMyNmVkNzY5Y2EwNjY4LmpwZw==.webp',
    'throne': 'https://static.wikia.nocookie.net/anime-characters-fight/images/6/6d/Buhoianc.png/revision/latest/'
              'scale-to-width-down/700?cb=20220924120451&path-prefix=ru',
    'salesman': r'https://i.playground.ru/p/YHdC7uONxlTs8noj6L7pUg.jpeg?800-auto',
    'items': r'https://ggdt.ru/file/2020/10/dota2items4.jpg',
    'anime1': r"https://i.scdn.co/image/ab67616d0000b2736134f695c97c4e83c12ee69b",
    'bg1': r'https://cq.ru/storage/uploads/posts/83811/cri/dota-geroi-fan-art-personazhi___'
           r'media_library_original_1332_850.jpg',
    'bg2': r'https://phonoteka.org/uploads/posts/2021-09/thumbs/1631660201_16-phonoteka-org-p-zadnii-fon-'
           r'dota-krasivo-16.jpg',
    'woman': r'https://indota2.ru/wp-content/uploads/2019/02/87.jpg'

}

next_text = """ ты зарегистрирован 
доступные команды:
/profile
/shop
"""

gold_user = 'голда выдана, итого сейчас'

reg_text = 'ты уже зарегистрирован\n'

enemy_click = [
    'пидор по своим кнопкам кликай',
    'это не твоя кнопка',
    'ээ потише',
]

new_reg_text = f'Также тебе выдан бонусный герой - пудж, не забудь заглянуть в профиль'

commands = '''/gold
/profile
/shop
'''

"""
hero_dick = {
    0: {'name': 'pudge', 'description': 'самый секс перс доты имба покупай', 'price': 8800,
        'stats': 'asasd', 'img':r'https://cq.ru/storage/uploads/images/1530144/1.jpg',
        'event_img': r'https://hsto.org/getpro/habr/post_images/6fc/750/e38/6fc750e38c21f9dc6a777c15cbf4be43.jpg', },
    1: {'name': 'tetchis', 'description': 'говно ', 'price':5000,
        'stats':'инвалид', 'img':r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp',
        'event_img': r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp', },

    2: {'name': 'sf', 'description': 'негр', 'price':10000,
        'stats': 'НЕГР', 'img':r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp',
        'event_img': r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp'},
}

item_dick = {
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

# photo_links_for_shop = [
#     r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp',
#     r'https://mmo13.ru/download/content/202004/15/11/image_5e96c4956372a8.29507748.jpg?1586944173',
#     r'https://www.rsi-llc.ru/upload/iblock/3d2/3d29c3bee8d6415b6072f4270ba136f2.jpg',
#     r'https://instamag.ru/upload/medialibrary/ccf/cards_polaroids_19_1_min.jpg',
#     #r'https://static.dw.com/image/38357849_605.jpg',
#     r'https://upload.wikimedia.org/wikipedia/commons/c/cd/Gay_Couple_Savv_and_Pueppi_02.jpg',
# ]

    }
}


арт красиво
"""
