from dota import NewHero, LocalHero, ShopItem  # FightItems

dick = {'exp': 300, 'hp': 50, 'fiz_armor': 1, 'mag_armor': 1,
        'fiz_tuple': ((10, 2),), 'mag_tuple': ((7, 0.21), (21, 0.27),),  # можно уменьшат кд (0 - не уменьшать)
        'total_farm': 5, 'farm_speed': 1, }
sf = NewHero(name='негр', price=80000, description=None, img1=None, img2=None, img3=None,
             hp=500, fiz_armor=15, mag_armor=15,
             farm_speed=250, total_farm=150, kef_farm=1.2, fiz_tuple=((50, 1),), mag_tuple=((100, 30,), (300, 20),),
             fiz_buf=0.7, mag_buf=1.4, exp=1000,  lvl_up=dick)
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
midas = ShopItem(price=2250, description=None, img1=None, img2=None, main_stat=None, hp=500,
                 fiz_armor=None, mag_armor=None, fiz_tuple=(None, 0.2), mag_tuple=(None, None),
                 mag_buf=None, farm_speed=None, total_farm=None)
"""price=0, description=None, img1=None, img2=None, main_stat=None, hp=None,
               fiz_armor=None, mag_armor=None, fiz_tuple=(None, None), mag_tuple=(None, None),
               mag_buf=None, farm_speed=None, total_farm=None"""
mom = ShopItem(price=0, description=None, img1=None, img2=None, main_stat=None, hp=None,
               fiz_armor=None, mag_armor=None, fiz_tuple=(None, None), mag_tuple=(None, None),
               mag_buf=None, farm_speed=None, total_farm=None)

hp, farm, fiz_dmg, mag_dmg, mag_buf = sf.lvlup_hero(5)
# print(hp, farm, fiz_dmg, mag_dmg, mag_buf, sep='\n')
local_hero1 = LocalHero(*hp, *farm, fiz_dmg, mag_dmg, mag_buf)
local_hero2 = LocalHero(*hp, *farm, fiz_dmg, mag_dmg, mag_buf)

hero_dick1 = midas * local_hero1.__dict__
hero_dick2 = local_hero2.no_items()
print(hero_dick1)
print(hero_dick2)
# сейчас у меня есть
print(LocalHero.battle(hero_dick1, hero_dick2))

# hero_dick2 = sf.no_items()
# сейчас есть словарь со всей боевой информацией
# нужен статик метод который примет 2 словаря и вернёт 2 кортежа
# print(hero_dick)
# print(local_hero.battle(hero_dick, hero_dick))
'''for i in items:
    buf = i.stats()
    for j in buf:
        pisapopa[j] += buf[j]
        print(pisapopa[j], buf[j])
# бафы итемов прибавлены
print(pisapopa)
end_farm = int(pisapopa['total_farm']*pisapopa['kef_farm'])
end_mag = int(pisapopa['total_mag']*pisapopa['kef_mag'])
end_fiz = int(pisapopa['total_fiz']*pisapopa['kef_fiz'])
'''

'''# действия
pisapopa = pudge.local_dick()  # сначала для рассчёта создам локальный словарь который будем насиловать
# сейчас мы должны прибавить бафы для лвла
print(pisapopa)
lvl_pudge = pudge.lvlup(5)
pisapopa['total_farm'] += lvl_pudge['farm']
pisapopa['total_mag'] += lvl_pudge['magic']
pisapopa['total_fiz'] += lvl_pudge['fiz']
# ура готово лвл прибавлен
print(pisapopa)
# сейчас мы должны прибавить бафы итемов
items = (midas, desolator)'''

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
    'farm': {
        0: {'name': 'топорик', 'global_id': 0, 'price': 100, 'description': 'шшаа', 'dis_stats':'немного фарма', 'farm': 5},
        1: {'name': 'мидас', 'global_id': 1, 'price': 2250, 'description': 'вс антиагаа', 'dis_stats': 'много фарма', 'farm': 100 },
        2: {'name': 'мидас', 'global_id': 1, 'price': 2250, 'description': 'вс антиагаа', 'dis_stats': 'много фарма', 'farm': 100 },
        3: {'name': 'дезолятор', 'global_id': 2, 'price': 3500, 'description': '', 'dis_stats': '', 'fight': 20 },
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

# photo_links_for_shop = [
#     r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp',
#     r'https://mmo13.ru/download/content/202004/15/11/image_5e96c4956372a8.29507748.jpg?1586944173',
#     r'https://www.rsi-llc.ru/upload/iblock/3d2/3d29c3bee8d6415b6072f4270ba136f2.jpg',
#     r'https://instamag.ru/upload/medialibrary/ccf/cards_polaroids_19_1_min.jpg',
#     #r'https://static.dw.com/image/38357849_605.jpg',
#     r'https://upload.wikimedia.org/wikipedia/commons/c/cd/Gay_Couple_Savv_and_Pueppi_02.jpg',
# ]

images = {
    'shop': {
       'shop': r'https://steamcommunity.com/sharedfiles/filedetails/?id=2527986587&searchtext=Hledat+n%C3%A1vody+pro+hru+Dota+2',
        'bg1' : r'https://phonoteka.org/uploads/posts/2021-09/thumbs/1631660201_16-phonoteka-org-p-zadnii-fon-dota-krasivo-16.jpg',
        'many_heroes': r'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAVG0yTq7HZqhIHwfXWrx_xvNZTkatNxxcdw&usqp=CAU',


    },
    'profile': {
        'anime1': r"https://i.scdn.co/image/ab67616d0000b2736134f695c97c4e83c12ee69b",
        'bg1' : r'https://cq.ru/storage/uploads/posts/83811/cri/dota-geroi-fan-art-personazhi___media_library_original_1332_850.jpg',

    }
}

пудж https://hsto.org/getpro/habr/post_images/6fc/750/e38/6fc750e38c21f9dc6a777c15cbf4be43.jpg
сф https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvL1HZYHXfLVYE6DrWT98DujBzDquKy8f0hLKKcvqudndYk4_GwOu_GbQoB7lgW91Naxw&usqp=CAU
ам(?) https://mmo-obzor.ru/_bd/1/27135127.jpg
химик https://mmo-obzor.ru/_bd/0/55786770.jpg 
вс https://avatars.dzeninfra.ru/get-zen_doc/3504072/pub_5ed0e87d7c1a732a1551b54a_5ed0fc29335fdd4d23a738bb/scale_1200
шторм https://static.wikia.nocookie.net/dota2_gamepedia/images/e/e7/Cosmetic_icon_Corridan_Maestro.png/revision/latest?cb=20161029000314 
 
арт красиво
"""
