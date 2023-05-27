from dota import NewHero, ShopItem

pudge_dick = {'exp': 300, 'hp': 50, 'fiz_armor': 1, 'mag_armor': 1,
              'fiz_tuple': ((5, 2),), 'mag_tuple': ((1, 0),),
              'total_farm': 3, 'farm_speed': 0, }
pudge_urls = ('https://cq.ru/storage/uploads/images/1530144/cri/1___media_library_original_1018_636.jpg',)
pudge_disc = 'тут и говорить нечего, имба'
pudge = NewHero(name='пудж', price=0, description=pudge_disc, img1=pudge_urls[0], img2=None, img3=None,
                hp=1000, fiz_armor=20, mag_armor=26,
                farm_speed=150, total_farm=80, kef_farm=1.5, fiz_tuple=((50, 50),), mag_tuple=((10, 0.5,),),
                fiz_buf=0.7, mag_buf=1.5, exp=1000, lvl_up=pudge_dick)

sf_dick = {'exp': 300, 'hp': 25, 'fiz_armor': 0.5, 'mag_armor': 0.5,
           'fiz_tuple': ((10, 10),), 'mag_tuple': ((10, 0.21), (10, 0.21), (10, 0.21)),
           'total_farm': 2.5, 'farm_speed': 0, }
sf_urls = (r'https://dota2ok.ru/wp-content/uploads/2021/01/SF-1024x576.jpg',
           )
sf_disc = 'если честно хз к чему он будет расположен как и пудж, все показатели говно кроме показателей, если собрать' \
          'кучу предмето то по идее будет самый сильный герой'
sf = NewHero(name='негр', price=80000, description=sf_disc, img1=sf_urls[0], img2=None, img3=None,
             hp=750, fiz_armor=5, mag_armor=5,
             farm_speed=150, total_farm=70, kef_farm=1.2, fiz_tuple=((50, 100),),
             mag_tuple=((100, 10,), (100, 10,), (100, 10,)),
             fiz_buf=1.7, mag_buf=1.5, exp=1000, lvl_up=sf_dick)

alch_urls = (
    r'https://mobimg.b-cdn.net/v3/fetch/c1/c1956cc5c07fdda1574eb5a814f334c8.jpeg',
)

alch_dick = {'exp': 250, 'hp': 50, 'fiz_armor': 2.5, 'mag_armor': 2.5,
              'fiz_tuple': ((9, 9),), 'mag_tuple': ((1, 0),),
              'total_farm': 8, 'farm_speed': 3, }
alch_desc = 'герой предназначен исключительно для фарма. Драться может только ближе к поздним стадиям игры'
alchemist = NewHero(name='алхимик', price=0, description=alch_desc, img1=alch_urls[0], img2=None, img3=None,
                hp=300, fiz_armor=7, mag_armor=0,
                farm_speed=300, total_farm=150, kef_farm=2, fiz_tuple=((35, 10),), mag_tuple=((100, 15,),),
                fiz_buf=1.7, mag_buf=0.5, exp=800, lvl_up=alch_dick)

void_spirit_ursl = (
    r'https://damion.club/uploads/posts/2022-09/1663907425_11-damion-club-p-void-spirit-oboi-pinterest-12.jpg',
)
void_spirit_dick = {'exp': 400, 'hp': 20, 'fiz_armor': 1, 'mag_armor': 1,
              'fiz_tuple': ((9, 9),), 'mag_tuple': ((8, 0,),(8, 0,), (5, 0,),),
              'total_farm': 0, 'farm_speed': 0, }
void_spirit_desc = 'герой предрасположен к ранним дракам'
void_spirit = NewHero(name='войд спирит', price=0, description=void_spirit_desc, img1=void_spirit_ursl[0], img2=None, img3=None,
                hp=700, fiz_armor=15, mag_armor=15,
                farm_speed=100, total_farm=100, kef_farm=0.5, fiz_tuple=((80,100),), mag_tuple=((200, 10,),(200, 10,), (30, 3,),),
                fiz_buf=1, mag_buf=1, exp=1200, lvl_up=void_spirit_dick)


hero_dick = {
    0: pudge,
    1: sf,
    2: alchemist,
    3: void_spirit,
}


midas_urls = (
    'https://avatars.dzeninfra.ru/get-zen_doc/3126430/pub_604f9ae70a7d51654a5834d3_604f9b59011181447bd702d5/scale_1200',
)
midas = ShopItem(price=2250, name='мидас', description=None, img1=midas_urls[0], img2=None, main_stat=None, hp=None,
                 fiz_armor=None, mag_armor=None, fiz_tuple=(None, 0.2), mag_tuple=(None, None),
                 mag_buf=None, farm_speed=None, total_farm=150)
"""price=0, name=None, description=None, img1=None, img2=None, main_stat=None, hp=None,
               fiz_armor=None, mag_armor=None, fiz_tuple=(None, None), mag_tuple=(None, None),
               mag_buf=None, farm_speed=None, total_farm=None"""
mom_urls = (
    'https://steamuserimages-a.akamaihd.net/ugc/5114431931285788573/9D8C5A31B5B184ECA192F18D172B1F3EFE28697A/',
)
mom = ShopItem(price=2000, name='мом', description=None, img1=mom_urls[0], img2=None, main_stat=None, hp=None,
               fiz_armor=-5, mag_armor=None, fiz_tuple=(None, 100), mag_tuple=(None, None),
               mag_buf=None, farm_speed=10, total_farm=None)
phylactery_urls = (
    r'https://i.pinimg.com/236x/a2/ce/ec/a2ceec4098c409a58b8e4a48e30f9157.jpg',
)
phylactery = ShopItem(price=1000, name='филактерия', description=None, img1=phylactery_urls[0], img2=None,
                      main_stat=None, hp=150,
                      fiz_armor=None, mag_armor=None, fiz_tuple=(None, None), mag_tuple=(100, 8),
                      mag_buf=0.1, farm_speed=None, total_farm=None)

dagon_urls = (
    r'https://pin.it/6XzkJ9I'
)
dagon = ShopItem(price=3000, name='дагон', description=None, img1=dagon_urls[0], img2=None,
                 main_stat=None, hp=150,
                 fiz_armor=None, mag_armor=None, fiz_tuple=(None, None), mag_tuple=(500, 15),
                 mag_buf=0.3, farm_speed=None, total_farm=None)
travel_boots_urls = (
    r'https://img1.etsystatic.com/069/0/10284703/il_570xN.818415665_6k6i.jpg',
)
travel_boots = ShopItem(price=1800, name='тревела', description=None, img1=travel_boots_urls[0], img2=None,
                        main_stat=None, hp=None,
                        fiz_armor=None, mag_armor=None, fiz_tuple=(None, None), mag_tuple=(None, None),
                        mag_buf=None, farm_speed=100, total_farm=None)

item_dick = {
    'farm': {0: midas,
             1: mom,
             2: travel_boots},
    'fight': {0: phylactery,
              1: dagon,}
}
all_items = {
    0: midas,
    1: mom,
    2: phylactery,
    3: dagon,
    4: travel_boots
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