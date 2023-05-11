class Item():
    def __init__(self, price, main_stat, mobiliti, name, index):
        self.name = name
        self.stat = main_stat
        self.price = price
        self.mobil = mobiliti
        self.index = index
    class Farm_Items():
        def __init__(self, farm, mobilit):
            self.farm = farm
            self.mobil_farm = mobilit
    class Fight_items():
        def __init__(self, helth, magic_damage, fiz_damage, esc, control):
            self.hp = helth
            self.mag_damage = magic_damage
            self.fiz_damage = fiz_damage
            self.esc = esc
            self.control = control
    class Ultimate_items():
        def __init__(self, farm, mobility, esc, helth, magic_damage, fiz_damage, control):
            self.hp = helth
            self.mag_damage = magic_damage
            self.fiz_damage = fiz_damage
            self.esc = esc
            self.farm = farm
            self.mobil_farm = mobility

siroi_topor =  Item(name='axe', price=123, main_stat='1', index=0, mobiliti=0)
notm_topor =  siroi_topor.Farm_Items(farm=123, mobilit=1.1)
test_class_items = [
    notm_topor
]
print(test_class_items[0].farm)
siroi_topor =  Item(name='axe', price=123, main_stat='1', index=0, mobiliti=0)
siroi_topor.Farm_Items(farm=123, mobilit=1.1)
print(siroi_topor.farm)


class Item1():
    def __init__(self, price, main_stat, mobiliti, name, index):
        self.name = name
        self.stat = main_stat
        self.price = price
        self.mobil = mobiliti
        self.index = index
class Farm_Items(Item):
    def __
    def __init__(self, farm, mobilit):
        self.farm = farm
        self.mobil_farm = mobilit


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
/ya_old
/profile
/shop
'''

name_of_heroes = [
'пудж',
'тетчис',
'снайпер'
]
prices_of_heroes = [
    8000,
    5000,
    3000,
]

items_names = [
    'топорик',
    'мидас',
    'мом',
]
netral_tems_names = [
    'веточка',
    ''
]

prices_of_items = [
    100,
    2250,
    1800,

]

photo_links =  [
    'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp',
    'https://mmo13.ru/download/content/202004/15/11/image_5e96c4956372a8.29507748.jpg?1586944173',
]