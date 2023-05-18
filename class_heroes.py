# class Hero:
#     def __init__(self, index, name):
#         self.index = index
#         self.name = name
#
#     def send_nudes(self):
#         return [self.name]
#
# class Test_Stats_hero(Hero):#ещё нужно добавить кэф маг и физ урона. Чтобы на дизрапторе не собирались в физ а на антимаге в маг
#     def __init__(self, index, name, hp, damage, lvl_up):
#         super().__init__(index, name)
#         self.hp = hp
#         self.damage = damage
#         self.up = lvl_up
#     def send_nudes(self):
#         return [self.hp, self.damage]
#     def lvl_up(self, lvl):
#         lvl = float(lvl)
#         return [self.hp+self.hp*self.up[0]*lvl,
#                 self.damage+self.damage+self.up[1]*lvl
#                 ]
# ##!!это сложно добавить потом
# # class Stats_hero(Hero):
# #     def __init__(self, index, name, main_stat, esc, fiz_damage, magic_gamage, farm, fiz_hp, mag_hp, lvl_up):
# #         super().__init__(index, name)
# #         self.stat = main_stat
# #         self.esc = esc
# #         self.fizik = fiz_damage
# #         self.magic = magic_gamage
# #         self.farm = farm
# #         self.mag_hp = mag_hp
# #         self.fiz_hp = fiz_hp
# #         self.up = lvl_up
# #     def send_nudes(self):
# #         return [self.index, self.stat, self.esc, self.fizik, self.magic, self.farm, self.mag_hp, self.fiz_hp]
# #     def lvl_up(self, lvl):
# #         lvl = float(lvl)
# #         return [self.index, self.stat,
# #                 int(float(self.esc)+(float(self.up[0])*lvl)),
# #                 int(float(self.fizik)+(float(self.up[1])*lvl)),
# #                 int(float(self.magic)+(float(self.up[2])*lvl)),
# #                 int(float(self.farm)+(float(self.up[3])*lvl)),
# #                 int(float(self.farm) + (float(self.up[3]) * lvl)),
# #                 int(float(self.farm) + (float(self.up[3]) * lvl)),
# #                 ]
# class Info_hero:
#     def __init__(self, price, name, description, stats, img, event_img):
#         self.price = price
#         self.name = name
#         self.description = description
#         self.stats = stats
#         self.img = img
#         self.event_img = event_img
#
# pudge = Info_hero(8800, 'пудж', 'самый секс перс доты имба покупай', 'много статов', r'https://cq.ru/storage/uploads/images/1530144/1.jpg',
#                   "https://hsto.org/getpro/habr/post_images/6fc/750/e38/6fc750e38c21f9dc6a777c15cbf4be43.jpg")

class Hero:
    def __init__(self, index, name, ):
        self.index = index
        self.name = name
    def send_nudes(self):
        return [self.index, self.name]
    def send_text(self):
        return Exception('не тот класс')
    def calculate(self):
        return ValueError('не тот класс')
    def new_stats_lvl(self):
        return ValueError('не тот класс')
class Info(Hero):
    def __init__(self, index, name, price, description,  img):
        super().__init__( index, name,)
        self.price = price
        self.description = description
        #self.stats = stats
        self.img = img
    def send_nudes(self):
        return [self.name, self.price, self.description]
    def send_text(self):
        text = f"это {self.name}, он стоит {self.price}"
        text+= f"{self.description}"
        return text
class Stat_hero(Info):
    def __init__(self, index, name, price, description, img, damage, hp, lvl_up):
        super().__init__(index, name, price, description, img)
        self.damage = damage
        self.hp = hp
        self.lvl_up = lvl_up
    def new_stats_lvl(self, lvl):
        return [self.damage + self.lvl_up[0]*lvl,
                self.hp + self.lvl_up[1]*lvl
                ]
    def calculate(self):
        return 1+1
pudge_lvl_up = [3, 5]
pudge = Stat_hero(0, 'пудж', 8800, 'топ чар', r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp',
                  100, 100, pudge_lvl_up)
tetchis_lvl_up = [1, 2]
tetchis = Stat_hero(1, 'тетчис', 5000, 'говно',r'https://cojo.ru/wp-content/uploads/2022/12/pudzh-kompendium-2020-1.webp',
                    50, 50,tetchis_lvl_up )
hero_dick = [
    pudge,
    tetchis
]
for i in hero_dick:
    print(i.index)
    print(i.name)
    print(i.price)
    print(i.description)
    print(i.img)
    print(i.damage)
    print(i.hp)
    print(i.lvl_up)
    print(i.new_stats_lvl(5))

#пусть универсал - 0, сила - 1, ловкость -2, интеллект 3
#pudge_lvl_up = [1,2]
#pudge = Test_Stats_hero(10, 10, pudge_lvl_up)

test_Stats_heroes = [
    pudge
]



############################

#слишком сложно для школяра, сначала проще сделаю
# pudge_lvl = 5
# pudge_lvl_up = [0, 1, 2, 2, 1, 1]
# pudge = Stats_hero(index=0, main_stat=1, esc=5, fiz_damage=10, magic_gamage=15, farm=30, fiz_hp=10, mag_hp=10, lvl_up=pudge_lvl_up,)
# #тут у  меня будут заданы все герои с их базовым характеристиками
# #это мы не меняем, тут у нас всегда определённые статы (кроме патчей)
# #print(50/30)
# antimage_lvl_up = [5, 3, 1, 1.6]
# antimage = Stats_hero(index=1, main_stat=2, esc=20, fiz_damage=5, magic_gamage=3, farm=50, fiz_hp=1, mag_hp=15, lvl_up=antimage_lvl_up)
# void_spirit_lvl_up = [1, 2.5, 2.5, 1]
# void_spirit = Stats_hero(index=2,main_stat=3, esc=15, fiz_damage=25, magic_gamage=25, farm=10, lvl_up=void_spirit_lvl_up )
# Stats_heroes = [
#     pudge,
#     antimage
# ]
#
# print('пудж 0 лвл', Stats_heroes[0].send_nudes())
# print('пудж 5 лвл', Stats_heroes[0].lvl_up(5))
# asd = Stats_heroes[0].lvl_up(5)
# dick = {}
# #for i in asd:
    #dick.items()
#эта хуйня должна возвращать текущие значения героя. то есть например у пуджа васи будет 10 лвл.
#тогда мы берём данные с героя, помножаем их на кэф васи, и возвращаем текущие данные его героя
#самого героя мы никак не возвращаем и не меняем