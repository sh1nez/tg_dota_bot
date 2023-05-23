from dota import NewHero, LocalHero
sf_stats = (
    *('url', 'url2', 'url3'),
    *(500, 0.22, 0.22,),  # hp, fiz_armor, mag_armor, от
    *(250, 150, 1.1),  # фарм, в мс, тотал и кефе
    *(((150, 10),), 0.7, ((100, 30,), (300, 20)), 1.488),
    # fiz_damage: int, attack_speed: float, fiz_buf: float, magic_tuple, mag_buff
    1000,  # базовый exp
    {'exp': 300, 'hp': 50, 'fiz_armor': 0.8, 'mag_armor': 0.7,
     'fiz_tuple': ((10, 2),), 'magic_tuple': ((7, 0.21), (21, 0.27)),
     'total_farm': 5, 'farm_speed': 1, }
    # можно уменьшат кд, можно не уменьшать добавив 0
)

sf = NewHero('негр', 80000, None, *sf_stats)
hp, farm, fiz_dmg, mag_dmg = sf.lvlup_hero(5)
print(sf.__dict__)
#print(hp, farm, fiz_dmg, mag_dmg, sep='\n')
local_hero = LocalHero(*hp, *farm, fiz_dmg, mag_dmg)
print(local_hero.__dict__)
"""изменены атрибуты в формате хп, физ armor, magic armor, кортеж физ урон, маг урон"""

'''хп, физ armor, маг armor, физ урон физ ас маг урон маг ас '''

"""name, price, description, img, good_event, bad_event, magic_damage_kef, fiz_damage_kef,
    total_mag_d, total_fiz_d, farm, total_farm, hp, lvl_up"""



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




next_text = """ ты зареган 
доступные команды:
/profile
/shop
"""

gold_user = 'голда выдана, итого сейчас'

reg_text = 'ты уже зареган\n'

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



hero_dick = {
    0: {'name': 'pudge', 'description': 'самый секс перс доты имба покупай', 'price': 8800,
        'stats': 'asasd', 'img':r'https://cq.ru/storage/uploads/images/1530144/1.jpg',
        'event_img': r'https://hsto.org/getpro/habr/post_images/6fc/750/e38/6fc750e38c21f9dc6a777c15cbf4be43.jpg', },
    1: {'name': 'tetchis', 'description': 'говно ', 'price':5000,
        'stats':'инвалид', 'img':r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp',
        'event_img': r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp', },

    2: {'name': 'sf', 'description': 'негр', 'price':10000,
        'stats':'НЕГР', 'img':r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp',
        'event_img': r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp'},
}
#шаблон
    #{'name': '', 'global_id': 0, 'price': 0, 'description': '', 'dis_stats': '', 'farm': 1 },
#всё это нужно для описания, другие классы в другом файле для работы
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

"""
пудж https://hsto.org/getpro/habr/post_images/6fc/750/e38/6fc750e38c21f9dc6a777c15cbf4be43.jpg
сф https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvL1HZYHXfLVYE6DrWT98DujBzDquKy8f0hLKKcvqudndYk4_GwOu_GbQoB7lgW91Naxw&usqp=CAU
ам(?) https://mmo-obzor.ru/_bd/1/27135127.jpg
химик https://mmo-obzor.ru/_bd/0/55786770.jpg 
вс https://avatars.dzeninfra.ru/get-zen_doc/3504072/pub_5ed0e87d7c1a732a1551b54a_5ed0fc29335fdd4d23a738bb/scale_1200
шторм https://static.wikia.nocookie.net/dota2_gamepedia/images/e/e7/Cosmetic_icon_Corridan_Maestro.png/revision/latest?cb=20161029000314 
 
файт арт красиво

"""

#class Description_items: хз нужно или нет
