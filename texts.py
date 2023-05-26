from dota import NewHero, ShopItem

sf_dick = {'exp': 300, 'hp': 25, 'fiz_armor': 0.5, 'mag_armor': 0.5,
           'fiz_tuple': ((10, 10),), 'mag_tuple': ((10, 0.21), (10, 0.21), (10, 0.21)),
           'total_farm': 5, 'farm_speed': 0, }
sf_urls = (r'https://dota2ok.ru/wp-content/uploads/2021/01/SF-1024x576.jpg',
           )
sf = NewHero(name='негр', price=80000, description=None, img1=sf_urls[0], img2=None, img3=None,
             hp=750, fiz_armor=5, mag_armor=5,
             farm_speed=250, total_farm=150, kef_farm=1.2, fiz_tuple=((50, 100),),
             mag_tuple=((100, 10,), (100, 10,), (100, 10,)),
             fiz_buf=1.7, mag_buf=1.5, exp=1000, lvl_up=sf_dick)

pudge_dick = {'exp': 300, 'hp': 50, 'fiz_armor': 1, 'mag_armor': 1,
              'fiz_tuple': ((5, 2),), 'mag_tuple': ((1, 0),),
              'total_farm': 5, 'farm_speed': 0, }
pudge_urls = ('https://cq.ru/storage/uploads/images/1530144/cri/1___media_library_original_1018_636.jpg',)
pudge = NewHero(name='пудж', price=0, description=None, img1=pudge_urls[0], img2=None, img3=None,
                hp=1000, fiz_armor=20, mag_armor=26,
                farm_speed=280, total_farm=200, kef_farm=1.5, fiz_tuple=((50, 50),), mag_tuple=((10, 0.5,),),
                fiz_buf=0.7, mag_buf=1.5, exp=1000, lvl_up=pudge_dick)

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
mom_urls = (
    'https://steamuserimages-a.akamaihd.net/ugc/5114431931285788573/9D8C5A31B5B184ECA192F18D172B1F3EFE28697A/',
)
mom = ShopItem(price=2000, name='мом', description=None, img1=mom_urls[0], img2=None, main_stat=None, hp=None,
               fiz_armor=None, mag_armor=None, fiz_tuple=(None, None), mag_tuple=(None, None),
               mag_buf=None, farm_speed=None, total_farm=None)

hero_dick = {
    0: pudge,
    1: sf
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
    'woman': r'https://indota2.ru/wp-content/uploads/2019/02/87.jpg',
    'jungle': r'https://img2.goodfon.ru/wallpaper/nbig/2/4e/dota-2-nature-s-prophet.jpg',


}
enemy_click = [
    'пидор по своим кнопкам кликай',
    'это не твоя кнопка',
    'ээ потише',
]

new_reg_text = f'Также тебе выдан бонусный герой - пудж, не забудь заглянуть в профиль /profile '

"""
next_text =  ты зарегистрирован 
доступные команды:
/profile
/shop


gold_user = 'голда выдана, итого сейчас'

reg_text = 'ты уже зарегистрирован\n'
"""